"""Numeric / symbolic smoke tests for math claims.

Used by the `math-numeric-verifier` agent. Designed to be invoked from the
command line so an agent can `Bash` a one-liner and parse the output.

Examples
--------
Identity check::

    python3 -m harness.sympy_check identity \\
        --lhs "sin(x)**2 + cos(x)**2" --rhs "1" --vars x

Inequality random sweep::

    python3 -m harness.sympy_check inequality \\
        --lhs "x**2 + 1" --rhs "2*x" --vars x \\
        --domain real --samples 200 --seed 12345

Limit::

    python3 -m harness.sympy_check limit --expr "sin(x)/x" --var x --to 0
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Iterable

import sympy as sp


# --------------------------------------------------------------------------- #
# command surface
# --------------------------------------------------------------------------- #

def _make_symbols(names: Iterable[str], domain: str) -> dict[str, sp.Symbol]:
    assumptions: dict[str, bool] = {}
    if domain == "real":
        assumptions["real"] = True
    elif domain == "positive":
        assumptions["positive"] = True
    elif domain == "integer":
        assumptions["integer"] = True
    elif domain == "complex":
        pass
    else:
        raise SystemExit(f"unknown --domain {domain!r}")
    return {n: sp.Symbol(n, **assumptions) for n in names}


def cmd_identity(args: argparse.Namespace) -> dict:
    syms = _make_symbols(args.vars, args.domain)
    lhs = sp.sympify(args.lhs, locals=syms)
    rhs = sp.sympify(args.rhs, locals=syms)
    diff = sp.simplify(lhs - rhs)
    holds = diff == 0
    return {
        "kind": "identity",
        "lhs": str(lhs),
        "rhs": str(rhs),
        "simplified_diff": str(diff),
        "holds": bool(holds),
        "verdict": "PASS" if holds else "FAIL",
    }


def cmd_inequality(args: argparse.Namespace) -> dict:
    import numpy as np

    rng = np.random.default_rng(args.seed)
    syms = _make_symbols(args.vars, args.domain)
    lhs = sp.sympify(args.lhs, locals=syms)
    rhs = sp.sympify(args.rhs, locals=syms)

    op_map = {
        "le": lambda a, b: a <= b,
        "lt": lambda a, b: a < b,
        "ge": lambda a, b: a >= b,
        "gt": lambda a, b: a > b,
    }
    if args.op not in op_map:
        raise SystemExit(f"unknown --op {args.op!r}")
    op = op_map[args.op]

    var_list = [syms[n] for n in args.vars]
    f_lhs = sp.lambdify(var_list, lhs, "numpy")
    f_rhs = sp.lambdify(var_list, rhs, "numpy")

    fails: list[dict] = []
    n = args.samples
    if args.domain == "positive":
        sample = rng.uniform(args.lo if args.lo > 0 else 1e-6, args.hi, size=(n, len(var_list)))
    elif args.domain == "integer":
        sample = rng.integers(int(args.lo), int(args.hi) + 1, size=(n, len(var_list)))
    else:
        sample = rng.uniform(args.lo, args.hi, size=(n, len(var_list)))

    for row in sample:
        try:
            l = f_lhs(*row)
            r = f_rhs(*row)
        except Exception:
            continue
        if not bool(op(l, r)):
            fails.append({"point": [float(v) for v in row], "lhs": float(l), "rhs": float(r)})
            if len(fails) >= 5:
                break

    return {
        "kind": "inequality",
        "lhs": str(lhs),
        "op": args.op,
        "rhs": str(rhs),
        "samples": n,
        "seed": args.seed,
        "fails": fails,
        "verdict": "FAIL" if fails else f"PASS (consistent, {n} samples)",
    }


def cmd_limit(args: argparse.Namespace) -> dict:
    syms = _make_symbols([args.var], args.domain)
    expr = sp.sympify(args.expr, locals=syms)
    target = sp.sympify(args.to)
    direction = args.direction
    L = sp.limit(expr, syms[args.var], target, direction)
    return {
        "kind": "limit",
        "expr": str(expr),
        "var": args.var,
        "to": str(target),
        "direction": direction,
        "value": str(L),
    }


def cmd_integrate(args: argparse.Namespace) -> dict:
    syms = _make_symbols([args.var], args.domain)
    expr = sp.sympify(args.expr, locals=syms)
    if args.lo is None or args.hi is None:
        F = sp.integrate(expr, syms[args.var])
        check = sp.simplify(sp.diff(F, syms[args.var]) - expr)
        return {
            "kind": "antiderivative",
            "expr": str(expr),
            "result": str(F),
            "verification": str(check),
            "verdict": "PASS" if check == 0 else "FAIL (derivative does not match)",
        }
    val = sp.integrate(expr, (syms[args.var], sp.sympify(args.lo), sp.sympify(args.hi)))
    return {
        "kind": "definite_integral",
        "expr": str(expr),
        "var": args.var,
        "lo": args.lo,
        "hi": args.hi,
        "value": str(val),
    }


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="harness.sympy_check")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_id = sub.add_parser("identity", help="check lhs - rhs simplifies to 0")
    p_id.add_argument("--lhs", required=True)
    p_id.add_argument("--rhs", required=True)
    p_id.add_argument("--vars", nargs="+", required=True)
    p_id.add_argument("--domain", default="real", choices=["real", "positive", "integer", "complex"])
    p_id.set_defaults(handler=cmd_identity)

    p_in = sub.add_parser("inequality", help="random sample test of an inequality")
    p_in.add_argument("--lhs", required=True)
    p_in.add_argument("--rhs", required=True)
    p_in.add_argument("--vars", nargs="+", required=True)
    p_in.add_argument("--op", default="le", choices=["le", "lt", "ge", "gt"])
    p_in.add_argument("--domain", default="real", choices=["real", "positive", "integer", "complex"])
    p_in.add_argument("--samples", type=int, default=200)
    p_in.add_argument("--seed", type=int, default=12345)
    p_in.add_argument("--lo", type=float, default=-100.0)
    p_in.add_argument("--hi", type=float, default=100.0)
    p_in.set_defaults(handler=cmd_inequality)

    p_lim = sub.add_parser("limit")
    p_lim.add_argument("--expr", required=True)
    p_lim.add_argument("--var", required=True)
    p_lim.add_argument("--to", required=True)
    p_lim.add_argument("--direction", default="+-", choices=["+", "-", "+-"])
    p_lim.add_argument("--domain", default="real", choices=["real", "positive", "integer", "complex"])
    p_lim.set_defaults(handler=cmd_limit)

    p_int = sub.add_parser("integrate")
    p_int.add_argument("--expr", required=True)
    p_int.add_argument("--var", required=True)
    p_int.add_argument("--lo", default=None)
    p_int.add_argument("--hi", default=None)
    p_int.add_argument("--domain", default="real", choices=["real", "positive", "integer", "complex"])
    p_int.set_defaults(handler=cmd_integrate)

    args = parser.parse_args(argv)
    result = args.handler(args)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
