"""
The solar calculator page (site/solar-calculator.html).

The calculator is the UK Solar Calculator's own page (tools/vendor/
solar-calculator.source.html, with its stylesheet in solar-shared.source.css),
kept as it is so its method and assumptions stay exactly in step with that
site. This script gives it this site's header, footer, name, contact details
and palette, and points its half-hourly links at this site's analyser.

To take a newer calculator from the UK Solar Calculator, copy its
calculator.html and css/shared.css over the two vendor files and rebuild.
If a replacement below no longer matches, the build stops and says which.

Called by build_pages.py; can also be run on its own.
"""
import re
from pathlib import Path

import kit

HERE = Path(__file__).resolve().parent
SITE = HERE.parent / 'site'
SRC = HERE / 'vendor' / 'solar-calculator.source.html'
CSS_SRC = HERE / 'vendor' / 'solar-shared.source.css'
FILE = 'solar-calculator.html'

TITLE = 'Hospital solar calculator: size, cost and payback'
DESC = ('Free solar calculator for NHS and private hospitals: draw roofs and car parks, use your half-hourly data, '
        'and see size, savings and payback, bought or on a PPA.')
# Healthcare questions, shown on the page and marked up as FAQPage.
FAQS = [
    ('How should a hospital use the calculator?',
     'Start in the <a href="analyser/">half-hourly analyser</a>. On a site\'s Solar tab, choose Size solar for this site, and the calculator opens with the share of '
     'solar your site would use, measured from its own readings. Then draw the roofs and car parks on the map, check the postcode and enter your unit price.'),
    ('What share of solar used on site should a hospital enter?',
     'Measure it if you can. A 24-hour hospital often uses 90% or more of a well-sized system\'s output; clinics and offices closed at weekends are often 55 to 80%. '
     'The calculator starts at 80% if you have no data.'),
    ('Can it cost solar car park canopies?',
     'Yes. Draw the car park as a carport area. Canopies are costed separately from roofs because the steel structure makes them dearer per kWp.'),
    ('Should an NHS trust buy the system or use a PPA?',
     'Buying gives the most value over 25 years; a power purchase agreement needs no capital. The calculator shows both side by side. Check with your finance team how a PPA would be accounted for before choosing. See <a href="paying-for-solar.html">paying for solar</a>.'),
    ('Do the figures include VAT?',
     'No. Costs are shown before VAT. How much VAT can be recovered differs between NHS bodies and private companies, so confirm it with your finance team.'),
    ('How accurate are the results?',
     'They are a first estimate. Generation uses SAP 10.3 sunshine data for your postcode and a typical layout. Shading from plant, roof condition, structure and the DNO offer all come from a survey.'),
]
OLD_EMAIL = 'enquiries@uksolarcalculator.co.uk'

# Palette: the same swaps as site/css/site.css.
COLOURS = {'#063C55': '#0B2E4F', '#042A3C': '#071F36', '#0065A4': '#0A66B7', '#004F80': '#084F8E', '#00853F': '#00806F',
           '#8FD16A': '#5FD3C6', '#F8C05D': '#F5B335', '#0A4A68': '#0E3F69', '#0F5A7D': '#13507F', '#4DB3F0': '#5AB0F0',
           'rgba(0,101,164,': 'rgba(10,102,183,', 'rgba(6,60,85,': 'rgba(11,46,79,'}
RGB = {'6, 60, 85': '11, 46, 79', '6,60,85': '11,46,79', '6,   60,  85': '11,  46,  79',
       '0, 101, 164': '10, 102, 183', '0,101,164': '10,102,183', '0, 133, 63': '0, 128, 111', '0,133,63': '0,128,111',
       '0,   133, 63': '0,   128, 111'}

FONT_FACE = '''  <style>
@font-face { font-family: 'Schibsted Grotesk'; font-weight: 400; font-display: swap; src: url('fonts/schibsted-grotesk-latin-400-normal.woff2') format('woff2'); }
@font-face { font-family: 'Schibsted Grotesk'; font-weight: 500 600; font-display: swap; src: url('fonts/schibsted-grotesk-latin-600-normal.woff2') format('woff2'); }
@font-face { font-family: 'Schibsted Grotesk'; font-weight: 700; font-display: swap; src: url('fonts/schibsted-grotesk-latin-700-normal.woff2') format('woff2'); }
@font-face { font-family: 'Schibsted Grotesk'; font-weight: 800 900; font-display: swap; src: url('fonts/schibsted-grotesk-latin-800-normal.woff2') format('woff2'); }
  </style>
'''


def must(text, old, new, count=1, label=''):
    n = text.count(old)
    if n < count:
        raise SystemExit(f'build_calculator: expected {label or old[:60]!r} at least {count} time(s), found {n}. Update the replacement.')
    return text.replace(old, new)


def site_chrome():
    """Header and footer exactly as every other page has them, from the shared layout."""
    page = kit.Page(FILE, TITLE, DESC, '<!--BODY-->')
    built = kit.layout(page)
    nav = re.search(r'<nav class="site-nav".*?</nav>', built, re.S).group(0)
    footer = re.search(r'<footer class="site-footer">.*?</footer>', built, re.S).group(0)
    script = re.search(r'</footer>\s*(<script>.*?</script>)', built, re.S).group(1)
    return nav, footer, script


def head():
    url = kit.url(FILE)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{TITLE}</title>
  <meta name="description" content="{DESC}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="en_GB">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="{DESC}">
  <meta property="og:image" content="{kit.url('images/og-image.png')}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="{kit.NAME}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" sizes="32x32" href="images/brand/favicon-32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="images/brand/favicon-16.png">
  <link rel="icon" type="image/png" sizes="48x48" href="images/brand/favicon-48.png">
  <link rel="icon" type="image/png" sizes="192x192" href="images/brand/favicon-192.png">
  <link rel="apple-touch-icon" sizes="180x180" href="images/brand/apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <meta name="theme-color" content="#0B2E4F">
{kit.jsonld(kit.Page(FILE, TITLE, DESC, '', crumbs=[('Home', 'index.html'), ('Solar calculator', FILE)], faqs=FAQS,
                     schema=[{'@type': 'WebApplication', 'name': f'{kit.NAME} solar calculator', 'url': url,
                              'applicationCategory': 'BusinessApplication', 'operatingSystem': 'Any',
                              'isAccessibleForFree': True, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'GBP'},
                              'description': DESC, 'provider': {'@id': kit.ORG_ID}}]))}{FONT_FACE}'''


def build():
    src = SRC.read_text(encoding='utf-8')
    # Keep everything from the calculator's own stylesheet link to the end of <head>.
    start = src.index('  <link rel="preconnect" href="https://fonts.googleapis.com">')
    rest = src[start:]
    rest = re.sub(r'  <link rel="preconnect" href="https://fonts\.googleapis\.com">\n  <link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\n  <link href="https://fonts\.googleapis\.com/css2[^"]*" rel="stylesheet">\n', '', rest)
    rest = re.sub(r'<link rel="stylesheet" href="css/shared\.css[^"]*">', '<link rel="stylesheet" href="css/solar.css?v=' + kit.CSS_VERSION + '">', rest)
    nav, footer, script = site_chrome()
    rest = re.sub(r'<nav class="site-nav" id="siteNav".*?</nav>', lambda m: nav.replace('href="solar-calculator.html"', 'href="solar-calculator.html" class="active" aria-current="page"', 1), rest, count=1, flags=re.S)
    rest = re.sub(r'<footer class="site-footer">.*?</footer>', lambda m: footer, rest, count=1, flags=re.S)
    if '<a class="skip"' not in rest:
        rest = rest.replace('<body>', '<body>\n<a class="skip" href="#main">Skip to content</a>', 1)

    # Words and links
    rest = must(rest, '<h1>Commercial solar calculator</h1>', '<h1>Solar calculator for healthcare sites</h1>')
    rest = must(rest, '<p>Outline your roof, add your postcode and unit price.',
                '<p>Best started from the <a href="analyser/">half-hourly analyser</a>, so the share of solar used on site comes from your own readings. Outline your roofs and car parks, add your postcode and unit price.')
    rest = must(rest, '<span>Calculator</span></nav>', '<span>Solar calculator</span></nav>')
    rest = must(rest, '<img src="images/brand/hhi-logo.png" width="370" height="132" alt="Half Hourly Insights">',
                '<img src="images/brand/hei-logo.png" width="367" height="132" alt="Hospital Energy Insights">')
    rest = must(rest, 'Your figures from Half Hourly Insights have arrived', 'Your figures from the half-hourly analyser have arrived')
    rest = must(rest, 'https://hhinsights.co.uk/analyser/" target="_blank" rel="noopener"', 'analyser/"', count=2)
    rest = must(rest, 'in Half Hourly Insights', 'in the analyser', count=2)
    rest = rest.replace('Using your half-hourly readings from Half Hourly Insights.', 'Using your half-hourly readings from the analyser.')
    rest = rest.replace('Half Hourly Insights analyser', 'half-hourly analyser on this site')
    rest = rest.replace('Half Hourly Insights', 'the analyser')
    rest = must(rest, 'Thank you for using the UK Solar Calculator.', f'Thank you for using the {kit.NAME} solar calculator.')
    rest = must(rest, 'https://uksolarcalculator.co.uk/how-it-works.html', kit.url('solar-calculator-method.html'))
    rest = must(rest, 'The Kinetic Energy Consulting Solar Calculator is designed to give commercial and industrial businesses',
                f'The {kit.NAME} solar calculator, run by Kinetic Energy Consulting, is designed to give healthcare estates and other organisations')
    rest = must(rest, OLD_EMAIL, kit.CONTACT_EMAIL, count=5)
    rest = must(rest, '<img id="pdfLogoImg" src="images/brand/ukscalc-pdf-logo-v2.png" style="display:none" alt="">',
                '<img id="pdfLogoImg" src="images/brand/hei-pdf-logo.png" width="800" height="200" style="display:none" alt="">')
    # Links to the UK Solar Calculator's own guides go to this site's copies.
    for a, b in {'your-energy-data.html': 'solar.html', 'planning-and-grid.html': 'solar-planning-and-grid.html',
                 'funding.html': 'paying-for-solar.html', 'calculator.html': 'solar-calculator.html', 'how-it-works.html': 'solar-calculator-method.html',
                 'commercial-solar-cost.html': 'solar-cost.html', 'commercial-solar-payback.html': 'solar-payback.html',
                 'commercial-solar-generation.html': 'solar-generation.html', 'nhs.html': 'solar-on-healthcare-estates.html'}.items():
        rest = re.sub(r'href="' + re.escape(a) + r'(#[^"]*)?"', lambda m, b=b: f'href="{b}{m.group(1) or ""}"', rest)
    # Leads go to the named contact only.
    rest = re.sub(r"(const LEAD_RECIPIENTS = \[\n)(.*?)(\n  \];)",
                  lambda m: m.group(1) + f"    {{ email: '{kit.LEAD_EMAIL}', name: 'Hospital Energy Insights' }}," + m.group(3), rest, count=1, flags=re.S)
    # Healthcare questions in place of the general ones.
    faq_html = ''.join(f'<details><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>\n' for q, a in FAQS)
    rest = re.sub(r'(<h2 id="calcFaqH">)Questions about the calculator(</h2>\n    <div class="faq">\n).*?(</div>\n    <p class="help")',
                  lambda m: m.group(1) + 'Questions from estates teams' + m.group(2) + faq_html + m.group(3), rest, count=1, flags=re.S)
    if 'Questions from estates teams' not in rest:
        raise SystemExit('build_calculator: FAQ block not found')
    # Healthcare guidance on the share used on site (the 80% default itself is unchanged).
    rest = rest.replace("80% suits most sites busy through the working week. Warehouses, farms and sites closed at weekends are often 40 to 70%. The rest is exported at 5p/kWh.",
                        "80% suits most sites busy through the working week. Hospitals open around the clock often use 90% or more; clinics and admin buildings closed at weekends are often 55 to 80%. Best of all, measure it from your half-hourly data. The rest is exported at 5p/kWh.")

    for a, b in COLOURS.items():
        rest = rest.replace(a, b).replace(a.lower(), b)
    for a, b in RGB.items():
        rest = rest.replace(f'[{a}]', f'[{b}]').replace(f'({a})', f'({b})')
    out = kit.clean_links(head() + rest)
    for bad in ['uksolarcalculator.co.uk', 'UK Solar Calculator', 'hhinsights.co.uk/analyser']:
        if bad in out.replace('hospitalenergy.co.uk', ''):
            raise SystemExit(f'build_calculator: {bad!r} is still in the calculator page')
    (SITE / FILE).write_text(out, encoding='utf-8')

    css = CSS_SRC.read_text(encoding='utf-8')
    css += ('\n/* Hospital Energy Insights: skip link, as on the rest of the site */\n'
            '.skip { position: absolute; left: -10000px; top: 8px; z-index: 2000; background: #fff; color: var(--ink); padding: 10px 16px; border-radius: 6px; font-weight: 600; }\n'
            '.skip:focus { left: 16px; }\n')
    css = css.replace('UK Solar Calculator — Shared Styles', 'Hospital Energy Insights: solar calculator styles (from the UK Solar Calculator, recoloured)')
    for a, b in COLOURS.items():
        css = css.replace(a, b).replace(a.lower(), b)
    (SITE / 'css' / 'solar.css').write_text(css, encoding='utf-8')
    return FILE


if __name__ == '__main__':
    print('wrote', build())
