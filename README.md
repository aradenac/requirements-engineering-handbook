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

## Verification methods

These methods show how satisfaction can be proven. They are not a workflow.

| Method | Use when |
| --- | --- |
| Inspection | The requirement can be checked by looking at the item, document, or attribute directly. |
| Analysis | The requirement can be proven by calculation, model, or reasoned evaluation. |
| Demonstration | The requirement can be shown in operation without a formal test setup. |
| Test | The requirement needs controlled execution with recorded results. |
| Review | The requirement depends on a structured human check of content or consistency. |
| Audit | The requirement concerns compliance against rules, records, or evidence. |

## Sentence patterns

Use these compact patterns to make the obligation, trigger, or scope explicit. Use `<subject>` instead of assuming a system.

| Pattern | When to use | Bad example | Better example | Why |
| --- | --- | --- | --- | --- |
| Universal: `The <subject> shall <verifiable action> <object>.` | Use when the obligation always applies. | The equipment should be sturdy. | The equipment shall withstand a 200 N load. | The obligation is direct and measurable. |
| Event-driven: `When <trigger>, the <subject> shall <verifiable action> <object>.` | Use when an event starts the obligation. | When something happens, the service should react. | When the container is opened, the alarm shall sound. | The trigger is explicit. |
| State-driven: `While <state>, the <subject> shall <verifiable action> <object>.` | Use when the obligation lasts while a condition remains true. | While open, it should remain safe. | While the access panel is open, the guard shall remain engaged. | The active state is clear. |
| Exception / fault: `If <undesired condition>, then the <subject> shall <required response>.` | Use for abnormal conditions or limit violations. | If there is a problem, the process should stop. | If pressure exceeds the limit, then the process shall stop within 2 s. | The fault response is unambiguous. |
| Variant / optional scope: `Where <feature or context applies>, the <subject> shall <verifiable action> <object>.` | Use when the rule applies only in a defined variant or context. | Where appropriate, the report should include details. | Where the extended report format applies, the report shall include a summary section. | The scope is defined instead of implied. |

## Weak wording replacement

Replace vague wording with observable, measurable, bounded, or referenced wording.

| Weak wording | Problem | Better strategy | Example correction |
| --- | --- | --- | --- |
| fast | No measurable threshold. | State a response time or delay limit. | The service shall respond within 2 s. |
| robust | Undefined resilience target. | Define loads, cycles, faults, or environmental bounds. | The bracket shall withstand 1,000 cycles at 200 N. |
| simple | Subjective and audience-dependent. | State steps, parts, or complexity limits. | The procedure shall require no more than 3 steps. |
| user-friendly | Subjective usability claim. | State task time, error rate, or training limit. | A trained user shall complete the form in under 3 min. |
| optimal | No objective criterion. | State the optimization goal and constraints. | The layout shall minimize storage volume within the envelope. |
| sufficient | Undefined adequacy. | State the minimum threshold or coverage. | The tank shall hold at least 20 L. |
| as needed | Open-ended frequency or extent. | State the trigger or quantity. | The alarm shall activate when pressure exceeds 5 bar. |
| where appropriate | Ambiguous applicability. | Define the condition for application. | Where the unit is installed outdoors, the casing shall be IP65-rated. |
| etc. | Unbounded list. | Enumerate the full list or define the extension rule. | The report shall include title, date, author, and revision. |
| manage | Vague action verb. | State the exact action or outcome. | The controller shall store the value in memory. |
| support | Broad and unclear. | State the supported function or interface. | The cart shall support a load of 150 kg. |
| handle | Undefined behavior. | State the response for each condition. | The system shall reject inputs outside the defined range. |
| improve | Relative and unmeasured. | State the target value or baseline comparison. | The process shall reduce scrap by 10 percent. |
| compatible | Missing reference. | Cite the standard, profile, version, or test suite. | The connector shall conform to the referenced profile version 3. |

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

Applicability / Constraints:
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
13. Its source, rationale, and verification intent can be identified.
14. A mandatory requirement statement uses exactly one `shall`.
15. It can be reviewed by someone who was not involved in writing it.
