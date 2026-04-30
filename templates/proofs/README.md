# Proof templates

Skeletons for the five highest-frequency proof shapes the harness will encounter. The `math-prover` agent should adapt these to the specific problem rather than reinvent the structure each time.

| Template | When to use |
|---|---|
| `epsilon-delta.md` | Continuity, limits of functions, uniform continuity |
| `induction.md` | Statements parameterized by `n ∈ ℕ`, recursive structures |
| `contradiction.md` | "Show X" when assuming ¬X gives a tractable contradiction (irrationality, infinitude of primes, density) |
| `bisection.md` | Existence on a real interval via completeness (IVT, root finding) |
| `discriminant.md` | Inequalities derived from a non-negative real-valued quadratic (Cauchy–Schwarz, AM–GM via squares) |

Each template:

1. States the structural skeleton (the things that must appear, in order).
2. Lists the canonical pitfalls the critic flags on this shape.
3. Gives a worked micro-example.

The prover is **not** required to mention which template was used. The templates are scaffolding for the prover's own reasoning, not output-shaping.
