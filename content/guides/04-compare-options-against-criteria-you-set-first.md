---
title: Compare options against criteria you set first
section: recipe
order: 4
case: business-analysis
case_label: Business analysis
summary: Set the criteria before looking at the options, then let the assistant build a sourced comparison, so the recommendation follows from the criteria and not the other way round.
use_when: you have two or more options and a decision-maker wants a recommendation.
boundary: You are producing a sourced comparison and a labeled recommendation, not the decision.
boundary_more: The criteria are agreed before the options are examined, so the recommendation follows from them rather than justifying a favorite.
outcome: a comparison table with a sourced, labeled recommendation
time: 45 to 90 minutes
you_need: the options' permitted documentation, agreed criteria with weights, and who decides
environment: browser
environment_label: Approved browser/document environment
risk: medium
key_a: Criteria: what matters, how much, and what rules an option out, agreed before the comparison.
key_b: Recommendation: an inference from the criteria. The decision belongs to the authorized person.
---
## Start with these six steps {: .part data-part="Part 1 · Do the work" }

The risk in this task is not that the assistant gets a fact wrong. It is that a comparison quietly gets built to reach a conclusion. The order of the steps is the protection.

<div class="flow" markdown="1">

1. **Agree the criteria first**
   With the stakeholders, before anyone looks at the options: what matters, how much, and what would rule an option out entirely. Record them with the date and who agreed. The assistant can help you draft criteria, but it should not invent them and then apply them.
2. **Gather the permitted option documentation**
   Whatever exists for each option, within the data boundary. Confidential figures and vendor material under agreement need a check on what may be used.
3. **Brief the assistant**
   The criteria and weights, the rule-outs, who will decide, and the form they want: a ranking, a shortlist, or a single choice with reasons.
4. **Ask for the table**
   Rule-outs applied first, saying which options fell and why. Then every cell a claim with its source, or an honest {{label kind=open}} where no source exists. Then the trade-offs, written as what each choice gives up, not only what it gains.
5. **Ask for a recommendation labeled Inferred**
   Citing the criteria it rests on, because that is what a recommendation is. Ask what would change if a criterion were dropped.
6. **Review for asymmetry, then record**
   Check the winner's and the loser's strongest cells the same way. Part 2 below has the checks and what the record holds.

</div>

!!! starter "Starter instruction"
    Copy this after the criteria are agreed and recorded.

        Compare these options against the criteria and weights I have listed, in this order. First apply the rule-out criteria and say which options fall and why. Then fill a table where every cell is a claim with its source, or is marked Open. Then write the trade-offs as what each choice gives up. Then draft a recommendation labeled Inferred that cites the criteria it rests on, and say what would change if any one criterion were dropped. Do not add or change criteria.

## Use this comparison shape {: .part data-part="The deliverable" }

The criteria come first on the page, as they did in the work.

<div class="shape" markdown="1">

1. **Criteria** With weights, the date, and who agreed them.
2. **Rule-outs applied** Which options fell, and why, with the source.
3. **The table** Every cell sourced or marked Open.
4. **Trade-offs** What each choice gives up, not only what it gains.
5. **The recommendation** Labeled Inferred, with the criteria it rests on.
6. **Sensitivity** What would change if a criterion were dropped.

</div>

## Review, preserve, and know when to stop {: .part data-part="Part 2 · Govern the work" }

These are not more drafting steps. They are the checks that make the comparison something a decision-maker can trust.

<div class="govern" markdown="1">

<div class="govern-card" markdown="1">

### What you decide

- The criteria and their weights. This is the decision that shapes everything, and it is yours or the stakeholders', never the assistant's.
- Whether the Open cells matter enough to delay the recommendation.
- The recommendation itself, before it goes anywhere. If you disagree with the assistant's inference, write down why.

</div>

<div class="govern-card" markdown="1">

### Check before use

- Were the criteria written before the table was filled? If they changed during the work, the document says so and why.
- Check the winning option's three strongest cells against their sources. Then do the same for the losing option. Bias hides in asymmetry.
- Ask whether the recommendation changes if one criterion is dropped. If yes, the document says so.

</div>

<div class="govern-card" markdown="1">

### Keep in the record

- The criteria, with their date and who agreed them.
- The sourced table and the trade-offs.
- The recommendation with its label, and later the decision with its owner and rationale. Future readers will ask "why did we choose this?" This is the answer.

</div>

<div class="govern-card" markdown="1">

### Stop and ask

- The criteria keep shifting to favor an option. That is a stakeholder conversation, not a table problem.
- Confidential figures or vendor material under agreement. Check what may be used, or work from summaries.
- A decision with budget, policy, or staffing consequences is being made by the table instead of by a person.

</div>

</div>

## What a useful exchange looks like {: .part data-part="Worked example" }

<div class="exchange" markdown="1">

You provide
:   "Three intake tools. The five criteria we agreed with the operations lead on Monday, with weights, are in the record. Two rule-outs: must work with our sign-in, must keep data in our tenant. The vendor documents are in the folder."

The assistant returns
:   Option C fails the tenant rule-out, source page 4 of its documentation. Options A and B are in the table with sources; two cells are Open because neither vendor states an accessibility conformance level. A shortlist of A and B, labeled Inferred, resting on criteria one and three. If criterion three were dropped, B would lead.

You correct
:   One of A's Verified cells cites a sales sheet rather than the product documentation. You move it to Open until the vendor confirms it in writing.

You keep
:   The criteria, the table, the trade-offs, and the Inferred shortlist, ready for the decision-maker.

</div>

## Boundaries to confirm before starting {: .part data-part="Authority" }

**This guide does not grant authority.** It describes a safe working pattern. Confirm the permitted environment, sources, and sharing boundary for this task before the assistant begins.
{: .authority-note }

| Once you have approved the boundary | In this task |
| --- | --- |
| The assistant may | read the permitted option documentation; fill and source the table; draft the trade-offs; draft a labeled recommendation |
| You review | the criteria; every cell in the winning and losing columns; the recommendation |
| An authorized decision-maker decides | the decision itself, and any change to the criteria after the table exists |
| Stop and escalate | when criteria shift to favor an option, confidential figures are involved, or the table is being used to make the decision |

!!! note "Not sure this is the right task?"
    Bring the options to a [guided first session](~/support/request-a-guided-session.html). The guide can help choose the task and the approved environment.
