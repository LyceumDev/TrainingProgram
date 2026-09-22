---
title: Separate verified facts, inferences, decisions, and open questions
section: recipe
order: 3
case: business-analysis
case_label: Business analysis
summary: Take any document, draft, or thread and sort every claim into the four labels, so the reader knows exactly what stands on what.
outcome: a labeled version of the document
environment: browser
environment_label: Approved browser/document environment
risk: low
time: 15 to 30 minutes
---
## What you are trying to accomplish

Most working documents mix four things without saying which is which: facts someone checked, conclusions someone reasoned to, decisions someone made, and questions nobody has answered. This recipe labels every claim with the shared vocabulary so that a reader, a reviewer, or your future self knows exactly what is standing on what.

{{labels}}

## What the assistant needs from you

- The document, draft, or thread to label, within the data boundary.
- The sources it rests on, if they are not in it.
- Who has authority to decide in this context, so the assistant can tell a decision from an opinion.

## What the assistant can carry

- Reading every sentence and proposing a label for each claim, with the reason: the source line for Verified, the reasoning for Inferred, the owner and rationale for Decided, the missing piece for Open.
- A short list of the Open items, each with a suggested owner or next step.
- Flagging sentences that sound like facts but are opinions, and sentences that sound like decisions but were made by nobody with the authority to make them.

## What you decide or approve

- Whether each label is right. You know that "the team agreed" meant two people in a hallway.
- Who owns each Open item.
- Whether the document is ready to circulate with its labels, or whether the Open items need answers first.

## What to check before you use it

!!! verify "Check before it leaves your hands"
    - Every Verified label points at a source you could open. Open the ones that carry the most weight.
    - Every Decided label names a person with the authority to decide it.
    - The Open list is honest. A long Open list is not a failure; it is information.

## What to keep in the record

!!! record "The record for this recipe"
    The labeled document and the Open list with owners. When an Open item is resolved, its label changes and the record says when and by whom.

## When to stop and ask

!!! stop "Stop and ask when"
    - A "decision" in the document would be consequential and was never actually made by someone authorized. Do not let the label launder it. Raise it.
    - The document contains sensitive personal data. Label a redacted copy.

## Authority in this recipe

| Level | In this recipe |
| --- | --- |
| The assistant may, without asking | read; propose labels with reasons; list Open items |
| You review | every label; every owner assignment |
| Needs an authorized decision-maker | any Open item that is a decision; any "Decided" claim without an authorized decider |
| Stop and escalate | a consequential decision presented as already made |

!!! example "What it looks like"
    *Assistant:* "Twenty-two claims. Nine Verified, six Inferred, three Decided, four Open. One flag: 'The vendor will be renewed in October' reads as Decided, but I can find no decision-maker or record; the only source is a forwarded note saying it 'probably' will. I have labeled it Open with the procurement lead as the suggested owner."
