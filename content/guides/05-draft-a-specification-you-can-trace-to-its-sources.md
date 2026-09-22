---
title: Draft a specification you can trace to its sources
section: recipe
order: 5
case: business-analysis
case_label: Business analysis
summary: Turn a traced requirements list and the decisions made about it into a specification where every statement can be followed back to its origin.
use_when: the requirements are agreed and someone needs a document a builder can build from and a reviewer can check.
boundary: You are drafting the specification, not deciding scope or priority.
boundary_more: Every statement must be traceable back to a source sentence and forward to the decision that accepted it. That is what makes it defensible six months later when someone asks who said we needed this.
outcome: a draft specification with a traceability table
time: 1 to 3 hours, in sittings
you_need: the traced requirements list with your keep-or-strike decisions, the decisions made so far with owners, and the house template
environment: browser
environment_label: Approved browser/document environment
risk: medium
key_a: Statement: one requirement, stated once, testably, with an identifier.
key_b: Trace: where the statement came from and who accepted it. A specification without the trace is an assertion.
---
## Start with these six steps {: .part data-part="Part 1 · Do the work" }

The assistant drafts and builds the table. You are the reviewer of every line, and the person who knows which decisions have actually been made.

<div class="flow" markdown="1">

1. **Gather what the draft rests on**
   The traced requirements list from the [requirements guide](~/guides/02-extract-requirements-in-the-authors-own-words.html) with your keep-or-strike decisions, the decisions made so far with their owners, the house template if there is one, and an example the organization considers good.
2. **Brief the assistant**
   Who will read it: the people who build, test, and approve. What is in scope and out, and who decided that.
3. **Ask for the first full draft**
   In the house shape, one requirement per statement, each with an identifier and a link back to its source sentence.
4. **Ask for the traceability table and the consistency checks**
   Identifier, statement, source, the decision that accepted it, its label. Then: statements that contradict each other, terms used two ways, requirements with no acceptance criterion, and everything still {{label kind=open}}, grouped by who can close it.
5. **Review every requirement's wording and follow the traces**
   Pick five at random and follow each back to its source sentence. Hunt the words that hide decisions. Part 2 below has the checks.
6. **Save the specification with its version, and the table beside it**
   The table is the record. It lives beside the document, not inside a conversation. Part 2 says what else the record holds.

</div>

!!! starter "Starter instruction"
    Copy this once the traced list and the decisions are in the folder.

        Draft a specification from this traced requirements list, using the house template. State each requirement once, testably, with an identifier and a link to its source sentence. Build a traceability table with the identifier, the statement, the source, the decision that accepted it, and its label. Run consistency checks for contradictions, terms used two ways, and requirements without an acceptance criterion. List everything still Open, grouped by who can close it. Do not introduce requirements that have no source or no named decision.

## Use this specification shape {: .part data-part="The deliverable" }

The house template governs the order. These parts should all be present.

<div class="shape" markdown="1">

1. **Purpose and readers** What the specification is for and who builds, tests, and approves from it.
2. **Scope** What is in and out, and who decided.
3. **Requirements** One per statement, identified, testable.
4. **Acceptance criteria** How each requirement will be checked.
5. **The traceability table** Identifier, statement, source, accepting decision, label.
6. **Open items** Grouped by who can close them.
7. **Version and change history** What changed, when, and why.

</div>

## Review, preserve, and know when to stop {: .part data-part="Part 2 · Govern the work" }

These are not more drafting steps. They are the checks that make the specification something a builder can build from and a reviewer can check.

<div class="govern" markdown="1">

<div class="govern-card" markdown="1">

### What you decide

- Every requirement's final wording. The assistant may draft or propose changes. You review and approve the final text, remain accountable for its use, and preserve contribution provenance where material.
- Priority and scope calls, or who makes them.
- Whether the specification is ready for review, or whether the Open list is still too long to be honest about.

</div>

<div class="govern-card" markdown="1">

### Check before use

- Five requirements at random, each followed back through the table to its source sentence. All five must arrive.
- The words that hide decisions: "appropriate," "as needed," "intuitive," "etc." Each is defined or becomes an Open item.
- No requirement introduced during drafting lacks a source or a named decision. Drafting is where requirements get invented.

</div>

<div class="govern-card" markdown="1">

### Keep in the record

- The specification, with its version.
- The traceability table, beside the document.
- The Open list, and the review comments when they come.

</div>

<div class="govern-card" markdown="1">

### Stop and ask

- The specification would commit the organization to something no authorized person has decided. Mark it Open and raise it.
- It touches personal, customer, or payroll data flows. Specify the data classes and rules without real examples, and involve Security early.
- Whole sections lack sources and decisions. The analysis is not done; that is not a gap for the assistant to fill.

</div>

</div>

## What a useful exchange looks like {: .part data-part="Worked example" }

<div class="exchange" markdown="1">

You provide
:   "The traced list with my keep-or-strike decisions, the scope decision from the operations lead, and the house template. Readers: the build team and the QA lead."

The assistant returns
:   Thirty-one requirements, each traced. Two contradictions: R-07 says acknowledgment within one business day, R-19 says same day; both trace to different sources and the conflict was never decided, so both are left Open with the operations lead as owner. Four uses of "as needed" without a definition, listed.

You correct
:   R-12 appeared during drafting with no source and no decision behind it. You strike it and note why in the change history.

You keep
:   The specification at version 0.1, the traceability table beside it, and the Open list, in the project folder.

</div>

## Boundaries to confirm before starting {: .part data-part="Authority" }

**This guide does not grant authority.** It describes a safe working pattern. Confirm the permitted environment, sources, and sharing boundary for this task before the assistant begins.
{: .authority-note }

| Once you have approved the boundary | In this task |
| --- | --- |
| The assistant may | draft; build the traceability table; run consistency checks; list Open items |
| You review | every requirement's wording; the table; readiness for review |
| An authorized decision-maker decides | scope, priority, and any requirement with budget, policy, or staffing effect |
| Stop and escalate | when a commitment no one authorized appears, or sensitive data flows are specified without Security involved |

!!! note "Not sure this is the right task?"
    Bring the requirements to a [guided first session](~/support/request-a-guided-session.html). The guide can help choose the task and the approved environment.
