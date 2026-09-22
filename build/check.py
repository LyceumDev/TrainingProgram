#!/usr/bin/env python
"""
AI Collaboration Portal — automated checks on the built site.

  python build/check.py            (run after build/build.py)

Checks: internal links and fragments · heading structure (one H1; no skipped
levels) · form destination · the known contrast pairs in both themes, computed
from the tokens in styles.css · a report of remaining "partner" wording for a
human read (never a failure by itself). Exits 1 on any failure.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE, BUILD = ROOT / "site", ROOT / "build"

failures, notes = [], []


def rd(p): return p.read_text(encoding="utf-8")


# ---------------------------------------------------------------- links
pages = sorted(SITE.rglob("*.html"))
ids = {}
for p in pages:
    ids[p] = set(re.findall(r'\sid="([^"]+)"', rd(p)))
refs = 0
for p in pages:
    html = rd(p)
    for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
        if ref.startswith(("http://", "https://", "mailto:", "data:")):
            continue
        if ref.startswith("/.auth/"):          # Azure Static Web Apps sign-in endpoints exist only on the host
            continue
        refs += 1
        path, _, frag = ref.partition("#")
        if path.startswith("/"):                # root-absolute (hosting pages): resolve against the site root
            target = (SITE / path.lstrip("/")).resolve()
        else:
            target = p if not path else (p.parent / path).resolve()
        if not target.exists():
            failures.append(f"{p.relative_to(SITE)}: broken link {ref}")
        elif frag and target in ids and frag not in ids[target]:
            failures.append(f"{p.relative_to(SITE)}: missing fragment #{frag} in {target.relative_to(SITE)}")
    if "{{" in html or 'href="~/' in html or "<!-- illustration" in html:
        failures.append(f"{p.relative_to(SITE)}: unexpanded shortcode, link, or illustration")
notes.append(f"links: {len(pages)} pages, {refs} internal references checked")

# ------------------------------------------------------------- headings
for p in pages:
    html = rd(p)
    if 'http-equiv="refresh"' in html:      # redirect stubs for moved pages carry no headings by design
        continue
    levels = [int(h) for h in re.findall(r"<h([1-6])[\s>]", html)]
    if levels.count(1) != 1:
        failures.append(f"{p.relative_to(SITE)}: {levels.count(1)} H1 elements (need exactly 1)")
    prev = 0
    for lv in levels:
        if prev and lv > prev + 1:
            failures.append(f"{p.relative_to(SITE)}: heading level skips h{prev} -> h{lv}")
            break
        prev = lv
notes.append("headings: one H1 per page, no skipped levels")

# ----------------------------------------------------------------- form
req = SITE / "support" / "request-a-guided-session.html"
if req.exists():
    m = re.search(r'data-to="([^"]*)"', rd(req))
    if not m or not m.group(1).strip():
        notes.append("form: WARNING — no recipient configured (data-to empty); the page tells the person to send the summary themselves")
    else:
        notes.append(f"form: recipient configured ({m.group(1)})")

# ------------------------------------------------------------- contrast
css = rd(BUILD / "styles.css")

def tokens(block):
    return dict(re.findall(r"--([a-z0-9-]+):\s*(#[0-9A-Fa-f]{6})", block))

light_block = css[css.find(":root {"): css.find("}", css.find(":root {"))]
dark_start = css.find(':root[data-theme="dark"] {')
dark_block = css[dark_start: css.find("\n}", dark_start)]
LIGHT = tokens(light_block)
DARK = dict(LIGHT); DARK.update(tokens(dark_block))

def lum(h):
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

# (foreground token or literal, background token, minimum, what it is)
PAIRS = [
    ("ink", "paper", 4.5, "body text"), ("ink-2", "paper", 4.5, "secondary text"), ("ink-3", "paper", 4.5, "eyebrows, meta labels"),
    ("ink", "paper-2", 4.5, "text on soft surfaces"), ("ink-2", "paper-2", 4.5, "secondary on soft surfaces"),
    ("ink", "paper-3", 4.5, "text on cards"), ("ink-2", "paper-3", 4.5, "card text"),
    ("accent-ink", "paper", 4.5, "links"), ("accent-ink", "paper-3", 4.5, "links on cards"), ("accent-ink", "accent-soft", 4.5, "current nav item, step numbers"),
    ("#FFFFFF", "accent", 4.5, "primary button text"),
    ("inverse-fg", "inverse-bg", 4.5, "support strip / skip link / code text"), ("inverse-fg-2", "inverse-bg", 4.5, "support strip secondary text"),
    ("inverse-line", "inverse-bg", 3.0, "support strip ghost-button border (non-text)"),
    ("ok", "ok-soft", 4.5, "Verified label, do callout"), ("info", "info-soft", 4.5, "Inferred label, verify callout"),
    ("warn", "warn-soft", 4.5, "Decided label, form warning"), ("stop", "stop-soft", 4.5, "stop callout"),
    ("warm-ink", "warm-soft", 4.5, "record callout"), ("warm-ink", "paper", 4.5, "warm text"),
    ("modernization", "paper-3", 4.5, "modernization eyebrow"), ("business-analysis", "paper-3", 4.5, "business-analysis eyebrow"), ("customer-support", "paper-3", 4.5, "customer-support eyebrow"),
    ("accent", "paper", 3.0, "focus ring (non-text)"),
]
rows = []
for theme, T in (("light", LIGHT), ("dark", DARK)):
    for fg, bg, minimum, what in PAIRS:
        f = fg if fg.startswith("#") else T.get(fg)
        b = T.get(bg)
        if not f or not b:
            failures.append(f"contrast: token missing for {fg} / {bg} in {theme}"); continue
        r = ratio(f, b)
        flag = "" if r >= minimum else "  <-- FAIL"
        rows.append(f"  {theme:5s} {r:6.2f}:1  (min {minimum})  {what}{flag}")
        if r < minimum:
            failures.append(f"contrast {theme}: {what} = {r:.2f}:1, needs {minimum}:1 ({fg} on {bg})")
notes.append("contrast pairs:\n" + "\n".join(rows))

# ---------------------------------------------- vocabulary drift report
hits = []
for p in pages:
    text = re.sub(r"<[^>]+>", " ", rd(p))
    for m in re.finditer(r"\b[Pp]artner(?:s|ship|ships)?\b", text):
        ctx = text[max(0, m.start() - 50): m.end() + 50].replace("\n", " ")
        hits.append(f"  {p.relative_to(SITE)}: …{' '.join(ctx.split())}…")
notes.append(f"vocabulary: {len(hits)} occurrence(s) of 'partner' wording in the built pages (review by hand; expected only on About):\n" + "\n".join(hits[:40]))

# ------------------------------------------------------------------ out
for n in notes:
    print(n)
print()
if failures:
    print(f"{len(failures)} FAILURE(S):")
    for f in failures:
        print("  -", f)
    sys.exit(1)
print("all checks passed")
