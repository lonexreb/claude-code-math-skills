"""Benchmark run scaffolding.

`/math-bench` is a Claude Code orchestrator command — it does the actual
problem-solving via subagents. This module just provides utilities the agent
calls via `Bash`:

    - `init <id>`     create a fresh run directory under benchmarks/runs/
    - `record <run>`  append a row to benchmarks/runs/_index.md
    - `list`          list all problems under benchmarks/problems/

Examples
--------

::

    python3 -m harness.run_bench init putnam-2023-a1
    # → prints `benchmarks/runs/putnam-2023-a1__2026-04-30T01-30-00Z/`

    python3 -m harness.run_bench record \\
        benchmarks/runs/putnam-2023-a1__2026-04-30T01-30-00Z/

    python3 -m harness.run_bench list
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "benchmarks" / "problems"
RUNS = ROOT / "benchmarks" / "runs"
INDEX = RUNS / "_index.md"


def _now() -> str:
    return _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%dT%H-%M-%SZ")


def cmd_init(args: argparse.Namespace) -> int:
    bench_id = args.id
    src = PROBLEMS / f"{bench_id}.md"
    if not src.exists():
        print(f"error: {src} does not exist", file=sys.stderr)
        return 2
    run_dir = RUNS / f"{bench_id}__{_now()}"
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "meta.json").write_text(json.dumps({
        "id": bench_id,
        "started_at": _dt.datetime.now(_dt.UTC).isoformat(),
        "problem_path": str(src.relative_to(ROOT)),
        "finished_at": None,
        "critic_rounds": 0,
        "critic_final_verdict": None,
        "used_counterexample_hunter": False,
        "used_numeric_verifier": False,
        "used_symbol_runner": False,
        "used_formalizer": False,
        "total_agent_calls": 0,
    }, indent=2) + "\n")
    print(str(run_dir.relative_to(ROOT)))
    return 0


def cmd_record(args: argparse.Namespace) -> int:
    run_dir = Path(args.run_dir)
    if not run_dir.is_absolute():
        run_dir = (ROOT / run_dir).resolve()
    meta_path = run_dir / "meta.json"
    if not meta_path.exists():
        print(f"error: {meta_path} missing", file=sys.stderr)
        return 2
    meta = json.loads(meta_path.read_text())
    if meta.get("finished_at") is None:
        meta["finished_at"] = _dt.datetime.now(_dt.UTC).isoformat()
        meta_path.write_text(json.dumps(meta, indent=2) + "\n")

    INDEX.parent.mkdir(parents=True, exist_ok=True)
    if not INDEX.exists():
        INDEX.write_text(
            "# Benchmark runs\n\n"
            "| started_at | id | verdict | critic rounds | proof |\n"
            "|---|---|---|---|---|\n"
        )

    proof_path = run_dir / "proof.md"
    proof_link = (
        f"[proof.md]({proof_path.relative_to(RUNS)})"
        if proof_path.exists()
        else "—"
    )
    row = (
        f"| {meta.get('started_at', '?')} "
        f"| {meta.get('id', '?')} "
        f"| {meta.get('critic_final_verdict') or '?'} "
        f"| {meta.get('critic_rounds', 0)} "
        f"| {proof_link} |\n"
    )
    with INDEX.open("a") as f:
        f.write(row)
    print(json.dumps({"recorded": str(run_dir.relative_to(ROOT))}, indent=2))
    return 0


def cmd_list(_args: argparse.Namespace) -> int:
    if not PROBLEMS.exists():
        print("[]")
        return 0
    ids = sorted(p.stem for p in PROBLEMS.glob("*.md"))
    print(json.dumps(ids, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="harness.run_bench")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("id")
    p_init.set_defaults(handler=cmd_init)

    p_rec = sub.add_parser("record")
    p_rec.add_argument("run_dir")
    p_rec.set_defaults(handler=cmd_record)

    p_list = sub.add_parser("list")
    p_list.set_defaults(handler=cmd_list)

    args = parser.parse_args(argv)
    return args.handler(args)


if __name__ == "__main__":
    sys.exit(main())
