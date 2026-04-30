"""
academic_chunker.py -- Structure-aware chunking for academic textbooks.

Detects theorems, definitions, lemmas, proofs, and other academic elements.
Provides chunking strategies that respect mathematical document structure.
"""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class AcademicElement:
    """A detected academic structural element (theorem, definition, proof, etc.)."""
    kind: str          # "theorem", "definition", "proof", "lemma", "example", etc.
    name: str          # "Bolzano-Weierstrass", "3.2.1", ""
    start_line: int
    end_line: int
    content: str


# Pattern fragments for academic element detection
_ELEMENT_KINDS = (
    "theorem", "lemma", "proposition", "corollary",
    "definition", "example", "proof", "remark",
    "claim", "conjecture", "axiom", "property",
)

# Build regex pattern for detecting academic elements
# Matches: **Theorem:** , **Theorem (Name):** , ### Theorem , THEOREM , Theorem. , Theorem N.M
_BOLD_PATTERN = re.compile(
    r'^\*\*(' + '|'.join(_ELEMENT_KINDS) + r')'
    r'(?:\s+(\d[\d.]*))?\s*'          # optional number like 3.2.1
    r'(?:\(([^)]+)\))?\s*'            # optional name in parens
    r'[.:]\*\*',                       # closing bold with . or :
    re.IGNORECASE | re.MULTILINE,
)

_HEADING_PATTERN = re.compile(
    r'^#{2,4}\s+(' + '|'.join(_ELEMENT_KINDS) + r')'
    r'(?:\s+(\d[\d.]*))?'             # optional number
    r'(?:\s*[:\-\u2014]\s*(.+))?'     # optional name after : or - or em-dash
    r'\s*$',
    re.IGNORECASE | re.MULTILINE,
)

_UPPER_PATTERN = re.compile(
    r'^(' + '|'.join(k.upper() for k in _ELEMENT_KINDS) + r')'
    r'(?:\s+(\d[\d.]*))?'
    r'(?:\s*[.:\-\u2014]\s*(.*))?'
    r'\s*$',
    re.MULTILINE,
)


def detect_academic_elements(text: str) -> list[AcademicElement]:
    """Parse text to identify theorems, definitions, proofs, and other academic elements.

    Detects patterns like:
      **Theorem 3.2 (Bolzano-Weierstrass):**
      ### Definition
      THEOREM.
      **Proof:**
    """
    lines = text.split('\n')
    elements: list[AcademicElement] = []

    # Find all element start positions
    starts: list[tuple[int, str, str, str]] = []  # (line_idx, kind, number, name)

    for i, line in enumerate(lines):
        # Bold pattern: **Theorem (Name):**
        m = _BOLD_PATTERN.match(line.strip())
        if m:
            starts.append((i, m.group(1).lower(), m.group(2) or "", m.group(3) or ""))
            continue

        # Heading pattern: ### Theorem
        m = _HEADING_PATTERN.match(line.strip())
        if m:
            starts.append((i, m.group(1).lower(), m.group(2) or "", m.group(3) or ""))
            continue

        # Uppercase pattern: THEOREM
        m = _UPPER_PATTERN.match(line.strip())
        if m:
            starts.append((i, m.group(1).lower(), m.group(2) or "", m.group(3) or ""))
            continue

    # Determine end lines: each element ends where the next one begins,
    # or at the next heading, or at the next blank line followed by a heading
    for idx, (start_line, kind, number, name) in enumerate(starts):
        if idx + 1 < len(starts):
            end_line = starts[idx + 1][0] - 1
        else:
            end_line = len(lines) - 1

        # Trim trailing blank lines
        while end_line > start_line and not lines[end_line].strip():
            end_line -= 1

        content = '\n'.join(lines[start_line:end_line + 1])
        display_name = f"{number} ({name})" if number and name else (number or name)

        elements.append(AcademicElement(
            kind=kind,
            name=display_name.strip(),
            start_line=start_line + 1,  # 1-indexed
            end_line=end_line + 1,
            content=content,
        ))

    return elements


def chunk_by_heading(text: str, level: int = 1) -> list[tuple[str, str]]:
    """Split markdown into chunks by heading level (backward-compatible).

    This is the same logic as the original convert_pdfs.py chunk_by_heading.
    """
    pattern = rf'^({"#" * level}\s+.+)$'
    parts = re.split(pattern, text, flags=re.MULTILINE)

    chunks: list[tuple[str, str]] = []
    if parts[0].strip():
        chunks.append(("_preamble", parts[0].strip()))

    for i in range(1, len(parts), 2):
        heading = parts[i].strip()
        content = parts[i + 1].strip() if i + 1 < len(parts) else ""
        chunks.append((heading, content))

    return chunks


def chunk_by_theorem(text: str) -> list[tuple[str, str]]:
    """Chunk by theorem/definition boundaries, keeping proofs with their theorems.

    Returns (label, content) tuples. Proofs are attached to the preceding
    theorem/lemma/proposition/corollary rather than split out separately.
    """
    elements = detect_academic_elements(text)
    if not elements:
        # Fallback to section-based chunking
        return chunk_by_heading(text, level=2)

    lines = text.split('\n')
    chunks: list[tuple[str, str]] = []

    # Collect non-element preamble
    first_elem_line = elements[0].start_line - 1  # 0-indexed
    if first_elem_line > 0:
        preamble = '\n'.join(lines[:first_elem_line]).strip()
        if preamble:
            chunks.append(("_preamble", preamble))

    # Group proofs with their preceding theorem
    i = 0
    while i < len(elements):
        elem = elements[i]

        # If this is a proof and there's a previous non-proof element,
        # it was already attached. Skip standalone proofs at the start.
        if elem.kind == "proof" and chunks:
            i += 1
            continue

        # Collect the element and any immediately following proof
        label = f"{elem.kind.title()}"
        if elem.name:
            label += f" {elem.name}"
        content = elem.content

        # Check if next element is a proof -- attach it
        if (i + 1 < len(elements)
                and elements[i + 1].kind == "proof"
                and elem.kind in ("theorem", "lemma", "proposition", "corollary", "claim")):
            proof = elements[i + 1]
            content += '\n\n' + proof.content
            i += 1  # skip the proof in next iteration

        chunks.append((label, content))
        i += 1

    return chunks


def chunk_hybrid(text: str) -> list[tuple[str, str]]:
    """Split by ## sections, but annotate theorem/definition boundaries within each.

    Each chunk is a section. Academic elements within each section get
    HTML comment markers for navigation.
    """
    sections = chunk_by_heading(text, level=2)
    result: list[tuple[str, str]] = []

    for heading, content in sections:
        elements = detect_academic_elements(content)
        if elements:
            # Add element index as HTML comments
            index_lines = ["<!-- Academic elements in this section:"]
            for elem in elements:
                label = f"  - {elem.kind.title()}"
                if elem.name:
                    label += f" {elem.name}"
                label += f" (line {elem.start_line})"
                index_lines.append(label)
            index_lines.append("-->")
            annotated = '\n'.join(index_lines) + '\n\n' + content
            result.append((heading, annotated))
        else:
            result.append((heading, content))

    return result


def chunk_academic(text: str, strategy: str = "section") -> list[tuple[str, str]]:
    """Chunk text using the specified strategy.

    Args:
        text: Full markdown text
        strategy: One of "section" (heading-based), "theorem" (theorem/definition
                  boundaries), or "hybrid" (sections with annotated elements)

    Returns:
        List of (heading/label, content) tuples
    """
    if strategy == "theorem":
        return chunk_by_theorem(text)
    elif strategy == "hybrid":
        return chunk_hybrid(text)
    else:
        return chunk_by_heading(text, level=2)


def generate_toc_from_elements(elements: list[AcademicElement]) -> str:
    """Auto-generate a Table of Contents from detected academic elements.

    Matches the existing reference file format:
    ## Table of Contents
    1. [Section Name](#anchor)
    """
    if not elements:
        return ""

    lines = ["## Table of Contents"]
    seen_sections: list[str] = []

    for i, elem in enumerate(elements, start=1):
        label = elem.kind.title()
        if elem.name:
            label += f" {elem.name}"

        # Create anchor from label
        anchor = label.lower()
        anchor = re.sub(r'[^a-z0-9\s-]', '', anchor)
        anchor = re.sub(r'\s+', '-', anchor.strip())

        if anchor not in seen_sections:
            lines.append(f"{i}. [{label}](#{anchor})")
            seen_sections.append(anchor)

    return '\n'.join(lines)


def add_section_separators(text: str) -> str:
    """Insert --- separators between ## sections (matching existing reference style)."""
    lines = text.split('\n')
    result: list[str] = []
    prev_was_content = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('## ') and prev_was_content:
            # Insert separator before this heading
            result.append('')
            result.append('---')
            result.append('')
        result.append(line)
        if stripped:
            prev_was_content = True

    return '\n'.join(result)
