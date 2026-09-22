---
title: Turn a vague request into a clear problem statement
section: recipe
order: 1
case: business-analysis
case_label: Business analysis
summary: From a forwarded email and a few attachments to a one-page statement of what is happening, who it affects, what is known, and what is not.
use_when: someone asks for a change, purchase, or solution before the underlying problem is clear enough to evaluate.
boundary: You are making a problem statement, not recommending a solution.
boundary_more: The result should give decision-makers a shared, evidence-based description of what is happening and what remains unknown.
outcome: a one-page problem statement
time: 20 to 40 minutes
you_need: the original request and the sources you are permitted to use
environment: browser
environment_label: Approved browser/document environment
risk: low
key_a: Problem: what is happening and what outcome is needed.
key_b: Solution: what the organization might do about it. This guide stops before the solution.
---
## Start with these six steps {: .part data-part="Part 1 · Do the work" }

The assistant can do much of the reading and drafting. You supply the permitted context, correct the framing, and approve what leaves the working space.

<div class="flow" markdown="1">

1. **Gather the request and its sources**
   Use the request in the requester's own words. Add the email, spreadsheet, process document, or earlier memo you are permitted to use. Replace restricted details with placeholders and reference numbers before sharing them.
2. **Brief the assistant**
   State who will read the result, what decision or conversation it will support, and any constraints already known. Identify unwritten knowledge as your own observation rather than as a sourced fact.
3. **Ask for a problem statement, not a solution**
   Request the seven-part shape below. Tell the assistant not to propose remedies, vendors, systems, staffing changes, or priorities.
4. **Label what each claim rests on**
   Every material claim should show its status: {{label kind=verified}} {{label kind=inferred}} {{label kind=decided}} {{label kind=open}}. These four labels travel with the work.
5. **Review the framing and the important claims**
   Open the sources behind consequential Verified claims. Check that "what good looks like" describes an outcome rather than hiding a preferred solution. Correct any framing the assistant cannot know from the documents. Part 2 below has the full checklist.
6. **Assign open questions and save the record**
   Name who can answer each Open item. Save the statement, the source list, the open questions, and later decisions in the project folder, not only in the conversation. Part 2 says what the record holds.

</div>

!!! starter "Starter instruction"
    Copy this as your first message and adjust the details to your request.

        Help me turn this request into a one-page problem statement. Use these sections: situation, affected people or process, evidence, prior attempts, constraints, desired outcome, and open questions. Do not propose a solution. Tie factual claims to their sources and label each material claim Verified, Inferred, Decided, or Open.

## Use this one-page shape {: .part data-part="The deliverable" }

These headings keep the draft focused on the problem. If a section cannot yet be supported, leave it visible and mark it Open.

<div class="shape" markdown="1">

1. **Situation** What is happening now, and where?
2. **Affected people or process** Who or what experiences the problem?
3. **Evidence** What sources show scale, frequency, cost, or impact?
4. **Prior attempts** What has already been tried, and what happened?
5. **Constraints** What cannot change, and what limits the work?
6. **Desired outcome** What would improve, without naming the solution?
7. **Open questions** What is still unknown, why it matters, and who can answer it?

</div>

## Review, preserve, and know when to stop {: .part data-part="Part 2 · Govern the work" }

These are not more drafting steps. They are the checks that make the result safe to use and possible to resume later.

<div class="govern" markdown="1">

<div class="govern-card" markdown="1">

### What you decide

- Whether this is the requester's actual problem.
- Which inferences you accept or want checked.
- Which questions go back to the requester.

</div>

<div class="govern-card" markdown="1">

### Check before use

- Read the sources behind important Verified claims.
- Look for a preferred solution hiding in the outcome.
- Confirm restricted details are absent.

</div>

<div class="govern-card" markdown="1">

### Keep in the record

- The final problem statement.
- The source list and locations.
- Open questions, owners, and later decisions.

</div>

<div class="govern-card" markdown="1">

### Stop and ask

- Sources contain restricted details.
- The "problem" was written to justify a decision already made.
- A consequential claim has no source.

</div>

</div>

## What a useful exchange looks like {: .part data-part="Worked example" }

<div class="exchange" markdown="1">

You provide
:   "Here are the operations manager's email, the backlog spreadsheet, and the 2025 intake process, with names replaced. The statement is for Thursday's planning meeting."

The assistant returns
:   A seven-part draft with every material claim labeled, plus a separate list of questions only the requester can answer.

You correct
:   The draft treats a staffing rumor as a cause. You mark it Open, assign it to the operations manager, and remove it from the factual description.

You keep
:   The revised statement, its source list, and the open-question owner in the project folder.

</div>

## Boundaries to confirm before starting {: .part data-part="Authority" }

**This guide does not grant authority.** It describes a safe working pattern. Confirm the permitted environment, sources, and sharing boundary for this task before the assistant begins.
{: .authority-note }

| Once you have approved the boundary | In this task |
| --- | --- |
| The assistant may | read the permitted sources you provide; draft the statement; propose questions; label claims |
| You review | every material claim; the framing of the problem; the desired outcome; questions before they go to anyone |
| An authorized decision-maker decides | scope, priority, policy, staffing, purchasing, and what the organization will build or adopt |
| Stop and escalate | when restricted data is required, a foregone decision is being disguised as analysis, or a consequential claim cannot be supported |

!!! note "Not sure this is the right task?"
    Bring the request to a [guided first session](~/support/request-a-guided-session.html). The guide can help choose the task and the approved environment.
