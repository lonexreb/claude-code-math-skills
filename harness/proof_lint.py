"""Structural proof linter.

Used by the `math-critic` agent as a fast pre-pass before line-by-line
review. Catches the high-frequency informal-proof bugs:

  - cited theorems that don't resolve to a known chunk / digest
  - bare ∀ / ∃ introductions ("Let x ∈ ℝ" without naming it as arbitrary;
    "there exists" without a witness or a named existence theorem)
  - banned filler ("WLOG" without justification, "clearly", "obviously",
    "by a standard result")
  - hypothesis underuse: a hypothesis named in the claim that never appears
    in the proof body

The linter does NOT understand semantics. It produces *signals* — the
critic decides whether each is a real finding.

Usage::

    python3 -m harness.proof_lint --proof path/to/proof.md \
        [--claim path/to/claim-or-problem.md] \
        [--references skills/formal-math-ai/references/]

Outputs JSON:

    {
      "findings": [
        {"severity": "HIGH",
         "category": "citation",
         "message": "...",
         "line": 12, "snippet": "..."},
        ...
      ],
      "summary": {"CRITICAL": 0, "HIGH": 2, "MEDIUM": 1, "LOW": 0}
    }
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

# --------------------------------------------------------------------------- #
# regex banks
# --------------------------------------------------------------------------- #

# Citation patterns we expect:
#   (Lebl Vol I, Thm 3.4.5)
#   (Lebl §3.4)
#   (Folland Thm 2.24)
#   *(Royden Ch. 4)*
#   [Trench §2.2]
_CITATION_RE = re.compile(
    r"""
    [\(\[\*]                     # opening ( [ or *
    \s*
    (?P<author>[A-Z][A-Za-z\-]+) # author surname
    \s*
    (?:Vol\s*[IVX]+\s*)?         # optional volume
    (?:,?\s*)
    (?P<kind>(?:§|Ch\.?\s*|Thm\s*|Theorem\s*|Lemma\s*|Cor\.?\s*|Prop\.?\s*|Definition\s*|Def\.?\s*|Eq\.?\s*))
    \s*
    (?P<id>[0-9]+(?:\.[0-9]+)*[a-z]?)
    \s*
    [\)\]\*]                     # closing ) ] or *
    """,
    re.VERBOSE,
)

# Banned filler. Each pattern carries a severity.
_FILLER_PATTERNS: list[tuple[re.Pattern, str, str]] = [
    (re.compile(r"\bclearly\b", re.I), "MEDIUM", "filler: 'clearly' — show it or cite it"),
    (re.compile(r"\bobviously\b", re.I), "MEDIUM", "filler: 'obviously' — show it or cite it"),
    (re.compile(r"\bit is easy to see\b", re.I), "HIGH", "filler: 'it is easy to see' — show it"),
    (re.compile(r"\btrivially\b", re.I), "MEDIUM", "filler: 'trivially' — at least name the underlying fact"),
    (re.compile(r"\bby a standard result\b", re.I), "HIGH", "unnamed citation: 'by a standard result' — cite the theorem by name"),
    (re.compile(r"\bby standard arguments?\b", re.I), "HIGH", "unnamed citation: 'by standard argument(s)' — name it"),
    (re.compile(r"\bWLOG\b(?![^\n]*\bbecause\b|[^\n]*\bsince\b)", re.I), "MEDIUM", "WLOG without justification on the same line"),
    (re.compile(r"\bsimilar(ly)?\b", re.I), "LOW", "'similarly' / 'similar' — make sure the symmetric case really is symmetric"),
]

# Quantifier introductions that should be present.
# Allow optional opening quote/bracket characters before the introduced
# variable so "Fix `c ∈ ℝ`", "Let \"x\" be …", "Consider (xₙ)", and
# "Take ε > 0" all register as introductions.
_FORALL_INTRO = re.compile(r"\b(let|fix|consider|take)\b\s+[`'\"\(\[]*\S", re.I)
_EXISTS_INTRO = re.compile(
    r"(\bthere\s+exists?\b|\bchoose\b|\bpick\b|\b∃\b)",
    re.I,
)
_EXISTS_NAMED = re.compile(
    r"(\bset\b|\blet\b|\bdefine\b|\bdenote\b|=|\bwitness\b|\bexists?\s+a\b|\bsuch\s+that\b)",
    re.I,
)

# --------------------------------------------------------------------------- #
# data
# --------------------------------------------------------------------------- #

_KINDS_NORMAL = {
    # Map to the slug used by the chunker in references/<book>/<book>-<kind>-<id>.md.
    "theorem": "theorem",
    "thm": "theorem",
    "lemma": "lemma",
    "cor": "corollary",
    "corollary": "corollary",
    "prop": "proposition",
    "proposition": "proposition",
    "def": "definition",
    "definition": "definition",
}


def _normalize_kind(raw: str) -> str:
    raw = raw.strip().lower().rstrip(".").strip()
    raw = raw.replace(" ", "")
    if raw in {"§", "ch", "ch.", "eq", "eq."}:
        return "section"
    return _KINDS_NORMAL.get(raw, raw or "?")


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #

def _check_filler(lines: list[str]) -> list[dict]:
    findings: list[dict] = []
    for i, line in enumerate(lines, start=1):
        for pat, severity, msg in _FILLER_PATTERNS:
            m = pat.search(line)
            if m:
                findings.append({
                    "severity": severity,
                    "category": "filler",
                    "message": msg,
                    "line": i,
                    "snippet": line.strip()[:160],
                })
    return findings


def _check_citations(lines: list[str], reference_index: dict[str, list[str]]) -> list[dict]:
    """Cross-check every (Author, kind id) against the reference index.

    The reference index is a dict mapping a normalized author key to a list
    of file slugs. We can't always resolve the *exact* theorem id within the
    chunked corpus from a regex alone, so we settle for "author appears in
    references" — anything else is flagged as MEDIUM (suspicious citation,
    not necessarily wrong).
    """
    findings: list[dict] = []
    for i, line in enumerate(lines, start=1):
        for m in _CITATION_RE.finditer(line):
            author = m.group("author").lower()
            kind = _normalize_kind(m.group("kind"))
            cid = m.group("id")
            files = reference_index.get(author)
            if files is None:
                findings.append({
                    "severity": "HIGH",
                    "category": "citation",
                    "message": (
                        f"citation '{m.group(0).strip()}' references author '{author}' "
                        f"not present in skills/formal-math-ai/references/"
                    ),
                    "line": i,
                    "snippet": line.strip()[:160],
                })
                continue
            # Author exists. Try to find a chunk file with the citation id.
            slug_id = cid.replace(".", "-")
            wanted = f"{kind}-{slug_id}"
            if not any(wanted in f for f in files):
                findings.append({
                    "severity": "MEDIUM",
                    "category": "citation",
                    "message": (
                        f"citation '{m.group(0).strip()}' resolves to author '{author}' "
                        f"but no chunk matches '{wanted}'. Verify the id is right."
                    ),
                    "line": i,
                    "snippet": line.strip()[:160],
                })
    return findings


def _check_quantifier_discipline(lines: list[str]) -> list[dict]:
    findings: list[dict] = []
    body = "\n".join(lines)
    has_forall_symbol = "∀" in body or re.search(r"\bfor\s+(all|every|each)\b", body, re.I)
    has_forall_intro = bool(_FORALL_INTRO.search(body))
    if has_forall_symbol and not has_forall_intro:
        findings.append({
            "severity": "HIGH",
            "category": "quantifier",
            "message": (
                "claim references a universal quantifier (∀ / 'for all') but the "
                "proof body contains no introduction of an arbitrary element "
                "('let x be arbitrary', 'fix x', 'consider x ∈ X')."
            ),
            "line": None,
            "snippet": "",
        })

    for i, line in enumerate(lines, start=1):
        if not _EXISTS_INTRO.search(line):
            continue
        # An ∃ should either name a witness on the same or next line, OR
        # invoke a named existence theorem upstream/inline.
        nearby = " ".join(lines[max(0, i - 2):min(len(lines), i + 2)])
        if not _EXISTS_NAMED.search(nearby):
            findings.append({
                "severity": "HIGH",
                "category": "quantifier",
                "message": (
                    "existence claim lacks a witness or a named existence "
                    "theorem nearby; check that the witness is actually "
                    "produced or invoked."
                ),
                "line": i,
                "snippet": line.strip()[:160],
            })
    return findings


def _check_hypothesis_use(claim_text: str | None, proof_lines: list[str]) -> list[dict]:
    if not claim_text:
        return []
    findings: list[dict] = []
    body = " ".join(proof_lines)
    # Heuristic: any free-floating named hypothesis like "Let f be continuous"
    # or "Suppose f ∈ L¹". We just look for capitalized tokens after Let/Suppose
    # and check they show up in the body.
    intro_re = re.compile(r"\b(?:Let|Suppose|Assume)\s+([A-Za-z][\w]*)\b")
    for m in intro_re.finditer(claim_text):
        name = m.group(1)
        if name in {"the", "f", "F", "g", "x", "X", "S", "n"}:
            # too generic to track usefully
            continue
        if name not in body:
            findings.append({
                "severity": "MEDIUM",
                "category": "hypothesis-use",
                "message": (
                    f"hypothesis introduces '{name}' but '{name}' does not "
                    f"appear in the proof body — claim may be stronger than "
                    f"the proof actually uses."
                ),
                "line": None,
                "snippet": "",
            })
    return findings


# --------------------------------------------------------------------------- #
# reference indexing
# --------------------------------------------------------------------------- #

def build_reference_index(reference_dir: Path) -> dict[str, list[str]]:
    """Build a {author_key -> [filenames]} index from references/."""
    if not reference_dir.exists():
        return {}
    out: dict[str, list[str]] = {}
    for path in reference_dir.rglob("*.md"):
        rel = path.relative_to(reference_dir).as_posix()
        # First token of the filename is the author/source slug.
        # e.g. lebl-basic-analysis-vol1-theorem-3-4-5.md → "lebl"
        first = path.stem.split("-")[0].lower()
        out.setdefault(first, []).append(rel)
    return out


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def lint(proof_text: str, claim_text: str | None,
         reference_index: dict[str, list[str]]) -> dict:
    lines = proof_text.splitlines()
    findings: list[dict] = []
    findings.extend(_check_filler(lines))
    findings.extend(_check_citations(lines, reference_index))
    findings.extend(_check_quantifier_discipline(lines))
    findings.extend(_check_hypothesis_use(claim_text, lines))
    summary = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in findings:
        summary[f["severity"]] = summary.get(f["severity"], 0) + 1
    return {"findings": findings, "summary": summary}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="harness.proof_lint")
    p.add_argument("--proof", required=True, type=Path)
    p.add_argument("--claim", default=None, type=Path,
                   help="optional path to the original problem/claim file")
    p.add_argument("--references", default=None, type=Path,
                   help="path to the references directory (default: auto-detect)")
    args = p.parse_args(argv)

    if not args.proof.exists():
        print(f"error: {args.proof} does not exist", file=sys.stderr)
        return 2
    proof_text = args.proof.read_text()

    claim_text: str | None = None
    if args.claim and args.claim.exists():
        claim_text = args.claim.read_text()

    ref_dir = args.references
    if ref_dir is None:
        # auto-detect from repo root
        repo_root = Path(__file__).resolve().parent.parent
        ref_dir = repo_root / "skills" / "formal-math-ai" / "references"
    ref_index = build_reference_index(ref_dir)

    result = lint(proof_text, claim_text, ref_index)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
