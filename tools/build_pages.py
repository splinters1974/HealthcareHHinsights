"""
Builds the Healthcare Energy Insights site in site/: every page from one layout,
plus robots.txt, llms.txt and (once the domain is set) sitemap.xml.

    python3 tools/build_pages.py

Settings, layout and structured data: tools/kit.py
Core pages: tools/pages_core.py
Guides and sector pages: tools/pages_guides.py
"""
import datetime as dt
import hashlib
import re
import json
from pathlib import Path

import kit
from kit import NAME, OPERATOR, SITE_URL, layout, url
from pages_core import core_pages
from pages_guides import PAGES as GUIDE_PAGES
from pages_data import PAGES as DATA_PAGES
from pages_prices import PAGES as PRICE_PAGES
from pages_solar import PAGES as SOLAR_PAGES
from pages_healthcare import PAGES as HEALTH_PAGES
from pages_solarguides import PAGES as SOLAR_GUIDE_PAGES
import build_calculator

SITE = Path(__file__).resolve().parent.parent / 'site'
DATES_FILE = Path(__file__).resolve().parent / 'page_dates.json'

# Crawlers that answer questions and cite sources, listed explicitly (as on
# the UK Solar Calculator) so a later change to the wildcard can't shut them out.
AI_SEARCH = ['OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'ClaudeBot', 'Claude-SearchBot', 'Google-Extended']
AI_TRAINING = ['GPTBot', 'Applebot-Extended', 'CCBot', 'Meta-ExternalAgent']


def robots():
    lines = ['# Healthcare Energy Insights. Everything here is public and intended to be found, indexed and cited.', '',
             'User-agent: *', 'Allow: /', '', '# Search engines', 'User-agent: Googlebot', 'Allow: /', '',
             'User-agent: Bingbot', 'Allow: /', '', '# AI answer engines that cite their sources']
    for bot in AI_SEARCH:
        lines += [f'User-agent: {bot}', 'Allow: /', '']
    lines += ['# AI training crawlers: allowed so models know the site exists. Change to Disallow to opt out.']
    for bot in AI_TRAINING:
        lines += [f'User-agent: {bot}', 'Allow: /', '']
    if SITE_URL:
        lines.append(f'Sitemap: {SITE_URL}/sitemap.xml')
    return '\n'.join(lines).rstrip() + '\n'


def llms(pages):
    """llms.txt: a plain summary for AI tools, in the format the solar site uses."""
    out = [f'# {NAME}', '',
           '> Free tools and guides for NHS trusts, health boards, ambulance trusts and independent hospitals in England, Scotland and Wales: '
           'a half-hourly (HH) electricity analyser (base load, day and night use, out-of-hours use in clinics and offices, peaks against agreed '
           'supply capacity and headroom for heat pumps, EV charging and CHP removal, unusual days, solar self-consumption, PDF and Excel reports), '
           'a solar PV calculator fed by the measured profile, and sourced guides to net zero targets, funding, heat decarbonisation, moving away '
           'from gas CHP, electrical capacity, solar and energy efficiency on healthcare estates.', '',
           'Independent: not part of, or endorsed by, the NHS.', '',
           f'Operated by {OPERATOR}. Free to use, no sign-up. The analyser runs entirely in the browser: meter data is never uploaded.', '',
           'Scope: healthcare estates, NHS and independent sector. Results are indicative estimates from the data loaded: costs are '
           'energy cost at the rates entered, not guaranteed savings, and whole-site data shows when energy is used, not which '
           'equipment uses it. The method is set out on the How it works page.', '',
           'Method in brief: base load is the 5th percentile of valid half-hourly demand; out-of-hours (closed-hours) excess is '
           'energy used outside the opening hours above that base load; missing readings are left out, never counted as zero; '
           'annual figures are scaled from valid hours and withheld under 180 days of data; kVA is kW divided by an assumed power factor.', '']
    out += ['## Tools', '', f'- [Analyser]({url("analyser/")}): the half-hourly analyser, in the browser.',
            f'- [Solar calculator]({url("solar-calculator.html")}): solar PV sizing, cost, payback and PPA comparison over 25 years; opens with the analyser\'s measured share of output used on site.', '']
    for section in ['Core pages', 'Guides', 'Sectors']:
        items = [p for p in pages if p.section == section and p.summary]
        if items:
            out += [f'## {section}', ''] + [f'- [{p.title.split(" | ")[0]}]({url(p.file)}): {p.summary}' for p in items] + ['']
    out += ['## Related', '', f'- [UK Solar Calculator]({kit.SOLAR_SITE}): sister site from the same team, for commercial solar PV estimates.',
            f'- [Half Hourly Insights]({kit.HHI_SITE}): sister site from the same team, the general-purpose version of the analyser.', '']
    return '\n'.join(out)


def fingerprint(p):
    """What a reader sees: title, description and body (not the layout around it).
    The decorative header photo is left out: swapping a picture is not a content update."""
    body = re.sub(r'<div class="hero-media" aria-hidden="true">.*?</picture></div>\n  ', '', p.body, flags=re.S)
    body = body.replace(' page-hero-photo', '')
    return hashlib.sha256('\n'.join([p.title, p.description, body]).encode()).hexdigest()[:16]


def update_dates(pages):
    """Give a page today's date when its content changes; keep it otherwise."""
    today = dt.date.today().isoformat()
    old = json.loads(DATES_FILE.read_text()) if DATES_FILE.exists() else {}
    new = {}
    for p in pages:
        h, prev = fingerprint(p), old.get(p.file)
        if prev is None:
            new[p.file] = {'published': today, 'modified': today, 'fingerprint': h}
        elif prev['fingerprint'] != h:
            new[p.file] = {**prev, 'modified': today, 'fingerprint': h}
        else:
            new[p.file] = prev
    DATES_FILE.write_text(json.dumps(dict(sorted(new.items())), indent=1) + '\n')
    kit.PAGE_DATES.update(new)


def sitemap(pages):
    rows = ''.join(f'  <url><loc>{url(p.file)}</loc><lastmod>{kit.page_dates(p.file)[1]}</lastmod></url>\n'
                   for p in pages if not p.noindex)
    rows += f'  <url><loc>{url("solar-calculator.html")}</loc><lastmod>{max(d["modified"] for d in kit.PAGE_DATES.values())}</lastmod></url>\n'
    rows += f'  <url><loc>{url("analyser/")}</loc><lastmod>{max(d["modified"] for d in kit.PAGE_DATES.values())}</lastmod></url>\n'
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}</urlset>\n'


def main():
    pages = core_pages() + HEALTH_PAGES + GUIDE_PAGES + SOLAR_PAGES + SOLAR_GUIDE_PAGES + DATA_PAGES + PRICE_PAGES
    update_dates(pages)
    for p in pages:
        (SITE / p.file).write_text(layout(p), encoding='utf-8')
    build_calculator.build()
    (SITE / 'robots.txt').write_text(robots(), encoding='utf-8')
    (SITE / 'llms.txt').write_text(llms(pages), encoding='utf-8')
    if SITE_URL:
        (SITE / 'sitemap.xml').write_text(sitemap(pages), encoding='utf-8')
    print(f'wrote {len(pages)} pages, robots.txt, llms.txt' + (', sitemap.xml' if SITE_URL else ' (sitemap waits for SITE_URL)'))


if __name__ == '__main__':
    main()
