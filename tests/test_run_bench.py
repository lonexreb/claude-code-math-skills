"""Unit tests for harness.run_bench.

These exercise init/record/list against a temporary mirror of the repo
layout so we don't write real artefacts under benchmarks/runs/.
"""
from __future__ import annotations

import io
import json
import sys
from contextlib import redirect_stdout

import pytest

from harness import run_bench as rb


@pytest.fixture(autouse=True)
def _isolate_runs(tmp_path, monkeypatch):
    """Redirect ROOT/PROBLEMS/RUNS/INDEX to a tmp scratch dir."""
    problems = tmp_path / "benchmarks" / "problems"
    runs = tmp_path / "benchmarks" / "runs"
    problems.mkdir(parents=True)
    runs.mkdir(parents=True)
    (problems / "demo.md").write_text("# demo\n## Problem\nProve 1 + 1 = 2.\n")
    monkeypatch.setattr(rb, "ROOT", tmp_path)
    monkeypatch.setattr(rb, "PROBLEMS", problems)
    monkeypatch.setattr(rb, "RUNS", runs)
    monkeypatch.setattr(rb, "INDEX", runs / "_index.md")
    yield


def _capture(argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = rb.main(argv)
    return rc, buf.getvalue().strip()


def test_list_lists_problems():
    rc, out = _capture(["list"])
    assert rc == 0
    ids = json.loads(out)
    assert ids == ["demo"]


def test_init_creates_run_dir_and_meta():
    rc, out = _capture(["init", "demo"])
    assert rc == 0
    rel = out
    run_dir = rb.ROOT / rel
    assert run_dir.exists()
    meta = json.loads((run_dir / "meta.json").read_text())
    assert meta["id"] == "demo"
    assert meta["finished_at"] is None
    assert meta["started_at"].endswith("+00:00")


def test_init_unknown_id_returns_2():
    rc, _ = _capture(["init", "does-not-exist"])
    assert rc == 2


def test_record_appends_index_row():
    _, rel = _capture(["init", "demo"])
    rc, out = _capture(["record", rel])
    assert rc == 0
    assert "recorded" in out

    index_text = (rb.RUNS / "_index.md").read_text()
    assert "| started_at | id | verdict | critic rounds | proof |" in index_text
    assert "| demo |" in index_text


def test_record_idempotent_for_finished_at():
    _, rel = _capture(["init", "demo"])
    _capture(["record", rel])
    meta1 = json.loads((rb.ROOT / rel / "meta.json").read_text())
    _capture(["record", rel])
    meta2 = json.loads((rb.ROOT / rel / "meta.json").read_text())
    assert meta1["finished_at"] == meta2["finished_at"]
