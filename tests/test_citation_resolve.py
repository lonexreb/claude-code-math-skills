"""Unit tests for harness.citation_resolve."""
from __future__ import annotations

import io
import json
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

import pytest

from harness import citation_resolve as cr
from harness.proof_lint import _CITATION_RE


@pytest.fixture
def fake_refs(tmp_path):
    refdir = tmp_path / "references"
    chunks = refdir / "lebl-basic-analysis-vol1"
    chunks.mkdir(parents=True)
    (chunks / "lebl-basic-analysis-vol1-theorem-3-4-5.md").write_text("# Thm 3.4.5\n")
    (chunks / "lebl-basic-analysis-vol1-corollary-1-3-3.md").write_text("# Cor 1.3.3\n")
    (chunks / "lebl-basic-analysis-vol1-definition-3-2-1.md").write_text("# Def 3.2.1\n")
    return refdir


def _run(argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        rc = cr.main(argv)
    return rc, out.getvalue(), err.getvalue()


def test_open_resolves_known(fake_refs):
    rc, out, _ = _run([
        "open", "--citation", "(Lebl Vol I, Thm 3.4.5)",
        "--references", str(fake_refs),
    ])
    assert rc == 0
    assert out.strip().endswith("lebl-basic-analysis-vol1-theorem-3-4-5.md")


def test_open_resolves_corollary(fake_refs):
    rc, out, _ = _run([
        "open", "--citation", "(Lebl Vol I, Cor 1.3.3)",
        "--references", str(fake_refs),
    ])
    assert rc == 0
    assert out.strip().endswith("lebl-basic-analysis-vol1-corollary-1-3-3.md")


def test_open_resolves_definition(fake_refs):
    rc, out, _ = _run([
        "open", "--citation", "(Lebl Vol I, Definition 3.2.1)",
        "--references", str(fake_refs),
    ])
    assert rc == 0
    assert "definition-3-2-1.md" in out


def test_open_unknown_author_returns_1(fake_refs):
    rc, _, err = _run([
        "open", "--citation", "(Bogus Vol I, Thm 1.1)",
        "--references", str(fake_refs),
    ])
    assert rc == 1
    assert "no chunk found" in err


def test_open_malformed_citation_returns_2(fake_refs):
    rc, _, err = _run([
        "open", "--citation", "see Lebl theorem somewhere",
        "--references", str(fake_refs),
    ])
    assert rc == 2
    assert "does not match" in err


def test_list_table_form(tmp_path, fake_refs):
    proof = tmp_path / "proof.md"
    proof.write_text(
        "By (Lebl Vol I, Thm 3.4.5) we have continuity.\n"
        "By (Bogus, Thm 1.1) something else.\n"
    )
    rc, out, _ = _run([
        "list", "--proof", str(proof), "--references", str(fake_refs),
    ])
    # 1 unresolved citation present → exit 1
    assert rc == 1
    assert "(Lebl Vol I, Thm 3.4.5)" in out
    assert "lebl-basic-analysis-vol1-theorem-3-4-5.md" in out
    assert "(Bogus, Thm 1.1)" in out
    assert "UNRESOLVED" in out


def test_list_json_form(tmp_path, fake_refs):
    proof = tmp_path / "proof.md"
    proof.write_text("By (Lebl Vol I, Thm 3.4.5) we are done.\n")
    rc, out, _ = _run([
        "list", "--proof", str(proof), "--references", str(fake_refs),
        "--json",
    ])
    assert rc == 0
    payload = json.loads(out)
    assert isinstance(payload, list)
    assert payload[0]["author"] == "Lebl"
    assert payload[0]["kind"] == "theorem"
    assert payload[0]["id"] == "3.4.5"
    assert payload[0]["resolved"].endswith("theorem-3-4-5.md")


def test_list_no_citations_returns_0(tmp_path, fake_refs):
    proof = tmp_path / "proof.md"
    proof.write_text("Just prose, no citations.\n")
    rc, out, _ = _run([
        "list", "--proof", str(proof), "--references", str(fake_refs),
    ])
    assert rc == 0
    assert "no citations" in out


def test_citation_regex_accepts_trailing_punctuation():
    """Regression: the cauchy proof writes (Lebl Vol I, Thm 2.3.7.) with a
    period inside the parens. The regex must accept that form."""
    text = "By (Lebl Vol I, Thm 2.3.7.) the result follows."
    matches = list(_CITATION_RE.finditer(text))
    assert len(matches) == 1
    assert matches[0].group("author") == "Lebl"
    assert matches[0].group("id") == "2.3.7"


def test_citation_regex_no_trailing_punctuation():
    text = "By (Lebl, Thm 2.3.7) the result follows."
    matches = list(_CITATION_RE.finditer(text))
    assert len(matches) == 1
    assert matches[0].group("id") == "2.3.7"
