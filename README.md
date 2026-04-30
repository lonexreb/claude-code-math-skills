# claude-code-math-skills

[![ci](https://github.com/lonexreb/claude-code-math-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/lonexreb/claude-code-math-skills/actions/workflows/ci.yml)

A Claude Code harness for solving rigorous math problems with agentic AI.

This repo bundles:

- A **knowledge skill** (`skills/formal-math-ai/`) covering real & functional analysis, measure theory, operator theory, computer vision, GPU programming, generative AI, and formal verification — backed by a 334-chunk corpus from Lebl's *Basic Analysis I*.
- A **subagent roster** (`.claude/agents/`) with seven specialized math agents.
- **Slash commands** (`.claude/commands/`) that orchestrate those agents into a Generator–Critic loop.
- **Python helpers** (`harness/`) for symbolic verification (SymPy), Lean skeleton emission, and benchmark runs.
- A small **benchmark suite** (`benchmarks/`) of Putnam, IMO, and textbook problems.

## Quick start

```bash
git clone https://github.com/lonexreb/claude-code-math-skills.git
cd claude-code-math-skills

python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Open in Claude Code
claude .
```

Once Claude Code is running in this directory, the agents and commands load automatically. Try:

```
/math-solve Prove that every Cauchy sequence in ℝ converges.
```

## The harness

When the user poses a math problem, the orchestrator routes through agents instead of answering from memory:

```
┌──────────────────┐
│  user problem    │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ math-strategist  │  domain classification + 2–4 candidate strategies
└────────┬─────────┘
         │
   ┌─────┴─────────────────────────────┐
   ▼                                   ▼
┌────────────────────────┐   ┌───────────────────────┐
│ counterexample-hunter  │   │ numeric-verifier      │  (in parallel; cheap falsification)
└──────────┬─────────────┘   └─────────┬─────────────┘
           │                           │
           └─────────────┬─────────────┘
                         ▼
            ┌──────────────────────────┐
            │ symbol-runner (optional) │  SymPy precomputation
            └────────────┬─────────────┘
                         ▼
            ┌──────────────────────────┐
            │      math-prover         │  generates the proof
            └────────────┬─────────────┘
                         ▼
            ┌──────────────────────────┐
            │      math-critic         │  ◀──┐ adversarial review
            └────────────┬─────────────┘     │
                         │                   │ revise
                         ├───────────────────┘
                         ▼ (APPROVE)
            ┌──────────────────────────┐
            │ math-formalizer (optional│  Lean 4 / mathlib skeleton
            └──────────────────────────┘
```

## Agents

| Agent | Model | Responsibility |
|---|---|---|
| `math-strategist` | opus | Domain classification, 2–4 candidate strategies, recommended path. |
| `math-prover` | opus | Rigorous proof generation with named theorem citations. |
| `math-counterexample-hunter` | sonnet | Adversarial: tries to falsify the claim with edge cases / pathologies / hypothesis-drop sweep. |
| `math-numeric-verifier` | haiku | Fast SymPy/numpy smoke test for claims with concrete numerical content. |
| `math-critic` | opus | Independent adversarial review of a written proof; severity-classified findings. |
| `math-formalizer` | opus | Translates approved proof into Lean 4 / mathlib skeleton. |
| `math-symbol-runner` | sonnet | SymPy step-by-step algebra for derivatives, integrals, identities. |

## Slash commands

| Command | Purpose |
|---|---|
| `/math-solve <problem>` | End-to-end pipeline: strategy → falsification sweep → proof → critic loop → optional formalization. |
| `/math-prove <claim>` | Lighter pipeline; user is committed to the claim being true. |
| `/math-disprove <claim>` | Counterexample-first pipeline. |
| `/math-check <proof>` | Audit-only pass via the critic. |
| `/math-formalize <proof>` | Lean 4 skeleton emission. |
| `/math-bench <id\|all>` | Run the harness on benchmark problems and record reproducible reports. |
| `/math-solve-deep <problem> [--branches N]` | Self-consistency mode: spawns N parallel strategist→prover branches, ranks them by critic verdict, refines the winner. Reserve for hard problems. |

## Knowledge base

`skills/formal-math-ai/SKILL.md` contains a 7-domain router pointing at:

- 16 hand-written reference digests under `references/*.md`
- A 334-chunk theorem-level corpus from Lebl's *Basic Analysis I* under `references/lebl-basic-analysis-vol1/`

To extend: see `skills/formal-math-ai/setup/README.md` for the PDF→markdown ingestion pipeline.

## Benchmarks

`benchmarks/problems/` ships with seed problems across domains:

- `lebl-3-1-7-cauchy-converges.md` — every Cauchy sequence in ℝ converges (textbook classic)
- `epsilon-delta-continuity.md` — show f(x)=x² is continuous at every point
- `putnam-2023-a1.md` — combinatorics warm-up
- `imo-2023-p1.md` — number theory
- `dominated-convergence-application.md` — Lebesgue + interchange of limits

Run all benchmarks with `/math-bench all`. Reports land in `benchmarks/runs/<id>__<ts>/`.

## Adding more knowledge

The `setup/convert_pdfs.py` pipeline ingests open-access textbook PDFs into theorem-level chunks. Recommended next ingestions are tracked in `skills/formal-math-ai/references/SOURCES.md` (Axler MIRA, Lebl Vol II, Erdman, Szeliski, …).

## Repository layout

```
.
├── CLAUDE.md                       # project rules / harness routing
├── LICENSE                         # MIT (textbook content per SOURCES.md)
├── README.md                       # this file
├── requirements.txt
├── .claude/
│   ├── settings.json               # hooks + permission allow-list
│   ├── agents/                     # 7 math subagents
│   └── commands/                   # 6 slash commands
├── skills/
│   └── formal-math-ai/             # knowledge skill (SKILL.md + references/)
├── harness/                        # Python helpers (sympy_check, lean_stub, run_bench)
├── benchmarks/
│   ├── problems/                   # benchmark inputs
│   └── runs/                       # reproducible run reports (gitignored)
└── docs/
```

## Status

This is an active project. Expect rough edges in the agent prompts; tune them and run `/math-bench all` to verify you didn't regress.

## License

MIT for the harness code. Textbook reference content under `skills/formal-math-ai/references/` retains its upstream license — see [`SOURCES.md`](skills/formal-math-ai/references/SOURCES.md).
