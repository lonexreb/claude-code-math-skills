---
description: Explain a math concept, theorem, or technique using the formal-math-ai skill references — no proof generation, no critic loop. Use for "what is X / state Y / explain Z" queries that don't need the full harness.
argument-hint: <concept, theorem, or technique to explain>
allowed-tools: Read, Grep, Glob
---

# /math-explain

The user wants an explanation, not a proof. Skip the harness; consult the skill directly.

## Topic

$ARGUMENTS

## Procedure

1. **Find the relevant reference file(s).** Read `skills/formal-math-ai/SKILL.md` Domain Router. For each domain row that touches the topic, identify the linked reference file.
2. **Read those reference files.** For real analysis, also grep the Lebl chunks under `skills/formal-math-ai/references/lebl-basic-analysis-vol1/` for the specific theorem or definition.
3. **Compose the explanation.** Structure:

```markdown
# <Topic>

## Statement (if a theorem)
**Theorem (<Name>).** Let … . Then … .

## Hypotheses, in plain English
- Hypothesis 1: what it says, why it matters.
- Hypothesis 2: …

## Conclusion, in plain English
…

## Why it's true (intuition only — not a proof)
2–4 sentence sketch of the key idea.

## Where it's used
- Application 1: …
- Application 2: …

## Common confusions
- Pitfall 1: …
- Pitfall 2: …

## References consulted
- skills/formal-math-ai/references/<file>.md
- skills/formal-math-ai/references/<chunk>.md
```

## Rules

- ❌ Do not write a full rigorous proof. If the user wants a proof, they should use `/math-prove`.
- ❌ Do not invent named theorems. If you can't find the result in the references, say so and suggest where it might live.
- ✅ Do quote the formal statement verbatim from the references when one exists.
- ✅ Do mention the textbook section / theorem id (e.g. "Lebl Vol I, Thm 3.4.5") so the user can dig deeper.
- ✅ Do flag if the topic is non-trivial enough to warrant a proof — offer to follow up with `/math-prove`.

## Length

Aim for under 400 words. This is a quick lookup, not a lecture.
