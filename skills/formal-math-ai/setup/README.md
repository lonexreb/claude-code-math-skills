# Setup — Adding PDF Reference Content

## Quick Start

```bash
# 1. Install the converter
pip install opendataloader-pdf --break-system-packages

# 2. Convert a textbook
python setup/convert_pdfs.py -i ~/Downloads/textbook.pdf -o references/new-topic.md

# 3. Or chunk a big book by chapter headings
python setup/convert_pdfs.py -i ~/Downloads/textbook.pdf --output-dir references/ --chunk

# 4. Convert specific pages only
python setup/convert_pdfs.py -i ~/Downloads/textbook.pdf -o references/ch3.md --pages 45-90

# 5. Academic math textbook with theorem-aware chunking
python setup/convert_pdfs.py -i ~/Downloads/textbook.pdf \
  --output-dir references/ --chunk --chunk-strategy theorem
```

## Engine Installation

The converter supports two engines. Only install what you need:

| Engine | Install | Use Case |
|--------|---------|----------|
| **OpenDataLoader** (primary) | `pip install opendataloader-pdf --break-system-packages` | Best accuracy (0.907 benchmark). Preserves LaTeX, tables, heading hierarchy. OCR for 80+ languages. |
| **PyMuPDF** (fallback) | `pip install PyMuPDF --break-system-packages` | Lightweight fallback. Basic text extraction without math-aware processing. |

The script auto-detects which engine is available. OpenDataLoader is tried first; if unavailable, PyMuPDF is used as fallback.

## Math-Aware Processing

By default, converted content goes through LaTeX post-processing (`setup/latex_postprocess.py`):

1. **Delimiter normalization**: `\(...\)` -> `$...$`, `\[...\]` -> `$$...$$`
2. **Artifact fixing**: Rejoins broken LaTeX commands, fixes OCR math errors
3. **Unicode simplification**: Converts simple LaTeX to Unicode to match existing reference style:
   - `\alpha` -> `α`, `\forall` -> `∀`, `\in` -> `∈`, `\leq` -> `≤`
   - `x^{2}` -> `x²`, `x_{n}` -> `xₙ` (single-char sub/superscripts)
4. **Complex preservation**: Keeps `\frac`, `\int`, matrices, etc. as `$...$`

Disable for non-math content: `--no-math-aware`

## Chunking Strategies

Use `--chunk` with `--chunk-strategy` to control how content is split:

| Strategy | Description | Best For |
|----------|-------------|----------|
| `section` (default) | Split by heading level (`--chunk-level`) | General textbooks |
| `theorem` | Split by theorem/definition/proof boundaries. Proofs stay attached to their theorems. | Math analysis, algebra |
| `hybrid` | Split by `##` sections, with theorem boundaries annotated as HTML comments | Mixed content |

Theorem detection recognizes: Theorem, Lemma, Proposition, Corollary, Definition, Example, Proof, Remark, Claim, Conjecture, Axiom.

Pattern formats detected: `**Theorem:**`, `### Theorem`, `THEOREM`, `**Theorem 3.2 (Name):**`

## Quality Validation

After conversion, the script runs quality validation (`setup/validate.py`) and reports a score:

- **0.9 - 1.0** (PASS): Good quality, ready to use
- **0.7 - 0.9** (REVIEW): Usable but review for issues
- **Below 0.7** (FAIL): Poor conversion, likely needs manual cleanup

Skip with `--no-validate`. Run standalone:

```bash
# Validate all reference files
python setup/validate.py references/

# Validate a single file
python setup/validate.py references/new-topic.md
```

### What validation checks

| Category | Checks |
|----------|--------|
| **LaTeX** | Unmatched `$`/`$$` delimiters, broken commands |
| **Structure** | Title heading, TOC, heading hierarchy, section separators |
| **Encoding** | Mojibake, remaining ligatures, control characters |
| **Content** | Paragraph density (too short = OCR fragments, too long = missing breaks) |

## Provenance Tracking

Track which PDF, engine, and pages produced each reference file:

```bash
python setup/convert_pdfs.py -i book.pdf -o references/topic.md \
  --provenance references/SOURCES.md
```

This appends a row to the `## Conversion Log` table in SOURCES.md with:
output file, source PDF, pages, engine used, quality score, and date.

## Academic Textbook Workflow

Step-by-step for adding a new textbook:

1. **Convert**: `python setup/convert_pdfs.py -i book.pdf -o references/topic.md --provenance references/SOURCES.md`
2. **Review score**: Check the quality score printed to console
3. **Review content**: Open the `.md` file and verify formulas, theorems, and structure
4. **Add to domain router**: Add a row to the Domain Router table in `SKILL.md`
5. **Update sources**: Add the source URL and license to `references/SOURCES.md`

For books over 500 pages, convert in chapter-sized chunks using `--pages`:
```bash
python setup/convert_pdfs.py -i big-book.pdf -o references/ch1.md --pages 1-80
python setup/convert_pdfs.py -i big-book.pdf -o references/ch2.md --pages 81-160
```

## Recommended PDFs to Convert

These are all legally free / open-access:

### Mathematics
| Book | URL | Suggested Output |
|------|-----|-----------------|
| Axler — Measure, Integration & Real Analysis | https://measure.axler.net/MIRA.pdf | `--chunk` by chapter |
| Lebl — Basic Analysis I | https://www.jirka.org/ra/ | Single file or chunk |
| Erdman — Functional Analysis & Operator Algebras | https://web.pdx.edu/~erdman/FAOA/functional_analysis_operator_algebras_pdf.pdf | `--chunk` |
| Trench — Intro to Real Analysis | http://ramanujan.math.trinity.edu/wtrench/texts/TRENCH_REAL_ANALYSIS.PDF | Single file |

### Computer Vision
| Book | URL | Suggested Output |
|------|-----|-----------------|
| Szeliski — Computer Vision 2nd Ed | https://szeliski.org/Book/ | `--chunk` (1500+ pages) |
| Prince — Understanding Deep Learning | https://udlbook.github.io/udlbook/ | `--chunk` |

### GPU / CUDA
| Book | URL | Suggested Output |
|------|-----|-----------------|
| NVIDIA CUDA Programming Guide | https://docs.nvidia.com/cuda/pdf/CUDA_C_Programming_Guide.pdf | `--chunk` |
| NVIDIA Best Practices Guide | https://docs.nvidia.com/cuda/pdf/CUDA_C_Best_Practices_Guide.pdf | Single file |

### Formal Verification
| Book | URL | Suggested Output |
|------|-----|-----------------|
| Chlipala — FRAP | https://adam.chlipala.net/frap/frap_book.pdf | `--chunk` |
| Nipkow — Concrete Semantics | http://concrete-semantics.org/concrete-semantics.pdf | `--chunk` |
| Lamport — Specifying Systems (TLA+) | https://lamport.azurewebsites.net/tla/book-02-08-08.pdf | `--chunk` |

## Fallback (if opendataloader-pdf isn't available)

The script falls back to PyMuPDF:
```bash
pip install PyMuPDF --break-system-packages
```

## After Conversion

1. Review the generated `.md` for quality
2. Add a table of contents at the top if missing (auto-generated with `--add-toc`)
3. Clean up any OCR artifacts (the script handles common ones)
4. Place in `references/` directory
5. Add an entry to the Domain Router in `SKILL.md`
