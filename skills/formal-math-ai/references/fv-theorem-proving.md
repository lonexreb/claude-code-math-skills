# Formal Verification: Theorem Proving

## Table of Contents
1. [Foundations: Type Theory and Logic](#foundations-type-theory-and-logic)
2. [Lean 4](#lean-4)
3. [Coq / Rocq](#coq--rocq)
4. [Isabelle/HOL](#isabellehol)
5. [Hoare Logic and Program Verification](#hoare-logic-and-program-verification)
6. [Separation Logic](#separation-logic)

---

## Foundations: Type Theory and Logic

### Curry-Howard Correspondence
Propositions = Types. Proofs = Programs.

| Logic | Type Theory |
|-------|-------------|
| Proposition P | Type P |
| Proof of P | Term of type P |
| P → Q (implication) | Function type P → Q |
| P ∧ Q (conjunction) | Product type P × Q |
| P ∨ Q (disjunction) | Sum type P + Q |
| ∀x:A, P(x) | Dependent function (x : A) → P x |
| ∃x:A, P(x) | Dependent pair Σ (x : A), P x |
| ¬P | P → False |
| True | Unit type (has exactly one inhabitant) |
| False | Empty type (has no inhabitants) |

### Dependent Types
Types that depend on values:
- Vec n α: vector of length n (length is in the type!)
- Fin n: natural numbers less than n
- (n : ℕ) → Vec n ℕ → ℕ: function taking a number and a vector of that length

This enables expressing precise specifications as types.

### Propositions as Types in Practice
To prove P → Q: write a function that takes a proof of P and returns a proof of Q.
To prove P ∧ Q: construct a pair (proof_of_P, proof_of_Q).
To prove ∃x, P(x): construct a pair (witness, proof_that_witness_satisfies_P).

---

## Lean 4

### Overview
- Dependently typed functional programming language AND proof assistant
- Created by Leonardo de Moura (Microsoft → AWS)
- Mathlib: largest formalized math library (150,000+ theorems)
- Fast: compiles to C, reasonable performance
- Metaprogramming: tactics written in Lean itself

### Basic Syntax
```lean
-- Define a function
def double (n : Nat) : Nat := 2 * n

-- State and prove a theorem
theorem double_zero : double 0 = 0 := by
  unfold double
  ring

-- Induction
theorem add_comm (m n : Nat) : m + n = n + m := by
  induction m with
  | zero => simp
  | succ m ih => simp [Nat.succ_add, ih]
```

### Common Tactics
| Tactic | What It Does |
|--------|-------------|
| `intro h` | Introduce hypothesis (for ∀ or →) |
| `apply f` | Apply function/theorem f to goal |
| `exact h` | Provide exact proof term |
| `rw [h]` | Rewrite using equation h |
| `simp` | Simplification using known lemmas |
| `ring` | Prove ring equations automatically |
| `omega` | Decide linear arithmetic over ℕ/ℤ |
| `linarith` | Linear arithmetic reasoning |
| `norm_num` | Evaluate numerical expressions |
| `constructor` | Split conjunction/existential goal |
| `cases h` | Case analysis on hypothesis |
| `induction n` | Structural induction |
| `contradiction` | Derive False from contradictory hypotheses |
| `ext` | Extensionality (functions, sets) |
| `funext` | Function extensionality |
| `have h : P := ...` | Introduce intermediate lemma |
| `calc` | Calculational proof chain |
| `aesop` | Automated reasoning (backtracking search) |

### Mathlib
The comprehensive formalized math library for Lean 4:
- 150,000+ lemmas and theorems
- Covers: algebra, analysis, topology, number theory, measure theory, category theory
- Import: `import Mathlib.Analysis.NormedSpace.Basic`
- Search: https://leanprover-community.github.io/mathlib4_docs/

### Example: Proving a Real Analysis Result in Lean
```lean
import Mathlib.Analysis.NormedSpace.Basic
import Mathlib.Topology.MetricSpace.Basic

-- Every convergent sequence is Cauchy
example {X : Type} [MetricSpace X] {s : ℕ → X} {a : X}
    (hs : Filter.Tendsto s Filter.atTop (nhds a)) :
    CauchySeq s := by
  exact hs.cauchySeq
```

---

## Coq / Rocq

### Overview
- One of the oldest proof assistants (1989)
- Based on Calculus of Inductive Constructions (CIC)
- Renamed to "Rocq" (2024), but Coq still widely used
- Software Foundations textbook series teaches Coq

### Basic Syntax
```coq
(* Define a function *)
Fixpoint double (n : nat) : nat :=
  match n with
  | O => O
  | S n' => S (S (double n'))
  end.

(* State and prove *)
Theorem double_zero : double 0 = 0.
Proof. reflexivity. Qed.

(* Induction *)
Theorem add_comm : forall n m : nat, n + m = m + n.
Proof.
  intros n m. induction n as [| n' IH].
  - simpl. rewrite Nat.add_0_r. reflexivity.
  - simpl. rewrite IH. rewrite Nat.add_succ_r. reflexivity.
Qed.
```

### Key Coq Tactics
`intros`, `apply`, `exact`, `rewrite`, `simpl`, `reflexivity`, `induction`,
`destruct`, `inversion`, `unfold`, `assert`, `auto`, `omega`, `lia`, `ring`.

### Software Foundations Volumes
1. **Logical Foundations (LF):** Basic logic, induction, lists, polymorphism
2. **Programming Language Foundations (PLF):** Operational semantics, type systems, Hoare logic
3. **Verified Functional Algorithms (VFA):** Sorting, BSTs, red-black trees — all verified
4. **QuickChick (QC):** Property-based testing in Coq
5. **Verifiable C (VC):** Verify real C programs using Verifiable C / VST
6. **Separation Logic Foundations (SLF):** Separation logic for heap-manipulating programs

---

## Isabelle/HOL

### Overview
- Based on Higher-Order Logic (HOL), simpler foundation than dependent types
- Extremely powerful automation (Sledgehammer, auto, simp)
- Large formal proof archive (AFP: 700+ entries)
- Isar proof language: human-readable structured proofs

### Isar Proof Style
```isabelle
theorem add_comm: "m + n = n + (m::nat)"
proof (induct m)
  case 0
  then show ?case by simp
next
  case (Suc m)
  then show ?case by simp
qed
```

### Sledgehammer
Isabelle's killer feature: automated theorem prover integration.
Calls external ATPs (E, Vampire, Z3, CVC5) to find proofs, then reconstructs in Isabelle.

```isabelle
lemma "finite A ⟹ finite B ⟹ finite (A ∪ B)"
  by (sledgehammer)  -- Finds proof automatically
```

---

## Hoare Logic and Program Verification

### Hoare Triple
{P} C {Q}
- P: precondition (what's true before)
- C: command (program)
- Q: postcondition (what's true after)

**Partial correctness:** IF P holds and C terminates, THEN Q holds.
**Total correctness:** IF P holds, THEN C terminates AND Q holds.

### Hoare Rules
| Rule | Triple |
|------|--------|
| Assignment | {Q[e/x]} x := e {Q} |
| Sequence | {P} C1 {R}, {R} C2 {Q} ⊢ {P} C1;C2 {Q} |
| If-then-else | {P∧B} C1 {Q}, {P∧¬B} C2 {Q} ⊢ {P} if B then C1 else C2 {Q} |
| While | {P∧B} C {P} ⊢ {P} while B do C {P∧¬B} (P is loop invariant) |
| Consequence | P'⊢P, {P}C{Q}, Q⊢Q' ⊢ {P'}C{Q'} |

### Loop Invariants
The hardest part. A loop invariant P must satisfy:
1. P holds before the loop (initialization)
2. If P ∧ B holds, then P holds after one iteration (maintenance)
3. P ∧ ¬B implies the desired postcondition (termination)

### Weakest Precondition
wp(C, Q) = weakest P such that {P} C {Q} is valid.
- wp(x := e, Q) = Q[e/x]
- wp(C1;C2, Q) = wp(C1, wp(C2, Q))
- wp(if B then C1 else C2, Q) = (B → wp(C1,Q)) ∧ (¬B → wp(C2,Q))

---

## Separation Logic

### Motivation
Hoare logic can't reason about pointer aliasing. Separation logic adds:
- **Separating conjunction (∗):** P ∗ Q means P and Q hold on DISJOINT parts of the heap
- **Points-to (↦):** x ↦ v means x points to value v (and nothing else)
- **emp:** Empty heap

### Frame Rule
{P} C {Q}
——————————————
{P ∗ R} C {Q ∗ R}

If C only touches memory described by P, then any disjoint frame R is preserved.
This enables modular reasoning about heap-manipulating programs.

### Concurrent Separation Logic
Extend to concurrent programs:
{P₁} C₁ {Q₁}    {P₂} C₂ {Q₂}
——————————————————————————————
{P₁ ∗ P₂} C₁ ∥ C₂ {Q₁ ∗ Q₂}

If C₁ and C₂ operate on disjoint memory, they can run in parallel safely.

### Tools
- **Iris:** State-of-the-art concurrent separation logic framework (in Coq)
- **VST (Verified Software Toolchain):** Verify C programs against separation logic specs
- **Viper:** Automated verification infrastructure for permission-based reasoning
