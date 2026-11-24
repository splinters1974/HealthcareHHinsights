import os
"""
Shared pieces for the page builder: site settings, the page layout, and the
structured data (schema.org JSON-LD) every page carries.
"""
import json
from dataclasses import dataclass, field
from html import escape

NAME = 'Hospital Energy Insights'
YEAR = 2026
# Each page's own dates (first published, last changed) live in
# tools/page_dates.json. build_pages.py keeps them current: a page whose
# wording changes gets today's date as "last updated"; a layout-only rebuild
# leaves its date alone. UPDATED is only the fallback for a page not yet built.
UPDATED = '2026-11-14'
PAGE_DATES = {}   # file -> {'published': 'YYYY-MM-DD', 'modified': 'YYYY-MM-DD'}
UPDATED_MARK = '<!--last-updated-->'


# Cloudflare Web Analytics: counts page views with no cookies and no personal
# data. On every page built from the template and the solar calculator, but
# deliberately NOT the analyser, so the analyser makes no outside requests.
ANALYTICS = ("<!-- Cloudflare Web Analytics --><script type='module' "
             "src='https://static.cloudflareinsights.com/beacon.min.js' "
             "data-cf-beacon='{\"token\": \"3882f52f6bbf4acdb6a2487a568d2dd3\"}'></script>"
             "<!-- End Cloudflare Web Analytics -->")

def page_dates(file):
    d = PAGE_DATES.get(file, {})
    return d.get('published', UPDATED), d.get('modified', UPDATED)


def long_date(iso):
    import datetime as _dt
    d = _dt.date.fromisoformat(iso)
    return f'{d.day} {d:%B %Y}'
# The site's public address, no trailing slash. Every page's canonical and
# share links, robots.txt and sitemap.xml are built from it, so moving to a
# custom domain (for example https://hospitalenergy.co.uk) is this one change plus
# a rebuild. Empty disables canonical links and the sitemap.
SITE_URL = 'https://hospitalenergy.co.uk'  # bought at Porkbun, 22 Nov 2026

# Run by Kinetic Energy Consulting, as with the UK Solar Calculator and Half Hourly Insights.
OPERATOR = 'Kinetic Energy Consulting'
OPERATOR_URL = 'https://www.kinetic-energy.co.uk'
CONTACT_NAME = 'Paul Johnston'
# Where calculator and customer-edition leads are emailed (EmailJS). Shown in the page code, so a named person's own address, not anyone else's.
LEAD_EMAIL = 'enquiries@hospitalenergy.co.uk'  # Porkbun forward; leads from the analyser and calculator
CONTACT_EMAIL = 'enquiries@hospitalenergy.co.uk'  # forwarded by Porkbun
# The solar calculator is part of this site (solar-calculator.html), fed by the analyser.
SOLAR_URL = 'solar-calculator.html'
SOLAR_SITE = 'https://uksolarcalculator.co.uk/'
HHI_SITE = 'https://hhinsights.co.uk/'
# Named author for the guides (byline and Article schema). Biography on about.html.
AUTHOR_NAME = 'Paul Johnston'
AUTHOR_ROLE = 'Managing Director, Kinetic Energy Consulting'
AUTHOR_PHOTO = 'images/people/paul-johnston.jpg'
# Verified public profiles, used as schema.org sameAs so search engines and AI
# tools can connect the site to the real company and person. Add only addresses
# you have checked, for example 'https://www.linkedin.com/in/...'.
AUTHOR_SAME_AS = []
ORG_SAME_AS = ['https://www.linkedin.com/company/kinetic-energy-consulting/']  # confirmed by the owner, 22 Nov 2026

# Pages kept here for the journey but written first for a sister site. Their
# canonical points at the original so search engines rank one copy, and they
# stay out of the sitemap and llms.txt.
_HHI = ['half-hourly-data-british-gas', 'half-hourly-data-edf', 'half-hourly-data-eon-next',
        'half-hourly-data-npower-business-solutions', 'half-hourly-data-totalenergies', 'half-hourly-settlement',
        'mpan-profile-class', 'non-energy-charges', 'non-energy-costs-outlook', 'electricity-prices-ten-years',
        'business-electricity-price', 'electricity-benchmarks']
CANONICAL_ELSEWHERE = {f'{n}.html': f'{HHI_SITE}{n}' for n in _HHI}
CANONICAL_ELSEWHERE.update({  # the solar calculator's own method and general solar guides
    'solar-calculator-method.html': f'{SOLAR_SITE}how-it-works.html',
    'solar-cost.html': f'{SOLAR_SITE}commercial-solar-cost.html',
    'solar-generation.html': f'{SOLAR_SITE}commercial-solar-generation.html',
})
ORIGINAL_ON_HHI = set(CANONICAL_ELSEWHERE)  # every page whose original is on a sister site


def canonical_url(file):
    return CANONICAL_ELSEWHERE.get(file) or url(file)


NAV = [
    ('index.html', 'Home'),
    ('how-it-works.html', 'How it works'),
    ('healthcare-estates-decarbonisation.html', 'Decarbonisation'),
    ('solar-calculator.html', 'Solar calculator'),
    ('guides.html', 'Guides'),
    ('sectors.html', 'Site types'),
    ('contact.html', 'Contact'),
]
# Pages that belong under a nav item, so it stays highlighted on them.
NAV_PARENT = {}


def clean(path):
    """Public address of a page: no .html (the host serves /base-load from base-load.html)."""
    if path == 'index.html':
        return ''
    return path[:-5] if path.endswith('.html') else path


def url(path):
    """Absolute URL once the domain is set, otherwise the relative path."""
    if not SITE_URL:
        return clean(path) or './'
    return f'{SITE_URL}/{clean(path)}'


def clean_links(html):
    """Point internal page links at clean addresses: href="base-load.html#x" -> href="base-load#x"."""
    import re
    html = re.sub(r'href="index\.html(#[^"]*)?"', lambda m: f'href="./{m.group(1) or ""}"', html)
    return re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: f'href="{m.group(1)}{m.group(2) or ""}"', html)


@dataclass
class Page:
    file: str
    title: str
    description: str
    body: str
    crumbs: list = field(default_factory=list)   # [(label, file)], home first, this page last
    faqs: list = field(default_factory=list)     # [(question, answer html)], marked up as FAQPage
    article: bool = False                        # a guide: gets Article schema with dates
    schema: list = field(default_factory=list)   # extra JSON-LD nodes
    noindex: bool = False
    extra_head: str = ''
    summary: str = ''                            # one line for llms.txt; empty leaves it out
    section: str = ''                            # llms.txt heading


# ── Structured data ────────────────────────────────────────────────────
ORG_ID = f'{OPERATOR_URL}/#organization'
ORG = {
    '@type': 'Organization', '@id': ORG_ID, 'name': OPERATOR, 'url': OPERATOR_URL,
    'email': CONTACT_EMAIL, 'logo': url('images/kec-logo.svg'),
    **({'sameAs': ORG_SAME_AS} if ORG_SAME_AS else {}),
    'areaServed': {'@type': 'Country', 'name': 'United Kingdom'},
    'contactPoint': {'@type': 'ContactPoint', 'contactType': 'Sales', 'email': CONTACT_EMAIL, 'areaServed': 'GB'},
}
WEBSITE = {
    '@type': 'WebSite', '@id': '#website', 'name': NAME, 'inLanguage': 'en-GB',
    'description': 'Free half-hourly electricity analysis, solar sizing and decarbonisation guides for UK healthcare estates',
    'image': url('images/brand/hei-logo.png'),
    'publisher': {'@id': ORG_ID},
}
APP = {
    '@type': 'WebApplication', 'name': f'{NAME} analyser', 'url': url('analyser/'),
    'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Any (runs in Chrome or Edge)',
    'browserRequirements': 'A recent desktop browser; works offline once loaded',
    'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'GBP'},
    'description': ('Analyses half-hourly electricity meter data from UK hospitals, health boards, NHS trusts and private '
                    'healthcare sites in the browser: base load, day and night use, peaks against agreed supply capacity '
                    'and headroom for heat pumps, solar self-consumption, unusual days, savings scenarios, PDF and Excel reports. '
                    'Meter data is never uploaded.'),
    'audience': {'@type': 'Audience', 'audienceType': 'NHS and private healthcare estates, facilities and energy managers'},
    'featureList': ['Excel and CSV half-hourly files', 'Several meters and sites at once', 'Headroom for heat pumps and EV charging', 'Solar self-consumption from your own profile, passed to the solar calculator', 'Data quality checks', 'Out-of-hours use priced at your rates',
                    'Base load', 'Supply capacity and headroom', 'Unusual days', 'Savings scenarios',
                    'PDF and Excel reports', 'Password-protected customer dashboards'],
    'provider': {'@id': ORG_ID},
}
PERSON_ID = f'{url("about.html")}#paul-johnston'
PERSON = {
    '@type': 'Person', '@id': PERSON_ID, 'name': AUTHOR_NAME, 'jobTitle': 'Managing Director',
    'worksFor': {'@id': ORG_ID}, 'url': url('about.html'), 'image': url(AUTHOR_PHOTO),
    **({'sameAs': AUTHOR_SAME_AS} if AUTHOR_SAME_AS else {}),
}
if SITE_URL:
    WEBSITE['url'] = url('index.html')
    WEBSITE['@id'] = f'{SITE_URL}/#website'


def strip_tags(html):
    import re
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', html)).strip()


def jsonld(page):
    graph = [ORG, WEBSITE]
    if page.crumbs:
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': label, 'item': url(href)}
            for i, (label, href) in enumerate(page.crumbs)]})
    if page.article or page.file == 'about.html':
        graph.append(PERSON)
    if page.article:
        graph.append({'@type': 'Article', 'headline': page.title.split(' | ')[0], 'description': page.description,
                      **({'image': url(guide_card(page.file))} if guide_card(page.file) else {}),
                      'inLanguage': 'en-GB', 'datePublished': page_dates(page.file)[0], 'dateModified': page_dates(page.file)[1],
                      'author': {'@id': PERSON_ID}, 'publisher': {'@id': ORG_ID},
                      'isPartOf': {'@id': WEBSITE['@id']}, **({'mainEntityOfPage': canonical_url(page.file)} if SITE_URL else {})})
    if page.faqs:
        graph.append({'@type': 'FAQPage', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}}
            for q, a in page.faqs]})
    graph += page.schema
    data = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)
    return f'  <script type="application/ld+json">\n{data}\n  </script>\n'


# ── Building blocks ────────────────────────────────────────────────────
# Photo headers for the main tab pages, in site/images/heroes/<name>.jpg (wide,
# dark on the left so the heading stays readable) plus <name>-900.jpg for
# phones. A page only shows its photo once the file exists.
HERO_DIR = os.path.join(os.path.dirname(__file__), '..', 'site', 'images', 'heroes')


def hero_photo(name):
    big = os.path.join(HERO_DIR, f'{name}.jpg')
    if not name or not os.path.exists(big):
        return ''
    from PIL import Image
    with Image.open(big) as im:
        w, h = im.size
    small = f'images/heroes/{name}-900.jpg'
    srcset = (f' srcset="{small} 900w, images/heroes/{name}.jpg {w}w" sizes="100vw"'
              if os.path.exists(os.path.join(HERO_DIR, f'{name}-900.jpg')) else '')
    webp = ''
    if os.path.exists(os.path.join(HERO_DIR, f'{name}.webp')):
        webp = (f'<source type="image/webp" srcset="images/heroes/{name}-900.webp 900w, images/heroes/{name}.webp {w}w" sizes="100vw">'
                if srcset else f'<source type="image/webp" srcset="images/heroes/{name}.webp">')
    return (f'<div class="hero-media" aria-hidden="true"><picture>{webp}<img src="images/heroes/{name}.jpg"{srcset} '
            f'width="{w}" height="{h}" alt="" fetchpriority="high"></picture></div>\n  ')


def page_hero(kicker, title, lead, extra='', crumbs=None, image=None):
    media = hero_photo(image)
    trail = ''
    if crumbs:
        trail = '<nav class="breadcrumb" aria-label="Breadcrumb">' + ' <span aria-hidden="true">/</span> '.join(
            f'<a href="{href}">{escape(label)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{escape(label)}</span>'
            for i, (label, href) in enumerate(crumbs)) + '</nav>\n    '
    return f'''<section class="page-hero{' page-hero-photo' if media else ''}">
  {media}<div class="page-hero-inner">
    {trail}<span class="page-hero-kicker">{kicker}</span>
    <h1 class="page-hero-title">{title}</h1>
    <p class="page-hero-lead">{lead}</p>{extra}
  </div>
</section>'''


def cta(title, lead):
    return f'''<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2 class="cta-strip-title">{title}</h2>
    <div class="cta-strip-btns">
      <a href="analyser/" class="btn btn-gold btn-lg">Upload HH data</a>
      <a href="contact.html" class="btn btn-outline-white btn-lg">Talk to an expert</a>
    </div>
    <p class="cta-strip-lead">{lead}</p>
  </div>
</section>'''


def faq_section(faqs, title='Questions people ask'):
    """Visible questions and answers; the same list feeds the FAQPage schema."""
    return f'<h2 id="questions">{title}</h2>\n<div class="faq">' + ''.join(
        f'<details><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q, a in faqs) + '</div>'


# Illustrations and photos in site/images/photos, each saved at 1600 px and 800 px wide.
PHOTO_SIZES = {
    'estate-hospital': (1448, 1086), 'estate-business-park': (1448, 1086), 'estate-town': (1600, 1200),
    'town-school-leisure': (1120, 820), 'town-street': (1600, 900), 'plant-outside': (1600, 900), 'solar-private-wire': (1600, 900),
    'switchroom-tablet': (1448, 1086), 'board-review': (1448, 1086), 'site-plans-substation': (1448, 1086),
    'contact-photo': (1200, 900),
    'solar-carport-depot': (1600, 900), 'solar-canopy-hospital': (1600, 900), 'solar-ground-campus': (1600, 900),
    'solar-site-team': (1600, 900),
    # Healthcare photos from tools/place_photos.py (illustrations of made-up sites)
    'hc-public-hospital-solar': (1448, 1086), 'hc-private-hospital-carport': (1448, 1086), 'hc-heat-pump-plant-room': (1448, 1086),
    'hc-efficient-ward': (1448, 1086), 'hc-energy-control-room': (1448, 1086), 'hc-rooftop-solar-install': (1448, 1086),
    'hc-battery-ev-charging': (1448, 1086), 'hc-strategy-meeting': (1448, 1086), 'hc-thermal-survey': (1448, 1086),
    'hc-private-hospital-dusk': (1448, 1086),
}


def photo(name, alt, caption='', cls='figure', lazy=True):
    w, h = PHOTO_SIZES[name]
    big = f'images/photos/{name}.jpg'
    small = f'images/photos/{name}-800.jpg'
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    load = ' loading="lazy"' if lazy else ''
    return (f'<figure class="{cls}"><img src="{big}" srcset="{small} 800w, {big} {w}w" '
            f'sizes="(max-width: 860px) 100vw, 860px" width="{w}" height="{h}" alt="{alt}"{load}>{cap}</figure>')


# Guide title cards (512 x 256) in site/images/guides, named after the page they belong to.
GUIDE_CARD_DIR = os.path.join(os.path.dirname(__file__), '..', 'site', 'images', 'guides')


def guide_card(file):
    name = file.replace('.html', '.jpg')
    return f'images/guides/{name}' if os.path.exists(os.path.join(GUIDE_CARD_DIR, name)) else None


def card_size(src):
    from PIL import Image
    with Image.open(os.path.join(GUIDE_CARD_DIR, '..', '..', src)) as im:
        return im.size


def link_card(f, t, d, more='Read the guide'):
    img = guide_card(f)
    thumb = ''
    if img:
        w, h = card_size(img)
        small = img.replace('.jpg', '-600.jpg')
        srcset = (f' srcset="{small} 600w, {img} {w}w" sizes="(max-width: 700px) 100vw, 400px"'
                  if os.path.exists(os.path.join(GUIDE_CARD_DIR, os.path.basename(small))) else '')
        thumb = f'<div class="card-thumb"><img src="{img}"{srcset} width="{w}" height="{h}" alt="" loading="lazy"></div>'
    return f'<a class="link-card{" has-thumb" if img else ""}" href="{f}">{thumb}<h3>{t}</h3><p>{d}</p><span class="more">{more}</span></a>'


# The downloadable user guide, built by tools/build_guide.py.
GUIDE_PDF = 'downloads/half-hourly-insights-user-guide.pdf'


def guide_download(lead='Prefer to read it on paper?'):
    return (f'<div class="note"><strong>{lead}</strong> <a href="{GUIDE_PDF}" download>Download the user guide</a> '
            '(PDF, 13 pages). It walks you through loading your data, setting opening hours, reading the results and sharing them.</div>')


def related(links):
    """'Read next' cards at the end of a guide: [(file, title, one line)]."""
    return '<h2 id="next">Read next</h2>\n<div class="link-grid">' + ''.join(
        link_card(f, t, d) for f, t, d in links) + '</div>'


def updated_line():
    # Filled in by layout() with the page's own date, so the date itself is not
    # part of the content fingerprint that decides when the date changes.
    return (f'<p class="byline">By <a href="about.html">{AUTHOR_NAME}</a>, {AUTHOR_ROLE}'
            f' <span aria-hidden="true">·</span> Last updated {UPDATED_MARK}</p>')


def toc(items):
    return ('    <nav class="toc" aria-label="On this page"><div class="toc-title">On this page</div><ol>'
            + ''.join(f'<li><a href="#{a}">{t}</a></li>' for a, t in items) + '</ol></nav>')


def guide(main, side=''):
    return f'''<div class="guide">
  <article class="guide-main prose">
{main}
  </article>
  <aside class="guide-side">
{side}
    <div class="side-cta"><strong>Try it on your own data</strong><p>It's free, there's no sign-up, and your file stays on your computer.</p><a href="analyser/" class="btn">Open the analyser</a></div>
  </aside>
</div>'''


# Fingerprint of the stylesheet, added to its link so browsers fetch a new copy after every change.
import hashlib
JS_VERSION = hashlib.sha1(open(os.path.join(os.path.dirname(__file__), '..', 'site', 'js', 'motion.js'), 'rb').read()).hexdigest()[:8]
CSS_VERSION = hashlib.sha1(open(os.path.join(os.path.dirname(__file__), '..', 'site', 'css', 'site.css'), 'rb').read()).hexdigest()[:8]
# Logo and icon files keep their names, so bust the 7-day image cache when they change.
LOGO_VERSION = hashlib.sha1(open(os.path.join(os.path.dirname(__file__), '..', 'site', 'images', 'brand', 'hei-logo.png'), 'rb').read()).hexdigest()[:8]


def og_image(page):
    card = guide_card(page.file)
    src, (w, h) = (card, card_size(card)) if card else ('images/og-image.png', (1200, 630))
    return (f'  <meta property="og:image" content="{url(src)}">\n  <meta property="og:image:width" content="{w}">\n'
            f'  <meta property="og:image:height" content="{h}">')


def layout(page):
    current = NAV_PARENT.get(page.file, page.file)
    active = ' class="active" aria-current="page"'
    links = ''.join(f'<li><a href="{href}"{active if href == current else ""}>{label}</a></li>' for href, label in NAV)
    canonical = (f'  <link rel="canonical" href="{canonical_url(page.file)}">\n  <meta property="og:url" content="{canonical_url(page.file)}">\n'
                 if SITE_URL and not page.noindex else '')
    robots = '  <meta name="robots" content="noindex">\n' if page.noindex else ''
    # The 404 page is served at any missing address, so anchor its relative links to the site root.
    base = '  <base href="/">\n' if page.file == '404.html' else ''
    modified = page_dates(page.file)[1]
    body = page.body.replace(UPDATED_MARK, f'<time datetime="{modified}">{long_date(modified)}</time>')
    return clean_links(f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
{base}  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page.title}</title>
  <meta name="description" content="{escape(page.description)}">
{canonical}{robots}  <meta property="og:type" content="{'article' if page.article else 'website'}">
  <meta property="og:locale" content="en_GB">
  <meta property="og:title" content="{escape(page.title)}">
  <meta property="og:description" content="{escape(page.description)}">
{og_image(page)}
  <meta property="og:site_name" content="{NAME}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" sizes="32x32" href="images/brand/favicon-32.png?v={LOGO_VERSION}">
  <link rel="icon" type="image/png" sizes="16x16" href="images/brand/favicon-16.png?v={LOGO_VERSION}">
  <link rel="icon" type="image/png" sizes="48x48" href="images/brand/favicon-48.png?v={LOGO_VERSION}">
  <link rel="icon" type="image/png" sizes="192x192" href="images/brand/favicon-192.png?v={LOGO_VERSION}">
  <link rel="apple-touch-icon" sizes="180x180" href="images/brand/apple-touch-icon.png?v={LOGO_VERSION}">
  <link rel="manifest" href="site.webmanifest">
  <meta name="theme-color" content="#0B2E4F">
  <link rel="preload" href="fonts/schibsted-grotesk-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/site.css?v={CSS_VERSION}">
  <script>if('IntersectionObserver' in window&&!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('motion')</script>
  <script src="js/motion.js?v={JS_VERSION}" defer></script>
{jsonld(page)}{page.extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<nav class="site-nav" id="siteNav" aria-label="Main">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo" aria-label="{NAME} home">
      <picture><source type="image/webp" srcset="images/brand/hei-logo.webp?v={LOGO_VERSION}"><img src="images/brand/hei-logo.png?v={LOGO_VERSION}" width="313" height="132" alt=""></picture>
    </a>
    <ul class="nav-links" id="navLinks">
      {links}
      <li><a href="analyser/" class="nav-cta">Upload HH data</a></li>
    </ul>
    <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-logo"><picture><source type="image/webp" srcset="images/brand/hei-logo-white.webp?v={LOGO_VERSION}"><img src="images/brand/hei-logo-white.png?v={LOGO_VERSION}" width="303" height="132" alt="{NAME}" loading="lazy"></picture></div>
        <p class="footer-desc">Free half-hourly electricity analysis, solar sizing and decarbonisation guides for NHS and independent healthcare estates across England, Scotland and Wales, run by {OPERATOR}. The analysis runs in your browser, so your meter data never leaves your computer.</p>
        <div class="footer-contact-item">Email: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></div>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Tools</div>
        <ul><li><a href="analyser/">Analyse half-hourly data</a></li><li><a href="solar-calculator.html">Solar calculator</a></li><li><a href="how-it-works.html">How the analyser works</a></li><li><a href="solar-calculator-method.html">How the solar calculator works</a></li><li><a href="sample-report.html">Sample report</a></li><li><a href="{GUIDE_PDF}" download>User guide (PDF)</a></li><li><a href="faq.html">FAQ</a></li></ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">Decarbonisation</div>
        <ul><li><a href="healthcare-estates-decarbonisation.html">The estates challenge</a></li><li><a href="nhs-net-zero-targets.html">Net zero targets</a></li><li><a href="decarbonisation-funding.html">Funding routes</a></li><li><a href="heat-decarbonisation.html">Heat decarbonisation</a></li><li><a href="moving-away-from-chp.html">Moving away from CHP</a></li><li><a href="hospital-electrical-capacity.html">Electrical capacity</a></li><li><a href="solar-on-healthcare-estates.html">Solar on healthcare estates</a></li><li><a href="hospital-energy-efficiency.html">Energy efficiency</a></li></ul>
      </div>
      <div class="footer-col">
        <div class="footer-col-title">About</div>
        <ul><li><a href="about.html">About us</a></li><li><a href="contact.html">Contact</a></li><li><a href="guides.html">All guides</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms of use</a></li></ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-copy">&copy; {YEAR} {OPERATOR}</div>
      <div class="footer-disclaimer">All analyser and calculator results are estimates based on the data you load and do not guarantee savings. Our guides are general information and are not financial, tax, legal or clinical engineering advice. Not affiliated with or endorsed by the NHS.</div>
    </div>
  </div>
</footer>
<script>
  document.getElementById('navToggle').addEventListener('click', function (e) {{
    var open = document.getElementById('siteNav').classList.toggle('nav-mobile-open');
    e.currentTarget.setAttribute('aria-expanded', open ? 'true' : 'false');
    e.currentTarget.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }});
</script>
{ANALYTICS}
</body>
</html>
''')


def sources(items):
    """Numbered source list at the end of a guide: [(title, url)]."""
    return ('<div class="sources"><h2 id="sources">Sources</h2><ol>'
            + ''.join(f'<li><a href="{u}">{t}</a></li>' for t, u in items) + '</ol></div>')
