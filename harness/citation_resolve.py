"""Resolve textbook citations in a proof to chunk file paths.

Complements `harness.proof_lint`. Where the linter says "this citation
looks suspicious", the resolver says "if it's valid, here is the file".

Two modes:

    list    print every citation found in the proof, with its resolved
            chunk path (or '— UNRESOLVED' if no chunk matches).

    open    print the absolute path to the chunk for a single citation
            string passed via --citation, suitable for piping to xargs / cat.

Examples
--------

    python3 -m harness.citation_resolve list \\
        --proof proofs/lebl-3-1-7-cauchy-converges.md

    python3 -m harness.citation_resolve open \\
        --citation "(Lebl Vol I, Thm 2.3.7)"

    # quick "open the cited chunk in $PAGER":
    p=$(python3 -m harness.citation_resolve open --citation "(Lebl, Thm 3.4.5)")
    [ -n "$p" ] && less "$p"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Reuse the citation regex + kind normalization from proof_lint so the two
# tools always agree on what is and isn't a citation.
from harness.proof_lint import _CITATION_RE, _normalize_kind, build_reference_index


_DEFAULT_REFS = (
    Path(__file__).resolve().parent.parent
    / "skills" / "formal-math-ai" / "references"
)


def _resolve_one(author: str, kind: str, cid: str,
                 ref_index: dict[str, list[str]],
                 ref_dir: Path) -> Path | None:
    files = ref_index.get(author.lower())
    if not files:
        return None
    slug = f"{kind}-{cid.replace('.', '-')}"
    for f in files:
        if slug in f:
            return ref_dir / f
    return None


def cmd_list(args: argparse.Namespace) -> int:
    ref_dir = args.references or _DEFAULT_REFS
    ref_index = build_reference_index(ref_dir)
    text = args.proof.read_text()

    results: list[dict] = []
    for m in _CITATION_RE.finditer(text):
        author = m.group("author")
        kind = _normalize_kind(m.group("kind"))
        cid = m.group("id")
        path = _resolve_one(author, kind, cid, ref_index, ref_dir)
        results.append({
            "citation": m.group(0).strip(),
            "author": author,
            "kind": kind,
            "id": cid,
            "resolved": str(path) if path else None,
        })

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        if not results:
            print("(no citations found)")
            return 0
        width = max(len(r["citation"]) for r in results)
        for r in results:
            cite = r["citation"].ljust(width)
            target = r["resolved"] or "— UNRESOLVED"
            print(f"{cite}  →  {target}")
    # exit 1 if any unresolved — useful for CI
    return 1 if any(r["resolved"] is None for r in results) else 0


def cmd_open(args: argparse.Namespace) -> int:
    ref_dir = args.references or _DEFAULT_REFS
    ref_index = build_reference_index(ref_dir)
    m = _CITATION_RE.search(args.citation)
    if not m:
        print("error: --citation does not match a recognized citation form",
              file=sys.stderr)
        return 2
    author = m.group("author")
    kind = _normalize_kind(m.group("kind"))
    cid = m.group("id")
    path = _resolve_one(author, kind, cid, ref_index, ref_dir)
    if path is None:
        print(f"error: no chunk found for {m.group(0).strip()}", file=sys.stderr)
        return 1
    print(str(path))
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="harness.citation_resolve")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_list = sub.add_parser("list",
                            help="list every citation in a proof and its resolved file")
    p_list.add_argument("--proof", required=True, type=Path)
    p_list.add_argument("--references", default=None, type=Path)
    p_list.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON instead of a table")
    p_list.set_defaults(handler=cmd_list)

    p_open = sub.add_parser("open",
                            help="resolve a single citation to its file path")
    p_open.add_argument("--citation", required=True,
                        help="e.g. '(Lebl Vol I, Thm 3.4.5)'")
    p_open.add_argument("--references", default=None, type=Path)
    p_open.set_defaults(handler=cmd_open)

    args = p.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
