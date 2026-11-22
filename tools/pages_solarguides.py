"""
Solar guides from the UK Solar Calculator, which built the calculator this site
uses: its method and assumptions, costs, payback, generation, planning and
grid, and paying for solar. The article text is kept in tools/content/solar/
(<name>.html for the article, <name>.side.html for its contents list), taken
from that site so the two stay consistent, with links pointed at this site.

The text was written by the same team for commercial and public sector sites
generally. Healthcare notes are added at the top of each page here. When the
UK Solar Calculator updates a guide, replace the fragment and rebuild.
"""
import json
import re
from pathlib import Path

from kit import NAV_PARENT, Page, cta, page_hero, faq_section, strip_tags
from pages_guides import GUIDES, HOME

DIR = Path(__file__).resolve().parent / 'content' / 'solar'
META = json.loads((DIR / 'meta.json').read_text(encoding='utf-8'))

NOTES = {
    'solar-calculator-method': 'This is the method behind this site\'s <a href="solar-calculator.html">solar calculator</a>. The one input that matters most for a hospital is the share of solar used on site: rather than the 80% default, measure it from your own half-hourly data in the <a href="analyser/">analyser</a> and pass it across.',
    'solar-cost': 'Hospital roofs often carry plant, flues and access routes, and car park canopies cost more per kWp because of the steelwork. Both are reflected in the per-kWp benchmarks below. Survey costs, structural work and any grid reinforcement are extra.',
    'solar-payback': 'On a 24-hour hospital the share of output used on site is usually high, which shortens payback. On clinics and offices closed at weekends it is lower. Measure it from your half-hourly data in the <a href="analyser/">analyser</a>.',
    'solar-generation': 'Generation depends on where you are and how the panels face, not on the type of building. What changes for a hospital is how much of that generation it uses, which you can measure from half-hourly data.',
    'solar-planning-and-grid': 'On hospital sites, also plan for glint and glare near helicopter landing sites, works around clinical areas and access routes, and how solar will behave with your standby generators during a power cut.',
    'paying-for-solar': 'For NHS organisations, see also <a href="decarbonisation-funding.html">funding routes</a>, including Great British Energy\'s solar funding for NHS sites and the devolved schemes in Scotland and Wales.',
}
TITLES = {
    'solar-calculator-method': ('How the solar calculator works: method and assumptions', 'How the solar calculator works'),
    'solar-cost': ('How much does solar cost for hospitals and large sites?', 'What solar costs'),
    'solar-payback': ('How long does solar take to pay back on a hospital or healthcare site?', 'Solar payback'),
    'solar-generation': ('How much electricity will solar panels generate?', 'How much solar generates'),
    'solar-planning-and-grid': ('Solar planning permission and grid connection for healthcare sites', 'Planning and grid connection'),
    'paying-for-solar': ('Paying for solar: buy, finance, lease or a PPA', 'Paying for solar'),
}

PAGES = []
for name, m in META.items():
    file = f'{name}.html'
    title, short = TITLES[name]
    art = (DIR / f'{name}.html').read_text(encoding='utf-8')
    side = (DIR / f'{name}.side.html').read_text(encoding='utf-8')
    side += ('\n    <div class="side-cta"><strong>Start with your half-hourly data</strong><p>The analyser measures how much solar each site '
             'would use, then opens the calculator with your figures.</p><a href="analyser/" class="btn">Upload HH data</a></div>')
    note = f'<div class="note"><strong>For healthcare sites.</strong> {NOTES[name]}</div>\n'
    # The note goes after the opening answer paragraph.
    m_ans = re.search(r'(<p class="answer">.*?</p>)', art, re.S)
    art = art.replace(m_ans.group(1), m_ans.group(1) + '\n' + note, 1) if m_ans else note + art
    crumbs = [HOME, GUIDES, (short, file)]
    NAV_PARENT[file] = 'guides.html'
    body = (page_hero('Solar guide', m['h1'], m['lead'] or strip_tags(m['description']), crumbs=crumbs, image=name)
            + f'''<div class="guide">
  <article class="guide-main prose">
<p class="byline">By the team behind the solar calculator <span aria-hidden="true">·</span> Last updated <!--last-updated--></p>
{art}
  </article>
  <aside class="guide-side" aria-label="On this page">
{side}
  </aside>
</div>'''
            + cta('See the numbers for your site', 'Start with your half-hourly data, then size the system in the solar calculator.'))
    PAGES.append(Page(file, f'{title} | Healthcare Energy Insights', m['description'], body, crumbs=crumbs,
                      faqs=[(q, a) for q, a in m['faqs']], article=True, section='Guides',
                      summary=strip_tags(m['description'])))
