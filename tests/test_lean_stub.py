"""Unit tests for harness.lean_stub."""
from __future__ import annotations

import json

import pytest

from harness.lean_stub import render


def test_render_minimal_emits_sorry():
    plan = {
        "name": "trivial",
        "imports": ["Mathlib.Tactic"],
        "binders": "(n : ℕ)",
        "conclusion": "n + 0 = n",
    }
    out = render(plan)
    assert "import Mathlib.Tactic" in out
    assert "theorem trivial" in out
    assert "(n : ℕ)" in out
    assert "n + 0 = n" in out
    assert "sorry" in out


def test_render_with_steps_and_conclude():
    plan = {
        "name": "midpoint_strictly_between",
        "imports": ["Mathlib.Order.Basic"],
        "binders": "(a b : ℝ) (h : a < b)",
        "conclusion": "∃ c, a < c ∧ c < b",
        "informal": "Take c = (a+b)/2.",
        "steps": [
            {"name": "h1", "type": "a < (a+b)/2", "comment": "since a < b",
             "proof": "by linarith"},
            {"name": "h2", "type": "(a+b)/2 < b", "comment": "since a < b",
             "proof": "by linarith"},
        ],
        "conclude": "⟨(a+b)/2, h1, h2⟩",
    }
    out = render(plan)
    assert "have h1 : a < (a+b)/2 := by linarith" in out
    assert "have h2 : (a+b)/2 < b := by linarith" in out
    assert "exact ⟨(a+b)/2, h1, h2⟩" in out
    # informal docstring lands in the /-- ... -/ block
    assert "Take c = (a+b)/2." in out
    # no `sorry` since each step has a real proof and the conclude is concrete
    assert "sorry" not in out


def test_render_open_decls():
    plan = {
        "name": "f",
        "open": ["Real", "Topology"],
        "binders": "",
        "conclusion": "True",
    }
    out = render(plan)
    assert "open Real Topology" in out


def test_render_default_imports_when_omitted():
    plan = {"name": "t", "binders": "", "conclusion": "True"}
    out = render(plan)
    # The default imports include Mathlib.Tactic.
    assert "import Mathlib.Tactic" in out
