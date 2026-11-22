"""
The core pages: home, how it works, getting your data, FAQ, contact, thanks,
privacy and 404. Bodies are HTML; metadata for search and AI tools is added
in core_pages() at the bottom.

Written for a general business reader, in the voice of the team that runs the
site ("we"). Explain terms on first use; write as much as the reader needs.
"""
import kit
from kit import (UPDATED_MARK, CONTACT_EMAIL, CONTACT_NAME, OPERATOR, OPERATOR_URL, SOLAR_URL, APP, Page,
                 cta, photo, faq_section, guide, page_hero, related, updated_line, GUIDE_PDF, guide_download, sources)
from pages_data import GOV_OFFER

FORM_ENDPOINT = 'https://formspree.io/f/xeagedqj'  # The Half Hourly Insights Formspree form for now. Where submissions go is set in Formspree, not here, so no personal address is in the page code. Replace with this site's own form ID.

HOME = ('Home', 'index.html')
GUIDES = ('Guides', 'guides.html')

PAGES = {}

# ── HOME ────────────────────────────────────────────────────────────────
def _card(f, title, text, more='Read the guide'):
    from kit import link_card
    return link_card(f, title, text, more)


PAGES['index.html'] = ('Half-hourly electricity analysis and solar for healthcare estates | Hospital Energy Insights',
  'Free tools for NHS trusts, health boards and private hospitals: analyse half-hourly electricity data, check headroom for heat pumps, size solar from your own profile, and plan decarbonisation.',
  f"""<div class="hero-wrap">
<div class="hero-media" aria-hidden="true"><picture><img src="images/photos/hc-public-hospital-solar.jpg" srcset="images/photos/hc-public-hospital-solar-800.jpg 800w, images/photos/hc-public-hospital-solar.jpg 1448w" sizes="100vw" width="1448" height="1086" alt="" fetchpriority="high"></picture></div>
<section class="hero" aria-labelledby="hero-h">
  <div class="hero-copy">
    <p class="hero-audience">For NHS trusts, health boards and independent hospitals in England, Scotland and Wales</p>
    <h1 id="hero-h">Start your estate's decarbonisation plan with the data you already have</h1>
    <p class="hero-lead">Upload the half-hourly readings from your electricity meters. In about a minute you'll see each site's base load, day and night use, waste in clinics and offices, peaks against your agreed supply capacity, how much room there is for heat pumps, and how much solar each site would use.</p>
    <p class="hero-check">Free, with no sign-up. Your data stays on your computer. Not sure where to find it? <a href="get-your-data.html">Here's how</a>.</p>
    <div class="hero-points">
      <div><strong>Whole estate at once</strong><span>One file per meter, every site ranked</span></div>
      <div><strong>Heat pump headroom</strong><span>Winter peaks against agreed capacity</span></div>
      <div><strong>Solar from your profile</strong><span>Measured share used, passed to the calculator</span></div>
    </div>
  </div>
  <div class="start-card">
    <h2>Step 1: upload your HH data</h2>
    <p>An Excel or CSV file for each meter, ideally 12 months. All the common supplier layouts work.</p>
    <a href="analyser/" class="btn btn-gold btn-lg">Upload HH data</a>
    <p class="start-sample"><a href="sample-report.html">Or see a sample report first</a></p>
    <div class="start-result">
      <div class="k">Then size solar from it</div>
      <div class="big">90%+</div>
      <div class="small">of a well-sized system's output is often used on a 24-hour hospital site. Measure yours, don't guess it.</div>
    </div>
    <p class="or">Only want a quick solar estimate? <a href="solar-calculator.html">Open the solar calculator</a>.</p>
  </div>
</section>
</div>

<section class="section">
  <div class="section-inner">
    <div class="head-row">
      <h2 class="section-title">One journey, from meter data to a fundable project</h2>
      <p>Most estates already have half-hourly data: suppliers record it for billing. It is the evidence behind almost every decarbonisation decision, so the journey starts there.</p>
    </div>
    <div class="steps steps-5">
      <div><div class="step-head"><span class="step-n">1</span><span class="step-line"></span></div><h3>Upload</h3><p>Drag in one file per meter for every site. The analyser checks the readings, flags gaps and clock changes, and builds each site's year.</p></div>
      <div><div class="step-head"><span class="step-n">2</span><span class="step-line"></span></div><h3>Understand</h3><p>See base load, day and night use, out-of-hours use in clinics and offices, unusual days and lasting changes, priced at your rates.</p></div>
      <div><div class="step-head"><span class="step-n">3</span><span class="step-line"></span></div><h3>Check headroom</h3><p>Compare each supply's peaks with its agreed capacity, and test the load from heat pumps, EV chargers or switching off CHP.</p></div>
      <div><div class="step-head"><span class="step-n">4</span><span class="step-line"></span></div><h3>Size solar</h3><p>The Solar tab measures how much output each site would use, then opens the <a href="solar-calculator.html">solar calculator</a> with your figures to map roofs and car parks.</p></div>
      <div><div class="step-head"><span class="step-n">5</span><span class="step-line"></span></div><h3>Report</h3><p>Download PDF and Excel reports for each site and the whole estate, ready for a Green Plan update, a capital bid or a funding application.</p></div>
    </div>
  </div>
</section>

<section class="section band-mist">
  <div class="section-inner">
    <div class="head-row">
      <h2 class="section-title">The challenge estates teams face</h2>
      <p>Net zero dates are fixed, the money has changed shape, and buildings that never close have to keep running while their heat is replaced. <a href="healthcare-estates-decarbonisation.html" style="color:var(--blue);text-decoration:underline">Read the full picture</a>.</p>
    </div>
    <div class="reasons">
      <div><h3>Net zero by 2040</h3><p>NHS England aims for net zero by 2040 for the emissions it controls, NHS Scotland by 2040 with renewable heat by 2038, and NHS Wales has set 34% by 2030. <a href="nhs-net-zero-targets.html">Targets compared</a>.</p></div>
      <div><h3>Heat is the big one</h3><p>Gas boilers and CHP are usually the largest source of carbon. Replacing them means heat pumps, lower flow temperatures and new answers for steam and hot water. <a href="heat-decarbonisation.html">Heat decarbonisation</a>.</p></div>
      <div><h3>CHP no longer adds up on carbon</h3><p>With the grid factor at about 0.13 kg CO₂e per kWh, a typical gas CHP engine now emits more than grid electricity and a boiler. <a href="moving-away-from-chp.html">Moving away from CHP</a>.</p></div>
      <div><h3>The grid connection</h3><p>Heat pumps add winter load, and removing CHP adds its full output to grid import. Headroom decides what is possible, and when. <a href="hospital-electrical-capacity.html">Electrical capacity</a>.</p></div>
      <div><h3>Funding has changed</h3><p>No new PSDS money is being committed. Great British Energy, devolved schemes, PPAs and energy performance contracts fill some of the gap. <a href="decarbonisation-funding.html">Funding routes</a>.</p></div>
      <div><h3>Waste comes first</h3><p>Theatre ventilation, BMS schedules, lighting and steam losses are usually the cheapest carbon to remove, and make everything after smaller. <a href="hospital-energy-efficiency.html">Energy efficiency</a>.</p></div>
    </div>
  </div>
</section>

<section class="section privacy-band">
  <div class="section-inner">
    <h2 class="section-title">Built for NHS information governance</h2>
    <p class="section-lead">The analyser does all its work inside your web browser. Meter files are read on your own computer and are never sent to us or anyone else. There is no patient data involved, no account and no tracking.</p>
    <div class="reasons">
      <div><h3>Nothing uploaded</h3><p>No server is involved in the analysis. Once the page has loaded, you can disconnect from the internet and carry on working.</p></div>
      <div><h3>No account</h3><p>No sign-up, no email address needed to analyse, and no tracking cookies.</p></div>
      <div><h3>You keep the results</h3><p>Reports, spreadsheets and project files are saved to your computer. Save a project to come back to it later.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-inner split">
    <div>
      <span class="section-kicker">Who it's for</span>
      <h2 class="section-title">Estates, facilities and energy teams</h2>
      <p class="section-lead">Built for the people who run healthcare buildings and have to make the numbers work: estates and facilities managers, energy and sustainability managers, capital planning teams and finance. In the NHS and in independent hospital groups.</p>
      <ul class="ticks">
        <li><strong>Acute hospitals</strong>: base load, peaks and headroom on 24-hour supplies</li>
        <li><strong>Community and mental health sites</strong>: inpatient units beside clinics with set hours</li>
        <li><strong>Health centres and clinics</strong>: waste while closed, and solar sized for quiet weekends</li>
        <li><strong>Ambulance stations</strong>: capacity for fleet charging</li>
        <li><strong>Private hospitals</strong>: ESOS, SECR and NHS supplier carbon plans</li>
      </ul>
      <p style="margin-top:24px"><a href="sectors.html" class="btn btn-outline">What to look for in your setting</a></p>
    </div>
    <div>{photo('hc-strategy-meeting', 'An estates, finance and clinical team reviewing a hospital decarbonisation roadmap and site plans')}</div>
  </div>
</section>

<section class="section band-mist">
  <div class="section-inner">
    <div class="head-row">
      <h2 class="section-title">Guides</h2>
      <p>Plain answers to the questions estates teams ask, each sourced and dated.</p>
    </div>
    <div class="link-grid" style="margin-top:36px">
      {_card('healthcare-estates-decarbonisation.html', 'The estates challenge', 'Targets, heat, CHP, capacity and funding in one place, and where to start.')}
      {_card('moving-away-from-chp.html', 'Moving away from gas CHP', 'Why the carbon case changed, and the capacity effect of switching it off.')}
      {_card('solar-on-healthcare-estates.html', 'Solar on healthcare estates', 'Why 24/7 sites suit solar, and how to size it from your data.')}
    </div>
    <div class="home-more">
      <div><h3>Decarbonisation</h3><ul><li><a href="nhs-net-zero-targets.html">Net zero targets across the UK</a></li><li><a href="decarbonisation-funding.html">Funding routes after PSDS</a></li><li><a href="heat-decarbonisation.html">Heat decarbonisation</a></li><li><a href="hospital-electrical-capacity.html">Electrical capacity</a></li><li><a href="hospital-energy-efficiency.html">Energy efficiency</a></li><li><a href="estates-returns-and-benchmarking.html">ERIC, EFPMS and benchmarking</a></li></ul></div>
      <div><h3>Solar</h3><ul><li><a href="solar-calculator.html">The solar calculator</a></li><li><a href="solar.html">Sizing solar from half-hourly data</a></li><li><a href="solar-calculator-method.html">How the calculator works</a></li><li><a href="solar-cost.html">What solar costs</a></li><li><a href="solar-planning-and-grid.html">Planning and grid connection</a></li><li><a href="paying-for-solar.html">Paying for solar</a></li></ul></div>
      <div><h3>Your data</h3><ul><li><a href="get-your-data.html">Getting your half-hourly data</a></li><li><a href="base-load.html">Base load</a></li><li><a href="supply-capacity.html">Supply capacity and kVA</a></li><li><a href="reading-a-heatmap.html">Reading a heatmap</a></li><li><a href="non-energy-charges.html">Non-energy charges</a></li><li><a href="glossary.html">Glossary</a></li></ul></div>
    </div>
    <p style="margin-top:24px"><a href="guides.html" class="btn btn-outline">All guides</a></p>
  </div>
</section>

{cta('Want help with your results?', 'We can help turn the findings into a project: heat pump feasibility, solar design, funding applications and procurement routes.')}
""")

# ── HOW IT WORKS ────────────────────────────────────────────────────────
PAGES['how-it-works.html'] = ('How the hospital energy analyser works | Hospital Energy Insights',
  'How the free analyser turns hospital and health centre half-hourly data into findings: file checks, 24/7 and clinic presets, base load, headroom and solar.',
  page_hero('How it works', 'What the analyser does with your data',
            'From the file your supplier sends to the figures in the report, step by step. Every finding in the analyser also has a "show calculation and evidence" link with the full working.',
            crumbs=[HOME, ('How it works', 'how-it-works.html')], image='how-it-works') +
  guide(updated_line() + '''
<p class="answer">You load one half-hourly file per meter. The analyser checks the readings, applies the right calendar for each building (24/7 for inpatient sites, set hours for clinics and offices), measures base load and peaks, prices the patterns at your rates, tests headroom for new load such as heat pumps, and estimates how much solar each site would use. It runs in your browser, so the meter data never leaves your computer.</p>
''' + photo('hc-energy-control-room', 'An estates team in an energy monitoring room, with screens showing campus energy use, carbon and building performance', 'The analyser points to where and when. Someone who knows the site works out why.') + guide_download('Want the practical steps?') + '''

<h2 id="files">1. Loading the meter files</h2>
<p>Each file becomes a site. Most trusts and health boards have a file per main meter, and some have sub-meters for theatres, outpatients or an energy centre too. Excel (.xlsx, .xls) and CSV both work, in any of the three layouts suppliers and monitoring systems use: one day per row with 48 readings, one day per column, or one timestamped reading per row. The analyser shows how it read each file, including whether readings were kWh or kW and what it ignored. Files longer than a year are analysed over the last 12 months by default, while the trend charts use everything.</p>
<p>Meters behind the same connection, such as two incomers on one hospital, can be grouped so capacity is checked against their combined demand.</p>

<h2 id="checks">2. Checking the readings first</h2>
<p>Bad data makes confident-looking wrong answers, so the checks come before any figures:</p>
<ul>
<li>missing half hours are left out, never treated as zero</li>
<li>whole days of zeros, and two-hour runs of exact zeros inside normal days, are flagged as likely data faults</li>
<li>the two clock-change days and any duplicate dates are held back for you to review</li>
<li>isolated spikes far above the normal peak are listed</li>
</ul>
<p>Each site gets a Good, Check or Poor rating. You can exclude readings you know are wrong, with a note of why, and the note stays with the analysis.</p>

<h2 id="calendar">3. The right calendar for each building</h2>
<p>New sites start on the <strong>hospital preset</strong>: open around the clock, with 01:00 to 05:00 as a low-activity window in place of closed hours. Change health centres, outpatient buildings and offices to the <strong>clinic</strong> or <strong>office</strong> preset, then add evening clinics, Saturday sessions and closures. The calendar is marked unconfirmed until you check it, and findings that depend on it carry lower confidence until you do.</p>

<h2 id="base">4. Base load, and use while closed</h2>
<p><strong>Base load</strong> is the 5th percentile of valid half-hourly demand: the level the site stays above 95% of the time. On a hospital that's wards, ventilation, imaging, fridges and IT; it's usually the largest part of the bill. The analyser also charts it month by month, because a step that doesn't follow the weather is often a fault, such as a theatre ventilation setback that stopped working. See <a href="base-load.html">base load on healthcare sites</a>.</p>
<p><strong>Closed-hours excess</strong> applies to buildings that close. It's the electricity used outside opening hours above the base load, priced at your rates and split by weeknights, Saturdays, Sundays and bank holidays. Buildings are ranked by it, so the worst health centre gets looked at first. See <a href="out-of-hours-electricity.html">out-of-hours use</a>.</p>

<h2 id="costs">5. Costs and annual figures</h2>
<p>Costs use the unit rates you enter, flat or by time of day, and leave out standing, capacity and other fixed charges. They're what a pattern costs now, not a promised saving. Annual figures are scaled from the valid hours: marked indicative below about 11 months of good data, and withheld below six.</p>

<h2 id="findings">6. Findings, impact and confidence</h2>
<p>Every finding carries two ratings. <strong>Impact</strong> reflects its cost and share of use. <strong>Confidence</strong> reflects the data quality, how many comparable days there were and whether the calendar is confirmed. High impact with low confidence means check before you quote it to the board.</p>

<h2 id="capacity">7. Capacity and headroom</h2>
<p>Enter the agreed supply capacity in kVA from the bill and a power factor (0.95 if you don't know it). The analyser compares every half hour with it, keeps a safety margin, and reports the firm headroom: the constant extra load that fits in every half hour. You can then test a specific load, such as a 150 kW heat pump running October to April or EV chargers in the evening, and see how many half hours it would breach. It's an early screen; only the DNO can confirm capacity. See <a href="supply-capacity.html">supply capacity and headroom</a>.</p>

<h2 id="solar">8. Solar</h2>
<p>The Solar tab overlays a typical UK solar day, scaled to your region, on the site's own readings to estimate how much of a system's output the site would use at a dozen sizes. <strong>Size solar for this site</strong> opens the <a href="solar-calculator.html">solar calculator</a> with that summary, so you can draw the roofs and car parks and see cost, savings and payback. The readings themselves are never passed. See <a href="solar.html">sizing solar from half-hourly data</a>.</p>

<h2 id="limits">What it can't tell you</h2>
<ul>
<li>A main meter shows when electricity is used, not which plant uses it. Findings are things to check on site.</li>
<li>Import meters miss what a CHP engine or solar supplies. Load the generation meter as its own file to see total demand.</li>
<li>Gas and heat aren't analysed yet, and figures aren't weather-adjusted.</li>
<li>Carbon uses one conversion factor for the year, which you choose.</li>
</ul>
''' + related([('example-hospital-analysis.html', 'Worked example', 'The method applied to one hospital, step by step.'),
               ('base-load.html', 'Base load', 'The biggest part of most hospital bills.'),
               ('supply-capacity.html', 'Supply capacity', 'Headroom for heat pumps and EV charging.')]), '''    <nav class="toc" aria-label="On this page"><div class="toc-title">On this page</div><ol>
      <li><a href="#files">Loading the meter files</a></li><li><a href="#checks">Checking the readings</a></li><li><a href="#calendar">The right calendar</a></li><li><a href="#base">Base load and use while closed</a></li><li><a href="#costs">Costs and annual figures</a></li><li><a href="#findings">Findings</a></li><li><a href="#capacity">Capacity and headroom</a></li><li><a href="#solar">Solar</a></li><li><a href="#limits">What it can't tell you</a></li></ol></nav>''')
  + cta('Try it on your own data', "It's free, there's no sign-up, and nothing is uploaded."))

# ── GET YOUR DATA ───────────────────────────────────────────────────────
GET_DATA_FAQS = [
    ('Who holds half-hourly data for an NHS hospital?', 'The electricity supplier, always. Often also the trust\'s energy or estates team through an automatic monitoring system, the energy broker or bureau, and on PFI sites the project company or its facilities management provider.'),
    ('How much data should we ask for?', 'At least 12 months for every main meter, and up to three years if it exists. A full year captures both winter heating and summer cooling peaks.'),
    ('Is there a charge?', 'Business customers with a smart or advanced meter can ask for up to 12 months of historic data free of charge. Many suppliers also offer downloads in their online portals.'),
    ('Does the data contain patient information?', 'No. It is the electricity used by the site in each half hour, nothing more. The analyser also keeps it on your computer.'),
]

PAGES['get-your-data.html'] = ('How NHS sites get half-hourly electricity data',
  'Where hospitals, health centres and NHS estates teams find half-hourly electricity data: suppliers, monitoring systems, PFI providers, what to ask for and formats.',
  page_hero('Guide', 'Getting half-hourly data for your sites',
            "Your trust or health board almost certainly has this data already. The trick is knowing who holds it. Here's where to look and what to ask for.",
            crumbs=[HOME, GUIDES, ('Getting your half-hourly data', 'get-your-data.html')], image='get-your-data') +
  guide(updated_line() + '''
<p class="answer">For each main electricity meter, ask your supplier (or whoever manages your energy contract) for 12 months of half-hourly consumption in kWh, one file per meter, as Excel or CSV. If your estates team runs an energy monitoring or BMS system, it may already hold the same data and be quicker to export. On PFI hospitals, ask the project company or its facilities management provider.</p>

<h2 id="who">Who holds it in a healthcare organisation</h2>
<div class="table-wrap"><table><thead><tr><th>Who</th><th>What they usually have</th></tr></thead><tbody>
<tr><td>The electricity supplier</td><td>Settlement data for every half-hourly meter, often downloadable from a business portal</td></tr>
<tr><td>Your energy or procurement team, or a broker or bureau</td><td>Access to the supplier portal, and often a monitoring and targeting system with every meter in it</td></tr>
<tr><td>Estates and the BMS</td><td>Main and sub-meter data for theatres, energy centres, outpatient blocks and plant rooms</td></tr>
<tr><td>A PFI project company or FM provider</td><td>On PFI hospitals, often the supply contract and the meter data</td></tr>
<tr><td>Landlords such as NHS Property Services or Community Health Partnerships</td><td>Data for health centres where the landlord holds the supply</td></tr>
</tbody></table></div>
<p>Many NHS bodies buy electricity through public sector frameworks, so the supplier relationship may sit with a central procurement or energy team rather than estates. Start with whoever pays the bill.</p>

<h2 id="which">Which meters to ask for</h2>
<ul>
<li><strong>Every main import meter</strong> on each hospital site, including second incomers.</li>
<li><strong>Generation meters</strong> for any CHP engine or solar, so you can see true site demand, not just import.</li>
<li><strong>Sub-meters</strong> for theatres, imaging, energy centres or outpatient wings, if you have them. They make findings much more specific.</li>
<li><strong>Health centres, clinics and offices</strong> with half-hourly meters, which is where out-of-hours savings usually sit.</li>
</ul>
<p>The MPAN, the 13-digit supply number on the bill, identifies each meter. <a href="mpan-profile-class.html">How to read an MPAN</a>.</p>

<h2 id="ask">What to ask for</h2>
<div class="note"><strong>Example request</strong><br>Please send half-hourly consumption data (kWh) for the MPANs listed below, from [date] to [date], as one Excel or CSV file per meter, with one row per day and 48 half-hourly columns. Please name each file after the site.</div>
<ul>
<li><strong>One file per meter, named after the site.</strong> The analyser uses the file name as the site name.</li>
<li><strong>Twelve months minimum</strong>; up to three years shows trends and a before-and-after for past projects.</li>
<li><strong>kWh per half hour</strong> is best. kW works too, and the analyser says which it found.</li>
</ul>
<p><a href="downloads/half-hourly-data-request.docx" download><strong>Download a request letter template</strong></a> (Word), with spaces for your MPANs and dates.</p>

<h2 id="right">Your right to the data</h2>
<p>Since 1 December 2022, business customers with a smart or advanced (AMR) meter, and anyone they nominate, can ask their supplier for up to 12 months of historic smart meter data free of charge, in a machine-readable format. The supplier must reply within 10 working days.<sup><a href="#sources">1</a></sup> For supplier-specific routes, see our guides to <a href="half-hourly-data-british-gas.html">British Gas</a>, <a href="half-hourly-data-edf.html">EDF</a>, <a href="half-hourly-data-eon-next.html">E.ON Next</a>, <a href="half-hourly-data-npower-business-solutions.html">npower Business Solutions</a> and <a href="half-hourly-data-totalenergies.html">TotalEnergies</a>.</p>

<h2 id="formats">Formats the analyser reads</h2>
<p>Excel (.xlsx, .xls) or CSV, laid out as one day per row with 48 readings, one day per column, or one timestamped reading per row. Extra columns such as meter references are ignored. If a file can't be read, the analyser says why. To see what a good file looks like, <a href="samples/example-hospital.csv" download>download our example hospital file</a>.</p>
''' + guide_download('Got your files?') + '''

<h2 id="ig">Information governance</h2>
<p>Half-hourly electricity data records energy use, not people, so it contains no patient information. The analyser reads files on your own computer and uploads nothing. If your IG team wants the detail, share the <a href="privacy.html">privacy notice</a>.</p>

<h2 id="no-data">If a site has no half-hourly meter</h2>
<p>Ask the supplier whether the meter can be replaced with a smart or advanced meter that records half-hourly. Check whether the BMS or a monitoring system logs the main meter's pulse output. Monthly readings show the seasons, but not the nights, weekends and peaks this analysis depends on.</p>
''' + sources([GOV_OFFER]) + faq_section(GET_DATA_FAQS) + related([
    ('example-hospital-analysis.html', 'Worked example', 'What a year of data shows about one hospital.'),
    ('how-it-works.html', 'How the analyser works', 'What it does with your files, step by step.'),
    ('base-load.html', 'Base load', 'The first thing to look at on a 24-hour site.')]), '''    <nav class="toc" aria-label="On this page"><div class="toc-title">On this page</div><ol><li><a href="#who">Who holds it</a></li><li><a href="#which">Which meters</a></li><li><a href="#ask">What to ask for</a></li><li><a href="#right">Your right to the data</a></li><li><a href="#formats">Formats</a></li><li><a href="#ig">Information governance</a></li><li><a href="#no-data">No half-hourly meter</a></li></ol></nav>''')
  + cta('Got your files?', 'Load them now. It takes about a minute and the data stays on your computer.'))

# ── FAQ ─────────────────────────────────────────────────────────────────
FAQ = [
  ('Using the analyser', [
    ('Who is it for?', 'Estates, facilities, energy and sustainability teams in NHS trusts, health boards, integrated care boards, ambulance trusts and independent hospitals across England, Scotland and Wales. It works for any building with a half-hourly meter, but the settings, guides and examples are written for healthcare.'),
    ('Is this an NHS tool?', 'No. Hospital Energy Insights is independent and is not part of, or endorsed by, the NHS. It is run by Kinetic Energy Consulting. Our guides summarise and link to NHS, Scottish Government and Welsh Government policy.'),
    ('Will it work for a 24-hour hospital?', 'Yes. Use the hospital preset, which has no closed hours. The analysis then focuses on base load, day and night use, peaks against capacity and lasting changes. Give clinics and offices on the site their real opening hours.'),
    ('Is it really free?', "Yes. There's no charge, no account and no limit on the number of sites. If you'd like help acting on the results you can contact us, but there's no obligation."),
    ('Do I need to install anything?', "No. It runs in Chrome or Edge on a recent computer. It isn't designed for phones, because the charts need a larger screen."),
    ('How many sites can I load?', 'As many as your computer can handle. Each meter file becomes a site, and the analyser ranks them so you know which to look at first.'),
    ('Is there a user guide?', f'Yes. <a href="{GUIDE_PDF}" download>Download the user guide</a> (PDF). It takes you through getting your data, loading it, setting opening hours, reading the results, downloading reports and creating customer dashboards.'),
    ('Can I save my work?', 'Yes. Save a project file to your computer and open it again later. It contains the readings and all your settings, so store it as carefully as the original data.'),
    ('Will our information governance team approve it?', 'The analysis runs in your browser and nothing is uploaded, so no meter data leaves your computer, and half-hourly electricity data contains no patient information. Share the <a href="privacy.html">privacy notice</a> with your IG team if they want the details.'),
    ('How does the solar calculator get my data?', 'On a site\'s Solar tab, Size solar for this site opens the solar calculator with a summary: the site\'s annual use, the share of solar output it would use at a dozen system sizes, and the postcode if you entered one. They travel after the # in the web address, which browsers do not send to any server. The readings stay on your computer.'),
    ('Can I share results with a client or colleague?', "Yes. You can download a PDF report for one site or your whole portfolio, export to Excel, or create a customer dashboard. That's a password-protected copy of the analyser containing only their sites."),
  ]),
  ('Your data', [
    ('Is my data uploaded anywhere?', 'No. The analysis runs entirely in your web browser. Your meter files are read on your own computer and nothing is sent to us or anyone else. Once the page has loaded you can even disconnect from the internet and keep working. Our <a href="privacy.html">privacy notice</a> has the details.'),
    ('What data do I need?', 'Half-hourly electricity readings for each meter, ideally covering 12 months or more. <a href="get-your-data.html">Here is how to get them.</a>'),
    ('What if my file has gaps or errors?', 'The analyser finds them before showing any figures. Missing readings are left out rather than counted as zero, and days with zero readings or clock changes are flagged for you to decide on.'),
  ]),
  ('The results', [
    ('Are the costs savings?', 'No. They show what a pattern costs now at the rates you entered. Any saving depends on what you change. The savings estimates are clearly labelled as estimates.'),
    ('How accurate is it?', "It's as accurate as the data and opening hours you give it. Each finding shows a confidence rating and the evidence behind it, and each figure is labelled as measured or estimated."),
    ('Can it size heat pumps?', 'Not the heat side: that needs heat data and a designer. It does answer the electrical question first, by testing a heat pump\'s electrical load against each supply\'s winter peaks and agreed capacity. See <a href="hospital-electrical-capacity.html">electrical capacity</a>.'),
    ('Does it analyse gas?', 'Not yet. It reads electricity meter data. Gas and heat analysis is planned. Our <a href="heat-decarbonisation.html">heat decarbonisation guide</a> covers what to look at in the meantime.'),
    ('Can it tell me which equipment is wasting energy?', 'No. Data from the main meter shows when electricity is used, but not what is using it. The findings tell you when and where to look, and a visit to the building finds the cause.'),
  ]),
]
PAGES['faq.html'] = ('Questions and answers | Hospital Energy Insights',
  'Common questions about the free half-hourly analyser and solar calculator for healthcare estates: who it is for, privacy and IG, 24-hour sites, solar, and what the results mean.',
  page_hero('FAQ', 'Questions and answers', 'If your question isn\'t answered here, <a href="contact.html">ask us</a>.', image='faq') +
  '<section class="section"><div class="section-inner" style="max-width:820px">'
  '<p class="answer">Hospital Energy Insights is a free half-hourly electricity analyser and solar calculator for NHS and independent healthcare estates across the UK, with guides to decarbonising the estate. '
  'The analyser runs in your web browser, so your meter files are never uploaded. You need one Excel or CSV file per meter, ideally covering 12 months.</p>' +
  ''.join(f'<h2 class="faq-group">{g}</h2><div class="faq">' + ''.join(
      f'<details><summary>{q}</summary><div class="faq-a"><p>{a}</p></div></details>' for q, a in items) + '</div>'
          for g, items in FAQ) +
  '</div></section>' + cta('Still have a question?', 'Try the analyser with the example file, or get in touch.'))

# ── CONTACT ─────────────────────────────────────────────────────────────
PAGES['contact.html'] = ('Contact | Hospital Energy Insights',
  'Talk to an energy expert about your half-hourly results, heat pump headroom, solar on your estate, funding or reducing waste across your sites.',
  page_hero('Contact', 'Talk to an expert',
            "The analyser and calculator show you where to look. If you'd like help turning the findings into projects, tell us about your estate and we'll be in touch. There's no obligation.",
            image='contact') +
  f'''<section class="section"><div class="section-inner contact-grid">
<div class="contact-info">
  <a href="{OPERATOR_URL}" target="_blank" rel="noopener noreferrer" class="kec-logo-link">
    <span class="kec-sponsored-by">Sponsored by</span>
    <img src="images/kec-logo.svg" alt="{OPERATOR}" class="kec-logo-img" width="220" height="105">
  </a>
  {photo('contact-photo', 'A laptop showing an electricity demand chart on a desk, beside a printed report and a notebook')}
  <h2>{CONTACT_NAME}</h2>
  <p>Managing Director of {OPERATOR}. <a href="about.html">About Paul, and why the analyser is free</a>.</p>
  <p>Get in touch to talk through your results, or for help with heat pump feasibility, solar design, funding applications or reducing waste across your estate. We aim to reply within one working day.</p>
  <dl class="contact-details">
    <div><dt>Email</dt><dd><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></dd></div>
    <div><dt>Response time</dt><dd>Within 1 working day</dd></div>
    <div><dt>Coverage</dt><dd>Across the UK</dd></div>
  </dl>
</div>
<form class="form" id="enquiry" method="POST" action="{FORM_ENDPOINT}">
  <input type="hidden" name="_subject" value="New Hospital Energy Insights enquiry">
  <input type="hidden" name="site" value="Hospital Energy Insights">
  <input type="hidden" name="from_page" id="fromPage" value="">
  <p class="hp"><label>Leave this empty <input name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
  <div class="form-row">
    <div><label for="name">Name <span class="req">*</span></label><input id="name" name="name" autocomplete="name" required></div>
    <div><label for="email">Email <span class="req">*</span></label><input id="email" name="email" type="email" autocomplete="email" required></div>
  </div>
  <div class="form-row">
    <div><label for="org">Organisation</label><input id="org" name="organisation" autocomplete="organization"></div>
    <div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
  </div>
  <div class="form-row">
    <div><label for="sector">Sector</label><select id="sector" name="sector"><option value="">Choose one</option><option>NHS trust (England)</option><option>Health board (Scotland)</option><option>Health board or trust (Wales)</option><option>Integrated care board</option><option>Ambulance trust</option><option>Independent or private hospital</option><option>Primary care or health centre</option><option>Other</option></select></div>
    <div><label for="sites">Number of sites</label><select id="sites" name="sites"><option value="">Choose one</option><option>1</option><option>2 to 10</option><option>11 to 50</option><option>More than 50</option></select></div>
  </div>
  <div><label for="message">How can we help? <span class="req">*</span></label><textarea id="message" name="message" required placeholder="For example: we ran our acute and community sites through the analyser and would like help with heat pump headroom and solar on two car parks."></textarea>
  <p class="help">Please don't paste meter data here. If we need it, we'll agree a secure way to share it.</p></div>
  <label class="check"><input type="checkbox" name="consent" value="yes" required> <span>I agree to you storing these details to reply to my enquiry, as set out in the <a href="privacy.html" style="color:var(--blue);text-decoration:underline">privacy notice</a>. <span class="req">*</span></span></label>
  <p class="form-error" role="alert" hidden></p>
  <div><button class="btn btn-gold btn-lg" type="submit">Send enquiry</button></div>
  <p class="help">If the form doesn't work for you, email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> instead. Please don't attach meter files.</p>
</form>
</div></section>
<script>
// Send the enquiry to Formspree, then show our own thank-you page.
// Without JavaScript the form posts to Formspree directly.
// Record which page on this site the visitor came from, so enquiries can be traced to a guide. Other sites are ignored.
try {{ const r = new URL(document.referrer); if (r.origin === location.origin) document.getElementById('fromPage').value = r.pathname; }} catch (_) {{}}
document.getElementById('enquiry').addEventListener('submit', async (e) => {{
  e.preventDefault();
  const form = e.target, btn = form.querySelector('button[type=submit]'), err = form.querySelector('.form-error');
  btn.disabled = true; btn.textContent = 'Sending…'; err.hidden = true;
  try {{
    const res = await fetch(form.action, {{ method: 'POST', body: new FormData(form), headers: {{ Accept: 'application/json' }} }});
    if (res.ok) {{ window.location.href = 'thanks.html'; return; }}
    const data = await res.json().catch(() => ({{}}));
    err.textContent = (data.errors || []).map((x) => x.message).join(' ') || 'Something went wrong. Please try again, or email us instead.';
  }} catch {{
    err.textContent = 'We could not send your enquiry. Please check your connection and try again, or email us instead.';
  }}
  err.hidden = false; btn.disabled = false; btn.textContent = 'Send enquiry';
}});
</script>''')

PAGES['thanks.html'] = ('Thank you | Hospital Energy Insights', 'Your enquiry has been sent.',
  page_hero('Contact', 'Thank you', 'Your enquiry has been sent. We\'ll reply by email, usually within one working day.',
            '\n    <a href="analyser/" class="btn btn-gold btn-lg">Back to the analyser</a>'),
  '  <meta name="robots" content="noindex">\n')

# ── PRIVACY ─────────────────────────────────────────────────────────────
PAGES['privacy.html'] = ('Privacy | Hospital Energy Insights',
  'How Hospital Energy Insights handles your data: meter files never leave your computer, and enquiry details are only used to reply.',
  page_hero('Privacy', 'Privacy notice', 'In short, your meter data never leaves your computer. If you contact us, we only use your details to reply.') +
  guide(f'''
<h2 id="analyser">The analyser</h2>
<p>The analyser runs entirely in your web browser. Meter files you load are read on your own computer. They are never uploaded and we never see them. The same goes for everything you enter (opening hours, rates, notes) and everything you download (PDFs, spreadsheets, project files and customer dashboards).</p>
<p>If you choose "Size solar for this site" on a site's Solar tab, the analyser opens this site's solar calculator in a new tab. It passes only that site's annual use, the estimated share of solar output used on site and, if you entered one on the Solar tab, the site postcode, in the part of the web address after "#", which browsers do not send to any server. Your readings are not passed. The calculator uses the postcode to set the sunshine for your area and to fill in its map search; it is sent to Google Maps only if you then choose to search the map there.</p>

<h2 id="calculator">The solar calculator</h2>
<p>The solar calculator also runs in your browser and remembers your last inputs in your browser's local storage, so they are there when you come back. If you use the map, your address search and the map view are handled by Google Maps, whose own privacy policy applies. If you ask for the PDF report by email, we receive the email address you enter and the headline figures of your estimate, sent through EmailJS, and we email you a summary. We use your email only to send the report and, if you reply, to follow up your enquiry. {OPERATOR} is the data controller; we keep these details for 24 months from our last contact with you, unless you ask us to delete them sooner.</p>
<p>The analyser stores nothing in your browser between visits. Save a project file if you want to come back to your work.</p>

<h2 id="editions">If you create a customer edition</h2>
<p>Before the analyser makes a customer edition (a locked dashboard for handing to someone else), it asks for your name, your organisation and your work email, and whether you would like to hear about licences and updates. It sends those details to us by email, with the number of sites in the edition and the date. It does not send the meter data, the site names, any figures or anything else in the file.</p>
<p>We ask because customer editions are how dashboards are handed to others, and using the analyser to produce work for clients needs a licence under our <a href="terms.html">terms of use</a>. We use the details to know who uses the feature and to contact you about licensing, which is in our legitimate interests. If you tick the box, we will also tell you about licences and updates, with your consent, which you can withdraw at any time by emailing us.</p>
<p>{OPERATOR} is the data controller. The details are sent through EmailJS, an email-sending service, which passes them to our inbox. EmailJS may process data outside the UK; its own privacy policy explains how. We keep these details for 24 months from our last contact with you and then delete them, unless we have to keep them for a legal reason. You can ask us to delete them sooner at any time.</p>

<h2 id="enquiries">Enquiries</h2>
<p>If you send the contact form, we receive the details you enter: your name, email, organisation, phone, sector, number of sites and message, plus the page on this site you came to the form from. We only use them to reply to your enquiry and any follow-up you ask for. We don't sell them or add you to a mailing list.</p>
<p>{OPERATOR} is responsible for the details you send (the data controller). The form is sent through Formspree, a form-handling service, which emails your enquiry to us and keeps a copy in our Formspree account on our behalf. Formspree may process data outside the UK; its own privacy policy explains how.</p>
<p>We keep enquiry details only for as long as we need them to deal with your enquiry and any follow-up you ask for. We then delete them, from our email and from Formspree, unless we have to keep them for a legal reason. You can ask us to delete them sooner at any time.</p>

<h2 id="cookies">Cookies and tracking</h2>
<p>This site sets no cookies and runs no advertising or tracking scripts. Every download from the analyser (PDFs, spreadsheets, chart images and customer editions) is marked "Made with Hospital Energy Insights", but that is printed in the file; it does not track you. Fonts are served from this site rather than a third party.</p>

<h2 id="rights">Your rights</h2>
<p>You can ask what we hold about you, and ask us to correct or delete it, by emailing <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>. You can also complain to the Information Commissioner's Office (ico.org.uk).</p>
'''))

# ── TERMS OF USE ────────────────────────────────────────────────────────
# Plain-English terms. Have them reviewed by a solicitor before relying on them.
PAGES['terms.html'] = ('Terms of use | Hospital Energy Insights',
  'Hospital Energy Insights is free for your own organisation. Using it to produce reports, dashboards or advice for clients needs a licence.',
  page_hero('Terms', 'Terms of use', 'Free for your own organisation. If you use it to produce work for clients, you need a licence.') +
  guide(f'''
<p class="byline">Last updated {UPDATED_MARK}</p>
<p class="answer">You can use Hospital Energy Insights free of charge to analyse your own organisation's electricity data. If you use it to produce reports, dashboards or advice for other organisations, as part of paid work or to win it, you need a licence from us.</p>

<h2 id="who">Who we are</h2>
<p>Hospital Energy Insights (hospitalenergyinsights.co.uk) is run by {OPERATOR}. See <a href="about.html">about us</a>. These terms apply to the website, the analyser and everything you download from it.</p>

<h2 id="free">Free use</h2>
<p>Any organisation can use the analyser, the guides and the downloads free for its own sites and buildings. That includes energy and estates managers, finance teams and facilities staff analysing their own organisation's data, and sharing the reports, spreadsheets and customer editions within their organisation and with its own board, landlord or auditors.</p>

<h2 id="licence">Work for clients needs a licence</h2>
<p>If you are a consultant, broker, supplier, installer or anyone else using the analyser to produce reports, dashboards, customer editions or advice for another organisation, as part of paid work or to win it, you need a licence. That includes handing a customer edition or a PDF from the analyser to a client. <a href="contact.html">Contact us</a> about a licence.</p>

<h2 id="attribution">Keep our name on what you download</h2>
<p>Every PDF page, spreadsheet, chart image and customer edition made with the analyser is marked "Made with Hospital Energy Insights" with this website's address. Do not remove, hide or change that marking, or present the output as made by another tool, unless your licence allows it.</p>

<h2 id="copying">Copying the site</h2>
<p>Do not copy the analyser or this website, in whole or in part, to offer a similar service, and do not resell access to it.</p>

<h2 id="estimates">Estimates, not advice</h2>
<p>Results are estimates from the data you load and the settings you enter. Costs are energy cost at the rates entered, not guaranteed savings, and the guides are general information, not financial, tax or legal advice. Check anything important before you rely on it. We are not responsible for decisions made on the results, but nothing in these terms limits liability that the law does not allow us to limit.</p>

<h2 id="data">Your data</h2>
<p>Your meter data stays on your computer. The <a href="privacy.html">privacy notice</a> explains the few things we do receive, such as contact form enquiries and the details asked for when you create a customer edition.</p>

<h2 id="changes">Changes and law</h2>
<p>We may update these terms; the date at the top shows the latest version. These terms are governed by the law of England and Wales.</p>
'''))

# ── SAMPLE REPORT ───────────────────────────────────────────────────────
# Figures are the office worked example (site/samples/example-office.csv) as
# the analyser reports them. Keep the two pages in step.
PAGES['sample-report.html'] = ('Sample half-hourly electricity report for an office',
  'A sample half-hourly electricity report for a made-up UK office: use while closed, base load, findings and what could be saved.',
  page_hero('Sample report', 'What a report looks like',
            'See the kind of results the analyser produces before you find your own meter data. This is a made-up office with made-up readings.',
            crumbs=[HOME, ('Sample report', 'sample-report.html')]) +
  f'''<section class="section"><div class="section-inner sample">
<div class="note"><strong>Made-up example.</strong> The office and its meter readings are invented, so nothing here is a real customer's result. Every figure is what the analyser reports for our example file, at an illustrative 25p/kWh.</div>

<p class="answer">This made-up office used 79,191 kWh of electricity in a year, costing about £19,798 at 25p/kWh. A third of it (33%) was used while the office was closed. Use above the base load during those closed hours costs about £2,776 a year, almost half of it on Saturdays.</p>

<h2 class="section-title">The year at a glance</h2>
<p class="section-lead">A small office, open 07:00 to 19:00 on weekdays, with 363 days of valid readings.</p>
<div class="stat-grid">
  <div><strong>79,191 kWh</strong><span>electricity used in the year, costing about £19,798</span></div>
  <div><strong>33%</strong><span>of it used while the office was closed</span></div>
  <div><strong>2.6 kW</strong><span>base load: what never switches off</span></div>
  <div><strong>£2,776</strong><span>a year spent on use while closed, above the base load</span></div>
</div>

<figure class="figure"><img src="images/heatmap-office.png" width="2464" height="896" alt="Heatmap of the office year: a dark weekday band, pale nights, and some busy Saturdays" loading="lazy"><figcaption>Every half hour of the year on one chart: one column per day, darker for higher demand. The weekday band is clear, and some Saturdays are as busy as weekdays.</figcaption></figure>

<h2 class="section-title">What the analyser found</h2>
<div class="finding-grid">
  <article class="finding">
    <span class="finding-tag high">High impact</span>
    <h3>Use while closed</h3>
    <p class="finding-value">£2,776 a year</p>
    <p>11,035 kWh used outside opening hours, above the base load. Almost half of it (5,155 kWh) is on Saturdays; weekday evenings and nights add 3,750 kWh.</p>
    <p><strong>What to check:</strong> whether the office is used on Saturdays, and the heating and ventilation schedules.</p>
  </article>
  <article class="finding">
    <span class="finding-tag medium">Medium impact</span>
    <h3>Bank holidays like working days</h3>
    <p class="finding-value">7 bank holidays</p>
    <p>Seven bank holidays, including Christmas Day, used at least 80% of a normal weekday's electricity (1,408 kWh above base load in all).</p>
    <p><strong>What to check:</strong> whether the building controls know about bank holidays.</p>
    <p class="finding-note">Already included in the £2,776.</p>
  </article>
  <article class="finding">
    <span class="finding-tag low">Low impact</span>
    <h3>Early starts and late finishes</h3>
    <p class="finding-value">£629 a year</p>
    <p>About 1,250 kWh above base load in the two hours before opening, and the same again in the two hours after closing.</p>
    <p><strong>What to check:</strong> timer and heating start-up settings.</p>
    <p class="finding-note">Already included in the £2,776.</p>
  </article>
</div>
<p>The smaller findings are parts of the £2,776, not extra to it, so don't add them up. The base load is separate: 2.6 kW running all year costs about £5,700.</p>

<h2 class="section-title">What could actually be saved?</h2>
<p>The figures above are what each pattern costs now. They are not a promised saving. What you save depends on what you change, and some of that closed-hours use may turn out to be needed, such as a regular Saturday team. The way to find out is to:</p>
<ol class="sample-steps">
  <li><strong>Confirm the opening hours.</strong> If Saturdays are planned working days, much of the £2,776 is normal use.</li>
  <li><strong>Walk round the building</strong> on a Saturday and after closing time, and note what's switched on.</li>
  <li><strong>Change one setting at a time</strong>, such as the heating schedule or bank holiday calendar.</li>
  <li><strong>Compare the weeks before and after</strong> with the analyser's before-and-after view. That gives you a measured saving rather than an estimate.</li>
</ol>

<div class="sample-cta">
  <a class="btn btn-gold btn-lg" href="analyser/">Analyse my own data</a>
  <a class="btn btn-outline btn-lg" href="samples/example-office.csv" download>Download the example file</a>
</div>
<p>For the same office explained figure by figure, see the <a href="{kit.HHI_SITE}example-office-analysis">office worked example</a> on our sister site, Half Hourly Insights. For a hospital, read our <a href="example-hospital-analysis.html">community hospital worked example</a>. To understand your own figures, see <a href="how-it-works.html">how the analyser works</a>.</p>
</div></section>''' + cta('Ready to see your own results?', 'Load your half-hourly meter file. It takes about a minute and your data stays on your computer.'))

PAGES['404.html'] = ('Page not found | Hospital Energy Insights', 'This page does not exist.',
  page_hero('404', 'Page not found', 'That page doesn\'t exist. Try the home page or open the analyser.',
            '\n    <a href="index.html" class="btn btn-gold btn-lg">Home</a>'),
  '  <meta name="robots" content="noindex">\n')





# ── ABOUT ───────────────────────────────────────────────────────────────
PAGES['about.html'] = ('About Hospital Energy Insights and Paul Johnston',
  'Who runs Hospital Energy Insights, the experience behind it, why the analyser and solar calculator are free, and how we write and check our guides.',
  page_hero('About', 'About Hospital Energy Insights',
            f'Hospital Energy Insights is run by {OPERATOR}. Here is who we are, why the analyser is free, and how we keep the guides accurate.',
            crumbs=[HOME, ('About', 'about.html')]) +
  f'''<section class="section"><div class="section-inner about">
<p class="answer">Hospital Energy Insights is a free half-hourly analyser, solar calculator and set of guides for NHS and independent healthcare estates. It is run by {OPERATOR}, whose Managing Director is Paul Johnston, and brings together the team's Half Hourly Insights analyser and UK Solar Calculator in one journey built for estates teams. It is independent, and not part of or endorsed by the NHS.</p>

<div class="about-person" id="paul-johnston">
  <img src="images/people/paul-johnston.jpg" width="480" height="600" alt="Paul Johnston, Managing Director of {OPERATOR}" loading="lazy">
  <div>
    <h2>Paul Johnston</h2>
    <p class="about-role">Managing Director, {OPERATOR}</p>
    <p>Paul has spent his career in the UK energy market. He has worked for some of the largest energy suppliers in the country and with private-equity-backed start-ups building new energy businesses.</p>
    <p>Working at that scale showed him how much useful information the industry collects about how businesses use electricity, and how little of it reaches the people who could act on it. Working with start-ups showed him how much can change when that information is put in front of the right person in a form they can use.</p>
    <p>Healthcare estates are where that gap matters most: buildings that never close, fixed net zero dates and grid connections that take years to change. He set up Hospital Energy Insights to put the evidence in front of the estates teams who have to act on it, and writes and reviews the guides on this site.</p>
    <p><a href="contact.html">Contact Paul</a></p>
  </div>
</div>

<h2 id="free">Why the analyser is free</h2>
<p>Most NHS trusts and health boards already have half-hourly electricity data. Their supplier records it every half hour, and it is used for billing. It rarely reaches the estates manager, the energy manager or the capital planning group, who are the people who could use it to cut waste and plan decarbonisation.</p>
<p>We built the analyser so anyone can load that data and, within a minute, see when their buildings use electricity, how close each supply is to its limit, and how much solar each site would use. Often the first changes cost nothing: a ventilation schedule, a BMS timer, a holiday calendar for a clinic.</p>
<p>It is free because that is the most useful way to start. Some organisations will act on the results themselves, and that is fine. Others will want help going further, and that is the work {OPERATOR} does. There is no sign-up and no obligation. Because the analysis runs in your web browser, we never see your data unless you choose to send it to us.</p>

<h2 id="how">How we write the guides</h2>
<ul>
<li><strong>Every figure has a source.</strong> Guides cite the primary source, such as NHS England, the Scottish and Welsh Governments, Ofgem, the UK government or the supplier concerned, with a date.</li>
<li><strong>Examples are labelled.</strong> Our worked examples use made-up buildings and say so. Every figure in them is what the analyser actually reports.</li>
<li><strong>Costs are not savings.</strong> We show the cost of a pattern of use, not a promised saving, and say when findings overlap.</li>
<li><strong>Pages are dated.</strong> Each guide shows when it was last updated. Rates and prices are reviewed every April.</li>
<li><strong>Corrections are welcome.</strong> If something is wrong or out of date, <a href="contact.html">tell us</a> and we will fix it.</li>
</ul>
</div></section>''' + cta('See what your data shows', "It's free, there's no sign-up, and your file stays on your computer."))


def core_pages():
    """The pages above, with breadcrumbs, schema and llms.txt lines."""
    home = ('Home', 'index.html')
    meta = {
        'index.html': dict(schema=[APP], section='Core pages',
                           summary='Free half-hourly analyser and solar calculator for NHS and independent healthcare estates: upload HH data, see base load, peaks and heat pump headroom, size solar from the measured profile, download reports; analysis runs in the browser.'),
        'how-it-works.html': dict(crumbs=[home, ('How it works', 'how-it-works.html')], article=True, section='Core pages',
                                  summary='The method in full: reading files, data checks, opening hours (hospital 24-7 preset), base load (5th percentile), closed-hours excess, costs, annualisation, findings, capacity and headroom, solar hand-off, and limits.'),
        'get-your-data.html': dict(crumbs=[home, ('Guides', 'guides.html'), ('Getting your half-hourly data', 'get-your-data.html')],
                                   article=True, faqs=GET_DATA_FAQS, section='Guides',
                                   summary='Who holds half-hourly data, what to ask your supplier for, the file layouts the analyser reads, and what to do if your supplier cannot provide it.'),
        'faq.html': dict(crumbs=[home, ('FAQ', 'faq.html')], faqs=[qa for _, items in FAQ for qa in items], section='Core pages',
                         summary='Who it is for, not an NHS tool, 24-hour sites, information governance, the solar hand-off, heat pumps, gas, cost, privacy and what the results mean.'),
        'contact.html': dict(crumbs=[home, ('Contact', 'contact.html')], section='Core pages',
                             summary=f'Enquiries to {OPERATOR}, which runs the site.'),
        'thanks.html': dict(noindex=True),
        'privacy.html': dict(crumbs=[home, ('Privacy', 'privacy.html')]),
        'terms.html': dict(crumbs=[home, ('Terms of use', 'terms.html')]),
        'sample-report.html': dict(crumbs=[home, ('Sample report', 'sample-report.html')], section='Core pages',
                                   summary='A sample report for a made-up office: 33% of use while closed, £2,776 a year above base load, base load 2.6 kW, findings and what could be saved.'),
        '404.html': dict(noindex=True),
        'about.html': dict(crumbs=[home, ('About', 'about.html')], section='Core pages',
                           summary=f'Who runs the site ({OPERATOR}, Managing Director Paul Johnston), why the analyser is free, and how the guides are sourced and checked.'),
    }
    out = []
    for file, (title, desc, body, *extra) in PAGES.items():
        extra_head = (extra[0] if extra else '').replace('  <meta name="robots" content="noindex">\n', '')
        out.append(Page(file, title, desc, body, extra_head=extra_head, **meta.get(file, {})))
    return out
