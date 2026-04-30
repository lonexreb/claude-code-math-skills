"""Unit tests for harness.sympy_check.

These exercise the four subcommands as Python (not subprocess) to keep
test runtime tight. The CLI surface is also lightly smoke-tested.
"""
from __future__ import annotations

import io
import json
import sys
from contextlib import redirect_stdout

import pytest

from harness import sympy_check as sc


def _run(argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = sc.main(argv)
    return rc, json.loads(buf.getvalue())


# --------------------------------------------------------------------- #
# identity
# --------------------------------------------------------------------- #

def test_identity_holds():
    rc, out = _run(["identity", "--lhs", "sin(x)**2 + cos(x)**2",
                    "--rhs", "1", "--vars", "x"])
    assert rc == 0
    assert out["holds"] is True
    assert out["verdict"] == "PASS"


def test_identity_fails():
    rc, out = _run(["identity", "--lhs", "x + 1", "--rhs", "x", "--vars", "x"])
    assert rc == 0
    assert out["holds"] is False
    assert out["verdict"] == "FAIL"


# --------------------------------------------------------------------- #
# inequality
# --------------------------------------------------------------------- #

def test_inequality_amgm_clean():
    # x² + 1 ≥ 2x for all real x (AM-GM-ish via (x-1)² ≥ 0)
    rc, out = _run([
        "inequality", "--lhs", "x**2 + 1", "--rhs", "2*x",
        "--vars", "x", "--op", "ge",
        "--samples", "50", "--seed", "42",
    ])
    assert rc == 0
    assert out["fails"] == []
    assert out["verdict"].startswith("PASS")


def test_inequality_finds_failure():
    # x ≥ 0 fails when x ranges over negatives
    rc, out = _run([
        "inequality", "--lhs", "x", "--rhs", "0",
        "--vars", "x", "--op", "ge",
        "--samples", "30", "--seed", "1",
        "--lo", "-10", "--hi", "10",
    ])
    assert rc == 0
    assert out["verdict"] == "FAIL"
    assert len(out["fails"]) >= 1


def test_inequality_two_variables():
    # x² + y² ≥ 2xy for all real x, y
    rc, out = _run([
        "inequality", "--lhs", "x**2 + y**2", "--rhs", "2*x*y",
        "--vars", "x", "y", "--op", "ge",
        "--samples", "100", "--seed", "7",
    ])
    assert rc == 0
    assert out["fails"] == []


# --------------------------------------------------------------------- #
# limit
# --------------------------------------------------------------------- #

def test_limit_sin_over_x():
    rc, out = _run(["limit", "--expr", "sin(x)/x", "--var", "x", "--to", "0"])
    assert rc == 0
    assert out["value"] == "1"


# --------------------------------------------------------------------- #
# integrate
# --------------------------------------------------------------------- #

def test_antiderivative_check():
    rc, out = _run(["integrate", "--expr", "2*x", "--var", "x"])
    assert rc == 0
    assert out["verdict"] == "PASS"


def test_definite_integral():
    rc, out = _run([
        "integrate", "--expr", "x", "--var", "x", "--lo", "0", "--hi", "1"
    ])
    assert rc == 0
    assert out["value"] == "1/2"
