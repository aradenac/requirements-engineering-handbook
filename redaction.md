# Requirements Redaction Handbook

## Introduction

Requirements redaction is the activity of turning stakeholder intent, constraints, and design decisions into requirements that can be read, reviewed, traced, and verified.

The goal is not to write elegant prose. The goal is to write requirements that are:

- necessary
- unambiguous
- verifiable
- feasible
- concise
- traceable
- consistent
- solution-neutral unless the solution is intentionally constrained

This handbook combines the main ideas from:

- ISO/IEC/IEEE 29148 for requirement quality
- INCOSE guidance for clear and testable wording
- EARS for compact sentence patterns
- NASA guidance for practical verification-oriented writing
- IREB / CPRE for structured requirements engineering practice

Use this handbook when you write a new requirement, revise an existing one, or review a requirement set before baselining.

## Rules

### 1. Write one requirement per statement

A requirement shall express one obligation only.

If a sentence contains multiple actions, conditions, or outcomes, split it into separate requirements unless they are inseparable for verification.

### 2. Keep the requirement necessary

A requirement shall exist for a reason.

Accept only requirements that can be traced to one of the following:

- a stakeholder need
- a business objective
- a risk
- a legal or regulatory constraint
- an external interface constraint
- a justified architectural or operational decision

If the source is unknown, the statement is not ready.

### 3. Make the wording unambiguous

Use language that has one reasonable interpretation for the intended audience.

Avoid:

- pronouns without a clear antecedent
- vague verbs such as `handle`, `manage`, `support`, or `ensure`
- subjective adjectives such as `fast`, `simple`, or `robust`
- open-ended phrases such as `etc.`, `as needed`, or `where appropriate`

Prefer concrete nouns, measurable quantities, defined terms, and explicit conditions.

### 4. Make it verifiable

Every requirement shall be testable by at least one defined verification method:

- inspection
- analysis
- demonstration
- test
- review
- audit

If nobody can explain how to verify it, rewrite it.

### 5. State the constraint on behavior, not the implementation

Requirements should describe what the system, product, or process must achieve.

Do not prescribe a solution unless the solution is part of the requirement itself.

Write:

- what must happen
- under what conditions
- with what thresholds or tolerances
- for which actor, object, or interface

Avoid prematurely choosing:

- technologies
- algorithms
- UI layouts
- internal components
- coding techniques

### 6. Use controlled wording

Prefer these keywords:

- `shall` for mandatory requirements
- `should` for recommendations
- `may` for permitted optional behavior

Avoid mixing `shall` and `must` unless your organization explicitly requires `must`.

Use active voice whenever possible.

### 7. Include the context needed for interpretation

A requirement is incomplete if it omits information required to understand or verify it.

Add the relevant:

- actor
- object
- trigger
- condition
- threshold
- unit
- tolerance
- exception
- timing constraint
- environmental constraint

### 8. Keep requirements concise

Use the minimum wording needed to preserve the exact meaning.

Concise does not mean vague. Remove filler, not information.

### 9. Maintain consistency

A requirement shall not contradict:

- another approved requirement
- a shared definition
- an architectural constraint
- an interface contract
- an approved assumption

When two requirements overlap, resolve the overlap explicitly.

### 10. Keep traceability intact

Every requirement should be traceable to:

- its source
- its rationale
- related requirements
- parent needs or objectives
- downstream design or implementation artifacts
- verification evidence when available

If a requirement cannot be traced, it is hard to defend and hard to maintain.

## Template

Use the following template to draft a requirement.

```text
[ID] [Title]

Statement:
When [trigger/condition], the [system/product/process] shall [observable behavior] within [threshold / time / limit] for [actor/object/interface].

Rationale:
[Why this requirement exists.]

Source:
[Stakeholder, regulation, risk, decision, interface, or other origin.]

Verification:
[Inspection | Analysis | Demonstration | Test | Review | Audit]

Fit / Constraints:
[Relevant assumptions, dependencies, bounds, interfaces, or excluded cases.]

Trace links:
[Parent need, related requirements, downstream artifacts, verification references.]
```

### Template notes

- Use `shall` only for mandatory behavior.
- Replace the bracketed fields with concrete content.
- If timing, quantity, or quality matters, make it measurable.
- If the requirement is conditional, state the condition explicitly.
- If the requirement depends on an interface, define the interface context.

### EARS-style patterns

Use one of these patterns when they fit:

- `When <trigger>, the system shall <response>.`
- `While <condition>, the system shall <response>.`
- `If <exception/condition>, then the system shall <response>.`
- `Where <constraint>, the system shall <response>.`

These patterns reduce ambiguity and help reviewers see the trigger, context, and expected behavior quickly.

## Checklist

Before you approve a requirement, check that it satisfies all of the following:

- It states one obligation only.
- It has a clear source or rationale.
- It is necessary.
- It uses controlled wording.
- It is unambiguous.
- It is concise without losing meaning.
- It is solution-neutral unless a solution is intentionally constrained.
- It includes the conditions needed for interpretation.
- It includes measurable terms where needed.
- It is verifiable.
- It identifies a verification method.
- It does not conflict with other approved requirements.
- It is traceable to related needs, constraints, or artifacts.
- It uses `shall`, `should`, and `may` consistently.
- It can be reviewed by someone who was not involved in writing it.

## Review Questions

Ask these questions during review:

1. What need justifies this requirement?
2. Can two competent readers interpret it the same way?
3. How would we prove it is satisfied?
4. What part of the requirement is measurable?
5. What context is missing, if any?
6. Does it describe the need, or does it accidentally prescribe the implementation?
7. Is it consistent with the rest of the set?
8. Can it be traced to something upstream and downstream?

If the answer to any of these questions is weak, revise the requirement before approval.
