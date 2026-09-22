---
title: Extract requirements while preserving source language
section: recipe
order: 2
case: business-analysis
case_label: Business analysis
summary: Lift every candidate requirement out of the sources, each with the exact sentence it came from, so nothing is invented and nothing is lost.
outcome: a traced list of candidate requirements
environment: browser
environment_label: Approved browser/document environment
risk: low
time: 30 to 60 minutes
---
## What you are trying to accomplish

A list of candidate requirements, each one traceable to the sentence in a source that gave rise to it, in language close enough to the original that the person who wrote it would recognize it. Paraphrase is where requirements quietly change meaning. This recipe keeps the words.

## What the assistant needs from you

- The sources you are permitted to use in this environment: interview notes, emails, policy documents, existing specifications, meeting minutes, with restricted details replaced first.
- The scope: which system, process, or decision the requirements are for. Without it the assistant will lift everything.
- Your definition of a requirement for this project, if you have one. A common one: a statement of something the solution must do or must be, testable in principle, owned by someone.

## What the assistant can carry

- A first pass through every source, lifting each candidate with the original sentence quoted beside it and the source and location named.
- Grouping by theme, and flagging duplicates and near-duplicates across sources.
- Flagging candidates that are wishes, constraints, or assumptions rather than requirements, with its reasoning shown.
- Noting where two sources conflict.

## What you decide or approve

- Which candidates are requirements and which are not. The assistant proposes; you strike and keep.
- How to resolve conflicts between sources, or who to ask.
- Whether a candidate's wording can be tightened without changing what the author meant. When in doubt, keep the quote and add your gloss beside it.

## What to check before you use it

!!! verify "Check before it leaves your hands"
    - Spot-check quoted sentences against their sources, more of them the more the list will be relied on. If one is not verbatim, check them all.
    - Look for requirements that appear in the list but not in any source. There should be none.
    - Read the conflicts section. Every conflict should name both sources.

## What to keep in the record

!!! record "The record for this recipe"
    The traced list, the sources, the strike decisions and why, the conflicts and who is resolving each. Keep the version with quotes; a later specification will cite it.

## When to stop and ask

!!! stop "Stop and ask when"
    - Sources contain personal, customer, or payroll information. Extract from redacted copies, or ask.
    - A "requirement" would commit the organization to a purchase, a policy change, or a staffing change. That is a decision for an authorized person, and it belongs in the open items, not the list.
    - The sources are so thin that the assistant is filling gaps by inference. Stop; go get the source.

## Authority in this recipe

| Level | In this recipe |
| --- | --- |
| The assistant may, without asking | read sources; lift and quote candidates; group; flag conflicts and non-requirements |
| You review | every keep-or-strike; every conflict resolution; the wording of anything tightened |
| Needs an authorized decision-maker | any candidate that is itself a policy, purchase, or staffing decision |
| Stop and escalate | sensitive data in the sources; sources too thin to support the list |

!!! example "What it looks like"
    *Assistant:* "Fourteen candidates from three sources. Two conflict: the process document says intake is acknowledged within one business day; the March email says same day. Both quoted. Three candidates look like wishes rather than requirements ('should feel effortless'), flagged with reasons. No candidate is without a source sentence."
