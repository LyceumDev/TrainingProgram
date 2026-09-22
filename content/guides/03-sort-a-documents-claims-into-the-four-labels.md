---
title: Sort a document's claims into the four labels
section: recipe
order: 3
case: business-analysis
case_label: Business analysis
summary: Take any document, draft, or thread and label every claim as Verified, Inferred, Decided, or Open, so the reader knows exactly what stands on what.
use_when: a document is about to circulate and you cannot tell which of its statements are checked facts, reasoning, decisions, or open questions.
boundary: You are labeling claims, not settling them.
boundary_more: A label says what a statement rests on. Resolving an Open item or making a decision belongs to whoever owns it.
outcome: a labeled version of the document with an Open list
time: 15 to 30 minutes
you_need: the document, its sources, and who holds authority to decide in this context
environment: browser
environment_label: Approved browser/document environment
risk: low
key_a: Decided: a choice made by an authorized person. Authoritative as a decision, not proof that its premises are true.
key_b: Inferred: a conclusion drawn from evidence, with the reasoning visible. Not a guess.
---
## Start with these six steps {: .part data-part="Part 1 · Do the work" }

The assistant reads every sentence and proposes a label with a reason. You know which labels are right, because you know what "the team agreed" actually meant.

<div class="flow" markdown="1">

1. **Gather the document and its sources**
   The document, draft, or thread, within the data boundary. If it holds personal data, label a redacted copy. Add the sources it rests on if they are not in it.
2. **Brief the assistant**
   Say who has authority to decide in this context, so it can tell a decision from an opinion. Name the audience the document is for.
3. **Ask for a label on every material claim**
   With the reason for each: the source line for {{label kind=verified}}, the reasoning for {{label kind=inferred}}, the owner and rationale for {{label kind=decided}}, the missing piece for {{label kind=open}}.
4. **Ask for the flags and the Open list**
   Sentences that sound like facts but are opinions. Sentences that sound like decisions but were made by nobody with the authority to make them. The Open items, each with a suggested owner or next step.
5. **Review the labels, especially every Decided**
   A Decided label needs a person with the authority to decide it. Part 2 below has the checks.
6. **Save the labeled version and the Open list**
   When an Open item is resolved, its label changes and the record says when and by whom. Part 2 says what the record holds.

</div>

!!! starter "Starter instruction"
    Copy this as your first message and name the decision-maker.

        Label every material claim in this document as Verified, Inferred, Decided, or Open. For each label give the reason: the source line for Verified, the reasoning for Inferred, the decision-maker and rationale for Decided, the missing piece for Open. In this context, [name or role] holds the authority to decide. Flag sentences that read as facts but are opinions, and sentences that read as decisions but were made by no one with authority. Then list the Open items with a suggested owner for each.

## Use this labeled shape {: .part data-part="The deliverable" }

The document stays as it is. The labels and the list sit beside it.

<div class="shape" markdown="1">

1. **The text, unchanged** Labeling does not edit.
2. **A label on each material claim** Verified, Inferred, Decided, or Open.
3. **The reason for each label** The source, the reasoning, the decider, or the missing piece.
4. **Flags** Fact-sounding opinions and decision-sounding non-decisions.
5. **The Open list** Each item with an owner or next step.

</div>

## Review, preserve, and know when to stop {: .part data-part="Part 2 · Govern the work" }

These are not more drafting steps. They are the checks that make the labeled document trustworthy.

<div class="govern" markdown="1">

<div class="govern-card" markdown="1">

### What you decide

- Whether each label is right.
- Who owns each Open item.
- Whether the document can circulate with its labels, or the Open items need answers first.

</div>

<div class="govern-card" markdown="1">

### Check before use

- Every Verified label points at a source you could open. Open the ones that carry the most weight.
- Every Decided label names a person with the authority to decide it.
- The Open list is honest. A long Open list is not a failure; it is information.

</div>

<div class="govern-card" markdown="1">

### Keep in the record

- The labeled document.
- The Open list with owners.
- Label changes, with when and by whom.

</div>

<div class="govern-card" markdown="1">

### Stop and ask

- A "decision" in the document would be consequential and was never made by someone authorized. Do not let the label launder it. Raise it.
- The document contains sensitive personal data. Label a redacted copy.

</div>

</div>

## What a useful exchange looks like {: .part data-part="Worked example" }

<div class="exchange" markdown="1">

You provide
:   "The Q4 planning memo and the two source decks, names removed. The steering committee holds the decisions here."

The assistant returns
:   Twenty-two claims: nine Verified, six Inferred, three Decided, four Open. One flag: "the vendor will be renewed in October" reads as Decided, but no decision-maker or record supports it; the only source is a forwarded note saying it "probably" will.

You correct
:   You confirm the renewal was never decided. It becomes Open, with the procurement lead as owner, and the memo's wording is softened to match.

You keep
:   The labeled memo and the Open list in the project folder.

</div>

## Boundaries to confirm before starting {: .part data-part="Authority" }

**This guide does not grant authority.** It describes a safe working pattern. Confirm the permitted environment, sources, and sharing boundary for this task before the assistant begins.
{: .authority-note }

| Once you have approved the boundary | In this task |
| --- | --- |
| The assistant may | read the document and its sources; propose labels with reasons; list Open items with suggested owners |
| You review | every label; every owner assignment |
| An authorized decision-maker decides | any Open item that is a decision; any Decided claim without an authorized decider |
| Stop and escalate | when a consequential decision is presented as already made |

!!! note "Not sure this is the right task?"
    Bring the document to a [guided first session](~/support/request-a-guided-session.html). The guide can help choose the task and the approved environment.
