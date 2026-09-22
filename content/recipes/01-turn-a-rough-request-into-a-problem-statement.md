---
title: Turn a rough request into a structured problem statement
section: recipe
order: 1
case: business-analysis
case_label: Business analysis
summary: From a forwarded email and a few attachments to a one-page statement of the problem, who has it, what is known, and what is not.
outcome: a one-page problem statement
environment: browser
environment_label: Approved browser/document environment
risk: low
time: 20 to 40 minutes
---
## What you are trying to accomplish

A rough request ("we need a better way to handle the intake backlog") becomes a statement everyone can agree is the problem: what is happening, to whom, how often, what it costs, what has been tried, and what a good outcome would look like. Not a solution. The statement is the thing you take to the people who will decide what to do.

## What the assistant needs from you

- The request as it arrived, in the requester's own words.
- The sources you have and are permitted to use in this environment: the email thread, the spreadsheet, the process document, the earlier memo. Point to them rather than summarizing them, within the data boundary: real personal, customer, or payroll details are replaced with placeholders and reference numbers first.
- The purpose in one or two sentences: what this statement is for and who will read it.
- Anything you already know that is not written down, labeled as such ("I know from the team that…").

## What the assistant can carry

- Reading all the sources and lifting the facts, each tied to where it came from.
- A first draft in the standard shape: situation, who is affected, evidence, what has been tried, constraints, what good looks like, open questions.
- Labeling each claim with the shared vocabulary: {{label kind=verified}} when a source supports it, {{label kind=inferred}} when it reasoned to it, {{label kind=open}} when nothing supports it yet.
- A list of the questions only the requester can answer.

## What you decide or approve

- Whether the statement describes the problem the requester actually has. You may know it is really about staffing, not process. Say so; the assistant cannot.
- Which inferences you accept and which you want checked.
- What goes to the requester as a question and what you can answer yourself.

## What to check before you use it

!!! verify "Check before it leaves your hands"
    - Open the sources behind the {{label kind=verified}} claims that matter most and read the lines they rest on. The more the statement will be relied on, the more of them you check.
    - Read the "what good looks like" paragraph as the requester would. Is it their outcome or a solution in disguise?
    - Confirm there are no real names, amounts, or identifiers from real people in the statement. Placeholders and reference numbers only.

## What to keep in the record

!!! record "The record for this recipe"
    The statement itself, the list of sources, the open questions with who owns each, and any decision the requester made when you asked. Put it in the project folder, not only in the conversation.

## When to stop and ask

!!! stop "Stop and ask when"
    - The sources contain real customer, employee, or payroll details you would need to paste. Rewrite with placeholders first, or ask your guide.
    - The request is really a decision that someone senior has already made and the "problem" is being written to fit it. That is a conversation for a person.
    - The assistant produces a claim it cannot source and you cannot either. Mark it Open. Do not let it into the statement as fact.

## Authority in this recipe

| Level | In this recipe |
| --- | --- |
| The assistant may, without asking | read the sources you provide; draft the statement; propose questions; label claims |
| You review | every claim in the statement; the framing of the problem; the questions before they go to anyone |
| Needs an authorized decision-maker | nothing in this recipe; the statement recommends nothing |
| Stop and escalate | real personal or payroll data in the sources; a request that is a foregone decision in disguise |

!!! example "What it looks like"
    *You:* "Here is the email from the operations manager, the backlog spreadsheet, and the 2025 intake process document, with the names replaced. The purpose is a one-page problem statement for Thursday's planning meeting. Draft it in the standard shape and label every claim."

    *Assistant:* "Drafted. Eleven claims: seven Verified from the spreadsheet and the process document, two Inferred, two Open. The Open ones: that the backlog grew because of the March form change, which nothing in these sources shows, and that two staff left, which the email implies but does not state. Both are questions for the manager."
