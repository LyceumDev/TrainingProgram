---
title: Check a memo before it goes out
section: recipe
order: 6
case: business-analysis
case_label: Business analysis
summary: Before a memo goes to people who will act on it, have the assistant read it the way a skeptical reader will, and fix what it finds.
use_when: a memo is about to go to people who will act on it.
boundary: You are reviewing the memo. The ask inside it still belongs to whoever must decide it.
boundary_more: The aim is a memo that survives a skeptical reader: every claim that matters has a source or is marked as an inference, every ambiguity is resolved or named, and every requested decision names its owner.
outcome: a review note with specific, sourced findings
time: 15 to 30 minutes
you_need: the memo, its sources, and who will read it
environment: browser
environment_label: Approved browser/document environment
risk: low
key_a: Finding: a specific problem in the memo, where it is, and why it matters.
key_b: Rewrite: a proposed fix, marked as a proposal, for you to accept or not.
---
## Start with these six steps {: .part data-part="Part 1 · Do the work" }

The assistant reads as the toughest person in the meeting would, before that person does. You decide which findings matter, because some ambiguity is deliberate and you know which.

<div class="flow" markdown="1">

1. **Gather the memo and its sources**
   Within the data boundary. If the memo names real people or figures that should not travel, work from a redacted copy.
2. **Brief the assistant**
   Who will read the memo and what they are being asked to do. Whether you want a light pass for clarity or the full skeptical read.
3. **Ask for the unsourced claims**
   Every claim that matters, asked "what is this based on?" The ones with no answer listed as {{label kind=open}}, with their location.
4. **Ask for the ambiguities and the missing decisions**
   Sentences with two readings, undefined terms, numbers without units or dates, "recently" and "significant" and "most." Places where the memo implies a choice has been made, or must be made, without saying who makes it.
5. **Review the findings and the proposed rewrites**
   For every Open claim: source it, restate it as Inferred, retain it explicitly as Open, or cut it. Record the disposition. Do not allow it to remain written as fact. Part 2 below has the checks.
6. **Save the review note and the version that went out**
   If a claim was cut for lack of a source, note it; the question will come back. Part 2 says what the record holds.

</div>

!!! starter "Starter instruction"
    Copy this as your first message and name the readers.

        Review this memo as a skeptical reader who will have to act on it. The readers are [who], and they are being asked to [what]. For every claim that matters, ask what it is based on and list the ones without a source as Open, with their location. Flag ambiguity: sentences with two readings, undefined terms, numbers without units or dates. Find any decision the memo implies without saying who makes it. Propose a specific rewrite for each finding, marked as a proposal. Do not add facts or strengthen certainty in a proposed rewrite.

## Use this review-note shape {: .part data-part="The deliverable" }

Findings first, rewrites second, your dispositions last.

<div class="shape" markdown="1">

1. **Unsourced claims** Each with its location, listed as Open.
2. **Ambiguities** Each with the two readings.
3. **Missing decisions** Each with a suggested owner.
4. **Restricted details found** Anything that should not travel.
5. **Proposed rewrites** Marked as proposals.
6. **Your dispositions** Sourced, restated as Inferred, retained explicitly as Open, or cut, with the reason.

</div>

## Review, preserve, and know when to stop {: .part data-part="Part 2 · Govern the work" }

These are not more drafting steps. They are the checks that make the memo safe to send.

<div class="govern" markdown="1">

<div class="govern-card" markdown="1">

### What you decide

- Which findings to act on. Some ambiguity is deliberate and appropriate; you know which.
- Whether an unsupported claim gets a source, is restated as Inferred, stays explicitly Open, or comes out.
- The final text. The assistant may draft or propose changes. You review and approve the final text, remain accountable for its use, and preserve contribution provenance where material.

</div>

<div class="govern-card" markdown="1">

### Check before use

- Every claim initially marked Open has a recorded disposition: sourced, restated as Inferred, retained explicitly as Open, or cut.
- The memo's ask, read aloud, says who is being asked to decide what, by when.
- No real personal, customer, or payroll detail remains that should not.

</div>

<div class="govern-card" markdown="1">

### Keep in the record

- The review note.
- The version of the memo that went out.
- Any claim cut for lack of a source, with a note.

</div>

<div class="govern-card" markdown="1">

### Stop and ask

- The memo asks a reader to approve something consequential on the strength of a claim nobody can source. Do not send it. Get the source or change the ask.
- The decision the memo asks for has already been made elsewhere. Find out where before circulating.

</div>

</div>

## What a useful exchange looks like {: .part data-part="Worked example" }

<div class="exchange" markdown="1">

You provide
:   "The intake process memo going to the directors on Friday, with the two source decks. Full skeptical read."

The assistant returns
:   Nine findings. Three claims with no source in the folder: the 40 percent figure in paragraph two, "most teams" in paragraph four, and the vendor's renewal date. Two ambiguities: "recently," and "the system," which refers to two different systems. One missing decision: paragraph six says the process "will change in Q1" without saying who decided or who approves. Rewrites proposed for all nine.

You correct
:   The 40 percent figure has a source the assistant could not see, the quarterly report. You add the citation and keep the claim. The renewal date has no source anywhere; you cut it.

You keep
:   The review note and the memo as sent, in the project folder.

</div>

## Boundaries to confirm before starting {: .part data-part="Authority" }

**This guide does not grant authority.** It describes a safe working pattern. Confirm the permitted environment, sources, and sharing boundary for this task before the assistant begins.
{: .authority-note }

| Once you have approved the boundary | In this task |
| --- | --- |
| The assistant may | read the memo and its sources; list unsourced claims and ambiguities; propose rewrites marked as proposals |
| You review | every finding; every rewrite; the final text |
| An authorized decision-maker decides | whatever the memo itself asks for |
| Stop and escalate | when a consequential ask rests on an unsourced claim |

!!! note "Not sure this is the right task?"
    Bring the memo to a [guided first session](~/support/request-a-guided-session.html). The guide can help choose the task and the approved environment.
