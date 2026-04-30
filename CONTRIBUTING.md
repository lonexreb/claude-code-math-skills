# Contributing

Thanks for your interest in `claude-code-math-skills`. This is a research-style harness, so contributions are lightweight: edit, test, push.

## Local setup

```bash
git clone https://github.com/lonexreb/claude-code-math-skills.git
cd claude-code-math-skills
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Run a smoke test on the SymPy CLI:

```bash
python3 -m harness.sympy_check identity --lhs "sin(x)**2 + cos(x)**2" --rhs "1" --vars x
```

## Editing an agent

Agents live in `.claude/agents/*.md`. Each file is read by Claude Code on session start. Frontmatter:

```yaml
---
name: <kebab-case>
description: <when the orchestrator should invoke this agent — be precise>
model: opus | sonnet | haiku            # optional, defaults to inheriting
tools: Read, Write, Bash, Grep, ...     # tight allowlist — fewer is better
---
```

After editing, regression-test by running `/math-bench all` and comparing reports under `benchmarks/runs/` against an earlier run.

## Adding a slash command

Drop a new `.md` under `.claude/commands/`. Frontmatter:

```yaml
---
description: <one line — what this command does>
argument-hint: <hint for $ARGUMENTS>
allowed-tools: Read, Write, Bash, Agent, ...
---
```

Body is the orchestrator script — Claude executes it as instructions when the user types `/<command-name>`.

## Adding a benchmark

1. Create `benchmarks/problems/<id>.md` with the schema in `benchmarks/README.md`.
2. Run `/math-bench <id>` to produce a baseline run under `benchmarks/runs/`.
3. Commit the problem file (do not commit the run output; runs are gitignored).

## Adding a textbook reference

Use the existing pipeline:

```bash
python3 skills/formal-math-ai/setup/convert_pdfs.py \
    -i ~/Downloads/book.pdf \
    --output-dir skills/formal-math-ai/references/ \
    --chunk --chunk-strategy theorem \
    --provenance skills/formal-math-ai/references/SOURCES.md
```

Then add a Domain Router row in `skills/formal-math-ai/SKILL.md`.

## Coding standards

- Python: standard PEP 8, type hints encouraged, no third-party deps without adding to `requirements.txt`.
- Markdown: no emojis in agent / command files unless the file is purely cosmetic.
- Don't add comments that explain *what* the code does — the code already says that. Add comments only for *why*.

## Pull requests

- Keep PRs focused: one agent edit, or one new benchmark, not a sprawling refactor.
- Include the diff in the runs index if the change might affect benchmark behaviour.
- No license-laundering of textbook content. Per-source licensing in `SOURCES.md` is binding.
