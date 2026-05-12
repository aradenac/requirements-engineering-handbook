# Requirements Authoring Handbook

## Purpose

This handbook defines clear, concise, domain-neutral rules for writing requirements.

Use it for requirements that concern products, systems, processes, hardware, documentation, operations, services, interfaces, organizations, or software.

The goal is not elegant prose. The goal is a requirement set that is:

- necessary
- unambiguous
- verifiable
- feasible
- concise
- solution-neutral unless a design constraint is intentional
- consistent

## Core Rules

### 1. Write one obligation per requirement

A requirement shall express exactly one obligation.

If a statement contains multiple obligations, split it into separate requirements unless the obligations are inseparable for verification.

Bad:

```text
The packaging shall protect the product and reduce storage cost.
```

Better:

```text
The packaging shall protect the product during transport and storage.
The packaging shall not exceed the storage volume limit defined for the product family.
```

### 2. Make the requirement necessary

A requirement shall exist for a reason.

Accept only requirements that can be traced to a stakeholder need, objective, risk, legal or regulatory constraint, interface constraint, or justified technical decision.

If the reason is unknown, the requirement is not ready.

### 3. Make it unambiguous

A requirement shall have one reasonable interpretation for the intended audience.

Avoid:

- pronouns without a clear antecedent
- vague verbs such as `handle`, `manage`, `support`, or `improve`
- subjective adjectives such as `fast`, `simple`, or `robust`
- open-ended phrases such as `etc.`, `as needed`, or `where appropriate`

Prefer defined terms, explicit conditions, measurable limits, and concrete objects.

### 4. Make it verifiable

A requirement shall be verifiable by at least one defined method:

- inspection
- analysis
- demonstration
- test
- review
- audit

If nobody can explain how to verify it, rewrite it.

### 5. Be feasible

A requirement shall be achievable within the intended constraints.

Do not write an obligation that cannot be satisfied with the available technology, resources, time, environment, or interface constraints.

If feasibility is uncertain, state the constraint explicitly or revise the requirement.

### 6. Keep it concise

A requirement shall use the minimum wording needed to preserve its meaning.

Concise does not mean vague. Remove filler, not information.

### 7. Stay solution-neutral unless a design constraint is intentional

A requirement shall describe the needed outcome, not the implementation, unless the design choice is part of the requirement.

Write:

- what must happen
- under what conditions
- within what limits
- for which subject, object, or interface

Avoid prescribing:

- technologies
- algorithms
- internal components
- procedures not needed by the requirement
- layouts or forms unless they are required

### 8. Use controlled modal verbs

A mandatory requirement statement shall use exactly one modal verb: `shall`.

Use modal verbs with fixed meaning:

| Modal verb | Meaning | Requirement use |
| --- | --- | --- |
| shall | Mandatory obligation | Use for required requirement statements |
| should | Recommendation | Guidance, not a binding requirement |
| may | Permission or optionality | Optional behavior or allowance |
| must | External obligation | Avoid unless imposed by law or an external standard |
| will | Fact or future intent | Not a requirement |
| can | Ability or possibility | Not a requirement |

Do not mix `shall` with other modal verbs in the same mandatory statement.

### 9. Include measurable criteria where needed

If a requirement uses a qualitative, quantitative, timing, capacity, performance, accuracy, availability, or compatibility concept, it shall define the associated measurable criterion or reference.

Examples:

- `fast` -> response time threshold
- `accurate` -> tolerance or error bound
- `available` -> availability target or operating condition
- `compatible` -> referenced standard, profile, version, or test suite
- `lightweight` -> mass limit

### 10. Separate the statement from metadata

The requirement statement is the obligation itself.

Metadata contains supporting information such as rationale, source, verification method, assumptions, notes, and trace links.

Do not embed metadata in the obligation sentence.

Bad:

```text
Because operators need safety, the door shall lock automatically when the machine starts, and this will be tested during validation.
```

Good:

```text
Statement:
When the machine starts, the door shall lock within 1 s.

Rationale:
Prevent operator access during operation.

Verification:
Test.
```

## Modal Verb Policy

Use the modal verbs below with these meanings only:

| Verb | Allowed meaning | Notes |
| --- | --- | --- |
| shall | Mandatory requirement | Use for every mandatory requirement statement |
| should | Recommendation | Not binding unless separately elevated to `shall` |
| may | Permission | Expresses optionality or allowance |
| must | External requirement | Use only when quoting or following an external rule |
| will | Declaration of fact or future intent | Do not use for requirements |
| can | Ability or possibility | Do not use for requirements |

### Mandatory statement rule

A mandatory requirement statement shall use exactly one modal verb: `shall`.

Bad:

```text
The container must shall remain closed.
```

Better:

```text
The container shall remain closed during transport.
```

## Generic Requirement Patterns

These patterns are concise sentence forms inspired by EARS. Keep them generic and domain-neutral. Use `<subject>` instead of assuming a system.

### 1. Simple obligation

Pattern:

```text
The <subject> shall <verifiable action> <object>.
```

Use when:

- the requirement is always applicable
- no trigger or condition is needed

Good:

```text
The cabinet shall resist a vertical load of 500 N.
```

Bad:

```text
The cabinet should be strong enough.
```

Why:

This form states a single, measurable obligation with no unnecessary context.

### 2. Triggered obligation

Pattern:

```text
When <trigger>, the <subject> shall <verifiable action> <object>.
```

Use when:

- the obligation is activated by an event
- the event is observable and specific

Good:

```text
When the machine starts, the door shall lock within 1 s.
```

Bad:

```text
When something happens, the door should secure itself.
```

Why:

The trigger is explicit, and the response can be checked.

### 3. State-driven obligation

Pattern:

```text
While <state>, the <subject> shall <verifiable action> <object>.
```

Use when:

- the obligation applies for as long as a condition remains true
- the state is stable and observable

Good:

```text
While the compartment is open, the indicator shall remain red.
```

Bad:

```text
While open, it should warn the user.
```

Why:

The state and response are both clear.

### 4. Exception or undesired condition

Pattern:

```text
If <undesired condition>, then the <subject> shall <required response>.
```

Use when:

- the requirement defines a response to a fault, limit violation, or abnormal condition

Good:

```text
If the measured temperature exceeds 80 C, then the heater shall switch off.
```

Bad:

```text
If there is a problem, the heater should react.
```

Why:

The condition is explicit and the required response is observable.

### 5. Feature- or variant-scoped obligation

Pattern:

```text
Where <feature or variant applies>, the <subject> shall <verifiable action> <object>.
```

Use when:

- the requirement applies only to a defined subset, option, or variant

Good:

```text
Where the product is supplied with the inspection option, the product shall provide a viewing panel.
```

Bad:

```text
Where appropriate, the product should include access.
```

Why:

The applicability is explicit, not implied.

## Weak Wording Guidance

Replace vague words with measurable, observable, or bounded statements.

| Weak wording | Problem | Better wording strategy | Example correction |
| --- | --- | --- | --- |
| fast | No measurable threshold | State a response time or delay limit | `The service shall respond within 2 s.` |
| robust | Undefined resilience target | Define loads, faults, cycles, or environmental bounds | `The bracket shall withstand 1,000 load cycles at 200 N.` |
| simple | Subjective and audience-dependent | Define steps, parts, or complexity limits | `The procedure shall require no more than 3 steps.` |
| user-friendly | Subjective usability claim | Define task success, time, error rate, or training limit | `A trained operator shall complete the task in under 2 min.` |
| optimal | No objective criterion | State the optimization goal and constraints | `The layout shall minimize storage volume within the defined envelope.` |
| sufficient | Undefined adequacy | State the minimum threshold or coverage | `The reservoir shall hold at least 20 L.` |
| as needed | Open-ended frequency or extent | State the trigger or number of occurrences | `The alarm shall activate when pressure exceeds 5 bar.` |
| where appropriate | Ambiguous applicability | Define the condition for application | `Where the unit is installed outdoors, the casing shall be rated IP65.` |
| etc. | Unbounded list | Enumerate the full list or define the rule for extension | `The report shall include title, date, author, and revision.` |
| manage | Vague action verb | State the exact action or outcome | `The controller shall store the value in memory.` |
| support | Broad and unclear | State the supported function or interface | `The cart shall support a load of 150 kg.` |
| handle | Undefined behavior | State the response for each condition | `The system shall reject inputs outside the defined range.` |
| improve | Relative and unmeasured | State the target value or comparison baseline | `The process shall reduce waste by 10 percent.` |
| compatible | Missing reference | Cite the standard, version, profile, or test suite | `The connector shall conform to ISO 12345-2:2024.` |

## Measurable Criteria

Use measurable criteria whenever a requirement includes a term that can otherwise be interpreted subjectively.

Bad:

```text
The device shall be fast.
```

Better:

```text
The device shall complete the operation within 3 s.
```

Bad:

```text
The sensor shall be accurate.
```

Better:

```text
The sensor shall measure within +/- 2 percent of the reference value.
```

Bad:

```text
The service shall be available.
```

Better:

```text
The service shall be available 99.5 percent of the time during the agreed operating window.
```

Bad:

```text
The interface shall be compatible.
```

Better:

```text
The interface shall conform to version 3 of the referenced profile and pass the associated conformance test suite.
```

Bad:

```text
The component shall be lightweight.
```

Better:

```text
The component shall have a mass below 2 kg.
```

## Statement and Metadata

Keep the requirement statement separate from supporting metadata.

### Bad

```text
Because operators need safety, the door shall lock automatically when the machine starts, and this will be tested during validation.
```

### Good

```text
Statement:
When the machine starts, the door shall lock within 1 s.

Rationale:
Prevent operator access during operation.

Verification:
Test.

Source:
Operator safety need.
```

The statement is the obligation. The metadata explains why it exists and how it will be handled.

## Bad to Better Examples

Each example below shows one common writing problem, the corrected statement, the rule applied, and a short explanation.

### 1. Vague adjective

Bad:

```text
The container shall be durable.
```

Better:

```text
The container shall withstand a 1 m drop onto a rigid surface without loss of function.
```

Rule applied:

- Make it verifiable
- Include measurable criteria where needed

Why:

`durable` does not tell the reader what to verify.

### 2. Weak verb

Bad:

```text
The system shall handle overloads.
```

Better:

```text
If the load exceeds 100 percent of nominal capacity, the unit shall shut down within 2 s.
```

Rule applied:

- Make it unambiguous
- Use controlled wording

Why:

`handle` does not state the required response.

### 3. Missing trigger

Bad:

```text
The alarm shall sound.
```

Better:

```text
When pressure exceeds 5 bar, the alarm shall sound within 1 s.
```

Rule applied:

- Include the context needed for interpretation

Why:

The trigger is required to know when the obligation applies.

### 4. Missing measurable criterion

Bad:

```text
The process shall be fast.
```

Better:

```text
The process shall complete within 10 min.
```

Rule applied:

- Include measurable criteria where needed

Why:

`fast` is subjective without a threshold.

### 5. Multiple obligations in one statement

Bad:

```text
The cabinet shall lock and display the status indicator.
```

Better:

```text
The cabinet shall lock when the access panel is closed.
The cabinet shall display the locked status on the indicator.
```

Rule applied:

- Write one obligation per requirement

Why:

Splitting the statement makes each obligation easier to verify.

### 6. Premature solution

Bad:

```text
The package shall use a magnetic latch.
```

Better:

```text
The package shall remain closed during transport.
```

Rule applied:

- Stay solution-neutral unless a design constraint is intentional

Why:

The need is closure, not the latch technology.

### 7. Ambiguous pronoun

Bad:

```text
When the unit is powered, it shall indicate fault.
```

Better:

```text
When the unit is powered, the indicator shall display a fault state.
```

Rule applied:

- Make it unambiguous

Why:

`it` can refer to more than one object.

### 8. Open-ended list

Bad:

```text
The report shall include date, name, signature, etc.
```

Better:

```text
The report shall include the date, the author name, and the signature.
```

Rule applied:

- Make it unambiguous
- Keep it concise

Why:

`etc.` leaves the list incomplete.

### 9. Non-verifiable requirement

Bad:

```text
The process shall be improved.
```

Better:

```text
The process shall reduce scrap rate by 15 percent compared with the current baseline.
```

Rule applied:

- Make it verifiable

Why:

`improved` does not define a checkable result.

### 10. Compatibility without reference

Bad:

```text
The connector shall be compatible.
```

Better:

```text
The connector shall conform to the referenced connector profile and pass the associated fit test.
```

Rule applied:

- Include measurable criteria where needed
- Make it unambiguous

Why:

Compatibility only has meaning when the reference is defined.

### 11. Subjective usability

Bad:

```text
The form shall be user-friendly.
```

Better:

```text
A trained user shall complete the form in under 3 min with no more than one correction.
```

Rule applied:

- Include measurable criteria where needed
- Make it verifiable

Why:

Usability must be stated as an observable outcome.

### 12. Condition or state driven requirement

Bad:

```text
The barrier shall stay active.
```

Better:

```text
While the machine is operating, the barrier shall remain closed.
```

Rule applied:

- Include the context needed for interpretation
- Use a generic requirement pattern

Why:

The state defines when the obligation applies.

## Practical Checklist

Before approving a requirement, check that it:

- states exactly one obligation
- uses `shall` for mandatory wording
- is necessary
- is unambiguous
- is verifiable
- is feasible
- is concise
- is solution-neutral unless a design constraint is intentional
- includes the trigger, state, object, or condition when needed
- includes measurable criteria when the wording could otherwise be subjective
- separates the statement from metadata
- avoids weak wording
- avoids `etc.`, `as needed`, and `where appropriate`
- can be traced to a source or rationale

