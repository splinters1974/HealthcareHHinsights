"""
Solar sizing from half-hourly data, for hospitals and healthcare sites: why
the share of output used on site decides the value, what HH data shows before
sizing, a worked example, and how the analyser hands over to the calculator.

Worked-example figures come from the analyser's own solar estimate
(analyser/src/local/solarFit.ts) run on site/samples/example-hospital.csv at
UK average output (905 kWh/kWp), locked in analyser/tests/website-claims.test.ts.
Values are first-year, at the solar calculator's default unit price (25p/kWh)
and export rate (5p/kWh).

REVIEW EACH APRIL: the Ofgem SEG scope, the business rates and capital
allowance references, and the calculator's assumptions.
"""
from kit import (NAV_PARENT, Page, photo, SOLAR_URL, guide, page_hero, faq_section, sources,
                 toc, updated_line)
from pages_guides import HOME

FILE = 'solar.html'
CALC = SOLAR_URL
SOLAR_CONTACT = 'contact.html?src=solar'
CRUMBS = [HOME, ('Solar calculator', SOLAR_URL), ('Sizing from half-hourly data', FILE)]
NAV_PARENT[FILE] = SOLAR_URL


def ref(*n):
    return f'<sup><a href="#sources">{",".join(str(x) for x in n)}</a></sup>'


SRC = [
    ('How the solar calculator works (method and assumptions)', 'solar-calculator-method.html'),
    ('Ofgem: Smart Export Guarantee (SEG)', 'https://www.ofgem.gov.uk/environmental-and-social-schemes/smart-export-guarantee-seg'),
    ('Solar planning permission and grid connection for healthcare sites', 'solar-planning-and-grid.html'),
    ('Explanatory Memorandum to SI 2022/405, business rates exemption for renewable plant',
     'https://www.legislation.gov.uk/uksi/2022/405/pdfs/uksiem_20220405_en.pdf'),
    ('Paying for solar on healthcare sites', 'paying-for-solar.html'),
    ('Department for Energy Security and Net Zero: Energy Trends section 6, renewables (table ET 6.1, solar generation by quarter)',
     'https://www.gov.uk/government/statistics/energy-trends-section-6-renewables'),
    ('GOV.UK: Standard Assessment Procedure (SAP 10.3)', 'https://www.gov.uk/guidance/standard-assessment-procedure'),
]

# Example community hospital, UK average output. (kWp, generated, used on site, share of the site's electricity %)
EXAMPLE = [
    (299.1, 268374, 267801, 20),
    (448.6, 402516, 383707, 29),
    (747.7, 670890, 506661, 38),
    (1196.3, 1073406, 584828, 44),
]
USE = 1341750  # kWh over the 363 valid days


def gbp(x):
    return f'£{round(x):,}'


def value(gen, used, unit=0.25, export=0.05):
    return used * unit + (gen - used) * export


def share(gen, used):
    return f'{used / gen * 100:.1f}%' if used / gen > 0.995 else f'{round(used / gen * 100)}%'


def example_rows():
    out = []
    for kwp, gen, used, cov in EXAMPLE:
        out.append(f'<tr><td style="white-space:nowrap">{kwp:,.0f} kWp</td><td class="num">{gen:,} kWh</td><td class="num">{share(gen, used)}</td>'
                   f'<td class="num">{cov}%</td><td class="num">{gbp(value(gen, used))}</td>'
                   f'<td class="num">{gbp(value(gen, gen * 0.8))}</td></tr>')
    return ''.join(out)


def gap(row):
    kwp, gen, used, _ = row
    return value(gen, gen * 0.8) - value(gen, used)


UNDER = -gap(EXAMPLE[1])
OVER = gap(EXAMPLE[3])
OVER_PCT = round(OVER / value(EXAMPLE[3][1], EXAMPLE[3][2]) * 100)

FAQS = [
    ('Will a hospital use all the solar it generates?',
     "Usually most of it, because wards, ventilation, imaging and fridges run through every sunny afternoon and at weekends. "
     "In our made-up community hospital, a system of up to about 300 kWp is used almost entirely on site. Very large systems "
     "still export at weekends and on long summer evenings, so measure it from your own data."),
    ('Is the 80% default in the solar calculator right for a hospital?',
     "Often it's too low for a well-sized system on a 24-hour site and too high for a very large one. Load a year of "
     "half-hourly data into the analyser and pass the measured figure across instead."),
    ('Should a health centre or clinic be sized differently?',
     "Yes. A building that closes at 18:30 and at weekends exports much more of its summer output, so the share used on site "
     "falls faster as the system gets bigger. Size it from that building's own meter, not the main hospital's."),
    ('Does solar cut our capacity charges?',
     "No. Capacity charges are set per kVA of agreed capacity and standing charges per day, so they don't change. Solar cuts "
     "the units you import. It also does little for winter evening peaks, because it's dark by about 4pm in midwinter."),
    ('Is our meter data sent to the solar calculator?',
     "No. Only the annual use, the share used on site at a dozen sizes and the postcode, if you entered one, are passed, in the "
     "part of the web address after the #. Browsers never send that part to a server."),
    ('Should we add a battery?',
     "On a 24-hour hospital there is often little surplus to store unless the array is large. Check how much the site exports "
     "on sunny weekends in the analyser's estimate, then model the battery in the calculator."),
]

TOC = [('why', 'Why healthcare sites fit solar'), ('share', 'The figure that matters most'), ('data', 'What your data shows'),
       ('example', 'A worked example'), ('how', 'From data to estimate'), ('calculator', 'What the calculator does'),
       ('limits', 'What this can and cannot tell you'), ('questions', 'Questions people ask'), ('sources', 'Sources')]

MAIN = f'''{updated_line()}
<p class="answer">On a hospital, solar is worth most when it's sized to the roof, car parks and connection you have, because a 24-hour site uses nearly all of a well-sized system's output. Your half-hourly data measures that share at each system size, replacing the guess that most estimates start from. The analyser passes the measured figure to the <a href="{SOLAR_URL}"><strong>solar calculator</strong></a>, which works out what fits, what it costs and how soon it pays back.</p>

<h2 id="why">Why healthcare sites fit solar</h2>
<ul>
<li><strong>Demand is there when the sun is.</strong> Wards, theatres, imaging, kitchens and ventilation all run through the middle of the day, every day of the week. That's rare among building types, and it's what makes solar pay on hospitals.</li>
<li><strong>Every unit used on site replaces a unit bought</strong> at the full import price.{ref(1)} Export earns far less: under the Smart Export Guarantee, a supplier pays for exported power from systems up to 5 MW, at a rate the supplier sets.{ref(2)}</li>
<li><strong>Rooftops rarely need planning permission in England</strong>, though listed buildings, conservation areas and car park canopies need more care, and almost every system needs DNO approval under G99.{ref(3)}</li>
<li><strong>On-site renewable plant is exempt from business rates in England</strong> from April 2022, which matters because NHS hospitals pay rates.{ref(4)}</li>
<li><strong>Funding has been aimed at NHS solar.</strong> Great British Energy has funded solar on NHS sites, and power purchase agreements need no capital at all.{ref(5)}</li>
</ul>
{photo('hc-public-hospital-solar', 'A large public hospital with solar panels across its flat roofs and car park canopies', 'Hospital roofs carry plant and flues, so the usable area is often smaller than it looks. Car parks add space.')}

<h2 id="share">The figure that matters most: the share you use yourself</h2>
<p>At a 25p unit price, each kWh of solar used on site saves 25p, while each kWh exported earns about 5p, the rate the calculator assumes.{ref(1)} That five-to-one gap means the share used on site moves the result more than almost any other input.</p>
<p>The calculator starts at 80% if you don't measure it.{ref(1)} For a 24-hour hospital that's often too cautious at the sizes most sites can fit, and too generous for very large arrays. For a health centre that closes at weekends, it can be too generous at almost any size. Half-hourly data settles it.</p>

<h2 id="data">What your half-hourly data shows before you size anything</h2>
<div class="table-wrap"><table><thead><tr><th>What the data shows</th><th>Why it matters for solar</th></tr></thead><tbody>
<tr><td>Summer daytime demand, weekdays and weekends</td><td>Sets how much output you can use. About three quarters of a year's solar output comes from April to September.{ref(6)}</td></tr>
<tr><td>Base load</td><td>What's running on a sunny Sunday afternoon. On a hospital it's high, which is why so little is exported.</td></tr>
<tr><td>Chiller load on hot afternoons</td><td>Cooling peaks line up with peak solar, so solar trims the year's highest import.</td></tr>
<tr><td>CHP running hours</td><td>While a CHP engine runs, there's less import for solar to replace. Plan for the site after the engine goes.</td></tr>
<tr><td>Peaks against agreed capacity</td><td>Background for the DNO's G99 assessment, and headroom for heat pumps later.</td></tr>
<tr><td>Separately metered clinics and offices</td><td>These close, so they export more. Size them on their own data.</td></tr>
</tbody></table></div>

<h2 id="example">A worked example: a community hospital</h2>
<p>Our <a href="example-hospital-analysis.html">example hospital</a> used {USE:,} kWh over the year analysed. In summer, between 10:00 and 16:00, it averages about 205 kW on weekdays and 147 kW at weekends. Here is the analyser's estimate at four system sizes, at UK average output (905 kWh per kWp). Values are first-year, at 25p/kWh for solar used on site and 5p/kWh for export. "Covers" is the share of the hospital's electricity the solar supplies. "At 80%" is the same system valued with the calculator's default guess.</p>
<div class="table-wrap" tabindex="0" role="region" aria-label="Worked example by system size"><table><thead><tr><th>Size</th><th class="num">Output a year</th><th class="num">Used on site</th><th class="num">Covers</th><th class="num">Value</th><th class="num">At 80%</th></tr></thead><tbody>
{example_rows()}
</tbody></table></div>
<p>Two things stand out. Up to about 450 kWp, the default guess <strong>undersells</strong> the system: at 449 kWp the measured value is about {gbp(UNDER)} a year higher than the 80% figure. By 748 kWp the guess has flipped and <strong>oversells</strong>, and at 1,196 kWp it overstates the first-year value by about {gbp(OVER)} ({OVER_PCT}%). Few community hospitals have room for 1 MW, so for most sites the measured figure makes the case stronger, not weaker.</p>

<h2 id="how">From your data to a solar estimate</h2>
<ol>
<li><strong>Load a year of half-hourly data</strong> for each main meter into the <a href="analyser/">analyser</a>. It runs in your browser. Need the files? See <a href="get-your-data.html">getting half-hourly data</a>.</li>
<li><strong>Open the site's Solar tab.</strong> Add the postcode to set the sunshine for your area. The tab shows output, share used on site and share of the site's electricity at each size.</li>
<li><strong>Choose "Size solar for this site".</strong> The calculator opens with your figures. Draw the roofs and car parks on the map, and it sets the share used on site for the system that fits, then works out cost, savings and payback.</li>
</ol>
<p>Only the annual use, the share used on site at a dozen sizes and the postcode, if entered, are passed, after the # in the web address. See the <a href="privacy.html">privacy notice</a>.</p>

<h2 id="calculator">What the solar calculator does</h2>
<p>The <a href="{SOLAR_URL}">solar calculator</a> on this site uses the same method as the UK Solar Calculator, built by the same team.</p>
<ul>
<li><strong>Measures roofs and car parks</strong> from satellite imagery or dimensions you enter, for pitched and flat roofs, ground mounts and carports.{ref(1)}</li>
<li><strong>Estimates generation at your postcode</strong> from the SAP 10.3 regional sunshine data.{ref(1, 7)}</li>
<li><strong>Prices the system</strong> from UK benchmarks per kWp, including an inverter replacement in year 13.{ref(1)}</li>
<li><strong>Compares buying with a PPA</strong> over 25 years, and models a battery if you want one.{ref(1)}</li>
</ul>
{photo('hc-rooftop-solar-install', 'Two installers checking solar panels on a hospital roof', 'An estimate tells you whether to take the next step. A survey, a structural check and a DNO offer give you the real cost.')}

<h2 id="limits">What this can and cannot tell you</h2>
<p>The analyser's estimate uses a typical UK solar day scaled to your region and the UK's seasonal pattern. It doesn't know about cloudy weeks, shading from plant or neighbouring blocks, roof orientation, or changes you'll make, such as removing a CHP engine. Treat it as a planning figure. The calculator's results are estimates, not a quotation.{ref(1, 3)}</p>
{faq_section(FAQS)}
{sources(SRC)}'''

SIDE = f'''{toc(TOC)}
    <div class="side-cta"><strong>Size solar for your site</strong><p>Postcode, roof and energy price. Results in seconds, with a 25-year report.</p><a href="{CALC}" class="btn">Open the solar calculator</a></div>'''

END = f'''<section class="cta-strip">
  <div class="cta-strip-inner">
    <h2 class="cta-strip-title">Measure it, then size it</h2>
    <div class="cta-strip-btns">
      <a href="analyser/" class="btn btn-gold btn-lg">Upload HH data</a>
      <a href="{CALC}" class="btn btn-outline-white btn-lg">Open the solar calculator</a>
    </div>
    <p class="cta-strip-lead">Both are free, with no sign-up. Want to talk it through? <a href="{SOLAR_CONTACT}" style="color:inherit;text-decoration:underline">Get in touch</a>.</p>
  </div>
</section>'''


PAGES = [Page(
    FILE, 'Hospital solar sizing from half-hourly data | Hospital Energy Insights',
    'How much solar would a hospital use? Measure it from half-hourly data, with a worked community hospital example, then size and cost it in the solar calculator.',
    page_hero('Solar', 'Size hospital solar from how the site really runs',
              "A 24-hour site uses most of what solar generates. Your half-hourly data shows exactly how much, at every system size.",
              crumbs=CRUMBS, image='solar')
    + guide(MAIN, SIDE).replace('<div class="side-cta"><strong>Try it on your own data</strong>', '<div class="side-cta"><strong>Measure it from your data</strong>', 1)
    + END,
    crumbs=CRUMBS, faqs=FAQS, article=True, section='Core pages',
    summary='Sizing solar for hospitals from half-hourly data: why share used on site decides value, a worked community hospital example (99.8% used at 299 kWp, 54% at 1,196 kWp), and how the analyser passes the figure to the solar calculator.')]
