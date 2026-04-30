# Lebl — Basic Analysis I (Volume I)

**Source:** Jiří Lebl, *Basic Analysis I: Introduction to Real Analysis, Volume I*, version 6.2 (May 2025)
**License:** CC BY-NC-SA 4.0 / CC BY-SA 4.0 (dual)
**Upstream:** https://www.jirka.org/ra/ — PDF: https://www.jirka.org/ra/realanal.pdf

This is a **deep reference** — the full extracted text of Lebl Vol I, chunked by
theorem/definition/proposition for fast lookup. Use it when the hand-written
digest in `real-analysis-foundations.md` is not specific enough.

## How to use

1. Find the result you need in `lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-manifest.md` (full chunk index).
2. Read the specific chunk file, e.g. `lebl-basic-analysis-vol1/lebl-basic-analysis-vol1-theorem-2-3-1.md`.
3. Cite as **Lebl, *Basic Analysis I*, Theorem 2.3.1** (the chunk filename encodes chapter.section.item).

## Coverage (chapters 0–7)

| Chapter | Topic | Useful for |
|---|---|---|
| 0 | Basic set theory, functions, cardinality | Foundations, countability |
| 1 | Real numbers — order, completeness, suprema, abs value, intervals | LUB property, Archimedean property |
| 2 | Sequences and series — limits, monotone, Cauchy, lim sup/inf, Bolzano–Weierstrass, series tests | Convergence proofs, sequence ε-N work |
| 3 | Continuous functions — limits, continuity, IVT, EVT, uniform continuity | Continuity ε-δ, compactness arguments |
| 4 | Derivatives — MVT, L'Hôpital, Taylor's theorem, inverse function theorem | Differentiation proofs |
| 5 | Riemann integral — Darboux sums, FTC, change of variables, log/exp | Integration on ℝ |
| 6 | Sequences and series of functions — uniform convergence, Weierstrass M-test, power series, Stone–Weierstrass | Uniform convergence, function spaces |
| 7 | Metric spaces — open/closed sets, completeness, compactness, continuity, connectedness | Metric topology, basis for functional analysis |

## Chunk inventory

- **332 theorem/definition chunks** (118 examples, 104 propositions, 71 definitions, 14 theorems, 13 lemmas, 12 corollaries) + preamble + manifest
- Total extracted text: ~1.9 MB PDF → ~660 KB markdown
- Engine: `pymupdf4llm` (Java JRE not available on this machine, so opendataloader-pdf was bypassed; see `setup/README.md`)
- Quality: most chunks PASS (≥0.9); a handful of large chunks flagged REVIEW or FAIL where theorem boundaries were ambiguous — useful as raw text but verify before quoting

## Relationship to existing references

- `real-analysis-foundations.md` — hand-written digest; route here first for quick orientation, then drill into Lebl chunks for the precise theorem/proof.
- `measure-integration.md`, `hilbert-banach-spaces.md`, etc. — Lebl Vol I covers prerequisites; Vol II (not yet ingested) covers the Lebesgue/multivariable extensions.
