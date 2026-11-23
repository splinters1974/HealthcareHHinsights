"""
Guides and sector pages. Each guide opens with a direct answer (what search
and AI answer engines quote), carries a few questions marked up as FAQPage,
and ends with links to related guides.

Written for a general business reader: plain words, terms explained on first
use, as long as it needs to be and no longer. "Closed-hours excess" is the
analyser's figure; "out-of-hours use" is the general idea.

Figures in the worked example come from the analyser run on
site/samples/example-hospital.csv (made-up data).
Re-check them if those files or the engine change.
"""
import re

import kit

from kit import (NAV_PARENT, SOLAR_URL, Page, cta, link_card, faq_section, guide, page_hero, photo, related, sources, strip_tags, toc,
                 updated_line)

HOME = ('Home', 'index.html')
GUIDES = ('Guides', 'guides.html')
SECTORS = ('Site types', 'sectors.html')
SOLAR = f'<a href="{SOLAR_URL}">solar calculator</a>'
S_NETB = ('NHS England: NHS Estates Technical Bulletin 2026/1, generating energy efficiency savings through controlling theatre ventilation (July 2026)',
          'https://www.england.nhs.uk/wp-content/uploads/2026/07/PRN02301-netb-2026-1-energy-savings-in-theatres-v1.1.pdf')


def ref(*n):
    return f'<sup><a href="#sources">{",".join(str(x) for x in n)}</a></sup>'


def guide_page(file, title, h1, lead, description, main, toc_items, faqs, next_links, summary, crumbs=None):
    crumbs = crumbs or [HOME, GUIDES, (h1, file)]
    NAV_PARENT[file] = crumbs[1][1]
    body = (page_hero(crumbs[1][0] if crumbs[1] != GUIDES else 'Guide', h1, lead, crumbs=crumbs, image=file[:-5])
            + guide(updated_line() + main + faq_section(faqs) + related(next_links), toc(toc_items + [('questions', 'Questions people ask')]))
            + cta('Try it on your own data', "It's free, there's no sign-up, and your file stays on your computer."))
    return Page(file, title, description, body, crumbs=crumbs, faqs=faqs, article=True, summary=summary,
                section='Guides' if crumbs[1] == GUIDES else 'Sectors')


PAGES = []

# ── WORKED EXAMPLE ──────────────────────────────────────────────────────
# Figures: the analyser run on site/samples/example-hospital.csv (made up) with
# the 24/7 hospital preset, 25p/kWh, 400 kVA agreed capacity, power factor 0.95
# and a 10% margin. Locked in analyser/tests/website-claims.test.ts.
PAGES.append(guide_page(
  'example-hospital-analysis.html',
  'Worked example: a year of HH data from a community hospital',
  'Worked example: a community hospital, one year',
  'We ran a year of half-hourly electricity data from a 60-bed community hospital through the analyser. The hospital and its readings are made up, but every figure below is what the analyser reports for that file.',
  'A year of half-hourly data from a community hospital: base load, a ventilation fault, summer peaks, heat pump headroom and how much solar it would use.',
  f'''
<p class="answer">This hospital spends about £211,000 a year on load that never switches off, and from September that load jumped by about 22 kW when the theatre ventilation stopped setting back at night. Fixing it is worth roughly £31,000 a year. The supply has room for a 100 kW heat pump through the winter but not a 150 kW one, and the site would use almost every unit from a solar system of up to about 300 kWp.</p>

<div class="note"><strong>Made-up data.</strong> We invented this hospital so we could show the method without using anyone's real data. <a href="samples/example-hospital.csv" download>Download the file</a> and load it into the <a href="analyser/">analyser</a> to follow along. It opens on the 24/7 hospital preset, which is right for this site. Enter 400 kVA as the agreed supply capacity to match the figures below.</div>

<h2 id="site">The site</h2>
<p>A community hospital with 60 inpatient beds, an outpatients wing and two day-surgery theatres, on one half-hourly meter. Wards, kitchens, IT and ventilation run around the clock. Outpatients and theatres run 08:00 to 18:00 on weekdays. Chillers add load on summer afternoons. The standby generators are tested on load for an hour on the first Tuesday of each month, which takes the site off the grid while they run.</p>

<h2 id="headline">The headline figures</h2>
<div class="table-wrap"><table><thead><tr><th>Measure</th><th class="num">Value</th><th>What it means</th></tr></thead><tbody>
<tr><td>Electricity a year</td><td class="num">1,350,066 kWh</td><td>Scaled from 363 days of valid readings (99.5% coverage). The two clock-change days are held back.</td></tr>
<tr><td>Energy cost a year</td><td class="num">£337,517</td><td>At a flat 25p/kWh, before standing and capacity charges</td></tr>
<tr><td>Base load</td><td class="num">96.3 kW</td><td>The level demand rarely falls below across the whole year</td></tr>
<tr><td>Share that is base load</td><td class="num">63%</td><td>About £211,000 a year of continuous load</td></tr>
<tr><td>Busiest half hour</td><td class="num">288.6 kW</td><td>16 July 2024 at 16:30, in a hot spell</td></tr>
<tr><td>Against supply capacity</td><td class="num">76%</td><td>About 304 kVA of a 400 kVA agreed capacity</td></tr>
</tbody></table></div>
<p>A hospital never closes, so there is no "out-of-hours" figure here. The 24/7 preset uses 01:00 to 05:00 as a low-activity window instead. On a site like this, the questions that matter are what's in the base load, whether it's moving, and how much room is left on the connection for heat pumps.</p>

<h2 id="base">Finding 1: base load jumped in September and stayed up</h2>
<p>The yearly base load of 96.3 kW hides a change. The base load by month chart shows it:</p>
<div class="table-wrap"><table><thead><tr><th>Month</th><th class="num">Base load</th><th>Month</th><th class="num">Base load</th></tr></thead><tbody>
<tr><td>Apr 2024</td><td class="num">99.8 kW</td><td>Oct 2024</td><td class="num">121.3 kW</td></tr>
<tr><td>May 2024</td><td class="num">96.0 kW</td><td>Nov 2024</td><td class="num">125.1 kW</td></tr>
<tr><td>Jun 2024</td><td class="num">93.1 kW</td><td>Dec 2024</td><td class="num">128.1 kW</td></tr>
<tr><td>Jul 2024</td><td class="num">91.9 kW</td><td>Jan 2025</td><td class="num">129.4 kW</td></tr>
<tr><td>Aug 2024</td><td class="num">93.2 kW</td><td>Feb 2025</td><td class="num">128.2 kW</td></tr>
<tr><td>Sep 2024</td><td class="num">117.0 kW</td><td>Mar 2025</td><td class="num">124.9 kW</td></tr>
</tbody></table></div>
<p>Between August and September the base load rose by about 24 kW. The weather barely changes between those two months, so this isn't heating. Some of the later rise is seasonal, but a step that size in one month points to something that started running and didn't stop.</p>
<p>The heatmap shows where: from 2 September, nights and weekends are darker (higher demand), while weekday daytime looks the same as before. In our made-up story, a controls upgrade over the summer left the theatre air handling units at full flow overnight and at weekends instead of setting back when the theatres are empty. HTM 03-01 treats switching off or setting back theatre ventilation when it isn't needed as the most energy-efficient policy, and NHS England's July 2026 estates bulletin on theatre energy puts the saving at 132 to 286 MWh per theatre a year, provided pressure cascades and temperatures are kept within limits.<sup><a href="https://www.england.nhs.uk/wp-content/uploads/2026/07/PRN02301-netb-2026-1-energy-savings-in-theatres-v1.1.pdf">1</a></sup></p>
<p>The extra is about 22 kW for around 5,700 hours a year, which is roughly 125,000 kWh, or about £31,000 a year at 25p/kWh if it's left running. It doesn't show up as an unusual day, because each day only moves a little. That's why the monthly base load chart is worth checking on every hospital site.</p>

<h2 id="generator">Finding 2: a short monthly dip that isn't a fault</h2>
<p>On the first Tuesday of each month, demand drops to about 30% of normal between 10:00 and 11:00. That's the generator test: the site runs on its own generators and imports little from the grid. It sets the lowest half hour of the year (53.3 kW), but it's too short to drag the base load figure down, because base load is the 5th percentile across the year, not the minimum. If you see the same pattern in your data, check it against the generator test log before treating it as missing data.</p>

<h2 id="capacity">Finding 3: summer sets the peak, winter sets the heat pump limit</h2>
<p>The five busiest half hours all fell in the hot week of 15 to 19 July, when the chillers were working hardest. The peak of 288.6 kW is about 304 kVA at an assumed power factor of 0.95, which is 76% of the 400 kVA agreed capacity. Holding back a 10% margin leaves 360 kVA usable.</p>
<p>The largest constant load that fits in every half hour of the year is about 53 kW. But a heat pump runs mainly from October to April, when there's no cooling load, so the analyser's headroom test lets you check a load in the heating months only:</p>
<ul>
<li><strong>A 100 kW heat pump, running around the clock from October to April, fits.</strong> The highest half hour with it added is about 354 kVA against 360 kVA usable. That's tight, with no room for anything else.</li>
<li><strong>A 150 kW heat pump doesn't fit.</strong> It would go over the usable capacity in 2,690 half hours on 154 days, by up to 46 kVA, mostly on winter weekday evenings. That needs a capacity increase from the network operator, a smaller heat pump, or controls that hold it back at peak times.</li>
</ul>
<p>This is the check to run before you plan to replace gas boilers or a CHP engine with heat pumps. See <a href="hospital-electrical-capacity.html">electrical capacity on hospital sites</a> and <a href="moving-away-from-chp.html">moving away from CHP</a>.</p>

<h2 id="solar">Finding 4: it would use almost every unit of solar</h2>
<p>Between 10:00 and 16:00 in summer, the site averages about 205 kW on weekdays and 147 kW at weekends. That's a lot of daytime demand to soak up solar. At UK average output (905 kWh per kWp a year), the analyser estimates:</p>
<div class="table-wrap"><table><thead><tr><th>System size</th><th class="num">Output a year</th><th class="num">Used on site</th><th class="num">Share of site's use</th></tr></thead><tbody>
<tr><td>299 kWp</td><td class="num">268,374 kWh</td><td class="num">99.8%</td><td class="num">20%</td></tr>
<tr><td>449 kWp</td><td class="num">402,516 kWh</td><td class="num">95%</td><td class="num">29%</td></tr>
<tr><td>748 kWp</td><td class="num">670,890 kWh</td><td class="num">76%</td><td class="num">38%</td></tr>
<tr><td>1,196 kWp</td><td class="num">1,073,406 kWh</td><td class="num">54%</td><td class="num">44%</td></tr>
</tbody></table></div>
<p>Up to about 300 kWp, the site would use all of it. Most community hospitals don't have that much suitable roof, so for a site like this the limit is space and the grid connection, not demand. Car park canopies are often the way to add more. See <a href="solar-on-healthcare-estates.html">solar on healthcare estates</a>, then open the {SOLAR} from the analyser's Solar tab to cost a system.</p>

<h2 id="next-steps">What we'd do next</h2>
<ol>
<li><strong>Take it to the Ventilation Safety Group.</strong> The NHS England bulletin makes the trust's Ventilation Safety Group the starting point for any change to theatre ventilation, with the Authorised Person (Ventilation) on the project team. Then have the BMS contractor restore the setback. Then load the next three months of data to confirm the base load has dropped back (see <a href="proving-savings.html">proving a saving worked</a>).</li>
<li><strong>Look for other continuous load.</strong> Even at 96 kW, base load is 63% of the bill. Walk the site at 02:00 with the night team: lighting in empty areas, pumps without variable speed drives, and plant left in hand. See <a href="base-load.html">base load on healthcare sites</a>.</li>
<li><strong>Confirm the agreed capacity</strong> on the bill before planning any heat pump, and get the 150 kW option priced with and without a capacity increase.</li>
<li><strong>Size solar to the roof and car parks you have.</strong> On this profile, almost all of it would be used on site.</li>
</ol>
''',
  [('site', 'The site'), ('headline', 'The headline figures'), ('base', 'Base load jumped in September'), ('generator', 'A monthly dip, not a fault'),
   ('capacity', 'Peaks and heat pump headroom'), ('solar', 'How much solar it would use'), ('next-steps', "What we'd do next")],
  [('Is this real data?', "No. We made up the hospital and its readings so we could show the method without using anyone's real data. Every figure is what the analyser reports for the example file."),
   ('Why is there no out-of-hours figure?', 'Because a hospital with inpatients never closes. The 24/7 preset has no closed hours. Use the base load, its monthly trend and the low-activity window from 01:00 to 05:00 instead.'),
   ('Can I run the same checks on my own hospital?', 'Yes. Ask your supplier for a year of half-hourly data for each main meter, load it into the analyser and enter your agreed supply capacity. It runs in your browser and nothing is uploaded.'),
   ('Are these figures savings?', "No. They're what each pattern costs now at 25p/kWh. A saving depends on what you change, and should be confirmed from the meter data afterwards.")],
  [('base-load.html', 'Base load', 'What runs around the clock on a healthcare site, and how to cut it.'),
   ('hospital-electrical-capacity.html', 'Electrical capacity', 'Headroom for heat pumps and EV charging.'),
   ('get-your-data.html', 'Get your own data', 'What to ask your supplier for.')],
  'A made-up community hospital run through the analyser: 1.35 GWh a year, 63% base load, a 22 kW ventilation setback fault from September worth about £31,000 a year, a 100 kW heat pump fits a 400 kVA supply but 150 kW does not, and it would use almost all output from up to about 300 kWp of solar.',
  crumbs=[HOME, GUIDES, ('Worked example', 'example-hospital-analysis.html')]))
# The example file, marked up as a free dataset so it can be found and cited.
PAGES[-1].schema.append({
    '@type': 'Dataset', 'name': 'Example half-hourly electricity data for a made-up community hospital',
    'description': ('A synthetic year (1 April 2024 to 31 March 2025) of half-hourly electricity import readings for an invented '
                    '60-bed community hospital, made to show the Hospital Energy Insights analyser: one row per day, 48 half-hourly kWh '
                    'readings. Not real data.'),
    'url': kit.url('example-hospital-analysis.html'), 'isAccessibleForFree': True, 'creator': {'@id': kit.ORG_ID},
    'temporalCoverage': '2024-04-01/2025-03-31', 'spatialCoverage': 'United Kingdom',
    'variableMeasured': 'Electricity imported, kWh per half hour',
    'distribution': [{'@type': 'DataDownload', 'encodingFormat': 'text/csv', 'contentUrl': kit.url('samples/example-hospital.csv')}],
})

# ── OUT-OF-HOURS ────────────────────────────────────────────────────────
PAGES.append(guide_page(
  'out-of-hours-electricity.html',
  'Out-of-hours electricity in clinics and health centres',
  'Out-of-hours use in clinics and support buildings',
  'Wards never close, but most of a healthcare estate does. Health centres, outpatient wings, offices and training centres often run plant all night because nobody changed the schedule.',
  'How to find electricity used while clinics, health centres, outpatients and estates offices are closed, what causes it on healthcare sites, and how to fix it safely.',
  f'''
<p class="answer">Out-of-hours use is electricity a building uses while it's closed, above what has to run all the time. On a healthcare estate, look for it in health centres, outpatient wings, clinics, estates offices, education centres and restaurants, not on the 24-hour inpatient supply. The fix is usually a schedule change in the building management system (BMS). Check any change to ventilation or hot water with the right safety group first.</p>

<h2 id="where">Where to look on a healthcare estate</h2>
<p>A hospital's main meter can't show out-of-hours use, because wards, theatres on call and emergency departments never close. The places that do close are where the savings hide:</p>
<ul>
<li><strong>Health centres and GP-led community buildings</strong>, usually open 08:00 to 18:30 on weekdays, with some evening and Saturday sessions.</li>
<li><strong>Outpatient departments and day units</strong>, if they're on their own meter or sub-meter.</li>
<li><strong>Estates, finance and HQ offices</strong>, often in older buildings with old controls.</li>
<li><strong>Education and training centres</strong>, which empty out in the evening and over holidays.</li>
<li><strong>Community bases and clinics</strong> used on a few days a week.</li>
</ul>
<p>In the analyser, set each of these to the <strong>Clinic / outpatients / health centre</strong> preset (08:00 to 18:30 on weekdays) or the office preset. Leave inpatient sites on the 24/7 preset.</p>

<h2 id="calendar">Get the opening hours right first</h2>
<p>Every out-of-hours figure depends on the calendar. Healthcare buildings often have patterns an office doesn't: extended-access evening clinics, Saturday vaccination sessions, a dental or physiotherapy list one evening a week, or a shared reception that opens early for a community team. Add those as open hours before you trust the numbers. If you don't, legitimate clinics show up as waste and the real problem gets buried.</p>

<h2 id="find">How to find it in half-hourly data</h2>
<ol>
<li><strong>Look at the heatmap.</strong> Opening hours form a dark weekday band. Dark patches outside it, at night, at weekends or over bank holidays, is what you're looking for. See <a href="reading-a-heatmap.html">how to read a heatmap</a>.</li>
<li><strong>Read the closed-hours excess.</strong> The analyser takes the base load away from every closed half hour and prices what's left at your rate. It splits the result into weekday nights, Saturdays, Sundays and bank holidays, because each usually has a different cause.</li>
<li><strong>Check the edges of the day.</strong> A ramp that starts two hours before the first appointment, or stays up long after the last, is usually optimum start or a fixed timer set too wide.</li>
<li><strong>Compare similar buildings.</strong> Load several health centres at once and rank them by closed-hours excess, so the worst one gets looked at first.</li>
</ol>

<h2 id="causes">What usually causes it in healthcare buildings</h2>
<ul>
<li><strong>Ventilation left on 24/7.</strong> Air handling units in clinics are often scheduled to run continuously "to be safe", or share plant with an area that does need it.</li>
<li><strong>Bank holidays missing from the BMS calendar.</strong> Christmas, Easter and the summer bank holiday look like normal clinic days.</li>
<li><strong>Clinical kit left on.</strong> Dental compressors and suction plant, X-ray and ultrasound left on standby, and treatment-room lighting.</li>
<li><strong>Heating and cooling fighting each other</strong> overnight, with split air-conditioning units cooling rooms the heating has warmed.</li>
<li><strong>One evening session running the whole building</strong>, because the BMS can't zone a single clinic room.</li>
<li><strong>Plant left in hand</strong> after maintenance and never put back to auto.</li>
</ul>

<h2 id="safely">Fixing it safely</h2>
<p>Most fixes are BMS schedule changes, holiday calendars and timers, and they cost little. Two need care in healthcare buildings:</p>
<ul>
<li><strong>Ventilation in clinical rooms.</strong> Treatment rooms, minor surgery rooms and dental surgeries can have specific ventilation requirements under HTM 03-01. Agree any setback with your Ventilation Safety Group and Authorised Person (Ventilation).</li>
<li><strong>Hot water.</strong> Calorifier and circulation temperatures are part of your water safety plan for legionella control under HTM 04-01. Don't switch off hot water or circulation pumps to save energy without the Water Safety Group.</li>
</ul>
<p>Vaccine and pharmacy fridges, IT, fire and security systems belong in the base load and should stay on.</p>

<h2 id="who">Who to involve</h2>
<p>You need someone who can change the controls (your estates officer or BMS contractor) and someone who knows how the building is actually used (the practice or clinic manager). Show both the heatmap and the split by type of day. Then load the next month's data and check the change worked, as set out in <a href="proving-savings.html">proving a saving worked</a>.</p>
''',
  [('where', 'Where to look'), ('calendar', 'Get the hours right'), ('find', 'How to find it'), ('causes', 'Common causes'), ('safely', 'Fixing it safely'), ('who', 'Who to involve')],
  [('Can I measure out-of-hours use on a hospital main meter?', 'Not directly, because an inpatient site never closes. Use the base load, its monthly trend and the 01:00 to 05:00 low-activity window instead, and sub-meter or separately meter the buildings that do close.'),
   ('Is it safe to switch off ventilation in a health centre at night?', 'Often yes for offices, waiting areas and consulting rooms, but not for every clinical room. Check the room types against HTM 03-01 and agree changes with your Ventilation Safety Group.'),
   ('Why do our bank holidays look like working days?', 'Usually because the BMS holiday calendar is empty or out of date. It is one of the cheapest fixes there is: enter the dates once a year.'),
   ('How soon can I see whether a schedule change worked?', 'After four to eight weeks of new data. Compare the same types of day before and after the change in the analyser.')],
  [('base-load.html', 'Base load', 'What has to run around the clock.'),
   ('health-centres-and-clinics.html', 'Health centres and clinics', 'What normal looks like in buildings that close.'),
   ('example-hospital-analysis.html', 'Worked example', 'A community hospital, finding by finding.')],
  'Out-of-hours electricity on healthcare estates: where to look (health centres, outpatients, offices, education centres), setting clinic hours, finding it in HH data, common causes, and safe fixes under HTM 03-01 and HTM 04-01.'))

# ── BASE LOAD ───────────────────────────────────────────────────────────
PAGES.append(guide_page(
  'base-load.html',
  'Hospital base load: what never switches off and how to cut it',
  'Base load on healthcare sites',
  "On a 24-hour hospital, the load that never switches off is usually the biggest part of the electricity bill. It's also the part most often left unexamined.",
  'What makes up base load on hospitals and health centres, how to measure it from half-hourly data, and safe ways to reduce it. 1 kW all year is 8,766 kWh.',
  f'''
<p class="answer">Base load is the level of electricity a site never drops below, day or night. On a hospital it covers wards, ventilation, imaging, fridges, IT and medical gas plant, and it is often the largest part of the bill. In our made-up <a href="example-hospital-analysis.html">community hospital</a>, it's 63%. Each kilowatt running all year is 8,766 kWh, or about £2,190 at 25p/kWh, so even small cuts add up.</p>

<h2 id="measure">How the analyser measures it</h2>
<p>The analyser converts every valid half-hourly reading to kW and takes the level demand stays above 95% of the time (the 5th percentile). It doesn't use the single lowest reading, because a generator test, a meter fault or a power cut can set that. On a hospital, the monthly generator test often sets the lowest half hour of the year, which is why the minimum is shown alongside the base load but not used for it.</p>
<p>Two more views matter on a 24-hour site:</p>
<ul>
<li><strong>Base load by month.</strong> A step up that doesn't follow the weather means something started running and didn't stop. Check this chart on every hospital.</li>
<li><strong>The low-activity window.</strong> The 24/7 preset uses 01:00 to 05:00, when wards are quiet and clinics, theatres and kitchens are shut. Demand in that window is as close to a hospital's "closed" state as you'll get.</li>
</ul>

<h2 id="what">What makes up base load in healthcare</h2>
<div class="table-wrap"><table><thead><tr><th>Load</th><th>Must it run all night?</th></tr></thead><tbody>
<tr><td>Ward lighting, nurse call, bed-head services</td><td>Yes, though corridor and stair lighting can often be dimmed or put on sensors</td></tr>
<tr><td>Theatre ventilation</td><td>Not when theatres are empty. Setback is an approved saving, see below</td></tr>
<tr><td>General ventilation and air handling</td><td>Ward areas yes; offices, outpatients and restaurants usually not</td></tr>
<tr><td>MRI cooling compressors and imaging standby</td><td>MRI cooling yes; other imaging can often go to a lower standby out of hours</td></tr>
<tr><td>Pharmacy, pathology, blood and vaccine fridges</td><td>Yes</td></tr>
<tr><td>Medical air and vacuum plant</td><td>Yes</td></tr>
<tr><td>IT rooms, servers and their cooling</td><td>Yes, but consolidation and higher room set points cut it</td></tr>
<tr><td>Heating and chilled water pumps</td><td>Often, but fixed-speed pumps at full flow rarely need to be</td></tr>
<tr><td>Kitchen refrigeration, vending, water coolers</td><td>Fridges yes; vending lighting and coolers can go on timers</td></tr>
<tr><td>External and car park lighting</td><td>At night, but on photocells and dimming, not timers stuck on</td></tr>
</tbody></table></div>

<h2 id="theatres">Theatre ventilation: the biggest single base load saving</h2>
<p>HTM 03-01 describes switching off or setting back theatre ventilation when it isn't needed as the most energy-efficient policy. NHS England's July 2026 estates technical bulletin estimates the saving at 132 to 286 MWh per theatre each year, across about 3,300 theatres in England.{ref(1)} The bulletin makes the trust's Ventilation Safety Group the starting point, and sets conditions: pressure cascades checked, temperatures kept between 16°C and 25°C while set back, and enough time to return to full flow before use (25 to 30 minutes after a long shutdown).{ref(1)}</p>
<p>In half-hourly data, a working setback shows as lower nights and weekends on the theatre block's meter, or on the main meter if theatres are a large share of the site. When a setback stops working, base load steps up and stays up, as it does in our <a href="example-hospital-analysis.html#base">worked example</a>.</p>

<h2 id="reduce">How to cut it safely</h2>
<ol>
<li><strong>Walk the site between 01:00 and 05:00</strong> with the night site manager or porters. Note what's on in empty offices, outpatients, restaurants and plant rooms.</li>
<li><strong>Sort it into three lists:</strong> must run (clinical, safety, fridges, medical gas), could run less (pumps, fans, lighting, IT cooling), and shouldn't be on.</li>
<li><strong>Fix the "shouldn't be on" list first.</strong> BMS schedules, timers and plant left in hand cost almost nothing to put right.</li>
<li><strong>Then the "could run less" list:</strong> theatre setback, variable speed drives on pumps and fans, LED and sensors in 24-hour corridors.</li>
<li><strong>Check base load by month afterwards.</strong> It should step down and stay down.</li>
</ol>
<p>Never switch off clinical equipment, fridges, medical gas plant, fire and security systems or water safety controls to save energy.</p>

<h2 id="solar">Base load and solar</h2>
<p>A hospital's base load runs through every sunny afternoon, including weekends, so it soaks up solar output. That's why 24-hour sites usually use nearly all of what a well-sized system generates. The analyser's Solar tab estimates the share from your own readings and passes it to the {SOLAR}. See <a href="solar.html">sizing solar from half-hourly data</a>.</p>

<h2 id="worth">Working out the saving</h2>
<p>Multiply the kilowatts you remove by the hours they would have run and by your unit rate. A load running all year is 8,766 hours (the average year, allowing for leap years), so 1 kW is about £2,190 a year at 25p/kWh. A load that only runs at night and weekends, like a failed theatre setback, runs for about 5,700 hours a year.</p>
{sources([S_NETB])}
''',
  [('measure', 'How it is measured'), ('what', 'What makes it up'), ('theatres', 'Theatre ventilation'), ('reduce', 'How to cut it safely'), ('solar', 'Base load and solar'), ('worth', 'Working out the saving'), ('sources', 'Sources')],
  [('What share of a hospital\'s electricity is base load?', 'It varies by site, so measure your own. On a 24-hour hospital it is commonly more than half. In our made-up community hospital it is 63%.'),
   ('Why not use the lowest half hour as the base load?', 'Because one generator test, meter fault or power cut can set it. The analyser uses the 5th percentile, which those short events barely move.'),
   ('How much does 1 kW of base load cost a year?', 'About 8,766 kWh, which is roughly £2,190 at 25p/kWh. Multiply 8,766 by your own unit rate.'),
   ('Is theatre ventilation setback safe?', 'NHS England guidance supports it when theatres are unused, under conditions on pressure, temperature and time to return to full flow, and with the Ventilation Safety Group overseeing it.')],
  [('out-of-hours-electricity.html', 'Out-of-hours use', 'For the buildings on your estate that do close.'),
   ('hospital-energy-efficiency.html', 'Energy efficiency in hospitals', 'The measures that cut base load.'),
   ('example-hospital-analysis.html', 'Worked example', 'How a base load jump showed up in one hospital.')],
  'Base load on healthcare sites: measured as the 5th percentile, base load by month and the 01:00 to 05:00 window; what makes it up in hospitals; theatre ventilation setback (132 to 286 MWh per theatre a year, NHS England 2026); safe ways to cut it.'))

# ── SUPPLY CAPACITY ─────────────────────────────────────────────────────
PAGES.append(guide_page(
  'supply-capacity.html',
  'Hospital supply capacity: kVA headroom for heat pumps',
  'Supply capacity and headroom',
  'Heat pumps, EV fleets and the end of gas CHP all add electrical load. Before any of them, check how close your busiest half hours already come to the agreed supply capacity.',
  'How to check a hospital\'s agreed supply capacity against half-hourly peaks in kVA, test a heat pump or EV load, and plan for CHP removal before a DNO application.',
  '''
<p class="answer">Agreed supply capacity is the most your connection is contracted to take, in kVA, and it's on your electricity bill. Convert your busiest half hours from kW to kVA (divide by the power factor), keep a safety margin, and the gap is your headroom. For heat pumps, test the heating months only: summer chiller peaks don't matter for a load that runs from October to April.</p>

''' + photo('plant-outside', 'Two engineers with a tablet beside packaged plant, flues and pipework outside a large building', "Heat pumps replacing boilers or CHP land on the electrical supply. Check the headroom before the design gets too far.") + '''
<h2 id="why">Why capacity decides decarbonisation plans</h2>
<p>Most routes to net zero on a healthcare estate move heat from gas to electricity. A heat pump producing 300 kW of heat at a seasonal efficiency (COP) of 3 draws about 100 kW of electricity. Switching off a gas CHP engine that generated 400 kW means importing that 400 kW from the grid instead. Electric vehicle fleets, pool cars and patient transport add more. If the connection can't take it, the network operator (DNO) has to increase it, which can take years and cost far more than the plant. See <a href="hospital-electrical-capacity.html">electrical capacity on hospital sites</a> and <a href="moving-away-from-chp.html">moving away from CHP</a>.</p>

<h2 id="kva">kW, kVA and power factor</h2>
<p>Half-hourly data gives average demand in each half hour, in kW. Capacity is set in kVA, which also counts reactive power drawn by motors, fans and older lighting. The link is the power factor:</p>
<div class="note"><strong>kVA = kW ÷ power factor.</strong> At 0.95, a 285 kW peak is 300 kVA. If your bill has reactive power charges, your power factor is lower than that, and your real headroom is smaller than a 0.95 assumption suggests.</div>

<h2 id="headroom">Working out headroom from half-hourly data</h2>
<ol>
<li><strong>Use at least a full year</strong>, so you catch both winter heating peaks and summer chiller peaks.</li>
<li><strong>Enter the agreed capacity</strong> from the bill and your power factor (0.95 if you don't know it).</li>
<li><strong>Keep a margin</strong>, typically 10%, for growth and short spikes the half-hour average hides.</li>
<li><strong>Read the firm headroom</strong>: the largest constant extra load that fits in every half hour of the year.</li>
<li><strong>Test the real load.</strong> The analyser's headroom test takes a load in kW, the hours it runs and whether it runs all year or October to April only, and counts the half hours it would push over the limit.</li>
</ol>
<p>In our <a href="example-hospital-analysis.html#capacity">worked example</a>, a community hospital on a 400 kVA supply has only 53 kW of firm headroom across the year, because July chillers set the peak. Tested over the heating months, a 100 kW heat pump fits and a 150 kW one doesn't.</p>

<h2 id="hospital">What's different on a hospital</h2>
<ul>
<li><strong>Two supplies and generators.</strong> Many hospitals have more than one incoming supply and standby generators for essential services. Check which supply new plant will sit on, and whether it needs to be generator-backed, because that sizes the generators too.</li>
<li><strong>CHP hides demand.</strong> While a CHP engine runs, the import meter shows only part of the site's load. The days the engine was off show the true import, so look at those before assuming you have headroom. The analyser's peaks list will often be CHP outage days.</li>
<li><strong>Nights aren't quiet.</strong> On an office, overnight EV charging fits in the trough. On a 24-hour hospital the trough is shallower, so test it rather than assume it.</li>
<li><strong>Several meters, one connection.</strong> Where a site has more than one meter behind one connection, add them up before comparing with capacity. The analyser can group meters into one site.</li>
</ul>

<h2 id="limits">What half-hourly data can't tell you</h2>
<p>Half-hour averages smooth out spikes such as motor starts, so treat the result as an early screen, not a design. Network capacity upstream of your site, fault levels and the cost of an increase come from the DNO. Use the analyser to decide which option to take to them, and to show them your measured profile.</p>

<h2 id="solar">Solar and your connection</h2>
<p>Solar lowers daytime import but adds export capacity questions under G99. On a 24-hour hospital, most output is used on site, so export limits rarely cost much. See <a href="solar-planning-and-grid.html">solar planning and grid connection</a>.</p>
''',
  [('why', 'Why capacity matters'), ('kva', 'kW, kVA and power factor'), ('headroom', 'Working out headroom'), ('hospital', "What's different on a hospital"), ('limits', 'What the data cannot tell you'), ('solar', 'Solar and your connection')],
  [('Where do I find our agreed supply capacity?', 'On the electricity bill, usually as agreed, authorised or available capacity in kVA. Your supplier or DNO can confirm it, and the connection agreement sets it.'),
   ('Why test a heat pump over the heating months only?', 'Because it runs mainly from October to April. A summer chiller peak sets the all-year headroom figure, but it does not coincide with heat pump load.'),
   ('What power factor should I use?', 'Use the figure from your bill or power quality data if you have it. If not, 0.95 is a reasonable starting point; it is probably lower if you pay reactive power charges.'),
   ('Is this enough for a DNO application?', 'No. It is the evidence to decide what to ask for. The DNO studies the network and makes the formal offer.')],
  [('hospital-electrical-capacity.html', 'Electrical capacity', 'The wider capacity question for electrifying heat.'),
   ('moving-away-from-chp.html', 'Moving away from CHP', 'What happens to import when the engine stops.'),
   ('example-hospital-analysis.html', 'Worked example', 'Summer peaks and heat pump headroom at one hospital.')],
  'Agreed supply capacity for hospitals: kW to kVA, headroom from a year of HH peaks with a margin, testing heat pumps over the heating months, CHP hiding demand, generator-backed supplies, and what to take to the DNO.'))

# ── READING A HEATMAP ───────────────────────────────────────────────────
PAGES.append(guide_page(
  'reading-a-heatmap.html',
  'How to read a hospital electricity heatmap',
  'How to read a half-hourly heatmap',
  'One chart, every half hour of the year. On a hospital it shows things no monthly bill can: a ventilation fault, a generator test, a CHP engine tripping.',
  'How to read a half-hourly electricity heatmap for a hospital or health centre: what normal looks like on a 24-hour site, and the patterns that point to faults or waste.',
  '''
<p class="answer">A heatmap has one column per day and one row per half hour, coloured by demand. On a 24-hour hospital you won't see pale weekends; instead, read the night rows (your base load), the weekday daytime band (outpatients, theatres and offices), summer afternoons (cooling), and any date where the pattern changes and stays changed.</p>

<figure class="figure"><img src="images/heatmap-hospital.png" width="1548" height="560" alt="Heatmap of a made-up community hospital year: a dark weekday daytime band, darker summer afternoons, and nights that get darker from September" loading="lazy"><figcaption>Our made-up <a href="example-hospital-analysis.html">community hospital</a>. Weekday days are the dark band. Summer afternoons are darker from the chillers. The short white marks mid-morning once a month are the generator tests. From early September the nights and weekends get darker: the theatre ventilation has stopped setting back.</figcaption></figure>

<h2 id="axes">What you're looking at</h2>
<ul><li><strong>Across:</strong> days, from the start of the period to the end.</li><li><strong>Down:</strong> time of day, midnight at the top.</li><li><strong>Colour:</strong> demand in each half hour, pale for low and dark for high.</li></ul>
<p>A year is about 17,500 half hours. A table can't show them; a heatmap shows them all, which is why it's the fastest way to understand a site you've never visited.</p>

<h2 id="hospital">What normal looks like on a hospital</h2>
<ul>
<li><strong>Nights are never pale.</strong> Wards, ventilation, imaging and fridges keep demand well above zero. How dark the night rows are is your base load.</li>
<li><strong>A weekday daytime band</strong> from outpatients, theatres, diagnostics, kitchens and offices. Weekends and bank holidays are lighter, but not empty.</li>
<li><strong>A morning ramp</strong> as plant starts and clinics open, and a smaller evening shoulder.</li>
<li><strong>Seasonal shading.</strong> Darker summer afternoons on sites with chillers; slightly darker winters where electric heating, frost protection or heating pumps run.</li>
</ul>
<p>A separately metered health centre or office should look like an office: a dark weekday band and pale nights and weekends. If it doesn't, read <a href="out-of-hours-electricity.html">out-of-hours use</a>.</p>

<h2 id="patterns">Patterns worth checking on healthcare sites</h2>
<div class="table-wrap"><table><thead><tr><th>What you see</th><th>What it often means</th></tr></thead><tbody>
<tr><td>Nights and weekends darker from a particular date</td><td>A setback or schedule has stopped working, often theatre or outpatient ventilation after a controls change</td></tr>
<tr><td>A pale stripe at the same time once a month</td><td>The generator test: the site runs on its own generators and imports less from the grid</td></tr>
<tr><td>Dark blocks of several days or weeks</td><td>The CHP engine was off for maintenance or a fault, so the grid supplied the whole site</td></tr>
<tr><td>Darker afternoons only in hot spells</td><td>Chillers and split cooling; these days usually set the year's peak</td></tr>
<tr><td>Weekday band starting well before clinics open</td><td>Optimum start or fixed timers set too early</td></tr>
<tr><td>Bank holidays as dark as weekdays</td><td>Holiday dates missing from the BMS calendar, mainly in outpatients and offices</td></tr>
<tr><td>A single dark or pale column</td><td>One unusual day: a major incident, an outage, works or a reading error</td></tr>
<tr><td>Grey gaps</td><td>Missing readings, not zero use. The analyser never counts missing data as zero</td></tr>
</tbody></table></div>

<h2 id="next">From what you see to what it costs</h2>
<p>The heatmap tells you where to look; the figures tell you whether it matters. In the analyser, click any day to compare it with a typical day of the same kind. Then check base load by month for lasting steps, the unusual days list for one-offs, and the headroom tab for the peak days.</p>
''',
  [('axes', "What you're looking at"), ('hospital', 'Normal on a hospital'), ('patterns', 'Patterns worth checking'), ('next', 'From what you see to what it costs')],
  [('What is a carpet plot?', 'Another name for the same chart: one column per day, one row per half hour, coloured by demand.'),
   ('Why does our hospital have a pale line once a month?', 'Most likely the on-load generator test, when the site runs on its own generators for an hour or so. Check the dates against the test log.'),
   ('Why are some days grey?', 'They have no valid readings. Missing data is shown as missing, so a gap never looks like the site was switched off.'),
   ('Can I see one day in detail?', 'Yes. Click any day in the analyser to compare its half hours with a typical day of the same kind.')],
  [('example-hospital-analysis.html', 'Worked example', 'The hospital in the heatmap, finding by finding.'),
   ('moving-away-from-chp.html', 'Moving away from CHP', 'Spotting engine outages in your import data.'),
   ('base-load.html', 'Base load', 'What the night rows are telling you.')],
  'Reading a half-hourly heatmap for hospitals and health centres: night rows as base load, the weekday band, summer cooling, and patterns such as failed ventilation setback, generator tests, CHP outages and missing data.'))

# ── PROVING A SAVING ────────────────────────────────────────────────────
PAGES.append(guide_page(
  'proving-savings.html',
  'Proving NHS energy savings with half-hourly data',
  'Proving a saving worked',
  "Funders, boards and finance teams all want to see that a project delivered. Half-hourly data can show it, as long as you compare like with like on a site that never stops changing.",
  'How estates teams can use half-hourly data to show an energy project worked: matched periods, the right measure for the change, weather, and when you need formal M&V.',
  '''
<p class="answer">Compare a period before the change with a matching period after it, using the same types of day and four to eight weeks either side. Measure the part of demand the change should affect, such as nights and weekends for a ventilation setback, rather than the total bill. On a hospital, total consumption moves with activity, weather and new equipment, so a real saving can easily get lost in it.</p>

''' + photo('board-review', 'A team reviewing charts and printed reports around a meeting table', 'A saving is easier to sign off when the before-and-after comparison is fair and the method is written down.') + '''
<h2 id="why">Why it matters on healthcare estates</h2>
<p>Grant-funded projects usually have to report what they saved, energy performance contracts pay on measured savings, and trust boards want evidence before funding the next phase. Even when nobody asks, checking the data is how you find out a setback was overridden or a timer reset after maintenance. The same check run monthly keeps savings from quietly drifting away.</p>

<h2 id="match">Compare like with like</h2>
<ul>
<li><strong>Same types of day.</strong> Weekdays with weekdays, weekends with weekends. Keep bank holidays and the Christmas period out of both sides unless the change is about them.</li>
<li><strong>Enough data.</strong> Four to eight weeks either side usually shows a real change. One week can be thrown by a single unusual day.</li>
<li><strong>Close together.</strong> The nearer the two periods, the less the weather and seasons get in the way.</li>
<li><strong>Leave out the works.</strong> Skip the days when contractors were on site or plant was isolated.</li>
<li><strong>Write down anything else that changed</strong>, such as a ward opening, new imaging equipment or a CHP outage, so you can explain the result.</li>
</ul>

<h2 id="measure">Measure the right thing</h2>
<div class="table-wrap"><table><thead><tr><th>Change</th><th>What to compare</th></tr></thead><tbody>
<tr><td>Theatre or outpatient ventilation setback</td><td>Demand at night and at weekends, and base load by month</td></tr>
<tr><td>LED and sensors in 24-hour corridors and wards</td><td>The 01:00 to 05:00 low-activity window, plus daytime demand</td></tr>
<tr><td>Variable speed drives on pumps and fans</td><td>Base load, and demand in the hours the plant runs</td></tr>
<tr><td>BMS schedules in clinics and offices</td><td>Closed-hours excess, by type of day</td></tr>
<tr><td>Solar</td><td>Daytime import on sunny days against the solar estimate (imports should fall)</td></tr>
<tr><td>Heat pumps replacing gas boilers or CHP</td><td>Electricity rises, as expected. Measure the fall in gas alongside it, and check the new peak against capacity</td></tr>
</tbody></table></div>

<h2 id="weather">Weather and seasons</h2>
<p>Chillers, electric heating and heat pumps follow the weather. If the before period was hotter or colder than the after period, some of the change is weather. For weather-sensitive changes, compare the same weeks a year apart as a cross-check, or adjust using degree days.</p>

<h2 id="analyser">In the analyser</h2>
<ul>
<li><strong>Did a change make a difference?</strong> on the Base load tab compares matched weeks either side of a date you choose.</li>
<li><strong>Compare periods</strong> on the Heatmap tab puts any two periods side by side.</li>
<li><strong>Persistent changes</strong> on the Unusual days tab flags lasting shifts, so you can check the change appears when you'd expect it to.</li>
</ul>

<h2 id="mv">When you need formal M&amp;V</h2>
<p>For an energy performance contract or a funded project with savings targets, agree a measurement and verification plan before work starts. The International Performance Measurement and Verification Protocol (IPMVP) sets out recognised methods: the baseline period, what gets adjusted for (weather, occupancy, operating hours) and how savings are reported. The half-hourly checks above are a good way to watch progress between formal reports.</p>
''',
  [('why', 'Why it matters'), ('match', 'Compare like with like'), ('measure', 'Measure the right thing'), ('weather', 'Weather and seasons'), ('analyser', 'In the analyser'), ('mv', 'Formal M&V')],
  [('How long should we wait before checking?', 'Four to eight weeks after the change, compared with the same length of time before it, is usually enough to see a real change.'),
   ('Why has the hospital bill not gone down after our project?', 'Activity, weather, prices and new equipment all move the total. Compare the specific part of demand the change should affect.'),
   ('Our electricity went up after installing heat pumps. Did it fail?', 'Not necessarily. Heat pumps move heat from gas to electricity, so electricity rises. Judge them on total energy, cost and carbon, with gas included.'),
   ('Can this replace a formal M&amp;V report?', 'No. It is a good check, but formal measurement and verification, for example under IPMVP, agrees the baseline and adjustments up front.')],
  [('base-load.html', 'Base load', 'The measure most switch-off changes affect.'),
   ('hospital-energy-efficiency.html', 'Energy efficiency in hospitals', 'The changes worth proving.'),
   ('decarbonisation-funding.html', 'Funding', 'Where the projects being proved come from.')],
  'Proving an energy saving on a healthcare estate with HH data: matched periods, the right measure per change (setback, LED, VSDs, BMS schedules, solar, heat pumps), weather, analyser tools and formal M&V under IPMVP.'))

# ── MHHS ────────────────────────────────────────────────────────────────
PAGES.append(guide_page(
  'half-hourly-settlement.html',
  'Market-wide half-hourly settlement (MHHS) explained',
  'Market-wide half-hourly settlement explained',
  "Britain is moving every electricity meter onto half-hourly settlement. Here's what that means for businesses and public sector organisations, and why it makes your half-hourly data more useful.",
  'What market-wide half-hourly settlement (MHHS) is, the timetable to 2027, who runs it, and what it means for business and public sector electricity customers.',
  '''
<p class="answer">Market-wide half-hourly settlement (MHHS) means suppliers will be charged for the electricity their customers actually use in each half hour, instead of an estimate based on standard usage profiles. The move began in October 2025 and is due to finish in May 2027. If you have a smart or advanced meter, your half-hourly readings become part of how your electricity is settled, so it's worth asking your supplier for them.</p>

''' + photo('site-plans-substation', 'Four people in hard hats and high-visibility vests reviewing site plans next to a substation and solar panels') + '''
<h2 id="what">What it is</h2>
<p>Large sites have been settled half-hourly for years. Most smaller sites have been settled using standard profiles, which are estimates of when a typical customer uses electricity. MHHS replaces those estimates with actual half-hourly readings wherever a meter can provide them.<sup><a href="#sources">1</a></sup></p>
<p>The programme's stated objective is "to maximise the opportunities provided by smart metering by developing and implementing an enduring process for MHHS, that delivers benefits for consumers and enables a smart, flexible energy system."<sup><a href="#sources">2</a></sup></p>

<h2 id="who">Who runs it</h2>
<p>Ofgem decided to go ahead with MHHS on 20 April 2021.<sup><a href="#sources">1</a></sup> Ofgem is the programme sponsor and appointed Elexon as Senior Responsible Owner and Implementation Manager. Delivery is led by the energy industry.<sup><a href="#sources">2</a></sup></p>

<h2 id="timeline">The timetable</h2>
<div class="table-wrap"><table><thead><tr><th>Date</th><th>Milestone</th></tr></thead><tbody>
<tr><td>20 April 2021</td><td>Ofgem decision to introduce MHHS (originally planned to finish in October 2025)</td></tr>
<tr><td>21 October 2025</td><td>Migration to the new arrangements began, for all meter types</td></tr>
<tr><td>7 May 2027</td><td>Migration due to be complete, with all energy settled under the new arrangements</td></tr>
<tr><td>2 July 2027</td><td>Settlement moves from a 14-month to a four-month timetable</td></tr></tbody></table></div>
<p>Dates as published by Ofgem and the MHHS programme in November 2026. Check the programme's milestone page for the latest.<sup><a href="#sources">1, 3</a></sup></p>

<h2 id="you">What it means for your organisation</h2>
<ul><li><strong>You don't need to do anything to be moved across.</strong> Your supplier handles it.</li><li><strong>Microbusinesses can't opt out.</strong> Ofgem's decision says half-hourly data will be processed for settlement for domestic customers unless they opt out, and that microbusiness customers will not be able to opt out.<sup><a href="#sources">1</a></sup></li><li><strong>Tariffs may change.</strong> Ofgem expects MHHS to encourage suppliers to offer tariffs that reward using electricity at cheaper times of day, known as time-of-use tariffs.<sup><a href="#sources">1</a></sup></li><li><strong>Half-hourly data becomes standard.</strong> If your meter records half-hourly readings, your supplier uses them. Ask for a copy and you can see exactly when your sites use electricity.</li></ul>
<p>Under half-hourly settlement and time-of-use tariffs, the time of day you use electricity will matter more. Understanding your half-hourly pattern now, including what runs overnight and at weekends, will help you choose a suitable tariff and reduce costs.</p>
''' + sources([
    ('Ofgem: Electricity Retail Market-wide Half-hourly Settlement: Decision and Full Business Case (20 April 2021)', 'https://www.ofgem.gov.uk/decision/electricity-retail-market-wide-half-hourly-settlement-decision-and-full-business-case'),
    ('MHHS Programme: Programme overview', 'https://www.mhhsprogramme.co.uk/programme-information/programme-overview'),
    ('MHHS Programme: Key programme milestones', 'https://www.mhhsprogramme.co.uk/programme-information/key-programme-milestones')]),
  [('what', 'What it is'), ('who', 'Who runs it'), ('timeline', 'The timetable'), ('you', 'What it means for your organisation')],
  [('When does market-wide half-hourly settlement finish?', "Migration is due to be complete on 7 May 2027, with the move to a four-month settlement timetable on 2 July 2027, according to the MHHS programme's published milestones."),
   ('Do I need to do anything?', 'No. Your supplier moves your meters across. It is worth asking them for your half-hourly data, so you can see when your sites use electricity.'),
   ('Can a business opt out of half-hourly data collection?', "Ofgem's 2021 decision says microbusiness customers will not be able to opt out of their half-hourly data being processed for settlement. Domestic customers can opt out.")],
  [('get-your-data.html', 'Getting your data', 'What to ask your supplier for.'),
   ('glossary.html', 'Glossary', 'Settlement, MPAN, kVA and other terms.'),
   ('out-of-hours-electricity.html', 'Out-of-hours use', 'The first thing to look at in your data.')],
  'Market-wide half-hourly settlement: Ofgem decision 20 April 2021; migration began 21 October 2025, due complete 7 May 2027; four-month settlement timetable from 2 July 2027; microbusinesses cannot opt out.'))

# ── GLOSSARY ────────────────────────────────────────────────────────────
GLOSSARY_GROUPS = [
  ('Healthcare estates', [
    ('Authorised Person (Ventilation)', 'The person appointed in writing to manage specialised ventilation systems on a healthcare site, under HTM 03-01. Part of any project that changes theatre ventilation.'),
    ('Capital departmental expenditure limit (CDEL)', 'The cap on capital spending set for NHS organisations. Whether a solar PPA or lease counts against it depends on how the contract is accounted for. <a href="paying-for-solar.html#ppa">More</a>.'),
    ('EFPMS', 'The Estates and Facilities Performance Management System: NHS Wales\'s mandatory annual estates return, covering energy and CHP among much else. <a href="estates-returns-and-benchmarking.html#efpms">More</a>.'),
    ('ERIC', 'The Estates Returns Information Collection: the mandatory annual estates and facilities return for NHS trusts in England, including energy use and cost by site. <a href="estates-returns-and-benchmarking.html#eric">More</a>.'),
    ('Essential supplies', 'The parts of a hospital\'s electrical system backed by standby generators, so clinical services keep running if the grid supply fails.'),
    ('Generator test', 'The routine on-load test of a hospital\'s standby generators, often monthly. While it runs the site imports less from the grid, which shows as a short dip in half-hourly data.'),
    ('Green Plan', 'An NHS organisation\'s board-approved plan for cutting its carbon emissions and wider environmental impact, in line with the NHS net zero targets.'),
    ('Heat decarbonisation plan (HDP)', 'A building-by-building plan for replacing fossil fuel heating with low carbon heat, often needed for public sector funding bids. <a href="heat-decarbonisation.html#plan">More</a>.'),
    ('Health Technical Memorandum (HTM)', 'Guidance on designing and running healthcare buildings and engineering services. The ones that matter most for energy are HTM 03-01 (specialised ventilation), HTM 04-01 (water safety) and HTM 06-01 (electrical services). Scotland and Wales publish their own versions (SHTM, WHTM).'),
    ('NHS Carbon Footprint', 'The emissions the NHS in England controls directly, including energy in its buildings, with a net zero target of 2040. The Carbon Footprint Plus adds the supply chain, with a 2045 target. <a href="nhs-net-zero-targets.html">More</a>.'),
    ('NHS Estates Technical Bulletin (NETB)', 'Technical guidance from NHS England that supplements the HTMs. NETB 2026/1 covers energy savings from controlling theatre ventilation. <a href="base-load.html#theatres">More</a>.'),
    ('NHS Net Zero Building Standard', 'The NHS England standard for new buildings and major refurbishments that need HM Treasury business case approval, covering operational energy and whole-life carbon. <a href="nhs-net-zero-targets.html#england">More</a>.'),
    ('PFI', 'Private Finance Initiative. On a PFI hospital a project company built the buildings and runs services under a long contract, and often holds the energy supply and meter data. Its consent is needed for works such as solar.'),
    ('Public Sector Decarbonisation Scheme (PSDS)', 'The government grant scheme, run by Salix, that funded heat and energy projects in public buildings in England from 2020. New rounds are not being funded beyond 2027/28. <a href="decarbonisation-funding.html#england">More</a>.'),
    ('Theatre ventilation setback', 'Reducing or switching off operating theatre ventilation when the theatre is empty, then returning to full flow before use. One of the largest energy savings available on a hospital. <a href="base-load.html#theatres">More</a>.'),
    ('Ventilation Safety Group (VSG)', 'The multidisciplinary group in an NHS organisation that oversees specialised ventilation, including estates, infection prevention and clinical staff. The starting point for any change to theatre ventilation.'),
    ('Water Safety Group', 'The group that owns an organisation\'s water safety plan for legionella and other risks under HTM 04-01. Changes to hot water temperatures or circulation need its agreement.'),
  ]),
  ('Heat, solar and the grid', [
    ('Agreed supply capacity', 'The most a site\'s connection is contracted to draw, in kVA, shown on larger electricity bills. Also called authorised or available capacity. <a href="supply-capacity.html">More</a>.'),
    ('Combined heat and power (CHP)', 'A gas engine that generates electricity on site and uses its waste heat for heating and hot water. Common on hospitals; its carbon advantage over grid electricity has largely gone. <a href="moving-away-from-chp.html">More</a>.'),
    ('Coefficient of performance (COP)', 'Heat delivered by a heat pump per unit of electricity used. A COP of 3 means 3 kWh of heat for 1 kWh of electricity. Averaged over a season it is the SCOP.'),
    ('Distribution network operator (DNO)', 'The company that runs the local electricity network, agrees your supply capacity and approves generation such as solar. The first two digits of the MPAN show which one you are on. <a href="mpan-profile-class.html#bottom">More</a>.'),
    ('Export limit', 'A cap, agreed with the DNO and enforced by a control system, on how much a site\'s solar or batteries can send back to the network. Usually costs a 24-hour hospital little. <a href="solar-planning-and-grid.html#g99">More</a>.'),
    ('Firm headroom', 'The largest constant extra load a supply could take in every half hour of the period without going over its agreed capacity less a safety margin. <a href="supply-capacity.html#headroom">More</a>.'),
    ('G99', 'The engineering recommendation setting how larger generators, including most hospital solar systems and batteries, apply to the DNO to connect. <a href="solar-planning-and-grid.html#g99">More</a>.'),
    ('Power purchase agreement (PPA)', 'A contract to buy electricity from a generator at an agreed rate, often from a solar system a funder owns on your site. <a href="paying-for-solar.html#ppa">More</a>.'),
    ('Self-consumption', 'The share of a solar system\'s output used on site at the time it is generated rather than exported. On a 24-hour hospital it is usually high. <a href="solar.html#share">More</a>.'),
  ]),
  ('Reading half-hourly data', [
    ('Annualised figure', 'A yearly total scaled up from the valid readings, used when the data falls short of a full year or has gaps. The analyser withholds it below six months.'),
    ('Base load', 'The level a site\'s demand rarely falls below, measured by the analyser as the 5th percentile of half-hourly demand. On a hospital it is usually the largest part of the bill. <a href="base-load.html">More</a>.'),
    ('Closed-hours excess', 'Electricity used while a building should be closed, above its base load. Used for clinics, health centres and offices, not 24-hour sites. <a href="out-of-hours-electricity.html">More</a>.'),
    ('Coverage', 'The share of expected half-hourly readings that are present and valid.'),
    ('Degree days', 'A measure of how cold or warm a period was, used to compare heating or cooling energy across periods with different weather.'),
    ('Half-hourly (HH) data', 'The electricity a meter records in each half hour: 48 readings a day, 17,520 in a normal year.'),
    ('Heatmap', 'One chart of every half hour in a period, a column per day and a row per half hour, coloured by demand. Also called a carpet plot. <a href="reading-a-heatmap.html">More</a>.'),
    ('kVA', 'Kilovolt-ampere, the unit of apparent power that supply capacity is set in. kVA = kW ÷ power factor.'),
    ('kW', 'Kilowatt, the rate electricity is being used. A half-hourly reading in kWh divided by 0.5 gives the average kW for that half hour.'),
    ('kWh', 'Kilowatt-hour, the unit of energy you are billed for. 1 kW for one hour is 1 kWh.'),
    ('Load factor', 'Average demand divided by peak demand. Hospitals have high load factors because demand never falls far.'),
    ('Low-activity window', 'The hours the analyser treats as a 24-hour site\'s quietest, 01:00 to 05:00 by default, in place of closed hours.'),
    ('MPAN', 'Meter point administration number: the 13-digit number on the bottom line of the supply number on an electricity bill. <a href="mpan-profile-class.html">More</a>.'),
    ('Peak demand', 'The highest half-hourly average demand in a period, in kW or kVA. On many hospitals it falls on a hot summer afternoon.'),
    ('Power factor', 'The ratio of real power (kW) to apparent power (kVA), between 0 and 1. Motors and fans lower it.'),
  ]),
  ('On the electricity bill', [
    ('Capacity Market (CM)', 'A scheme paying providers to keep reliable capacity available, charged on use between 4pm and 7pm on working days from November to February. <a href="non-energy-charges.html#cm">More</a>.'),
    ('Climate Change Levy (CCL)', 'A tax per kWh on energy used by businesses and public bodies. <a href="non-energy-charges.html#ccl">More</a>.'),
    ('Distribution Use of System (DUoS)', 'Charges for using the local network, set by the DNO: unit rates by time band, capacity charges and daily charges. <a href="non-energy-charges.html#duos">More</a>.'),
    ('Market-wide half-hourly settlement (MHHS)', 'The move to settle every electricity meter in Great Britain on half-hourly data. <a href="half-hourly-settlement.html">More</a>.'),
    ('Non-energy costs', 'Everything in the electricity price apart from the wholesale energy: network charges, policy costs and taxes. <a href="non-energy-charges.html">More</a>.'),
    ('Profile class', 'The first two digits of the top line of the supply number. 00 means the supply is settled half-hourly. <a href="mpan-profile-class.html#top">More</a>.'),
    ('Transmission Network Use of System (TNUoS)', 'Charges for the national high-voltage network, mainly a fixed daily charge per site for business supplies. <a href="non-energy-charges.html#tnuos">More</a>.'),
  ]),
]
for _, items in GLOSSARY_GROUPS:
    items.sort(key=lambda t: t[0].lower())
GLOSSARY = [t for _, items in GLOSSARY_GROUPS for t in items]


def _term_id(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower().split(' (')[0]).strip('-')


NAV_PARENT['glossary.html'] = 'guides.html'
PAGES.append(Page(
  'glossary.html', 'Glossary of hospital energy and HH data terms',
  'Plain definitions of healthcare estates and half-hourly electricity terms: base load, kVA, MPAN, CHP, COP, ERIC, HTM, theatre setback, PSDS and more.',
  page_hero('Guide', 'Glossary', 'The estates, energy and data terms used on this site, in plain words.',
            crumbs=[HOME, GUIDES, ('Glossary', 'glossary.html')], image='glossary')
  + guide(updated_line() + '<p class="answer">These are the terms estates teams meet when they work with half-hourly electricity data and plan decarbonisation: estates terms such as ERIC, HTM and theatre setback; heat, solar and grid terms such as COP, G99 and firm headroom; data terms such as base load, kW and kVA; and the charges on the bill.</p>'
          + ''.join(f'<h2 id="{_term_id(g)}">{g}</h2><dl class="glossary">' + ''.join(
              f'<div id="{_term_id(t)}"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in items) + '</dl>' for g, items in GLOSSARY_GROUPS),
          toc([(_term_id(g), g) for g, _ in GLOSSARY_GROUPS]))
  + cta('See the terms in your own data', "It's free, there's no sign-up, and nothing is uploaded."),
  crumbs=[HOME, GUIDES, ('Glossary', 'glossary.html')], article=True, section='Guides',
  summary='Definitions for healthcare estates and half-hourly data: ERIC, EFPMS, HTM, NETB, theatre ventilation setback, Ventilation Safety Group, PFI, PSDS, CHP, COP, G99, firm headroom, self-consumption, base load, low-activity window, kW, kVA, MPAN and bill charges.',
  schema=[{'@type': 'DefinedTermSet', 'name': 'Hospital energy and half-hourly data glossary', 'hasDefinedTerm': [
      {'@type': 'DefinedTerm', 'name': t, 'description': strip_tags(d).replace(' More.', '')} for t, d in GLOSSARY]}]))

# ── HEALTHCARE SETTINGS ─────────────────────────────────────────────────
# (file, short name, h1, lead, what normal looks like, what to check first,
#  how to set the hours, decarbonisation notes, questions)
SECTOR_DATA = [
  ('acute-hospitals.html', 'Acute hospitals', 'Half-hourly electricity in acute hospitals',
   'An acute hospital never closes, so out-of-hours use tells you little. Day and night, base load, peaks against capacity and lasting changes tell you a lot.',
   'Expect continuous demand with a daytime rise from outpatients, theatres, imaging and offices, and often a summer peak from cooling. The base load is high because so much has to run all the time, which makes changes in it easy to spot and expensive to ignore.',
   ['Night-time demand in non-clinical blocks (offices, education centres, restaurants, outpatients) close to daytime levels', 'Theatre ventilation running at full rate overnight and at weekends', 'Steps up in base load after new equipment, a refurbishment or a BMS change', 'Winter and summer peaks against each supply\'s agreed capacity, with and without CHP running', 'How much of a solar system\'s output each supply would use, before you size one'],
   'Set the main hospital supply to the "Hospital / 24-7 inpatient site" preset, which has no closed hours and uses 01:00 to 05:00 as a low-activity window. If you have sub-meters for outpatients, offices or education buildings, give them their real opening hours so their out-of-hours use shows.',
   'Acute sites carry most of the heat load and most of the CHP on the estate, so they decide the electrical capacity question. Check headroom in winter with any CHP switched off, before heat pump schemes are designed. See <a href="hospital-electrical-capacity.html">electrical capacity</a> and <a href="moving-away-from-chp.html">moving away from CHP</a>.',
   [('Can out-of-hours analysis work for a hospital?', 'Not for the main 24-hour supply, which has no closed hours. Compare day with night, track the base load and watch for lasting changes instead. For clinics and offices on the site, out-of-hours analysis works as it does anywhere.'),
    ('Why does supply capacity matter so much?', 'Replacing gas heating with heat pumps adds a large electrical load in winter, and removing CHP adds its full output to grid import. Check how close your peaks already come to the agreed capacity first.')]),
  ('community-and-mental-health.html', 'Community and mental health sites', 'Half-hourly electricity in community hospitals and mental health sites',
   'Inpatient units run around the clock, while the clinics, therapy spaces and offices beside them keep working hours. Separating the two is where the savings show.',
   'Inpatient wards give a steady base with a daytime rise. Community clinics, therapy buildings and offices on the same estate should fall to a low base in the evening and at weekends. Many of these sites are older, gas-heated and spread across several buildings, so they are often good early candidates for heat pumps and solar.',
   ['Clinics and therapy buildings heated and ventilated on the inpatient unit\'s 24-hour schedule', 'Weekend use in buildings that are closed at weekends', 'Kitchens, laundries and plant rooms with equipment left running', 'Base load steps after refurbishments', 'Headroom on smaller supplies before adding heat pumps or EV charging'],
   'Use the 24-7 preset for inpatient units and the clinic preset for outpatient and therapy buildings, then adjust the hours to match each site. Add bank holiday and Christmas closures for clinics.',
   'Smaller, separate supplies often have little spare capacity, so a heat pump for one building can need a connection upgrade. They also suit solar well where the inpatient unit is on the same supply. See <a href="heat-decarbonisation.html">heat decarbonisation</a>.',
   [('Should we treat a community hospital as 24/7?', 'If it has inpatient beds, yes for that supply. Give separately metered clinics and offices their own opening hours.'),
    ('Which sites should we analyse first?', 'Load every meter at once. The analyser ranks sites, so you can start where the evidence is strongest.')]),
  ('health-centres-and-clinics.html', 'Health centres, clinics and GP premises', 'Half-hourly electricity in health centres and clinics',
   'Health centres keep set hours, so use while they are closed is easy to see and often cheap to fix.',
   'Expect a clear weekday pattern, falling to a low base load in the evening and at weekends, with extra hours on extended-access evenings and Saturdays. Many buildings have shared occupation, so the landlord, the practice and other services may each control part of the building.',
   ['Heating, cooling and ventilation running all night or all weekend', 'Vaccine fridges and IT, which are part of the base load and should be steady', 'Extended hours that were never added to the building controls, or were never removed', 'Lighting in corridors, stairs and car parks on all night', 'Solar output that would be exported at weekends, before sizing a system'],
   'Start from the clinic preset (08:00 to 18:30 weekdays) and add any evening and Saturday sessions as open hours, so the out-of-hours figure only shows use that could be avoided.',
   'Health centres often have flat roofs and car parks that suit solar, but closed weekends mean a smaller share of output is used on site, so size from your data. See <a href="solar-on-healthcare-estates.html">solar on healthcare estates</a>.',
   [('Who can act on the findings in a shared building?', 'Whoever controls the plant, often the landlord or facilities provider. The analyser\'s PDF gives them the evidence in a form they can use.'),
    ('Is a high base load normal for a health centre?', 'Some is: vaccine fridges, IT and security systems run all the time. A base load that rises without a clear reason is worth investigating.')]),
  ('ambulance-stations-and-fleet.html', 'Ambulance stations and fleet depots', 'Half-hourly electricity at ambulance stations and fleet depots',
   'Stations run around the clock and fleets are moving to electric vehicles, so supply capacity is the question to answer first.',
   'Expect a steady base with peaks around shift changes. As electric ambulances and support vehicles arrive, charging creates new, large peaks that can arrive at the same time every day.',
   ['Peaks at shift changes against the agreed supply capacity', 'Room for EV charging before any chargers are ordered', 'Workshop and make-ready equipment left running between shifts', 'Heating in vehicle bays and stores', 'Daytime demand that solar could cover'],
   'Use the 24-7 preset for operational stations, and the clinic or office preset for administration buildings with set hours.',
   'Fleet electrification is a capacity project. Use the headroom check with your planned chargers as a test load, and look at smart charging to keep within the limit. See <a href="hospital-electrical-capacity.html">electrical capacity</a>.',
   [('How much capacity do EV chargers need?', 'As an illustration, two 50 kW rapid chargers running together need about 100 kW. Smart charging can spread the load so fewer chargers run at full power at once.'),
    ('Can solar help with EV charging?', 'It can cover some daytime charging, but vehicles often charge overnight. Batteries can store solar for later use.')]),
]

SECTOR_PHOTOS = {
    'acute-hospitals.html': ('estate-hospital', 'Illustration of a hospital estate with clinical buildings, a multi-storey car park, plant compounds and a substation'),
    'community-and-mental-health.html': ('hc-efficient-ward', 'A bright hospital ward corridor with a nurse, a porter and a wall-mounted building systems display'),
    'health-centres-and-clinics.html': ('hc-private-hospital-carport', 'A healthcare building with solar panels on the roof and a solar car park canopy'),
    'ambulance-stations-and-fleet.html': ('solar-carport-depot', 'A depot with solar car park canopies over parked vehicles'),
}

for file, short, h1, lead, normal, checks, calendar_tip, decarb, faqs in SECTOR_DATA:
    PAGES.append(guide_page(
      file, f'{short}: half-hourly electricity, capacity and solar', h1, lead,
      f'Half-hourly electricity data in {short.lower()}: what normal looks like, what to check first, how to set the hours, and what it means for heat pumps, capacity and solar.',
      f"""
<p class="answer">{normal}</p>
{photo(*SECTOR_PHOTOS[file])}
<h2 id="check">What to check first</h2>
<ul>{''.join(f'<li>{c}</li>' for c in checks)}</ul>

<h2 id="calendar">Setting the hours in the analyser</h2>
<p>{calendar_tip}</p>
<p>Each site is compared with its own calendar, so getting the hours right matters more than the type of building.</p>

<h2 id="decarbonisation">Heat, capacity and solar</h2>
<p>{decarb}</p>
<p>The analyser's Solar tab shows how much of a system's output each supply would use, and passes it to the <a href="solar-calculator.html">solar calculator</a>, so the payback is based on your own profile. See <a href="solar.html">sizing solar from half-hourly data</a>.</p>

<h2 id="compare">How does your site compare?</h2>
<p>To see whether a site's total use is high for its type, compare its kWh per square metre with similar sites. In England, ERIC site data is public; see <a href="estates-returns-and-benchmarking.html">estates returns and benchmarking</a>. Then use the half-hourly pattern to find out why. Questions about the analyser are answered in the <a href="faq.html">FAQ</a>.</p>
""",
      [('check', 'What to check first'), ('calendar', 'Setting the hours'), ('decarbonisation', 'Heat, capacity and solar'), ('compare', 'How does your site compare?')],
      faqs,
      [('hospital-electrical-capacity.html', 'Electrical capacity', 'Room for heat pumps and EV charging.'),
       ('base-load.html', 'Base load', 'What always runs.'),
       ('sectors.html', 'Other site types', 'Acute, community, clinics, ambulance and private.')],
      f'{short}: what normal half-hourly demand looks like, what to check first, how to set the hours, and the capacity and solar questions.',
      crumbs=[HOME, SECTORS, (short, file)]))

SETTINGS_CARDS = [(f, s, lead) for f, s, _, lead, *_ in SECTOR_DATA] + [
    ('private-hospitals.html', 'Private and independent hospitals', 'The same engineering, different targets, finance and reporting duties.'),
]

PAGES.append(Page(
  'sectors.html', 'Healthcare site types: what to look for in HH data',
  'What half-hourly electricity data shows in acute hospitals, community and mental health sites, health centres and clinics, ambulance stations and private hospitals.',
  page_hero('Site types', 'What normal looks like for your type of site', 'An acute hospital, a health centre and an ambulance station use electricity very differently. Choose your type of site to see what normal looks like, what to check first and how to set it up in the analyser.',
            crumbs=[HOME, SECTORS], image='sectors') +
  '<section class="section"><div class="section-inner">' +
  photo('estate-hospital', 'Illustration of a hospital estate with clinical buildings, solar on roofs and car park canopies, plant compounds and a substation', cls='figure figure-wide', lazy=False) +
  '<div class="link-grid">' +
  ''.join(link_card(f, s, lead, 'Read more') for f, s, lead in SETTINGS_CARDS) +
  '</div></div></section>' + cta('Check your whole estate', 'Load every meter at once and the analyser ranks the sites, so you know which to look at first.'),
  crumbs=[HOME, SECTORS], section='Sectors', summary='Index of healthcare site types: acute hospitals, community and mental health, health centres and clinics, ambulance stations, private hospitals.'))

GUIDE_GROUPS = [
  ('Decarbonising the estate', [
    ('healthcare-estates-decarbonisation.html', 'The estates challenge', 'Targets, heat, CHP, capacity and funding in one place, and where to start.'),
    ('nhs-estates-energy-facts.html', 'Facts and figures', 'The key numbers on NHS estates energy, each sourced and dated.'),
    ('nhs-net-zero-targets.html', 'Net zero targets across the UK', 'England, Scotland and Wales side by side, plus supplier rules.'),
    ('decarbonisation-funding.html', 'Funding routes', 'After PSDS: Great British Energy, devolved schemes and funded models.'),
    ('heat-decarbonisation.html', 'Heat decarbonisation', 'Heat pumps, flow temperatures, steam, hot water and heat networks.'),
    ('moving-away-from-chp.html', 'Moving away from gas CHP', 'Why the carbon case changed, and the capacity effect of removing it.'),
    ('hospital-electrical-capacity.html', 'Electrical capacity', 'Headroom for heat pumps, EV charging and CHP removal.'),
    ('hospital-energy-efficiency.html', 'Energy efficiency', 'Theatre ventilation, controls, lighting and steam.'),
    ('estates-returns-and-benchmarking.html', 'Estates returns and benchmarking', 'ERIC, EFPMS and comparing sites fairly.'),
    ('private-hospitals.html', 'Private and independent hospitals', 'ESOS, SECR, NHS supplier rules and the IHPN commitment.'),
  ]),
  ('Solar', [
    ('solar-on-healthcare-estates.html', 'Solar on healthcare estates', 'Roofs, car parks and land, and why 24/7 sites suit it.'),
    ('solar.html', 'Sizing solar from half-hourly data', 'How the analyser measures the share you would use.'),
    ('solar-calculator-method.html', 'How the solar calculator works', 'Method, sunshine data and every assumption.'),
    ('solar-cost.html', 'What solar costs', 'Installed costs by roof and mounting type.'),
    ('solar-payback.html', 'Solar payback', 'How long it takes, and what moves it.'),
    ('solar-generation.html', 'How much solar generates', 'Output by region, orientation and tilt.'),
    ('solar-planning-and-grid.html', 'Planning and grid connection', 'Permitted development, G99 and other hurdles.'),
    ('paying-for-solar.html', 'Paying for solar', 'Buying, finance, leasing and PPAs.'),
  ]),
  ('Your half-hourly data', [
    ('get-your-data.html', 'Getting your half-hourly data', 'Who has it, what to ask for, a letter template, and the file formats the analyser reads.'),
    ('example-hospital-analysis.html', 'Worked example: a community hospital', 'What the analyser found in a year of data from one hospital.'),
    ('reading-a-heatmap.html', 'How to read a heatmap', 'Every half hour of a year on one chart, and the patterns to look for.'),
    ('base-load.html', 'Base load', 'What always runs, how to measure it and how to reduce it.'),
    ('out-of-hours-electricity.html', 'Out-of-hours electricity use', 'Clinics, offices and other buildings with set hours.'),
    ('supply-capacity.html', 'Supply capacity and kVA', 'The basics of capacity, power factor and headroom.'),
    ('proving-savings.html', 'Proving a saving worked', 'How to compare before and after fairly.'),
    ('half-hourly-settlement.html', 'Half-hourly settlement (MHHS)', 'What the move to half-hourly settlement means.'),
    ('mpan-profile-class.html', 'Reading your MPAN', 'Profile class, network region and meter type.'),
    ('electricity-benchmarks.html', 'Electricity benchmarks', 'Typical kWh per m² by building type.'),
    ('glossary.html', 'Glossary', 'kW, kVA, ERIC, HTM, PSDS, CHP and other terms.'),
  ]),
  ('Prices and bills', [
    ('business-electricity-price.html', "What's in a non-domestic electricity price", 'Wholesale, network, policy, tax and supplier costs.'),
    ('non-energy-charges.html', 'Non-energy charges explained', 'TNUoS, DUoS, BSUoS, levies and taxes.'),
    ('electricity-prices-ten-years.html', 'Ten years of electricity prices', 'What organisations paid from 2015 to 2026, and why.'),
    ('non-energy-costs-outlook.html', 'Where non-energy costs are heading', 'Published forecasts and decisions for 2027 and beyond.'),
  ]),
]
GUIDE_LIST = [g for _, items in GUIDE_GROUPS for g in items]


def guide_group(title, items):
    """One group on the guides page: our own guides as picture cards, then any
    general pages whose original lives on a sister site as a plain list, so
    the page isn't a wall of near-identical cards."""
    own = [i for i in items if i[0] not in kit.CANONICAL_ELSEWHERE]
    ref = [i for i in items if i[0] in kit.CANONICAL_ELSEWHERE]
    out = f'<h2 class="section-title" style="margin-top:40px">{title}</h2>'
    if own:
        out += '<div class="link-grid">' + ''.join(link_card(f, t, d) for f, t, d in own) + '</div>'
    if ref:
        out += ('<div class="ref-list"><h3>' + ('General reference' if own else 'Reference guides') + '</h3><ul>'
                + ''.join(f'<li><a href="{f}">{t}</a><span>{d}</span></li>' for f, t, d in ref) + '</ul></div>')
    return out
NAV_PARENT['get-your-data.html'] = 'guides.html'
PAGES.append(Page(
  'guides.html', 'Guides for healthcare estates: decarbonisation, solar and half-hourly data',
  'Plain guides for NHS and private healthcare estates teams: net zero targets, funding, heat pumps, moving away from CHP, electrical capacity, solar and half-hourly electricity data.',
  page_hero('Guides', 'Guides for healthcare estates', 'Clear answers to the questions estates, facilities and energy teams ask about decarbonisation, solar and half-hourly data.',
            crumbs=[HOME, GUIDES], image='guides') +
  '<section class="section"><div class="section-inner">' +
  ''.join(guide_group(g, items) for g, items in GUIDE_GROUPS) +
  '<p class="note" style="margin-top:32px">Looking for your type of site? See <a href="sectors.html" style="color:var(--blue);text-decoration:underline">what to look for by site type</a>.</p></div></section>'
  + cta('Ready to look at your own data?', "It's free, there's no sign-up, and nothing is uploaded."),
  crumbs=[HOME, GUIDES], section='Guides', summary='Index of guides.'))
