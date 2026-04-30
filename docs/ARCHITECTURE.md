# Architecture

## Goals

1. **Solve hard math problems with verifiable rigor** — not just "produce plausible-looking proofs". Every proof must survive an adversarial critic pass before it ships.
2. **Be Claude-Code-native** — agents and slash commands sit in `.claude/`, no SDK glue. A user can `git clone && claude .` and have a working harness.
3. **Be reproducible** — `/math-bench` writes a meta.json + proof.md per run. Changes to agent prompts can be A/B'd against the same problem set.
4. **Stay extensible** — adding a new domain (combinatorics references, ODE references) is a matter of dropping a new `.md` into `skills/formal-math-ai/references/` and adding a Domain Router row.

## Why subagents

Claude Code subagents have:

- their own context window,
- their own (optional) model and tool allowlist,
- a defined scope (`description`) so the orchestrator can route to them.

This matches the **separation of concerns** we want for a math harness:

| Concern | Where it lives |
|---|---|
| Strategy / planning | `math-strategist` (opus, no proof writing) |
| Construction | `math-prover` (opus, can read references) |
| Falsification | `math-counterexample-hunter` (sonnet) |
| Numerical sanity | `math-numeric-verifier` (haiku — cheap and fast) |
| Adversarial review | `math-critic` (opus, separate context — won't anchor on prover's framing) |
| Symbolic algebra | `math-symbol-runner` (sonnet, drives SymPy) |
| Formalization | `math-formalizer` (opus, emits Lean) |

Each agent has a single job and a tight prompt. The model tier matches the task: cheap models for sweeps and smoke tests, expensive ones for synthesis.

## Why a Generator–Critic loop

Single-shot proof generation is unreliable. The most robust pattern — borrowed from GAN harnesses, RLHF-style verifier loops, and AlphaProof-style search — is:

```
prover → critic → revise → critic → revise → … (bounded)
```

`math-critic` runs in its own context. It has not seen the prover's chain-of-thought; it sees only the final proof. That makes it a useful adversary: it can't be fooled by the same blind spot the prover has.

We bound the loop at 3 critic rounds. Past that, the harness reports the impasse rather than burning cycles.

## Why falsification before construction

For `∀`-claims, the *cheapest* failure mode is "the claim is false". Running `math-counterexample-hunter` and `math-numeric-verifier` in parallel before the prover spends opus tokens on construction is a strict cost win:

- If a counterexample exists, you find it and report a disproof.
- If none surfaces in the sweep, you've raised your prior on the claim and the prover writes more confidently.

We skip the sweep on `/math-prove` because the user has signaled commitment. We always run it on `/math-solve` and `/math-disprove`.

## Why a Lean formalizer

Most attempted formalizations of an informal proof end with `sorry` somewhere. That's fine. The point of `math-formalizer` is not to fully verify; it's to:

1. Force the prover's structure to typecheck at the level of statements (catches subtle hypothesis errors).
2. Produce a scaffold a human (or a future LLM with mathlib search) can complete.
3. Make the result *exportable* to a real proof assistant.

A `sorry`-bearing Lean file is a strictly better artifact than an English-only proof for downstream work.

## Why SymPy in the loop

Lots of "math problems" reduce to algebra. If the prover spends compute on simplifying `(sin² + cos²)³`, that's wasted. `math-symbol-runner` drives SymPy directly — exact computation in milliseconds — and feeds the result to the prover.

The numerical verifier (`math-numeric-verifier`) is similar in spirit but for non-symbolic claims (random sweeps, asymptotic checks).

## Knowledge skill

`skills/formal-math-ai/SKILL.md` is the **knowledge router**. When the strategist or prover needs to invoke a named theorem, they read the relevant entry from the Domain Router table and quote precisely.

The 334-chunk Lebl corpus under `references/lebl-basic-analysis-vol1/` gives theorem-level granularity — the prover can cite "(Lebl Vol I, Thm 3.4.5)" and the corresponding `.md` file contains the exact statement.

## Repository layout (full)

```
.
├── CLAUDE.md
├── LICENSE
├── README.md
├── requirements.txt
├── .claude/
│   ├── settings.json
│   ├── agents/
│   │   ├── math-strategist.md
│   │   ├── math-prover.md
│   │   ├── math-counterexample-hunter.md
│   │   ├── math-numeric-verifier.md
│   │   ├── math-critic.md
│   │   ├── math-formalizer.md
│   │   └── math-symbol-runner.md
│   └── commands/
│       ├── math-solve.md
│       ├── math-prove.md
│       ├── math-disprove.md
│       ├── math-check.md
│       ├── math-formalize.md
│       └── math-bench.md
├── skills/
│   └── formal-math-ai/
│       ├── SKILL.md
│       ├── references/        # 16 hand-written digests + 334-chunk Lebl corpus
│       └── setup/             # PDF→md ingestion pipeline
├── harness/
│   ├── __init__.py
│   ├── sympy_check.py         # symbolic / numeric smoke tests CLI
│   ├── lean_stub.py           # Lean 4 skeleton emitter
│   └── run_bench.py           # benchmark runner scaffold
├── benchmarks/
│   ├── README.md
│   ├── problems/              # input problems
│   └── runs/                  # output reports (gitignored)
└── docs/
    ├── ARCHITECTURE.md        # this file
    └── ROADMAP.md
```

## Extension points

- **Add an agent** — drop a new `.md` under `.claude/agents/`. Wire it into a slash command if the orchestrator should call it.
- **Add a reference** — drop a new `.md` under `skills/formal-math-ai/references/`, add a Domain Router row to `SKILL.md`, log the source in `references/SOURCES.md`.
- **Add a slash command** — drop a new `.md` under `.claude/commands/`. Most commands are short orchestrators that call existing agents in a different order.
- **Add MCP servers** — Lean MCP and SymPy MCP are obvious next steps. Wire them into `.claude/settings.json` and the relevant agent's `tools:` list.

## Non-goals

- We do **not** try to build a full theorem-proving search loop (LeanDojo / AlphaProof scale). The formalizer emits scaffolds, not closed proofs.
- We do **not** implement cross-validation against external solvers (Z3, etc) at the harness level — it can be added per-agent if a problem warrants.
- We do **not** parallelize across multiple solvers for self-consistency voting in v1. That's a future extension.
