<!-- Thanks for the PR. -->

## Summary
<!-- One paragraph: what changed and why. -->

## Type of change

- [ ] new agent / agent prompt edit
- [ ] new slash command / command edit
- [ ] new benchmark
- [ ] new harness utility
- [ ] knowledge skill (references / digests)
- [ ] bugfix
- [ ] docs / CI / chore

## Checks

- [ ] `pytest -q` passes locally
- [ ] If you edited `proofs/*.md` or added one, `python3 -m harness.proof_lint --proof proofs/<file>.md` reports zero CRITICAL/HIGH findings
- [ ] If you edited an agent prompt, re-ran a relevant `/math-bench <id>` and the report didn't regress
- [ ] If you added a textbook reference, `SOURCES.md` row reflects the upstream license

## Related issues

<!-- e.g. closes #42 -->
