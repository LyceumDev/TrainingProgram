# AI Collaboration Portal — prototype

> **For reviewers:** open the prototype at the published link your program guide sent you, or download the repository (Code, then Download ZIP), unzip it, and open `site/index.html` in your browser. Nothing to install. This is prototype v0.4, under review: the Standards page is marked as a draft for Security review, the request form has no recipient address yet, and the Environments page states what is approved and what is still being assessed. Comments are welcome by any route. The About page says who made it and the words it uses.

The clickable prototype from the settled plan (`docs/training-program/PLAN_AI-Partnership-Portal_v1.0-SETTLED_2026-09-22.md`, P1) as revised in v0.4 after Aster's full review (2026-09-22). Content is the product; the prototype is one rendering of it, and the SharePoint pages are the other. Nothing is written twice.

The folder keeps its original name (`ai-partnership-portal`) and the plan documents keep theirs; the program's public name is the **AI Collaboration Portal**. See "Vocabulary" below for why.

## Build, check, view

```
pip install -r build/requirements.txt
python build/build.py
python build/check.py
```

Then open `site/index.html` in a browser. No server needed. Do not run the build while `site/` is being served from a live process on Windows: the folder is held and the clean-and-rebuild falls back to overwriting in place.

`check.py` verifies internal links and fragments, heading structure (one H1, no skipped levels), the form recipient, and the known contrast pairs in both themes, computed from the tokens in `styles.css`. It also prints every remaining occurrence of "partner" wording for a human read. It exits 1 on any failure.

## Theme

Light is the front door on every first visit. Dark is a deliberate choice made with the header control (a toggle button with a constant name, "Dark theme", and an `aria-pressed` state), remembered in `localStorage` under `portal-theme`. The site never follows the operating system's theme. Print output is always light. Reduced motion is honored. Inverse surfaces (the support strip, the skip link, code blocks, active filter chips) use dedicated `--inverse-*` tokens rather than reversing the theme's foreground and background, so they hold contrast in both themes.

## Vocabulary (an interface decision, recorded)

On 2026-09-22 the program owner, with Aster's review, decided the portal's public vocabulary. It is written into the About page ("The words we use") and it governs every page:

- **AI Collaboration Portal** for the portal and program.
- **AI assistant** as the familiar general term for an AI system that helps research, analyze, draft, and organize.
- **AI agent** only where the system can use tools or perform actions within an environment.
- **AI collaboration** or **working with AI** for the continuing practice.
- **human–AI working team** when the person and the AI must be named as a unit.
- **program guide** for the human supporting a participant.
- **Never "tool" for an AI entity.** A product, interface, or capability is a tool; the AI system is not called one.
- **Named authorship is outside the substitution.** Where the portal credits Osiris, Sage, or Aster, it keeps the names, roles, and underlying-system information (About → "Who made it").

This is a translation of the entrance so an unfamiliar reader reaches the working model. It is not a description of the relationship the program's authors practice, which the framework beneath the portal calls partnership. The About page carries the bridge sentence that says so in public terms.

## Layout

```
content/      portable source — markdown + front-matter, one file per page
  index.md                  home
  cases/                    the three entrances (business analysis complete; two previews)
  recipes/                  the returning spine (six for business analysis)
  lessons/                  the six literacy lessons
  environments/             where the assistant will work — branches + "I don't know yet"
  support/                  a person · guided-session request · FAQ · "I don't know yet" · urgent route
  standards/                standards and safety (draft for Security review) · the environment-readiness standard
  leaders/                  the one-page leadership view
  about.md                  what this is · the words we use · who made it · seminar · consent · accessibility
build/
  build.py                  markdown → site (python-markdown; shortcodes for the few components)
  check.py                  automated checks on the built site (see above)
  requirements.txt          pinned dependency
  template.html             the page shell (theme control, nav, breadcrumb, support strip, footer)
  styles.css                the design system (tokens, components, dark theme, print)
  site.js                   progressive enhancement only (theme, menu, recipe filters, request handoff)
  illustrations/*.svg       inline art (CSS variables; works in both themes)
site/                       the rendered prototype (generated; do not edit)
```

## Content conventions

- **Front-matter keys:** `title`, `section` (home · case · recipe · lesson · environment · support · page), `order`, `summary`, `kicker`, `art`, `layout: wide` (home only). Recipes add `case`, `case_label`, `outcome`, `environment`, `environment_label` (always "Approved browser/document environment" or the equivalent approved wording), `risk` (workflow risk: low · medium · high), `time`. Cases add `status` (e.g. `preview`) and `cta`.
- **Workflow risk** is rendered with its definition on every recipe page and beside the filters: it assumes permitted information in an approved environment and is always overridden by data sensitivity, consequential actions, and policy.
- **Links between pages** are written `~/path/page.html`; the build rewrites them for the page's depth so the site works from `file://` and from any folder.
- **Block shortcodes** on their own line: `{{hero}}` `{{cases}}` `{{recipes case=business-analysis}}` `{{recipes chips=yes}}` `{{lessons}}` `{{labels}}`.
- **Inline shortcodes:** `{{label kind=verified}}` (verified · inferred · decided · open) and `{{illustration name=…}}`.
- **Callouts** are markdown admonitions: `!!! do "Do this"`, `!!! verify "Check before you use it"`, `!!! stop "Stop and ask"`, `!!! record "Keep in the record"`, `!!! example "What it looks like"`, `!!! note "Note"`.
- **No H1 in content**; the template renders it from `title`. Headings start at `##`. Card groups on index pages sit under an H2.
- **Voice:** warm, plain, active, task-first, sentence case. Reassurance brief and specific. No hype. No institutional guarantees the program does not own (response times, employment, non-retaliation): state the route and the expectation, and name the owner where a formal commitment exists. Claims about environment status must match the environments page.
- **The shared work-state vocabulary** is the only label set: Verified · Inferred · Decided · Open (plan §13).
- **The guided-session form** hands the request to the person's email application. Set the approved program address in `data-to` in `content/support/request-a-guided-session.md`; until it is set, the page tells the person to send the summary themselves and the build prints a warning.

## Hosting for reviewers (a link, sign-in, the full site)

The plan's approved fallback for hosting is an Azure Static Web App with organizational sign-in (plan §11). This repository is ready for it: `build/staticwebapp.config.json` is copied into `site/` on every build and requires the custom role **reviewer** on every route, so only people invited by email can see anything; anonymous visitors are sent to the Microsoft sign-in, and signed-in people who were not invited see `not-invited.html`. The GitHub Actions workflow runs the automated checks on every push and deploys `site/` only once the deployment token exists as a repository secret.

To turn it on (IT's tenant preferred; the program owner's subscription is acceptable for a prototype review with IT informed):

1. Azure portal: create a **Static Web App** (Free plan is enough for a review), deployment source **Other**. Copy its **deployment token**.
2. GitHub, this repository: Settings, Secrets and variables, Actions, new secret `AZURE_STATIC_WEB_APPS_API_TOKEN` with that token. The next push to `main` (or Actions, "Check and deploy", Run workflow) deploys the site.
3. Azure portal, the Static Web App, **Role management**, Invite: each reviewer's work email, provider **Microsoft Entra ID**, role `reviewer`, and an expiry for the invitation link. Send each person the link the portal produces, or simply the site URL; they sign in with their normal work account and are through.
4. Invite the program owner as `reviewer` too. Uninvited sign-ins get the not-invited page, not the content.

Nothing is public at any point: the repository is private, the site requires sign-in and an invitation, and every page is marked no-index. Rotate the deployment token if it is ever exposed; it lives only in the GitHub secret.

## To SharePoint

Each content file is one page. Paste the rendered body (or the markdown, via a converter) into a modern page; keep the section order. Product-specific setup pages stay separate and replaceable; the collaboration model, safety rules, and recipes never name a vendor.
