# Requirements Authoring Handbook

This handbook defines clear, concise, domain-neutral rules for writing requirements.

Use it for requirements that concern products, systems, processes, hardware, documentation, operations, services, interfaces, organizations, or software.

## Rules

1. Write one obligation per requirement.

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

2. Make the requirement necessary.

   A requirement shall exist for a reason.

   Accept only requirements that can be traced to a stakeholder need, objective, risk, legal or regulatory constraint, interface constraint, or justified technical decision.

   If the reason is unknown, the requirement is not ready.

3. Make it unambiguous.

   A requirement shall have one reasonable interpretation for the intended audience.

   Avoid:

   - pronouns without a clear antecedent
   - vague verbs such as `handle`, `manage`, `support`, or `improve`
   - subjective adjectives such as `fast`, `simple`, or `robust`
   - open-ended phrases such as `etc.`, `as needed`, or `where appropriate`

   Prefer defined terms, explicit conditions, measurable limits, and concrete objects.

4. Make it verifiable.

   A requirement shall be verifiable by at least one defined method:

   - inspection
   - analysis
   - demonstration
   - test
   - review
   - audit

   If nobody can explain how to verify it, rewrite it.

5. Be feasible.

   A requirement shall be achievable within the intended constraints.

   Do not write an obligation that cannot be satisfied with the available technology, resources, time, environment, or interface constraints.

   If feasibility is uncertain, state the constraint explicitly or revise the requirement.

6. Keep it concise.

   A requirement shall use the minimum wording needed to preserve its meaning.

   Concise does not mean vague. Remove filler, not information.

7. Stay solution-neutral unless a design constraint is intentional.

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

8. Use controlled modal verbs.

   A mandatory requirement statement shall use exactly one modal verb: `shall`.

   | Modal verb | Meaning | Requirement use |
   | --- | --- | --- |
   | shall | Mandatory obligation | Use for required requirement statements |
   | should | Recommendation | Guidance, not a binding requirement |
   | may | Permission or optionality | Optional behavior or allowance |
   | must | External obligation | Avoid unless imposed by law or an external standard |
   | will | Fact or future intent | Not a requirement |
   | can | Ability or possibility | Not a requirement |

   Do not mix `shall` with other modal verbs in the same mandatory statement.

9. Include measurable criteria where needed.

   If a requirement uses a qualitative, quantitative, timing, capacity, performance, accuracy, availability, or compatibility concept, it shall define the associated measurable criterion or reference.

   Examples:

   - `fast` -> response time threshold
   - `accurate` -> tolerance or error bound
   - `available` -> availability target or operating condition
   - `compatible` -> referenced standard, profile, version, or test suite
   - `lightweight` -> mass limit

10. Separate the statement from metadata.

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

## Template

Use this template to draft a requirement.

```text
[ID] [Title]

Statement:
When [trigger/condition], the [subject] shall [observable behavior] within [threshold / time / limit] for [actor/object/interface].

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

## Checklist

1. It states one obligation only.
2. It has a clear source or rationale.
3. It is necessary.
4. It uses controlled wording.
5. It is unambiguous.
6. It is concise without losing meaning.
7. It is solution-neutral unless a solution is intentionally constrained.
8. It includes the conditions needed for interpretation.
9. It includes measurable terms where needed.
10. It is verifiable.
11. It identifies a verification method.
12. It does not conflict with other approved requirements.
13. It is traceable to related needs, constraints, or artifacts.
14. It uses `shall`, `should`, and `may` consistently.
15. It can be reviewed by someone who was not involved in writing it.

