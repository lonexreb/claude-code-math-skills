# Formal Verification: Model Checking, TLA+, SAT/SMT

## Table of Contents
1. [Model Checking Foundations](#model-checking-foundations)
2. [Temporal Logics](#temporal-logics)
3. [TLA+](#tla)
4. [SAT Solvers](#sat-solvers)
5. [SMT Solvers and Z3](#smt-solvers-and-z3)
6. [Industrial Applications](#industrial-applications)

---

## Model Checking Foundations

### What is Model Checking?
Automatically verify that a finite-state model satisfies a specification.
Input: System model M + Property φ
Output: M ⊨ φ (yes) or counterexample trace (no)

### Kripke Structure
M = (S, S₀, R, L) where:
- S: finite set of states
- S₀ ⊂ S: initial states
- R ⊂ S × S: transition relation (must be total)
- L: S → 2^{AP}: labeling function (which atomic propositions hold in each state)

### State Space Explosion
The fundamental challenge: states grow exponentially with system components.
n bits → 2ⁿ states. 10 processes with 10 states each → 10¹⁰ states.

**Mitigation techniques:**
- **Symbolic model checking (BDD-based):** Represent sets of states symbolically
- **Bounded model checking (SAT-based):** Unroll transitions k steps, check with SAT solver
- **Partial order reduction:** Exploit independence of concurrent actions
- **Abstraction:** CEGAR (counterexample-guided abstraction refinement)
- **Compositional verification:** Verify components separately, compose guarantees

---

## Temporal Logics

### LTL (Linear Temporal Logic)
Reasons about single execution paths.

**Operators:**
- **Xφ (Next):** φ holds in the next state
- **Fφ (Eventually/Finally):** φ holds at some future state
- **Gφ (Always/Globally):** φ holds at all future states
- **φ U ψ (Until):** φ holds until ψ becomes true

**Common properties:**
- **Safety** (nothing bad happens): G(¬bad)
- **Liveness** (something good eventually happens): GF(good) — infinitely often good
- **Fairness:** GF(enabled) → GF(executed)
- **Response:** G(request → F(response))
- **Mutual exclusion:** G(¬(crit₁ ∧ crit₂))

### CTL (Computation Tree Logic)
Reasons about branching time (all paths vs some paths).

**Path quantifiers:** A (all paths), E (some path)
**Temporal operators:** X, F, G, U (same as LTL)

Combined: AX, EX, AF, EF, AG, EG, AU, EU

**Key properties in CTL:**
- AG(¬deadlock): no deadlock on any path
- AG(request → AF(response)): every request is eventually answered on all paths
- EF(goal): there exists a path reaching goal

### CTL vs LTL
- LTL can express fairness constraints naturally (GFφ)
- CTL can express existential properties (EFφ) — "is it possible to reach state φ?"
- CTL* subsumes both but is more expensive to check
- Neither LTL nor CTL subsumes the other

---

## TLA+

### Overview
- Created by Leslie Lamport (Turing Award 2013)
- Specifies concurrent/distributed systems using math (set theory + temporal logic)
- TLC: explicit-state model checker
- TLAPS: proof system for TLA+ (connects to Isabelle, Zenon, SMT)

### Basic TLA+ Structure
```tla+
---- MODULE SimpleCounter ----
EXTENDS Integers

VARIABLE count

Init == count = 0

Increment == count' = count + 1    \* count' is the next-state value

Spec == Init /\ [][Increment]_count  \* Initial state + always Increment or stutter

TypeInvariant == count \in Nat

THEOREM Spec => []TypeInvariant     \* count is always a natural number
====
```

### Key TLA+ Concepts
- **State:** Assignment of values to all variables
- **Action:** Relation between current state and next state (uses primed variables: x')
- **Stutter step:** Step where nothing changes (allows composition)
- **Fairness:** WF_vars(Action) = weak fairness, SF_vars(Action) = strong fairness

### TLA+ for Distributed Systems
```tla+
---- MODULE TwoPhaseCommit ----
EXTENDS Integers, FiniteSets, TLC

CONSTANTS RM           \* Set of resource managers

VARIABLES rmState,     \* rmState[r] \in {"working","prepared","committed","aborted"}
          tmState,     \* "init", "committed", "aborted"
          tmPrepared,  \* Set of RMs that sent Prepared
          msgs         \* Set of messages

\* Transaction manager commits if all RMs prepared
TMCommit == /\ tmState = "init"
            /\ tmPrepared = RM
            /\ tmState' = "committed"
            /\ msgs' = msgs \cup {[type |-> "Commit"]}
            /\ UNCHANGED <<rmState, tmPrepared>>
====
```

### PlusCal
Higher-level language that compiles to TLA+. Imperative syntax, easier for programmers:
```
--algorithm Transfer
variables accounts = [a |-> 100, b |-> 100];
process transfer = "T"
begin
  t1: accounts["a"] := accounts["a"] - 50;
  t2: accounts["b"] := accounts["b"] + 50;
end process;
end algorithm;
```

---

## SAT Solvers

### Boolean Satisfiability (SAT)
Given a Boolean formula in CNF: (x₁ ∨ ¬x₂) ∧ (¬x₁ ∨ x₃) ∧ ...
Find an assignment of variables that makes it true, or prove unsatisfiable.

### DPLL Algorithm (foundation)
1. **Unit propagation:** If a clause has one unset literal, set it to true
2. **Pure literal elimination:** If variable appears only positive (or negative), set accordingly
3. **Branching:** Pick an unset variable, try true/false, recurse
4. **Backtrack:** If conflict found, undo last decision

### CDCL (Conflict-Driven Clause Learning)
Modern SAT solvers extend DPLL with:
- **Conflict analysis:** When conflict found, analyze why → learn new clause
- **Non-chronological backtracking:** Jump back to the decision that caused the conflict
- **Restarts:** Periodically restart search with learned clauses
- **VSIDS heuristic:** Pick branching variable based on recent conflict involvement

### Applications of SAT
- Hardware verification
- Bounded model checking (unroll k steps → SAT query)
- Planning (AI)
- Cryptanalysis
- Configuration and scheduling

---

## SMT Solvers and Z3

### SMT (Satisfiability Modulo Theories)
SAT extended with background theories:
- **Linear integer/real arithmetic:** 3x + 2y ≤ 7
- **Arrays:** select(store(a, i, v), i) = v
- **Bit vectors:** Fixed-width integer arithmetic
- **Uninterpreted functions:** f(x) = f(y) → x = y (congruence)
- **Strings, regular expressions**
- **Floating point**

### Z3 (Microsoft Research)
Most widely used SMT solver. MIT licensed.

```python
from z3 import *

# Simple example
x, y = Ints('x y')
s = Solver()
s.add(x + y == 10)
s.add(x > 0, y > 0)
s.add(x > y)
print(s.check())  # sat
print(s.model())   # [y = 1, x = 9]

# Prove a theorem
x = Int('x')
prove(Implies(x > 0, x * x > 0))  # proved

# Verify a program (weakest precondition)
# {x > 0} y := x + 1 {y > 1}
x, y = Ints('x y')
precondition = x > 0
postcondition = y > 1
assignment = y == x + 1
prove(Implies(And(precondition, assignment), postcondition))
```

### Z3 for Verification Tasks
```python
# Verify array bounds
from z3 import *
i, n = Ints('i n')
s = Solver()
s.add(n > 0)          # array has positive size
s.add(i >= 0)         # loop starts at 0
s.add(i < n)          # loop guard
# Prove: array access a[i] is in bounds
# (this is trivially true given the constraints)
s.add(Not(And(i >= 0, i < n)))  # negate what we want to prove
print(s.check())  # unsat → the property holds!

# Find loop invariant candidates
# for (i = 0; i < n; i++) { s += a[i]; }
# Invariant: 0 <= i <= n
```

### Other SMT Solvers
- **CVC5:** Open-source, strong on strings and quantifiers
- **Yices 2:** Efficient for linear arithmetic
- **MathSAT:** Good for interpolation
- **dReal:** Handles nonlinear real arithmetic (delta-decidable)

---

## Industrial Applications

### Amazon (TLA+)
- S3, DynamoDB, EBS all verified with TLA+
- Found bugs in designs that passed code review and testing
- TLA+ used before implementation to catch design flaws

### Microsoft (Z3, VCC, Dafny)
- Z3 powers many verification tools (Dafny, Boogie, Corral)
- Windows kernel components verified with VCC
- Dafny: verification-aware programming language

### Intel/AMD (Model Checking)
- Hardware verification of processor designs
- Cache coherence protocols verified with model checking
- Bug found in Pentium FDIV — could have been caught by formal methods

### CompCert (Coq)
- Formally verified C compiler (Leroy et al.)
- Guarantees: compiled code preserves semantics of source
- Used in avionics and automotive

### seL4 (Isabelle/HOL)
- Formally verified microkernel
- Functional correctness: C code matches abstract specification
- Security: information flow guarantees, capability-based access control
- Used in military, aerospace, automotive
