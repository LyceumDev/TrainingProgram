---
title: Business analysis and specification writing
section: case
order: 2
art: case-business-analysis
cta: Start here
summary: Requirements, specifications, research, comparisons, memos, decision records, and traceability. The first complete case, because everyone does some of it.
---
## What working with an assistant looks like in this work

Business analysis is the work of turning what people say they need into something the organization can act on: a problem statement, a set of requirements, a comparison, a specification, a decision. Most of it is reading, structuring, cross-checking, and writing. An AI assistant is very good at the reading, structuring, and cross-checking. You are the one who knows which stakeholder meant what, which constraint is real, and what the organization is actually willing to decide.

The division that works: you supply the purpose, the sources, and the judgment; the assistant produces structure and drafts fast, labels what it could and could not verify, and asks when the sources disagree.

## A realistic day

Tuesday morning. A manager forwards a two-paragraph email asking for "a better way to handle the intake backlog," plus a spreadsheet and last year's process document.

1. You open the project record for this request, add the three sources, and write the purpose in two sentences.
2. With the [problem statement guide](~/guides/01-turn-a-vague-request-into-a-clear-problem-statement.html), the assistant drafts a structured statement from the email and the documents. Two claims come back labeled Open, because nothing in the sources supports them. You call the manager; one is confirmed, one was a guess. The record gets both.
3. With the [requirements guide](~/guides/02-extract-requirements-in-the-authors-own-words.html), the assistant lifts fourteen candidate requirements, each with the sentence it came from. You exclude three that were wishes, not requirements, and record why.
4. By lunch you have a one-page problem statement and a traced requirements list, both with sources, to take to Thursday's meeting. The record is updated: what was decided, what is open, who owns the next step.

The workflow itself depends on no particular product. Using it with organizational material still depends on an approved environment, or on the guide's approved environment during the recorded interim. Beyond that, it took the documents and an hour.

## The first three task guides to try

1. [Turn a vague request into a clear problem statement](~/guides/01-turn-a-vague-request-into-a-clear-problem-statement.html)
2. [Extract requirements in the authors' own words](~/guides/02-extract-requirements-in-the-authors-own-words.html)
3. [Sort a document's claims into the four labels](~/guides/03-sort-a-documents-claims-into-the-four-labels.html)

Then: [compare options against criteria you set first](~/guides/04-compare-options-against-criteria-you-set-first.html), [draft a specification you can trace to its sources](~/guides/05-draft-a-specification-you-can-trace-to-its-sources.html), and [check a memo before it goes out](~/guides/06-check-a-memo-before-it-goes-out.html).

{{recipes case=business-analysis}}

## Environments that may be involved

This case can begin in an [approved browser or document environment](~/environments/index.html#browser). It does not need access to a code repository or an operational system. While no business-user environment is yet approved, a guided first session runs the work in the guide's approved environment, under the guide's hands, with non-sensitive material. That counts as a guided demonstration on your real work; your own onboarding begins when you have an approved environment you can resume from.

## Data and authority boundaries

- **Data.** Analysis documents often contain names, amounts, and case details. The [one absolute](~/lessons/05-safety-and-organizational-data.html) applies: real customer, employee, and payroll information does not go into the conversation. Describe the kind of thing, use placeholders, and point with reference numbers.
- **Authority.** In this case the assistant reads, drafts, and recommends. It does not decide scope, priority, or what the organization will build or buy. Every task guide on this page ends with the boundaries to confirm before the assistant begins.

## Common failure and recovery moments

- **The confident summary.** The assistant summarizes a policy document and one sentence is not in the document. You ask "what is that based on?" The assistant cannot point to a line. The sentence becomes Open, and the record notes it. Ordinary; no drama.
- **The wish dressed as a requirement.** "The system should be intuitive" arrives as requirement seven. You send it back: intuitive to whom, doing what? It becomes an open question for the stakeholder, which is where it belonged.
- **Lost context on Thursday.** You open the conversation and the assistant has nothing from Tuesday. You open the project record, and the context is there. That is the record doing its job.
