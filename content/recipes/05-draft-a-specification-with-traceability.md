---
title: Draft a specification with traceability to sources
section: recipe
order: 5
case: business-analysis
case_label: Business analysis
summary: Turn a traced requirements list and the decisions made about it into a specification where every statement can be followed back to its origin.
outcome: a draft specification with a traceability table
environment: browser
environment_label: Approved browser/document environment
risk: medium
time: 1 to 3 hours, in sittings
---
## What you are trying to accomplish

A specification a builder can build from and a reviewer can check: each requirement stated once, testably, with an identifier, and a table that follows every statement back to the source sentence and forward to the decision that accepted it. Traceability is what makes a specification defensible six months later when someone asks "who said we needed this?"

## What the assistant needs from you

- The traced requirements list from [recipe 2](~/recipes/02-extract-requirements-preserving-source-language.html), with your keep-or-strike decisions.
- The decisions made so far, with owners: scope, priorities, anything ruled out.
- The house template for specifications, if there is one, and an example the organization considers good.
- The intended readers: the people who will build, test, and approve.

## What the assistant can carry

- A first full draft in the house shape, one requirement per statement, each with an identifier and a link back to its source sentence.
- The traceability table: identifier, statement, source, decision that accepted it, label.
- Consistency checks: statements that contradict each other, terms used two ways, requirements with no acceptance criterion.
- A list of everything that is still {{label kind=open}}, grouped by who can close it.

## What you decide or approve

- Every requirement's final wording. The assistant may draft or propose changes. You review and approve the final text, remain accountable for its use, and preserve contribution provenance where material.
- Priority and scope calls, or who makes them.
- Whether the specification is ready for review, or whether the Open list is still too long to be honest about.

## What to check before you use it

!!! verify "Check before it leaves your hands"
    - Pick five requirements at random and follow each back through the table to its source sentence. All five must arrive.
    - Search the draft for words that hide decisions: "appropriate," "as needed," "intuitive," "etc." Each one is either defined or turned into an Open item.
    - Confirm that no requirement introduced during drafting lacks a source or a named decision. Drafting is where requirements get invented.

## What to keep in the record

!!! record "The record for this recipe"
    The specification with its version, the traceability table, the Open list, and the review comments when they come. The table is the record; keep it beside the document, not inside a conversation.

## When to stop and ask

!!! stop "Stop and ask when"
    - The specification would commit the organization to something no authorized person has decided. Mark it Open and raise it; do not let the document decide.
    - It touches personal, customer, or payroll data flows. Specify the data classes and rules without pasting real examples, and involve Security early.
    - Sources and decisions are missing for whole sections. That is a sign the analysis is not done, not a gap for the assistant to fill.

## Authority in this recipe

| Level | In this recipe |
| --- | --- |
| The assistant may, without asking | draft; build the traceability table; run consistency checks; list Open items |
| You review | every requirement's wording; the table; readiness for review |
| Needs an authorized decision-maker | scope, priority, and any requirement with budget, policy, or staffing effect |
| Stop and escalate | commitments no one authorized; sensitive data flows without Security involved |

!!! example "What it looks like"
    *Assistant:* "Draft has thirty-one requirements, each traced. Two contradictions: R-07 says acknowledgment within one business day, R-19 says same day; both trace to different sources and the conflict was never decided. I have left both, labeled Open, with the operations lead as owner. Four requirements use 'as needed' without a definition; listed for you."
