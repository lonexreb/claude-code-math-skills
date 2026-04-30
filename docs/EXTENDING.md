# Extending the harness

How to add an agent, a slash command, a benchmark problem, a textbook reference, or a new harness CLI utility — without breaking what's there.

All paths in this guide are relative to the repo root.

## Add an agent

Drop a new `.md` file under `.claude/agents/`. The filename (without extension) is the agent's name; the `Agent` tool can invoke it via `subagent_type: "<name>"`.

### Frontmatter

```yaml
---
name: math-<role>          # kebab-case, must match filename
description: >             # one-paragraph; this is what the orchestrator
  reads when deciding to invoke the agent. Be specific about
  what the agent does AND what it doesn't.
model: opus | sonnet | haiku    # match tier to task: opus = synthesis,
                                # sonnet = balanced, haiku = cheap sweeps
tools: Read, Grep, Glob, Bash, Write    # tight allowlist; fewer is better
---
```

### Body

Body is a system-prompt-style instruction. Patterns from the existing roster:

- **State the role in one sentence**: "You are an adversarial reviewer …".
- **List inputs explicitly**: what the orchestrator passes you.
- **Operating procedure**: numbered steps the agent must execute.
- **Hard rules**: ❌ banned moves and ✅ required moves.
- **Output format**: the exact markdown shape the agent must return.

Keep it under ~250 lines. Larger prompts dilute focus.

### Wire it into a command

Edit `.claude/commands/<existing>.md` to invoke your new agent at the right step, or create a new command that uses it (see below).

### Test

Add a benchmark that exercises the agent's failure mode (e.g. for a new `math-graph-theorist`, add a Putnam combinatorics problem). Run `/math-bench all` and compare the resulting `benchmarks/runs/*/report.md` against the previous baseline.

---

## Add a slash command

Drop a `.md` under `.claude/commands/`. The filename (without extension) is the command name (`/math-foo` → `.claude/commands/math-foo.md`).

### Frontmatter

```yaml
---
description: <one-line; shown in the slash-command picker>
argument-hint: <hint for $ARGUMENTS, e.g. "<problem statement>" or "<id>">
allowed-tools: Read, Write, Bash, Glob, Grep, Agent
---
```

### Body

The body is read as instructions when the user types `/<name>`. Inside, `$ARGUMENTS` is replaced with whatever the user passed.

Pattern from the existing commands:

1. State the goal in one paragraph.
2. Describe each step of the pipeline, naming the agent invoked at each step.
3. Specify the response shape.
4. Add a "When NOT to use this command" section to keep dispatch clean.

---

## Add a benchmark problem

Drop a `.md` under `benchmarks/problems/`. The filename's stem is the benchmark id (`benchmarks/problems/foo-bar.md` → id `foo-bar`).

### Required schema

```markdown
---
id: <slug>                          # required; must match filename
domain: <real-analysis | …>         # required; pick from domains used
difficulty: <1–5>                   # required
source: <where the problem comes from>   # required
formalize: <true|false>             # whether /math-bench should also emit Lean
---

# <Title>

## Problem
<the actual problem statement, formal or informal>

## Reference solution (optional)
<a sketch — not fed to the harness, used for human review>

## Notes (optional)
<gotchas, common wrong proofs, what makes this benchmark interesting>
```

CI validates that every problem has the four required frontmatter keys plus a `## Problem` section. See `.github/workflows/ci.yml` job `validate-benchmarks`.

### Choosing difficulty

| difficulty | typical problem |
|---|---|
| 1 | direct definition unwinding (sqrt-2-irrational) |
| 2 | textbook classics with one named theorem invocation |
| 3 | multi-step constructions (Banach fixed-point, Bolzano–Weierstrass) |
| 4 | requires choosing among multiple non-obvious strategies (DCT application, Putnam) |
| 5 | research-style or olympiad-grade (IMO, USAMO) |

### Add a reference proof (optional but recommended)

If the benchmark is in your sweet spot, hand-write a canonical solution under `proofs/<id>.md`. Make sure it passes `python3 -m harness.proof_lint --proof proofs/<id>.md` with zero CRITICAL/HIGH findings (the CI gate enforces this).

---

## Add a textbook reference

Use the existing PDF→markdown pipeline:

```bash
python3 skills/formal-math-ai/setup/convert_pdfs.py \
    -i ~/Downloads/<book>.pdf \
    --output-dir skills/formal-math-ai/references/ \
    --chunk --chunk-strategy theorem \
    --provenance skills/formal-math-ai/references/SOURCES.md
```

Then:

1. Verify quality with `python3 skills/formal-math-ai/setup/validate.py skills/formal-math-ai/references/<chunk-dir>/`.
2. Add a Domain Router row in `skills/formal-math-ai/SKILL.md` pointing at the new digest and chunk directory.
3. Confirm the source URL and license in `skills/formal-math-ai/references/SOURCES.md`.

The chunker emits files of the form `<book-slug>-<kind>-<id>.md` (e.g. `axler-mira-theorem-2-1-1.md`). The `harness/citation_resolve.py` resolver maps `(Axler, Thm 2.1.1)` → that file as long as the slug `axler` matches the first dash-separated token of the filename.

If the upstream PDF requires a Java Runtime (some opendataloader-pdf paths do), the pipeline auto-falls-back to `pymupdf4llm`; quality is recorded in the `engine` column of `SOURCES.md`.

---

## Add a harness CLI utility

Create `harness/<name>.py` following the pattern of `sympy_check.py` / `lean_stub.py` / `proof_lint.py`:

- `from __future__ import annotations` at the top.
- An `argparse` `main(argv: list[str] | None = None) -> int` function.
- `if __name__ == "__main__": sys.exit(main())` so `python3 -m harness.<name>` works.
- Output JSON or a stable plain-text format — agents will parse it.
- No third-party deps unless added to `requirements.txt`.

### Test

Add `tests/test_<name>.py`. The CI matrix runs Python 3.10/3.11/3.12, so avoid version-only features (`datetime.UTC` is 3.11+ — use `datetime.timezone.utc`).

### Wire into an agent

Edit the relevant agent's `.md` to mention the new utility under "Operating procedure". Existing examples:

- `math-numeric-verifier` invokes `harness.sympy_check`
- `math-formalizer` invokes `harness.lean_stub`
- `math-critic` invokes `harness.proof_lint` and `harness.citation_resolve`

---

## Add an MCP server (future work)

Roadmapped in `docs/ROADMAP.md`. The pattern: register the server in `.claude/settings.json`, then list its tool prefix (`mcp__<server>__*`) in the relevant agent's `tools:` allowlist.

A SymPy MCP server would let `math-symbol-runner` keep state across calls instead of paying subprocess startup per query. A Lean LSP MCP would let `math-formalizer` typecheck incrementally.

These aren't shipped yet because Bash subprocess works fine for the current scale — add MCP only when subprocess overhead becomes the bottleneck.
