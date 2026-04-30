# Proof by contradiction template

Use for: claims of the form `¬X`, irrationality / non-existence proofs, infinitude proofs, negative results in topology and analysis.

## Skeleton

```
Claim: <statement>.

Proof. Suppose, for contradiction, that <negation of the claim> holds.
[Derive consequences of the assumed negation.]
[Reach a concrete contradiction — either a false numerical equality,
 or a violation of an established fact, or a witness that contradicts
 a uniqueness claim.]
This contradicts <named fact / earlier step>.
Therefore the assumption was false, and the claim holds. □
```

## When to prefer contradiction over a direct proof

- Proving `¬X` directly would require fighting through the negation of a complicated statement.
- The negation gives a concrete *object* you can manipulate (e.g. "suppose √2 = p/q in lowest terms" — now you have a rational number to argue about).
- Direct construction is hopeless, but the negation lets you derive a contradiction with completeness, well-ordering, or a counting argument.

## Canonical pitfalls

1. **Negating the wrong statement.** The negation of `∀x P(x)` is `∃x ¬P(x)` — pick a *specific* counterexample to assume, not a vague "P fails".
2. **Reaching a contradiction "with intuition".** The contradiction must be with a *named* fact: a previously proved result, a hypothesis, or basic arithmetic. "It feels wrong" is not a contradiction.
3. **Circular reasoning.** It's easy to invoke a fact whose proof depends on the claim being shown. Re-trace the dependency chain.
4. **Constructive context.** In intuitionistic logic / formal verification, classical contradiction (¬¬X ⇒ X) is not always available. State explicitly when you use the law of excluded middle.

## Worked micro-example: √2 is irrational

```
Suppose, for contradiction, that √2 = p / q for some integers p, q with q > 0,
and assume the fraction is in lowest terms (gcd(p, q) = 1).
Then 2 q² = p², so p² is even, hence p is even (parity of squares).
Write p = 2 r. Substituting: 2 q² = 4 r², so q² = 2 r², hence q² is even,
hence q is even.
Both p and q are even, contradicting gcd(p, q) = 1. □
```

Note the named contradiction: "contradicting gcd(p, q) = 1". Not "contradicting our setup".

## Variant: contrapositive

Sometimes "proving ¬B ⇒ ¬A" is easier than "proving A ⇒ B". This is **not** the same as contradiction — it's a direct proof of the contrapositive, which is logically equivalent to the original implication.

```
Claim: A ⇒ B.
Equivalent: ¬B ⇒ ¬A.

Proof of contrapositive. Assume ¬B. [show ¬A.] □
```

Prefer contrapositive when ¬B is more concrete than A.
