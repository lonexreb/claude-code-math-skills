#!/usr/bin/env python3
"""
convert_pdfs.py — Convert PDF textbooks to chunked Markdown for Claude Code skills.

Uses OpenDataLoader-PDF (Apache 2.0) for high-fidelity extraction:
  - Preserves LaTeX math formulas
  - Handles complex/borderless tables
  - Maintains heading hierarchy for semantic chunking
  - OCR support for 80+ languages

Usage:
  # Single file
  python convert_pdfs.py --input book.pdf --output references/topic.md

  # Batch directory
  python convert_pdfs.py --input-dir ./pdfs/ --output-dir ./references/

  # With chunking (split by heading level)
  python convert_pdfs.py --input book.pdf --output-dir ./references/ --chunk --chunk-level 1

  # With page range
  python convert_pdfs.py --input book.pdf --output references/ch1.md --pages 1-50

Requirements:
  pip install opendataloader-pdf --break-system-packages
"""

import argparse
import os
import re
import sys
from datetime import date
from pathlib import Path

# Import enhanced modules (available when running from setup/ or formal-math-ai/)
try:
    from latex_postprocess import latex_postprocess
except ImportError:
    try:
        from setup.latex_postprocess import latex_postprocess
    except ImportError:
        latex_postprocess = None  # type: ignore[assignment]

try:
    from academic_chunker import (
        chunk_academic,
        detect_academic_elements,
        generate_toc_from_elements,
    )
except ImportError:
    try:
        from setup.academic_chunker import (
            chunk_academic,
            detect_academic_elements,
            generate_toc_from_elements,
        )
    except ImportError:
        chunk_academic = None  # type: ignore[assignment]
        detect_academic_elements = None  # type: ignore[assignment]
        generate_toc_from_elements = None  # type: ignore[assignment]

try:
    from validate import validate_file
except ImportError:
    try:
        from setup.validate import validate_file
    except ImportError:
        validate_file = None  # type: ignore[assignment]


def check_dependencies() -> bool:
    """Verify opendataloader-pdf is installed AND a working JRE is available.

    opendataloader-pdf is a thin Python wrapper around a Java JAR; without a
    real JRE the subprocess call fails at runtime. We check both up front so
    the caller can choose the PyMuPDF fallback cleanly.
    """
    try:
        import opendataloader_pdf  # noqa: F401
    except ImportError:
        print("opendataloader-pdf not installed (pip install opendataloader-pdf).")
        return False

    import subprocess
    try:
        result = subprocess.run(
            ["java", "-version"],
            capture_output=True,
            timeout=10,
        )
        if result.returncode != 0:
            print("Java runtime not available (opendataloader-pdf needs a JRE).")
            return False
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("Java runtime not available (opendataloader-pdf needs a JRE).")
        return False

    return True


def convert_with_opendataloader(input_path: str, pages: str = None) -> str:
    """Convert PDF to markdown using opendataloader-pdf v2.x.

    The library writes output files to a directory; we use a temp dir,
    locate the produced markdown, read it, and return the text.
    """
    import tempfile
    import opendataloader_pdf

    with tempfile.TemporaryDirectory(prefix="odlpdf-") as tmpdir:
        opendataloader_pdf.convert(
            input_path=input_path,
            output_dir=tmpdir,
            format="markdown",
            pages=pages,
            quiet=True,
            image_output="off",
        )

        md_files = sorted(Path(tmpdir).rglob("*.md"))
        if not md_files:
            raise RuntimeError(
                f"opendataloader-pdf produced no .md files in {tmpdir}"
            )

        parts = [p.read_text(encoding="utf-8", errors="replace") for p in md_files]
        return "\n\n".join(parts)


def convert_with_fallback(input_path: str, pages: str = None) -> tuple[str, str]:
    """Fallback when opendataloader-pdf isn't usable.

    Prefers pymupdf4llm (markdown with heading detection from font sizes),
    falls back to plain PyMuPDF text extraction (no headings).

    Returns (text, engine_name) so callers can record which engine produced
    the output for provenance.
    """
    page_range = None
    if pages:
        s, e = map(int, pages.split("-"))
        page_range = list(range(s - 1, e))

    try:
        import pymupdf4llm
        kwargs = {}
        if page_range is not None:
            kwargs["pages"] = page_range
        return pymupdf4llm.to_markdown(input_path, **kwargs), "pymupdf4llm"
    except ImportError:
        pass

    try:
        import fitz  # PyMuPDF
    except ImportError:
        print("ERROR: No PDF backend available.")
        print("Install one of (in order of preference):")
        print("  pip install opendataloader-pdf  # plus a JRE")
        print("  pip install pymupdf4llm")
        print("  pip install PyMuPDF")
        sys.exit(1)

    doc = fitz.open(input_path)
    parts = []
    start_page = 0 if page_range is None else page_range[0]
    end_page = len(doc) if page_range is None else page_range[-1] + 1
    for page_num in range(start_page, min(end_page, len(doc))):
        page = doc[page_num]
        text = page.get_text("text")
        if text.strip():
            parts.append(f"<!-- Page {page_num + 1} -->\n{text}")
    doc.close()
    return "\n\n".join(parts), "pymupdf"


def clean_markdown(text: str, math_aware: bool = True) -> str:
    """Post-process extracted markdown for quality.

    Args:
        text: Raw markdown text from PDF conversion.
        math_aware: When True, runs LaTeX post-processing to convert simple
            LaTeX to Unicode and normalize math delimiters. Default True.
    """
    # Fix common OCR/extraction artifacts
    text = re.sub(r'\n{4,}', '\n\n\n', text)           # Collapse excessive newlines
    text = re.sub(r'[ \t]+\n', '\n', text)              # Trailing whitespace
    text = re.sub(r'\x0c', '\n---\n', text)             # Form feeds → section breaks
    text = re.sub(r'(\w)-\n(\w)', r'\1\2', text)        # Rejoin hyphenated words
    text = re.sub(r'ﬁ', 'fi', text)                     # Common ligature
    text = re.sub(r'ﬂ', 'fl', text)                     # Common ligature
    text = re.sub(r'ﬀ', 'ff', text)                     # Common ligature

    # LaTeX-aware post-processing
    if math_aware and latex_postprocess is not None:
        text = latex_postprocess(text)

    return text.strip()


def chunk_by_heading(text: str, level: int = 1) -> list[tuple[str, str]]:
    """Split markdown into chunks by heading level.

    Args:
        text: Full markdown text
        level: Heading level to split on (1 = #, 2 = ##, etc.)

    Returns:
        List of (heading_text, content) tuples
    """
    pattern = rf'^({"#" * level}\s+.+)$'
    parts = re.split(pattern, text, flags=re.MULTILINE)

    chunks = []
    if parts[0].strip():
        chunks.append(("_preamble", parts[0].strip()))

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        chunks.append((heading, content))

    return chunks


def heading_to_filename(heading: str) -> str:
    """Convert a heading to a safe filename."""
    name = heading.lstrip('#').strip().lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    name = name.strip('-')
    return name[:80]  # Truncate long names


def write_provenance(output_path: str, input_path: str, engine: str,
                     pages: str, score: float,
                     provenance_file: str = None) -> None:
    """Append conversion metadata to a provenance log file.

    If provenance_file is not specified, appends to references/SOURCES.md
    under the '## Conversion Log' section.
    """
    if provenance_file is None:
        # Default: references/SOURCES.md relative to output_path
        ref_dir = os.path.dirname(output_path)
        provenance_file = os.path.join(ref_dir, 'SOURCES.md')

    today = date.today().isoformat()
    out_name = os.path.basename(output_path)
    in_name = os.path.basename(input_path)
    pages_str = pages or "all"
    row = f"| `{out_name}` | {in_name} | {pages_str} | {engine} | {score:.2f} | {today} |\n"

    if not os.path.exists(provenance_file):
        return

    with open(provenance_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if '## Conversion Log' not in content:
        # Add the section if it doesn't exist
        content += (
            "\n\n## Conversion Log\n\n"
            "| Output File | Source PDF | Pages | Engine | Quality Score | Date |\n"
            "|-------------|-----------|-------|--------|---------------|------|\n"
        )

    content += row

    with open(provenance_file, 'w', encoding='utf-8') as f:
        f.write(content)


def convert_single(input_path: str, output_path: str, pages: str = None,
                   math_aware: bool = True, do_validate: bool = True,
                   add_toc: bool = True, provenance_file: str = None):
    """Convert a single PDF to markdown.

    Args:
        input_path: Path to input PDF.
        output_path: Path for output markdown file.
        pages: Optional page range (e.g. '1-50').
        math_aware: Run LaTeX post-processing. Default True.
        do_validate: Run quality validation after conversion. Default True.
        add_toc: Auto-generate Table of Contents from detected elements. Default True.
        provenance_file: Optional file to append conversion metadata to.
    """
    print(f"Converting: {input_path}")

    engine = "opendataloader"
    if check_dependencies():
        text = convert_with_opendataloader(input_path, pages)
    else:
        print("Falling back to PyMuPDF...")
        text, engine = convert_with_fallback(input_path, pages)

    text = clean_markdown(text, math_aware=math_aware)

    # Auto-generate TOC from detected academic elements
    if add_toc and detect_academic_elements is not None:
        elements = detect_academic_elements(text)
        if elements:
            toc = generate_toc_from_elements(elements)
            if toc and '## Table of Contents' not in text:
                # Insert TOC after the first heading
                lines = text.split('\n')
                insert_idx = 0
                for i, line in enumerate(lines):
                    if line.strip().startswith('# '):
                        insert_idx = i + 1
                        break
                lines.insert(insert_idx, '\n' + toc + '\n')
                text = '\n'.join(lines)

    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    size_kb = os.path.getsize(output_path) / 1024
    print(f"  → {output_path} ({size_kb:.1f} KB)")

    # Quality validation
    score = 1.0
    if do_validate and validate_file is not None:
        report = validate_file(output_path)
        score = report.score
        status = "PASS" if score >= 0.9 else ("REVIEW" if score >= 0.7 else "FAIL")
        print(f"  Quality: {score:.2f} ({status}, {len(report.issues)} issues)")
        if report.issues:
            for issue in report.issues[:5]:
                prefix = {"error": "ERR", "warning": "WRN", "info": "INF"}.get(issue.severity, "???")
                print(f"    [{prefix}] {issue.message}")
            if len(report.issues) > 5:
                print(f"    ... and {len(report.issues) - 5} more")

    # Provenance tracking
    if provenance_file is not None:
        write_provenance(output_path, input_path, engine, pages, score, provenance_file)

    return text


def convert_chunked(input_path: str, output_dir: str, chunk_level: int = 1,
                    pages: str = None, math_aware: bool = True,
                    chunk_strategy: str = "section",
                    do_validate: bool = True,
                    provenance_file: str = None):
    """Convert a PDF and split into per-section .md files.

    Args:
        input_path: Path to input PDF.
        output_dir: Directory for output chunk files.
        chunk_level: Heading level for section-based chunking (1=#, 2=##).
        pages: Optional page range (e.g. '1-50').
        math_aware: Run LaTeX post-processing. Default True.
        chunk_strategy: One of "section", "theorem", "hybrid". Default "section".
        do_validate: Run quality validation on each chunk. Default True.
        provenance_file: Optional file to append a single aggregated row to
            (output: chunk-dir + manifest, score: mean across chunks).
    """
    print(f"Converting + chunking: {input_path}")

    engine = "opendataloader"
    if check_dependencies():
        text = convert_with_opendataloader(input_path, pages)
    else:
        print("Falling back to PyMuPDF...")
        text, engine = convert_with_fallback(input_path, pages)

    text = clean_markdown(text, math_aware=math_aware)

    # Use academic chunker for theorem/hybrid strategies
    if chunk_strategy in ("theorem", "hybrid") and chunk_academic is not None:
        chunks = chunk_academic(text, strategy=chunk_strategy)
    else:
        chunks = chunk_by_heading(text, chunk_level)

    os.makedirs(output_dir, exist_ok=True)
    book_name = Path(input_path).stem

    manifest = []
    scores = []
    score_counts = {"PASS": 0, "REVIEW": 0, "FAIL": 0}
    for heading, content in chunks:
        if not content.strip():
            continue
        fname = f"{book_name}-{heading_to_filename(heading)}.md"
        fpath = os.path.join(output_dir, fname)
        full_content = f"{heading}\n\n{content}" if not heading.startswith('_') else content
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(full_content)
        size_kb = os.path.getsize(fpath) / 1024
        manifest.append((fname, heading, size_kb))
        print(f"  → {fpath} ({size_kb:.1f} KB)")

        # Validate each chunk
        if do_validate and validate_file is not None:
            report = validate_file(fpath)
            scores.append(report.score)
            status = "PASS" if report.score >= 0.9 else ("REVIEW" if report.score >= 0.7 else "FAIL")
            score_counts[status] += 1
            print(f"    Quality: {report.score:.2f} ({status})")

    # Write manifest
    manifest_path = os.path.join(output_dir, f"{book_name}-manifest.md")
    with open(manifest_path, 'w') as f:
        f.write(f"# {book_name} — Chunk Manifest\n\n")
        f.write(f"Strategy: {chunk_strategy}\n\n")
        f.write(f"Engine: {engine}\n\n")
        f.write("| File | Section | Size (KB) |\n")
        f.write("|------|---------|----------|\n")
        for fname, heading, size in manifest:
            f.write(f"| `{fname}` | {heading} | {size:.1f} |\n")

    print(f"\nManifest: {manifest_path}")
    print(f"Total chunks: {len(manifest)}")

    # Aggregate provenance — one row that captures the whole chunked output.
    if provenance_file is not None:
        mean_score = sum(scores) / len(scores) if scores else 1.0
        chunk_dir_name = os.path.basename(os.path.normpath(output_dir)) or output_dir
        summary_label = (
            f"{chunk_dir_name}/ ({len(manifest)} chunks, "
            f"PASS={score_counts['PASS']} REVIEW={score_counts['REVIEW']} "
            f"FAIL={score_counts['FAIL']})"
        )
        write_provenance(
            output_path=os.path.join(output_dir, summary_label),
            input_path=input_path,
            engine=engine,
            pages=pages,
            score=mean_score,
            provenance_file=provenance_file,
        )


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF textbooks to Markdown for Claude Code skills"
    )
    parser.add_argument("--input", "-i", help="Input PDF file")
    parser.add_argument("--input-dir", help="Directory of PDFs to batch convert")
    parser.add_argument("--output", "-o", help="Output .md file (single file mode)")
    parser.add_argument("--output-dir", help="Output directory (batch/chunk mode)")
    parser.add_argument("--pages", help="Page range, e.g. '1-50'")
    parser.add_argument("--chunk", action="store_true", help="Split output by headings")
    parser.add_argument("--chunk-level", type=int, default=1,
                       help="Heading level to chunk on (1=#, 2=##, default=1)")
    parser.add_argument("--chunk-strategy", choices=["section", "theorem", "hybrid"],
                       default="section",
                       help="Chunking strategy: section (heading-based), theorem "
                            "(theorem/definition boundaries), hybrid (sections with "
                            "annotated elements). Default: section")
    parser.add_argument("--no-validate", action="store_true",
                       help="Skip quality validation after conversion")
    parser.add_argument("--no-toc", action="store_true",
                       help="Don't auto-generate Table of Contents")
    parser.add_argument("--no-math-aware", action="store_true",
                       help="Disable LaTeX post-processing (for non-math content)")
    parser.add_argument("--provenance", metavar="FILE",
                       help="Append conversion metadata to this file")

    args = parser.parse_args()

    if not args.input and not args.input_dir:
        parser.print_help()
        print("\nExample usage:")
        print("  python convert_pdfs.py -i textbook.pdf -o references/topic.md")
        print("  python convert_pdfs.py -i textbook.pdf --output-dir refs/ --chunk")
        print("  python convert_pdfs.py -i textbook.pdf --chunk --chunk-strategy theorem")
        print("  python convert_pdfs.py --input-dir ./pdfs/ --output-dir ./references/")
        print("  python convert_pdfs.py -i textbook.pdf -o refs/topic.md --no-math-aware")
        sys.exit(1)

    math_aware = not args.no_math_aware
    do_validate = not args.no_validate
    add_toc = not args.no_toc

    # Single file mode
    if args.input:
        if args.chunk:
            out_dir = args.output_dir or "references"
            convert_chunked(args.input, out_dir, args.chunk_level, args.pages,
                          math_aware=math_aware, chunk_strategy=args.chunk_strategy,
                          do_validate=do_validate, provenance_file=args.provenance)
        else:
            out_path = args.output or f"references/{Path(args.input).stem}.md"
            convert_single(args.input, out_path, args.pages,
                         math_aware=math_aware, do_validate=do_validate,
                         add_toc=add_toc, provenance_file=args.provenance)

    # Batch mode
    elif args.input_dir:
        out_dir = args.output_dir or "references"
        for fname in sorted(os.listdir(args.input_dir)):
            if fname.lower().endswith('.pdf'):
                fpath = os.path.join(args.input_dir, fname)
                if args.chunk:
                    convert_chunked(fpath, out_dir, args.chunk_level, args.pages,
                                  math_aware=math_aware,
                                  chunk_strategy=args.chunk_strategy,
                                  do_validate=do_validate,
                                  provenance_file=args.provenance)
                else:
                    out_path = os.path.join(out_dir, Path(fname).stem + '.md')
                    convert_single(fpath, out_path, args.pages,
                                 math_aware=math_aware, do_validate=do_validate,
                                 add_toc=add_toc, provenance_file=args.provenance)


if __name__ == "__main__":
    main()
