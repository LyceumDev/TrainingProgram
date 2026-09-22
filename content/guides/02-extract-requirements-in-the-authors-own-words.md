---
title: Extract requirements in the authors' own words
section: recipe
order: 2
case: business-analysis
case_label: Business analysis
summary: Lift every candidate requirement out of the sources, each with the exact sentence it came from, so nothing is invented and nothing is lost.
use_when: someone hands you notes, emails, or documents and asks what the requirements are.
boundary: You are listing candidate requirements with their sources, not deciding what gets built.
boundary_more: Keeping the authors' words is the point. Paraphrase is where requirements quietly change meaning.
outcome: a traced list of candidate requirements
time: 30 to 60 minutes
you_need: the permitted sources and a one-line statement of scope
environment: browser
environment_label: Approved browser/document environment
risk: low
key_a: Candidate: a statement lifted from a source, quoted exactly, that might be a requirement.
key_b: Accepted requirement: a candidate an authorized requirement owner has approved. This guide produces candidates and proposed dispositions; it records, but does not make, the acceptance decision.
---
## Start with these six steps {: .part data-part="Part 1 · Do the work" }

The assistant reads everything and quotes exactly. You set the scope, define what counts as a requirement here, and review every proposed disposition. Acceptance stays with the requirement owner, who may or may not be you.

<div class="flow" markdown="1">

1. **Gather the permitted sources**
   Interview notes, emails, policy documents, existing specifications, meeting minutes. Replace restricted details before sharing anything, and keep each source's name and location so quotes can be checked.
2. **Brief the assistant**
   State the scope in one line: which system, process, or decision the requirements are for. Give your definition of a requirement for this project. A common one: a statement of something the solution must do or must be, testable in principle, owned by someone.
3. **Ask for the traced list**
   Every candidate with the exact sentence it came from, quoted, and the source and location named. No paraphrase of the requirement text.
4. **Ask it to group and flag**
   Group by theme. Flag duplicates and near-duplicates across sources, candidates that are wishes, constraints, or assumptions rather than requirements, and places where two sources conflict.
5. **Recommend retain, exclude, or ask, then route the decision**
   The assistant proposes classifications and dispositions. You review them and, where you hold the authority, decide; otherwise route each acceptance or conflict to the requirement owner. Record who decided and why. Part 2 below has the checks.
6. **Save the list with its quotes**
   The version with the quoted sentences is the record. A later specification will cite it. Part 2 says what else the record holds.

</div>

!!! starter "Starter instruction"
    Copy this as your first message and fill in the scope.

        Help me extract candidate requirements from these sources for [scope]. For each candidate, quote the exact sentence it comes from and name the source and its location. Group the candidates by theme. Flag duplicates, and flag anything that is a wish, a constraint, or an assumption rather than a requirement. List every place where two sources conflict. Do not paraphrase the requirement text. For each candidate, propose a disposition (retain as a candidate, exclude, or refer for acceptance) with the reason; do not mark anything as accepted.

## Use this list shape {: .part data-part="The deliverable" }

One row per candidate. If a column cannot be filled from the sources, leave it visible and mark it Open.

<div class="shape" markdown="1">

1. **Identifier** A short code so the candidate can be cited later.
2. **Candidate, in the source's words** The exact sentence, quoted.
3. **Source and location** Which document, and where in it.
4. **Theme** The group it belongs to.
5. **Flag** Duplicate, wish, constraint, assumption, or conflict, with the reason.
6. **Disposition** Retain as a candidate, exclude from the candidate list, or refer for acceptance, with the reason and the decision owner.

</div>

## Review, preserve, and know when to stop {: .part data-part="Part 2 · Govern the work" }

These are not more drafting steps. They are the checks that make the list safe to build on.

<div class="govern" markdown="1">

<div class="govern-card" markdown="1">

### What you decide

- Each candidate's proposed disposition: retain, exclude, or refer. Where you hold requirement authority, the acceptance itself; otherwise, who it is routed to.
- How each conflict between sources is resolved, or who to ask.
- Whether tightened wording still says what the author meant. When in doubt, keep the quote and add your gloss beside it.

</div>

<div class="govern-card" markdown="1">

### Check before use

- Spot-check quoted sentences against their sources, more of them the more the list will be relied on. If one is not verbatim, check them all.
- Confirm no candidate appears without a source sentence.
- Confirm every conflict names both sources.

</div>

<div class="govern-card" markdown="1">

### Keep in the record

- The traced list, with the quotes.
- Each disposition, who decided it, and why.
- The conflicts and who is resolving each.

</div>

<div class="govern-card" markdown="1">

### Stop and ask

- Sources hold personal, customer, or payroll information. Extract from redacted copies, or ask.
- A candidate is itself a purchase, policy, or staffing decision. It belongs to an authorized person, in the open items.
- The sources are so thin that the assistant is filling gaps by inference. Go get the source.

</div>

</div>

## What a useful exchange looks like {: .part data-part="Worked example" }

<div class="exchange" markdown="1">

You provide
:   "Three sources: the March email thread, the intake process document, and the interview notes, with names replaced. Scope: the intake process. A requirement here is something the process must do or be, testable, with an owner."

The assistant returns
:   Fourteen candidates, each quoted with its location, grouped in four themes. Three flagged as wishes ("should feel effortless"). One conflict: the process document says acknowledgment within one business day; the March email says same day.

You correct
:   Two of the "wishes" are constraints from the compliance note that the assistant read as preferences. You relabel them and retain them as candidates.

You keep
:   The traced list with the quotes, each disposition with its reason and owner, and the conflict assigned to the operations lead.

</div>

## Boundaries to confirm before starting {: .part data-part="Authority" }

**This guide does not grant authority.** It describes a safe working pattern. Confirm the permitted environment, sources, and sharing boundary for this task before the assistant begins.
{: .authority-note }

| Once you have approved the boundary | In this task |
| --- | --- |
| The assistant may | read the permitted sources; lift and quote candidates; group them; flag conflicts and non-requirements |
| You review | every proposed disposition; every conflict resolution; the wording of anything tightened |
| An authorized requirement owner decides | which candidates become accepted requirements, and how substantive conflicts are resolved |
| An authorized decision-maker decides | any candidate that is itself a policy, purchase, or staffing decision |
| Stop and escalate | when sources hold restricted data, or are too thin to support the list |

!!! note "Not sure this is the right task?"
    Bring the sources to a [guided first session](~/support/request-a-guided-session.html). The guide can help choose the task and the approved environment.
