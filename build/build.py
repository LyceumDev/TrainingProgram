#!/usr/bin/env python
"""
AI Partnership Portal — prototype build.

content/**/*.md  (markdown + front-matter; portable source)
    -> site/**/*.html  (the clickable prototype; open site/index.html)

Nothing is built twice: the same content is the reference for the SharePoint
pages. Run from anywhere:  python build/build.py
"""
import io, re, sys, shutil, html, json, datetime
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("python-markdown is required:  pip install markdown")

ROOT = Path(__file__).resolve().parent.parent
CONTENT, BUILD, SITE = ROOT / "content", ROOT / "build", ROOT / "site"
ILLUS = BUILD / "illustrations"

MD_EXT = ["tables", "fenced_code", "toc", "attr_list", "admonition",
          "sane_lists", "smarty", "md_in_html", "def_list"]
MD_CFG = {"toc": {"toc_depth": "2-3", "title": "On this page"}}

NAV = [  # label, path (site-relative), section key
    ("Home", "index.html", "home"),
    ("Cases", "cases/index.html", "case"),
    ("Task guides", "guides/index.html", "recipe"),
    ("Lessons", "lessons/index.html", "lesson"),
    ("Environments", "environments/index.html", "environment"),
    ("Support", "support/index.html", "support"),
]

LABELS = [  # the shared work-state vocabulary (plan §13, Aster's definitions)
    ("verified", "Verified", "a factual claim supported by a source or a completed check"),
    ("inferred", "Inferred", "a conclusion drawn from identified evidence, with the reasoning visible"),
    ("decided",  "Decided",  "a choice made by an authorized person, with owner and rationale; authoritative as a decision, not proof that every premise is true"),
    ("open",     "Open",     "unresolved, unsupported, or awaiting a decision, with an owner or next disposition where needed"),
]

CASE_ORDER = ["modernization", "business-analysis", "customer-support"]

RISK_NOTE = ("Workflow risk assumes permitted information in an approved environment. Data sensitivity, "
             "consequential actions, and organizational policy may require stronger controls and always override this label.")

# Old addresses that reviewers may hold; each gets a small redirect page.
REDIRECTS = {
    "recipes/index.html": "guides/index.html",
    "recipes/01-turn-a-rough-request-into-a-problem-statement.html": "guides/01-turn-a-vague-request-into-a-clear-problem-statement.html",
    "recipes/02-extract-requirements-preserving-source-language.html": "guides/02-extract-requirements-in-the-authors-own-words.html",
    "recipes/03-separate-facts-inferences-decisions-and-open-questions.html": "guides/03-sort-a-documents-claims-into-the-four-labels.html",
    "recipes/04-compare-options-against-explicit-criteria.html": "guides/04-compare-options-against-criteria-you-set-first.html",
    "recipes/05-draft-a-specification-with-traceability.html": "guides/05-draft-a-specification-you-can-trace-to-its-sources.html",
    "recipes/06-review-a-memo-for-unsupported-claims.html": "guides/06-check-a-memo-before-it-goes-out.html",
}


# ----------------------------------------------------------------- helpers
def read(p):  return io.open(p, encoding="utf-8").read()
def write(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
def esc(s):   return html.escape(str(s), quote=True)

def front_matter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].strip("\n").splitlines():
                if ":" in line and not line.startswith("#"):
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip()
            return meta, text[end + 4:].lstrip("\n")
    return meta, text

def illustration(name, cls=""):
    p = ILLUS / f"{name}.svg"
    if not p.exists():
        return f'<!-- illustration "{name}" missing -->'
    svg = read(p).strip()
    if cls:
        svg = svg.replace("<svg ", f'<svg class="{cls}" ', 1)
    return svg


# ------------------------------------------------------------------ pages
class Page:
    def __init__(self, path):
        self.src = path
        self.rel = path.relative_to(CONTENT).with_suffix(".html").as_posix()
        self.meta, self.body = front_matter(read(path))
        self.title = self.meta.get("title", path.stem)
        self.section = self.meta.get("section", "page")
        self.order = int(self.meta.get("order", 999))
        self.depth = self.rel.count("/")
        self.prefix = "../" * self.depth
        self.slug = path.stem

    def url(self):  return "~/" + self.rel


def load_pages():
    pages = [Page(p) for p in sorted(CONTENT.rglob("*.md"))]
    return {p.rel: p for p in pages}


# -------------------------------------------------------------- shortcodes
def sc_label(kind):
    for k, name, _ in LABELS:
        if k == kind:
            return f'<span class="label label-{k}">{name}</span>'
    return f'<span class="label">{esc(kind)}</span>'

def sc_labels():
    items = "".join(
        f'<li class="labels-item"><span class="label label-{k}">{n}</span><span class="labels-def">{esc(d)}</span></li>'
        for k, n, d in LABELS)
    return f'<ul class="labels" aria-label="The shared work-state vocabulary">{items}</ul>'

def sc_cases(pages, band=True):
    cases = sorted([p for p in pages.values() if p.section == "case" and p.slug != "index"],
                   key=lambda p: CASE_ORDER.index(p.slug) if p.slug in CASE_ORDER else 99)
    cards = []
    for c in cases:
        status = c.meta.get("status", "")
        badge = f'<span class="badge">{esc(status)}</span>' if status else ""
        cards.append(
            f'<a class="card card-case case-{c.slug}" href="{c.url()}">'
            f'<div class="card-art">{illustration("case-" + c.slug, "art")}</div>'
            f'<div class="card-body"><h3 class="card-title">{esc(c.title)}</h3>'
            f'<p class="card-text">{esc(c.meta.get("summary", ""))}</p>'
            f'<span class="card-cta">{esc(c.meta.get("cta", "See this case"))}{badge}</span></div></a>')
    grid = f'<div class="grid grid-3 cases">{"".join(cards)}</div>'
    return grid

def sc_recipes(pages, case=None, chips=False, limit=None):
    rs = [p for p in pages.values() if p.section == "recipe" and p.slug != "index"]
    if case:
        rs = [p for p in rs if p.meta.get("case") == case]
    rs.sort(key=lambda p: (p.meta.get("case", ""), p.order))
    if limit:
        rs = rs[:limit]
    cards = []
    for r in rs:
        cards.append(
            f'<a class="card card-recipe" href="{r.url()}" data-case="{esc(r.meta.get("case",""))}" '
            f'data-environment="{esc(r.meta.get("environment",""))}" data-risk="{esc(r.meta.get("risk",""))}">'
            f'<span class="eyebrow">{esc(r.meta.get("case_label", ""))}</span>'
            f'<h3 class="card-title">{esc(r.title)}</h3>'
            f'<p class="card-text">{esc(r.meta.get("summary",""))}</p>'
            f'<dl class="card-meta"><div><dt>You\'ll create</dt><dd>{esc(r.meta.get("outcome",""))}</dd></div>'
            f'<div><dt>Environment</dt><dd>{esc(r.meta.get("environment_label",""))}</dd></div>'
            f'<div><dt>Workflow risk</dt><dd>{esc(r.meta.get("risk",""))}</dd></div></dl></a>')
    out = ""
    if chips:
        out += (
            '<div class="filters" role="group" aria-label="Filter recipes">'
            '<label class="search"><span class="visually-hidden">Search task guides</span>'
            '<input type="search" id="recipe-search" placeholder="Search task guides…" autocomplete="off"></label>'
            '<div class="chips" data-filter="case"><span class="chips-label">Work</span>'
            '<button class="chip is-on" data-value="">All</button>'
            '<button class="chip" data-value="modernization">Modernization</button>'
            '<button class="chip" data-value="business-analysis">Business analysis</button>'
            '<button class="chip" data-value="customer-support">Customer support</button></div>'
            '<div class="chips" data-filter="risk"><span class="chips-label">Workflow risk</span>'
            '<button class="chip is-on" data-value="">Any</button>'
            '<button class="chip" data-value="low">Low</button>'
            '<button class="chip" data-value="medium">Medium</button>'
            '<button class="chip" data-value="high">High</button></div></div>'
            f'<p class="risk-note">{RISK_NOTE}</p>')
    out += f'<div class="grid grid-2 recipes" id="recipe-grid">{"".join(cards)}</div>'
    out += '<p class="empty" id="recipe-empty" hidden>No task guide matches yet. Clear a filter, or <a href="~/support/request-a-guided-session.html">ask for a guided first session</a> and we will write the guide with you.</p>'
    return out

def sc_lessons(pages):
    ls = sorted([p for p in pages.values() if p.section == "lesson" and p.slug != "index"], key=lambda p: p.order)
    items = "".join(
        f'<li class="step"><a href="{l.url()}"><span class="step-n" aria-hidden="true">{l.order}</span>'
        f'<span class="step-body"><span class="step-title">{esc(l.title)}</span>'
        f'<span class="step-text">{esc(l.meta.get("summary",""))}</span></span></a></li>' for l in ls)
    return f'<ol class="steps">{items}</ol>'

def sc_hero(page):
    m = page.meta
    art = illustration("hero", "hero-art")
    cta1 = f'<a class="btn btn-primary" href="{esc(m.get("cta_link", "~/cases/index.html"))}">{esc(m.get("cta", "Find your work"))}</a>'
    cta2 = f'<a class="btn btn-ghost" href="{esc(m.get("cta2_link", "~/support/request-a-guided-session.html"))}">{esc(m.get("cta2", "Book a guided first session"))}</a>'
    return (f'<section class="hero"><div class="wrap hero-row"><div class="hero-copy">'
            f'<p class="eyebrow">{esc(m.get("kicker", "For everyone who plans, decides, writes, or supports"))}</p>'
            f'<h1 class="hero-title">{esc(m.get("hero_title", page.title))}</h1>'
            f'<p class="hero-sub">{esc(m.get("hero_sub", ""))}</p>'
            f'<div class="hero-actions">{cta1}{cta2}</div></div>'
            f'<div class="hero-art-wrap" aria-hidden="true">{art}</div></div></section>')

SC_RE = re.compile(r"\{\{\s*([a-z-]+)((?:\s+[a-z_]+=[^\s}]+)*)\s*\}\}")

def expand_inline(text, page, pages):
    """Inline shortcodes only (labels, illustrations)."""
    def rep(m):
        name, args = m.group(1), dict(a.split("=", 1) for a in m.group(2).split())
        if name == "label":       return sc_label(args.get("kind", "open"))
        if name == "illustration": return illustration(args.get("name", ""), args.get("class", "inline-art"))
        return m.group(0)
    return SC_RE.sub(rep, text)

def expand_block(name, args, page, pages):
    if name == "hero":    return sc_hero(page)
    if name == "cases":   return sc_cases(pages)
    if name == "recipes": return sc_recipes(pages, case=args.get("case"), chips=args.get("chips") == "yes",
                                            limit=int(args["limit"]) if "limit" in args else None)
    if name == "lessons": return sc_lessons(pages)
    if name == "labels":  return sc_labels()
    return f"<!-- unknown block shortcode {name} -->"


# --------------------------------------------------------------- rendering
def md(text):
    return markdown.markdown(text, extensions=MD_EXT, extension_configs=MD_CFG, output_format="html5")

def render_body(page, pages):
    body = expand_inline(page.body, page, pages)
    wide = page.meta.get("layout") == "wide"
    parts, out = re.split(r"^(\{\{[^}\n]+\}\})\s*$", body, flags=re.M), []
    for part in parts:
        if not part.strip():
            continue
        m = SC_RE.fullmatch(part.strip())
        if m and m.group(1) in ("hero", "cases", "recipes", "lessons", "labels"):
            args = dict(a.split("=", 1) for a in m.group(2).split())
            h = expand_block(m.group(1), args, page, pages)
            out.append(h if (m.group(1) == "hero" or not wide) else f'<section class="band"><div class="wrap">{h}</div></section>')
        else:
            h = md(part)
            out.append(f'<section class="band"><div class="wrap prose">{h}</div></section>' if wide else h)
    return "".join(out), wide

def nav_html(page):
    items = []
    for label, path, key in NAV:
        cur = ' aria-current="page"' if (page.rel == path or (page.section == key and page.rel != "index.html")) else ""
        items.append(f'<li><a href="~/{path}"{cur}>{label}</a></li>')
    return f'<ul>{"".join(items)}</ul>'

def crumbs_html(page, pages):
    if page.rel == "index.html":
        return ""
    trail = [('~/index.html', 'Home')]
    parent = page.rel.split("/")[0] + "/index.html"
    if page.depth and parent in pages and parent != page.rel:
        trail.append(("~/" + parent, pages[parent].title))
    lis = "".join(f'<li><a href="{u}">{esc(t)}</a></li>' for u, t in trail)
    lis += f'<li aria-current="page">{esc(page.title)}</li>'
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'

def heading_html(page):
    if page.meta.get("layout") == "wide":
        return ""
    m = page.meta
    kicker = m.get("kicker", "")
    is_index = page.slug == "index"
    if page.section == "lesson" and not is_index:
        kicker = kicker or f"Lesson {page.order} of 6"
    elif page.section == "recipe" and not is_index:
        kicker = kicker or f"Task guide · {m.get('case_label', '')}"
    art = illustration(m["art"], "head-art") if m.get("art") else ""
    meta = ""
    is_guide = page.section == "recipe" and not is_index
    if is_guide:
        use_when = f'<p class="use-when"><strong>Use this when</strong> {esc(m.get("use_when", ""))}</p>' if m.get("use_when") else ""
        boundary = (f'<div class="boundary"><p><strong>{esc(m.get("boundary", ""))}</strong> {esc(m.get("boundary_more", ""))}</p></div>'
                    if m.get("boundary") else "")
        meta = (use_when + boundary +
                '<dl class="meta-strip">'
                f'<div><dt>You\'ll create</dt><dd>{esc(m.get("outcome",""))}</dd></div>'
                f'<div><dt>Time</dt><dd>{esc(m.get("time",""))}</dd></div>'
                f'<div><dt>You\'ll need</dt><dd>{esc(m.get("you_need",""))}</dd></div>'
                f'<div><dt>Environment</dt><dd>{esc(m.get("environment_label",""))}</dd></div>'
                f'<div><dt>Workflow risk</dt><dd>{esc(m.get("risk",""))}<span class="meta-caption">Review level, not data permission.</span></dd></div></dl>'
                f'<p class="risk-note">{RISK_NOTE}</p>')
    summary = "" if is_guide else (f'<p class="lede">{esc(m["summary"])}</p>' if m.get("summary") else "")
    k = f'<p class="eyebrow">{esc(kicker)}</p>' if kicker else ""
    return (f'<header class="page-head"><div class="wrap page-head-row"><div>{k}<h1>{esc(page.title)}</h1>{summary}{meta}</div>'
            f'{f"<div class=head-art-wrap aria-hidden=true>{art}</div>" if art else ""}</div></header>')

def prevnext_html(page, pages):
    if page.section not in ("lesson", "recipe") or page.slug == "index":
        return ""
    if page.section == "lesson":
        seq = sorted([p for p in pages.values() if p.section == "lesson" and p.slug != "index"], key=lambda p: p.order)
    else:
        seq = sorted([p for p in pages.values() if p.section == "recipe" and p.slug != "index" and p.meta.get("case") == page.meta.get("case")], key=lambda p: p.order)
    i = seq.index(page)
    prev = seq[i - 1] if i > 0 else None
    nxt = seq[i + 1] if i + 1 < len(seq) else None
    a = f'<a class="pn pn-prev" href="{prev.url()}" rel="prev"><span class="pn-k">Previous</span><span>{esc(prev.title)}</span></a>' if prev else '<span></span>'
    if nxt:
        b = f'<a class="pn pn-next" href="{nxt.url()}" rel="next"><span class="pn-k">Next</span><span>{esc(nxt.title)}</span></a>'
    else:
        done = "~/lessons/06-begin-real-work.html" if page.section == "lesson" else "~/support/request-a-guided-session.html"
        label = "You have read all six lessons" if page.section == "lesson" else "Done with this case? Book a guided first session"
        b = f'<a class="pn pn-next" href="{done}"><span class="pn-k">Next</span><span>{esc(label)}</span></a>'
    return f'<nav class="wrap prevnext" aria-label="Previous and next">{a}{b}</nav>'

def relink(htmltext, prefix):
    return htmltext.replace('href="~/', f'href="{prefix}').replace('src="~/', f'src="{prefix}')


def guide_wrap(page, body):
    """Task-guide layout: an overview rail (read first) beside the two-part body."""
    m = page.meta
    h2s = re.findall(r'<h2[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', body, flags=re.S)
    toc = "".join(f'<li><a href="#{esc(i)}">{esc(re.sub(r"<[^>]+>", "", t)).strip()}</a></li>' for i, t in h2s)
    before = [b.strip() for b in m.get("before", "").split("|") if b.strip()] or [
        "Confirm the environment is approved for this work.",
        "Replace personal, customer, payroll, or credential details.",
        "Keep source names and locations so claims can be checked."]
    before_html = "".join(f"<li>{esc(b)}</li>" for b in before)
    key = ""
    if m.get("key_a") and m.get("key_b"):
        ka, _, ta = m["key_a"].partition(":")
        kb, _, tb = m["key_b"].partition(":")
        key = (f'<section class="rail-card" aria-labelledby="rail-key"><h2 id="rail-key">The key distinction</h2>'
               f'<p><strong>{esc(ka.strip())}:</strong> {esc(ta.strip())}</p><p><strong>{esc(kb.strip())}:</strong> {esc(tb.strip())}</p></section>')
    rail = (
        '<aside class="rail" aria-label="Guide overview">'
        '<section class="rail-card rail-how" aria-labelledby="rail-how"><h2 id="rail-how">How this guide works</h2>'
        '<p>The page has two layers. Complete the task first; then apply the review and authority checks before the work goes anywhere.</p>'
        '<ol class="rail-steps"><li>Do the work step by step</li><li>Review claims and framing</li><li>Confirm boundaries and save</li></ol></section>'
        f'<section class="rail-card" aria-labelledby="rail-before"><h2 id="rail-before">Before you start</h2><ul class="rail-checks">{before_html}</ul></section>'
        f'<nav class="rail-card" aria-labelledby="rail-toc"><h2 id="rail-toc">On this page</h2><ul class="rail-toc">{toc}</ul></nav>'
        f'{key}</aside>')
    return f'<div class="wrap guide">{rail}<div class="guide-main prose">{body}</div></div>'


def write_redirects():
    import posixpath
    for old, new in REDIRECTS.items():
        rel = posixpath.relpath(new, posixpath.dirname(old) or ".")
        write(SITE / old, (
            '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex, nofollow">'
            f'<meta http-equiv="refresh" content="0; url={rel}"><title>Moved · AI Collaboration Portal</title>'
            f'<link rel="canonical" href="{rel}"></head><body><p>This page has moved to <a href="{rel}">{esc(new)}</a>.</p></body></html>\n'))


def build():
    pages = load_pages()
    template = read(BUILD / "template.html")
    if SITE.exists():
        try:
            shutil.rmtree(SITE)
        except OSError:
            # A server (or an open Explorer window) may be holding the folder on
            # Windows; fall back to overwriting in place and clearing stale pages.
            for stale in SITE.rglob("*.html"):
                stale.unlink()
    (SITE / "assets").mkdir(parents=True, exist_ok=True)
    for asset in ("styles.css", "site.js", "favicon.svg"):
        src = BUILD / asset
        if src.exists():
            shutil.copy(src, SITE / "assets" / asset)
    for hosting in ("staticwebapp.config.json", "not-invited.html"):   # Azure Static Web Apps: auth rules + the 403 page
        src = BUILD / hosting
        if src.exists():
            shutil.copy(src, SITE / hosting)
    brand = illustration("brandmark", "brandmark")
    index = []
    for page in pages.values():
        body, wide = render_body(page, pages)
        if page.section == "recipe" and page.slug != "index":
            body, wide = guide_wrap(page, body), True   # the guide layout supplies its own wrap
        out = (template
               .replace("{{title}}", esc(page.title if page.rel != "index.html" else page.meta.get("hero_title", page.title)))
               .replace("{{description}}", esc(page.meta.get("summary", "")))
               .replace("{{section}}", esc(page.section))
               .replace("{{brandmark}}", brand)
               .replace("{{nav}}", nav_html(page))
               .replace("{{crumbs}}", crumbs_html(page, pages))
               .replace("{{heading}}", heading_html(page))
               .replace("{{body}}", body if wide else f'<div class="wrap prose">{body}</div>')
               .replace("{{prevnext}}", prevnext_html(page, pages))
               .replace("{{year}}", str(datetime.date.today().year)))
        out = relink(out, page.prefix)
        write(SITE / page.rel, out)
        index.append({"title": page.title, "url": page.rel, "section": page.section, "summary": page.meta.get("summary", "")})
    write(SITE / "assets" / "index.json", json.dumps(index, indent=1))
    write_redirects()
    print(f"built {len(pages)} pages (+{len(REDIRECTS)} redirect stubs) -> {SITE}")
    req = SITE / "support" / "request-a-guided-session.html"
    if req.exists() and 'data-to=""' in read(req):
        print("WARNING: the guided-session form has no recipient (data-to is empty). "
              "Set the approved program address in content/support/request-a-guided-session.md before participant use.")
    return pages


if __name__ == "__main__":
    build()
