---
description: Translate an informal proof into a Lean 4 (mathlib) skeleton. Produces a checkable scaffold even when full automation isn't possible.
argument-hint: <proof text or path to .md file>
allowed-tools: Read, Write, Bash, Agent
---

# /math-formalize

## Proof to formalize

$ARGUMENTS

(If `$ARGUMENTS` is a path, read it.)

## Pipeline

1. (Optional) Run `math-critic` first if the proof hasn't been audited. A formalization of a wrong proof is wasted effort.
2. **`math-formalizer`** — emit a Lean 4 file with `theorem` statement, mirrored proof structure, named subgoals, and `sorry` placeholders.
3. If a Lean toolchain is available (check via `which lean`), attempt `lake env lean <file>` and report the typecheck status.

## Final response shape

```markdown
# Formalization

## Lean 4 file
```lean
…
```

## Subgoals (sorrys)
- Line N: `<what's needed>`
- …

## Toolchain
Typechecked: yes / no (reason).
```

If Lean isn't installed, recommend the user install via `elan` and `lake`:
```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
elan default leanprover/lean4:stable
```
