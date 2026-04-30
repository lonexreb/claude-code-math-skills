# Reference proofs

Hand-written canonical solutions to seed benchmark problems. Each proof:

- Passes `python3 -m harness.proof_lint --proof proofs/<id>.md` with **zero CRITICAL or HIGH findings**.
- Cites theorems by name, with a chunk reference where one exists.
- Includes a "where each hypothesis is used" coda.
- Includes a tightness check (what breaks if a hypothesis is dropped).

These are the **rigor bar** for the harness output. When `/math-bench` produces a proof, the result should be at least this clean — ideally cleaner. Diff a fresh `/math-bench <id>` run against the corresponding reference proof to detect regressions.

## Index

| id | strategy | template | reference proof |
|---|---|---|---|
| `epsilon-delta-continuity` | direct ε–δ construction | `templates/proofs/epsilon-delta.md` | [epsilon-delta-continuity.md](epsilon-delta-continuity.md) |
| `lebl-3-1-7-cauchy-converges` | bounded ⇒ Bolzano-Weierstrass + Cauchy collapse | n/a (compositional) | [lebl-3-1-7-cauchy-converges.md](lebl-3-1-7-cauchy-converges.md) |
| `intermediate-value-bisection` | nested intervals + completeness | `templates/proofs/bisection.md` | [intermediate-value-bisection.md](intermediate-value-bisection.md) |
| `cauchy-schwarz-inner-product` | non-negative discriminant | `templates/proofs/discriminant.md` | [cauchy-schwarz-inner-product.md](cauchy-schwarz-inner-product.md) |

## Why hand-written, not harness-generated

The harness should be evaluated against a fixed standard. If the standard itself is harness output, regressions become invisible — both the bar and the test slip together. These proofs are the immutable target.

If a future improvement to the harness produces something *better* than one of these (shorter, clearer, with stronger citations), update the reference proof in a separate commit so the change is auditable.

## How to use these

- **As a writing model**: when authoring a new agent prompt or template, point it here and ask "produce output of this rigor".
- **As a critic input**: feed one of these to `math-critic` as a sanity check — the critic should `APPROVE` with no CRITICAL/HIGH findings. If it doesn't, the critic prompt has drifted.
- **As a regression baseline**: see "diff against `/math-bench` output" above.
