---
title: Compare options against explicit criteria
section: recipe
order: 4
case: business-analysis
case_label: Business analysis
summary: Set the criteria first, then let the assistant build the comparison, so the recommendation follows from the criteria and not the other way round.
outcome: a comparison table with a sourced recommendation
environment: browser
environment_label: Approved browser/document environment
risk: medium
time: 45 to 90 minutes
---
## What you are trying to accomplish

A comparison of two or more options that a decision-maker can trust: the criteria stated before the options were examined, each cell in the table tied to a source, the trade-offs named plainly, and a recommendation that follows from the criteria rather than justifying a favorite. The risk in this recipe is not that the assistant gets a fact wrong. It is that the comparison quietly gets built to reach a conclusion.

## What the assistant needs from you

- The options, named, with whatever documentation exists for each and is permitted in this environment.
- The criteria, agreed before the comparison starts: what matters, how much, and what would rule an option out entirely. If you do not have criteria, run that conversation with the stakeholders first. The assistant can help you draft the criteria, but it should not invent them and then apply them.
- Who will decide, and what kind of recommendation they want: a ranking, a shortlist, or a single choice with reasons.

## What the assistant can carry

- Filling the table: every cell a claim with a source, or an honest {{label kind=open}} where no source exists.
- Applying the rule-out criteria first and saying which options fell and why.
- Writing the trade-offs as trade-offs: what you give up with each choice, not only what you gain.
- A draft recommendation that cites the criteria it rests on, labeled {{label kind=inferred}}, because that is what a recommendation is.

## What you decide or approve

- The criteria and their weights. This is the decision that shapes everything, and it is yours or the stakeholders', never the assistant's.
- Whether the Open cells matter enough to delay the recommendation.
- The recommendation itself, before it goes anywhere. You may disagree with the assistant's inference; write down why.

## What to check before you use it

!!! verify "Check before it leaves your hands"
    - Were the criteria written before the table was filled? If they changed during the work, say so in the document and why.
    - Pick the option that won and check its three strongest cells against their sources. Then pick the one that lost and do the same. Bias hides in asymmetry.
    - Read the recommendation and ask: would it change if criterion two were dropped? If yes, the document should say so.

## What to keep in the record

!!! record "The record for this recipe"
    The criteria with their date and who agreed them, the sourced table, the trade-offs, the recommendation with its label, and, once made, the decision with its owner and rationale. Future readers will ask "why did we choose this?" This is the answer.

## When to stop and ask

!!! stop "Stop and ask when"
    - The criteria keep shifting to favor an option. That is a stakeholder conversation, not a table problem.
    - The comparison involves cost or contract figures that are confidential, or vendor material under agreement. Check what may be used in this environment, or work from summaries.
    - The decision has budget, policy, or staffing consequences. The recipe ends at recommendation; the decision belongs to the authorized person.

## Authority in this recipe

| Level | In this recipe |
| --- | --- |
| The assistant may, without asking | read option documentation; fill and source the table; draft trade-offs; draft a labeled recommendation |
| You review | the criteria; every cell in the winning and losing columns; the recommendation |
| Needs an authorized decision-maker | the decision itself, and any change to the criteria after the table exists |
| Stop and escalate | shifting criteria; confidential figures; a decision being made by the table instead of by a person |

!!! example "What it looks like"
    *You:* "Three options for the intake tool. The criteria are the five we agreed with the operations lead on Monday, in the record, weights attached. Two rule-outs: must work with our sign-in, must keep data in our tenant. Fill the table from the vendor documents in the folder and draft a shortlist."

    *Assistant:* "Option C fails the tenant rule-out; its documentation places data in a shared region, source page 4. Options A and B are in the table with sources; two cells are Open because neither vendor states an accessibility conformance level. Shortlist of A and B drafted as Inferred, resting on criteria one and three. If criterion three were dropped, B would lead."
