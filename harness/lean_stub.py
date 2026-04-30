"""Generate a Lean 4 + mathlib skeleton from a structured proof plan.

Used by the `math-formalizer` agent. The agent supplies a JSON plan describing
the theorem and its informal proof steps; this script emits a `.lean` file
with mirrored structure and `sorry` placeholders.

Plan schema::

    {
      "name": "snake_case_theorem_name",
      "imports": ["Mathlib.Analysis.SpecialFunctions.Basic", ...],
      "open": ["Real", "Topology"],
      "binders": "(a b : ℝ) (h₁ : 0 < a) (h₂ : a < b)",
      "conclusion": "∃ c, a < c ∧ c < b",
      "informal": "Pick c = (a+b)/2 and verify both inequalities.",
      "steps": [
        {"name": "h_mid",  "type": "a < (a+b)/2", "comment": "since a < b"},
        {"name": "h_mid2", "type": "(a+b)/2 < b", "comment": "since a < b"}
      ],
      "conclude": "⟨(a+b)/2, h_mid, h_mid2⟩"
    }

Usage::

    python3 -m harness.lean_stub --plan plan.json --out thm.lean
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


_DEFAULT_IMPORTS = ("Mathlib.Tactic",)


def render(plan: dict[str, Any]) -> str:
    name = plan["name"]
    imports = plan.get("imports") or list(_DEFAULT_IMPORTS)
    open_decls = plan.get("open") or []
    binders = plan.get("binders", "").strip()
    conclusion = plan["conclusion"]
    informal = plan.get("informal", "").strip()
    steps = plan.get("steps") or []
    conclude = plan.get("conclude")

    lines: list[str] = []
    for imp in imports:
        lines.append(f"import {imp}")
    lines.append("")
    if open_decls:
        lines.append("open " + " ".join(open_decls))
        lines.append("")

    if informal:
        lines.append("/--")
        for ln in informal.splitlines():
            lines.append(ln)
        lines.append("-/")

    head = f"theorem {name}"
    if binders:
        head += f" {binders}"
    head += f" :\n    {conclusion} := by"
    lines.append(head)

    if not steps and not conclude:
        lines.append("  sorry")
    else:
        for step in steps:
            comment = step.get("comment", "").strip()
            if comment:
                lines.append(f"  -- {comment}")
            sname = step["name"]
            stype = step["type"]
            sproof = step.get("proof", "by sorry").strip()
            lines.append(f"  have {sname} : {stype} := {sproof}")
        if conclude:
            lines.append(f"  exact {conclude}")
        else:
            lines.append("  sorry")

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="harness.lean_stub")
    parser.add_argument("--plan", required=True, type=Path, help="JSON plan path")
    parser.add_argument("--out", required=True, type=Path, help="output .lean path")
    parser.add_argument(
        "--print", action="store_true", help="also print the rendered file to stdout"
    )
    args = parser.parse_args(argv)

    plan = json.loads(args.plan.read_text())
    rendered = render(plan)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(rendered)
    sorry_count = rendered.count("sorry")
    print(json.dumps(
        {"out": str(args.out), "sorry_count": sorry_count, "lines": rendered.count("\n")},
        indent=2,
    ))
    if args.print:
        print()
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
