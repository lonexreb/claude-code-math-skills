"""Unit tests for harness.proof_lint."""
from __future__ import annotations

import pytest

from harness.proof_lint import lint, build_reference_index


def _ref_index_with_lebl():
    # Pretend lebl chunks exist
    return {
        "lebl": [
            "lebl-basic-analysis-vol1-theorem-3-4-5.md",
            "lebl-basic-analysis-vol1-definition-2-1-1.md",
        ],
    }


def test_clean_proof_no_findings():
    proof = (
        "# Proof\n"
        "Let ε > 0 be arbitrary.\n"
        "Set δ = ε / 2; then δ > 0.\n"
        "Let x ∈ ℝ with |x − c| < δ.\n"
        "Then |f(x) − f(c)| ≤ 2|x − c| < ε. Done.\n"
    )
    result = lint(proof, claim_text=None, reference_index={})
    # the only thing that *could* trip is the ∀ check, but the proof
    # contains 'Let' introductions, so it shouldn't fire.
    assert result["summary"]["CRITICAL"] == 0
    assert result["summary"]["HIGH"] == 0


def test_filler_clearly_flagged():
    result = lint("Clearly x > 0.\n", None, {})
    assert any(f["category"] == "filler" and "clearly" in f["message"].lower()
               for f in result["findings"])


def test_unnamed_citation_flagged_high():
    proof = "By a standard result, x = 0.\n"
    result = lint(proof, None, {})
    sevs = [f["severity"] for f in result["findings"] if f["category"] == "filler"]
    assert "HIGH" in sevs


def test_unknown_author_citation_flagged_high():
    proof = "By (Bogus, Thm 1.1), the claim holds.\n"
    result = lint(proof, None, _ref_index_with_lebl())
    cit = [f for f in result["findings"] if f["category"] == "citation"]
    assert cit, "expected a citation finding"
    assert cit[0]["severity"] == "HIGH"


def test_known_author_unknown_id_flagged_medium():
    proof = "By (Lebl Vol I, Thm 99.99.99), the claim holds.\n"
    result = lint(proof, None, _ref_index_with_lebl())
    cit = [f for f in result["findings"] if f["category"] == "citation"]
    assert cit, "expected a citation finding"
    assert cit[0]["severity"] == "MEDIUM"


def test_known_author_known_id_clean():
    proof = "By (Lebl Vol I, Thm 3.4.5), continuity follows.\n"
    result = lint(proof, None, _ref_index_with_lebl())
    cit = [f for f in result["findings"] if f["category"] == "citation"]
    assert cit == []


def test_universal_quantifier_without_intro_flagged():
    proof = "For all x, x² ≥ 0 by squaring.\n"  # no "Let x" intro
    result = lint(proof, None, {})
    assert any(f["category"] == "quantifier" and f["severity"] == "HIGH"
               for f in result["findings"])


def test_existence_with_witness_clean():
    proof = (
        "Let x ∈ ℝ be arbitrary.\n"
        "There exists N such that for n ≥ N, |aₙ − L| < ε.\n"
        "Set N = ⌈1/ε⌉.\n"
    )
    result = lint(proof, None, {})
    quant_high = [f for f in result["findings"]
                  if f["category"] == "quantifier" and f["severity"] == "HIGH"]
    # 'Set N = ...' counts as a witness via the named-witness pattern
    assert quant_high == [] or all("existence" not in f["message"] for f in quant_high)


def test_summary_counts_match_findings():
    proof = "Clearly x > 0. By a standard result, y = 0.\n"
    result = lint(proof, None, {})
    counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for f in result["findings"]:
        counts[f["severity"]] += 1
    assert counts == result["summary"]


def test_build_reference_index_smoke(tmp_path):
    refdir = tmp_path / "refs"
    refdir.mkdir()
    (refdir / "lebl-basic-analysis-vol1-theorem-3-4-5.md").write_text("...")
    (refdir / "axler-mira-thm-2-1-1.md").write_text("...")
    idx = build_reference_index(refdir)
    assert "lebl" in idx
    assert "axler" in idx
    assert any("3-4-5" in f for f in idx["lebl"])


def test_build_reference_index_missing_dir():
    from pathlib import Path
    idx = build_reference_index(Path("/nonexistent/path/does/not/exist"))
    assert idx == {}
