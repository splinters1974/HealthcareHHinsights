"""
Guides and sector pages. Each guide opens with a direct answer (what search
and AI answer engines quote), carries a few questions marked up as FAQPage,
and ends with links to related guides.

Written for a general business reader: plain words, terms explained on first
use, as long as it needs to be and no longer. "Closed-hours excess" is the
analyser's figure; "out-of-hours use" is the general idea.

Figures in the worked examples come from the analyser run on
site/samples/example-office.csv (made-up data).
Re-check them if those files or the engine change.
"""
import re

from kit import (NAV_PARENT, SOLAR_URL, Page, cta, link_card, faq_section, guide, page_hero, photo, related, sources, strip_tags, toc,
                 updated_line)

HOME = ('Home', 'index.html')
GUIDES = ('Guides', 'guides.html')
SECTORS = ('Healthcare settings', 'sectors.html')
SOLAR = f'<a href="{SOLAR_URL}">solar calculator</a>'


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
PAGES.append(guide_page(
  'example-office-analysis.html',
  'Worked example: a year of half-hourly data for an admin building',
  'Worked example: an admin building, one year',
  'Most healthcare estates include offices, headquarters and training buildings that keep set hours. We ran a year of half-hourly data from a small office building through the analyser. The building and its data are made up, but every figure below is exactly what the analyser reports.',
  'One office, one year of half-hourly data: use while closed, base load, peaks against supply capacity, and what to do next.',
  f'''
<p class="answer">This office used a third of its electricity (33%) while the building was closed. Leaving aside what always has to run, that closed-hours use costs about £2,800 a year at 25p/kWh, and almost half of it happens on Saturdays.</p>

<div class="note"><strong>Made-up data.</strong> We invented this office so we could show the method without using anyone's real data. <a href="samples/example-office.csv" download>Download the file</a> and load it into the <a href="analyser/">analyser</a> to follow along. New sites start on the 24-hour hospital preset, so choose <strong>Admin, offices and HQ</strong> as the building type first.</div>

<h2 id="headline">The headline figures</h2>
<div class="table-wrap"><table><thead><tr><th>Measure</th><th class="num">Value</th><th>What it means</th></tr></thead><tbody>
<tr><td>Electricity a year</td><td class="num">79,191 kWh</td><td>Scaled up from 363 days of valid readings (99.5% coverage)</td></tr>
<tr><td>Energy cost a year</td><td class="num">£19,798</td><td>At a flat rate of 25p/kWh, before standing and capacity charges</td></tr>
<tr><td>Base load</td><td class="num">2.6 kW</td><td>The level demand rarely drops below</td></tr>
<tr><td>Busiest half hour</td><td class="num">25.5 kW</td><td>28 January 2025, midday</td></tr>
<tr><td>Use while closed</td><td class="num">33%</td><td>Using the default office hours, 07:00 to 19:00 on weekdays</td></tr>
<tr><td>Closed-hours excess</td><td class="num">£2,776</td><td>Electricity used while closed, above the base load, at 25p/kWh</td></tr>
</tbody></table></div>

<h2 id="split">Where the electricity goes</h2>
<p>The analyser splits each half hour's use at the base load. The three parts add up to the total:</p>
<ul><li><strong>Base load, 29%</strong> (22,606 kWh). What runs around the clock, whether anyone is in or not.</li><li><strong>Use above base load while open, 57%</strong> (45,062 kWh). The building in normal use: lights, heating, computers and kitchens during the working day.</li><li><strong>Closed-hours excess, 14%</strong> (11,035 kWh). Use above base load while the building should be closed. This is the place to start, because it usually costs little to fix.</li></ul>

<h2 id="findings">What the analyser found</h2>
<h3>1. Use while closed: £2,776 a year (high impact)</h3>
<p>Breaking this down by type of day is the most useful step, because each type usually has a different cause:</p>
<div class="table-wrap"><table><thead><tr><th>When</th><th class="num">Above base load</th></tr></thead><tbody>
<tr><td>Saturdays</td><td class="num">5,155 kWh</td></tr><tr><td>Weekday evenings and nights</td><td class="num">3,750 kWh</td></tr>
<tr><td>Bank holidays</td><td class="num">1,408 kWh</td></tr><tr><td>Sundays</td><td class="num">722 kWh</td></tr></tbody></table></div>
<p>Saturdays account for almost half. Sundays are quiet, so this isn't heating or ventilation running all weekend. The building is being used on some Saturdays. If that's planned, add Saturdays to the calendar and the figure falls. If it isn't, a Saturday booking or a few staff may be running the whole building.</p>

<h3>2. Seven bank holidays look like working days (medium impact)</h3>
<p>On seven bank holidays, including Christmas Day and Boxing Day, the office used at least 80% of a normal weekday's electricity. If the office was closed, the heating and ventilation schedules probably don't include bank holidays, which is very common. If it was open, the calendar needs updating.</p>

<h3>3. Early starts and late finishes: £629 a year (low impact)</h3>
<p>Demand rises before opening and stays high after closing. That's about 1,250 kWh a year above base load in the two hours before opening, and the same again in the two hours after closing. Timers and heating start-up settings are the usual cause, and they're quick to adjust.</p>

<h2 id="capacity">Supply capacity</h2>
<p>Assuming an agreed supply capacity of 40 kVA and a power factor of 0.95, the busiest half hour reaches 27 kVA, which is 67% of capacity. Keeping a 10% safety margin, the site could take about 9 kW of extra constant load. That's enough for modest EV charging, such as one 7 kW charger, but nowhere near enough for a heat pump to heat the whole building. See <a href="supply-capacity.html">supply capacity and kVA</a>.</p>

<h2 id="next-steps">What we'd do next</h2>
<ol><li><strong>Confirm the opening hours</strong>, including Saturdays. Every closed-hours figure depends on them.</li><li><strong>Check the heating and ventilation schedules</strong> for bank holidays and start times.</li><li><strong>Walk round the building on a Saturday</strong> to see what's switched on and who is using it.</li><li><strong>Look at the base load.</strong> 2.6 kW running all year is about 22,800 kWh, roughly £5,700 at 25p/kWh. See <a href="base-load.html">how to reduce it</a>.</li></ol>
<p>57% of this office's electricity is used during the working day, which is when solar panels generate. The {SOLAR} estimates what a roof system would save, and the <a href="solar.html">solar page</a> shows how to size one from this data.</p>
''',
  [('headline', 'The headline figures'), ('split', 'Where the electricity goes'), ('findings', 'What the analyser found'), ('capacity', 'Supply capacity'), ('next-steps', "What we'd do next")],
  [('Is this real data?', "No. We made up the office and its readings so we could show the method without using anyone's real data. Every figure is what the analyser reports for the example file."),
   ('How long does an analysis like this take?', 'Loading a year of data takes about a minute. Confirming the opening hours and reading the findings takes longer, and matters more.'),
   ('Are these figures savings?', "No. They're what each pattern costs now at 25p/kWh. Any saving depends on what you change.")],
  [('out-of-hours-electricity.html', 'Out-of-hours use', 'How to find and reduce use while the building is closed.'),
   ('base-load.html', 'Base load', 'What always runs, and why it adds up.'),
   ('get-your-data.html', 'Get your own data', 'What to ask your supplier for.')],
  'A small office run through the analyser: 33% of use while closed, £2,776 a year above base load, almost half on Saturdays; base load 2.6 kW; 67% of a 40 kVA supply.',
  crumbs=[HOME, GUIDES, ('Worked example', 'example-office-analysis.html')]))

# ── OUT-OF-HOURS ────────────────────────────────────────────────────────
PAGES.append(guide_page(
  'out-of-hours-electricity.html',
  'Out-of-hours electricity use: how to find and cut it',
  'Out-of-hours electricity use',
  'Electricity used while a building should be closed is often the cheapest kind to cut. This guide explains how to find it in half-hourly data, what usually causes it, and who to involve in fixing it.',
  'How to find out-of-hours electricity use in half-hourly data, what usually causes it, and how to reduce it by changing timers and controls.',
  '''
<p class="answer">Out-of-hours use is electricity used while a building should be closed. On a healthcare estate that means clinics, outpatient departments, health centres, offices, education centres and restaurants, not the 24-hour inpatient supply. To find it, compare each half hour with the opening hours and take away what always has to run (the base load). What's left is the closed-hours excess. It's usually the cheapest use to cut, because the fix is often a change to a timer or control setting.</p>

<h2 id="what">What counts as out-of-hours</h2>
<p>Any half hour outside opening hours counts: evenings, nights, weekends, bank holidays and closure periods. Some of this use is unavoidable. Servers, fridges, security systems and emergency lighting have to run all the time, and together they make up the <a href="base-load.html">base load</a>.</p>
<p>The figure to focus on is the <strong>excess</strong>, meaning use while closed above the base load. The analyser calls this the closed-hours excess and ranks sites by it, so you can see which buildings to look at first.</p>

<h2 id="find">How to find it</h2>
<ol><li><strong>Set the opening hours accurately.</strong> Every figure depends on them, so include bank holidays, closure weeks and any regular evening or weekend use.</li><li><strong>Look at the heatmap.</strong> It shows every half hour of the year on one chart. Opening hours appear as a dark band, and anything dark outside that band is out-of-hours use.</li><li><strong>Break it down by type of day.</strong> Weeknights, Saturdays, Sundays and bank holidays usually have different causes.</li><li><strong>Check the start and end of the day.</strong> If demand rises an hour or two before opening, or stays high after closing, timers or heating start-up settings are usually to blame.</li></ol>

<h2 id="causes">What usually causes it</h2>
<ul><li>Heating, ventilation and air conditioning running to the wrong schedule, or not set up for bank holidays</li><li>Lights left on, or on timers that no longer match how the building is used</li><li>A small evening or weekend booking that runs the whole building</li><li>Equipment left on manual override after maintenance, then forgotten</li><li>IT, catering and hot water equipment left on instead of being put on timers</li></ul>

<h2 id="cut">How to cut it</h2>
<p>Most fixes are changes to settings: building management system schedules, timers, holiday calendars and switch-off routines. Start with the biggest block of use, which is often weekends or a regular evening. Then check the half-hourly data a month later to see whether it worked. The analyser's before-and-after comparison is designed for this.</p>

<h2 id="who">Who to involve</h2>
<p>Fixes usually need two people working together: someone who can change the controls, such as your facilities team or building management system contractor, and someone who knows how the building is really used, such as a site manager or caretaker. Share the heatmap and the breakdown by type of day with both. It's much easier to agree a new schedule when everyone can see exactly when the building is using electricity.</p>
''',
  [('what', 'What counts as out-of-hours'), ('find', 'How to find it'), ('causes', 'What usually causes it'), ('cut', 'How to cut it'), ('who', 'Who to involve')],
  [('Is all out-of-hours use waste?', 'No. Some equipment has to run all the time. The part worth investigating is the excess, meaning use while closed above the base load.'),
   ('Why do opening hours matter so much?', "They decide which half hours count as closed. If a building is used on Saturdays but the calendar says it's closed, Saturday use shows up as out-of-hours. Confirm the hours before acting on the figures."),
   ('How quickly can I see whether a change worked?', "Within a few weeks. Compare the same days before and after the change using the analyser's before-and-after view.")],
  [('base-load.html', 'Base load', 'The other half of the picture: what always runs.'),
   ('example-office-analysis.html', 'Worked example', 'Out-of-hours use in one office, with figures.'),
   ('sectors.html', 'By healthcare setting', 'What normal looks like in hospitals, clinics and support buildings.')],
  'What out-of-hours electricity use is, how to find it in half-hourly data (opening hours, heatmap, day types, start and end of the day), common causes, fixes and who to involve.'))

# ── BASE LOAD ───────────────────────────────────────────────────────────
PAGES.append(guide_page(
  'base-load.html',
  'Base load electricity: what it is and how to cut it',
  'Base load: what never switches off',
  'Every building has a level of electricity use it never drops below. Because that use continues every hour of the year, even small reductions add up.',
  'What base load electricity is, how to measure it from half-hourly data, what makes it up, and how to reduce it. Each kilowatt running all year is 8,760 kWh.',
  '''
<p class="answer">Base load is the minimum electricity a building uses at all times, overnight and at weekends as well as during the day. Each kilowatt of base load runs for 8,760 hours a year. That's 8,760 kWh, or about £2,190 at 25p/kWh. You can measure it from half-hourly data, find out what makes it up, and switch off anything that doesn't need to run.</p>

<h2 id="measure">How to measure it</h2>
<p>The analyser takes every valid half-hourly reading, converts it to kW (the kWh reading divided by half an hour) and finds the level that demand stays above 95% of the time. This is called the 5th percentile, and it's what the analyser uses as the base load.</p>
<p>It doesn't use the single lowest reading, because one meter fault or power cut could set it and make the base load look lower than it really is. The analyser shows the lowest half hour alongside so you can compare.</p>

<h2 id="what">What makes it up</h2>
<ul><li>IT: servers, network equipment and phone systems</li><li>Clinical equipment on standby, imaging cooling and medical gas plant</li><li>Refrigeration: vaccine and pharmacy fridges, kitchen fridges, freezers, vending machines and water coolers</li><li>Pumps and fans that run continuously</li><li>Water heaters and boilers kept on standby</li><li>Security systems, fire alarms and emergency lighting</li><li>Equipment left on standby, or left running by mistake</li></ul>

<h2 id="reduce">How to reduce it</h2>
<ol><li><strong>Walk round the building at night or at a weekend</strong> and note everything that's switched on. It's often a surprise.</li><li><strong>Sort what you find</strong> into must run, could run less, and shouldn't be on.</li><li><strong>Fix the easy ones first</strong>, such as timers on water heaters and vending machines, switch-off routines and combining servers.</li><li><strong>Check the base load every month.</strong> A step up usually means new equipment has been installed or something has been left on. The analyser flags lasting changes like this.</li></ol>

<h2 id="solar">Base load and solar</h2>
<p>Base load runs through the day as well as the night, so it is the part of your demand that solar panels can supply most reliably. The analyser's Solar tab estimates how much of a solar system's output your site would use itself at different sizes, from your own half-hourly readings, and can pass that figure to the ''' + SOLAR + ''' on this site, to work out costs and payback. The <a href="solar.html">solar page</a> explains how.</p>

<h2 id="worth">Working out the saving</h2>
<p>Because base load runs every hour of the year, savings are easy to estimate: multiply the kilowatts you remove by 8,760 hours and by your unit rate. At 25p/kWh, 1 kW is worth about £2,190 a year, and switching off a 0.5 kW water heater that was left on all the time saves about £1,100.</p>
''',
  [('measure', 'How to measure it'), ('what', 'What makes it up'), ('reduce', 'How to reduce it'), ('solar', 'Base load and solar'), ('worth', 'Working out the saving')],
  [('What is a typical base load?', 'It depends on the building. An acute hospital\'s base load is high because wards, theatres, imaging and ventilation run all the time; a health centre\'s is mostly IT, vaccine fridges and security. Compare each site with its own history, and with similar buildings in your estate.'),
   ('Why is my base load higher at weekends than overnight on weekdays?', "It shouldn't be. If it is, something is switching on at weekends, such as frost protection on the heating, a scheduled process or a booking. Check the weekend pattern on the heatmap."),
   ('How much does 1 kW of base load cost?', "It runs 8,760 hours a year, so it uses 8,760 kWh. At 25p/kWh that's about £2,190 a year. Multiply 8,760 by your own rate to check.")],
  [('out-of-hours-electricity.html', 'Out-of-hours use', 'Use above the base load while the building is closed.'),
   ('supply-capacity.html', 'Supply capacity', 'The other end of the scale: your busiest half hours.'),
   ('example-office-analysis.html', 'Worked example', 'Base load in one office, with figures.')],
  'What base load is, how to measure it from half-hourly data (5th percentile, not the minimum), what makes it up, how to reduce it; 1 kW all year is 8,760 kWh.'))

# ── SUPPLY CAPACITY ─────────────────────────────────────────────────────
PAGES.append(guide_page(
  'supply-capacity.html',
  'Supply capacity and kVA: room for heat pumps and EVs',
  'Supply capacity and kVA',
  'Before adding heat pumps, EV chargers or other new equipment, check how close your busiest half hours already come to your agreed supply capacity.',
  'Agreed supply capacity explained: kW to kVA, comparing half-hourly peaks with capacity, and room for heat pumps and EV charging.',
  '''
<p class="answer">Your agreed supply capacity is the maximum demand your electricity connection is set up for, measured in kVA. To see how much room you have, convert your busiest half hours from kW to kVA (divide by the power factor) and compare them with the agreed capacity. The gap is your headroom for new equipment such as heat pumps and EV chargers.</p>

''' + photo('plant-outside', 'Two engineers with a tablet beside packaged plant, flues and pipework outside a large building', "New equipment such as heat pumps has to fit within the site's supply. Half-hourly data shows how close the busiest periods already come to it.") + '''
<h2 id="what">What agreed supply capacity is</h2>
<p>Larger electricity supplies have an agreed capacity, sometimes called authorised or available capacity. It's set in the connection agreement and usually shown on the bill in kVA. You normally pay a daily charge for it whether you use it or not. If you go over it you may face extra charges, and the network operator may ask you to increase it.</p>

<h2 id="kva">kW and kVA</h2>
<p>Meters measure energy in kWh. Half-hourly data gives the average power in each half hour, in kW. Capacity is set in kVA, which also includes reactive power: power drawn by equipment such as motors that doesn't do useful work. The two are linked by the power factor:</p>
<div class="note"><strong>kVA = kW ÷ power factor.</strong> At a power factor of 0.95, a 95 kW peak is 100 kVA. If your bill includes reactive power charges, your power factor is probably below 0.95.</div>

<h2 id="headroom">Working out headroom</h2>
<ol><li><strong>Find your busiest half hours</strong> over at least a year, so winter peaks are included.</li><li><strong>Convert them to kVA</strong> using your power factor.</li><li><strong>Keep a safety margin</strong>, for example 10%, below the agreed capacity.</li><li><strong>Your headroom</strong> is the largest constant extra load you could add without going over that margin in any half hour.</li></ol>
<p>Half-hourly readings are averages, so they smooth out very short spikes. Treat this as an early check, and confirm with your network operator before relying on it.</p>

<h2 id="new-load">Heat pumps and EV charging</h2>
<p>A heat pump uses much less electricity than the heat it produces. With a coefficient of performance (COP) of 3, a heat pump producing 150 kW of heat draws about 50 kW of electricity. It works hardest in winter, which is usually when a building's peaks are highest, so the two add together. EV charging is different: if it happens overnight, it falls when most sites are quietest, although on a 24-hour hospital nights are not quiet. Removing a gas CHP engine adds its full output to grid import; see <a href="moving-away-from-chp.html">moving away from CHP</a> and <a href="hospital-electrical-capacity.html">electrical capacity for electrification</a>. The analyser lets you test a new load at a chosen time of day and season against your actual half-hourly peaks.</p>
<h2 id="solar">Solar panels and your connection</h2>
<p>Solar can reduce the electricity you draw from the grid during the day, but any output you don't use is exported through the same connection. See our <a href="solar-planning-and-grid.html">guide to planning and grid connections</a>. The analyser's Solar tab estimates how much of a system's output your site would use itself. See <a href="solar.html">sizing solar from half-hourly data</a>.</p>
''',
  [('what', 'What agreed supply capacity is'), ('kva', 'kW and kVA'), ('headroom', 'Working out headroom'), ('new-load', 'Heat pumps and EV charging'), ('solar', 'Solar and your connection')],
  [('Where do I find my agreed supply capacity?', 'On your electricity bill or connection agreement, in kVA. Your supplier can confirm it.'),
   ('What power factor should I use?', "If you don't know it, 0.95 is a reasonable starting assumption. It's probably lower if your bill shows reactive power charges."),
   ('Is half-hourly data enough to plan a new connection?', "It's a good first check, but half-hour averages hide very short peaks. For a significant new load, speak to your network operator before committing.")],
  [('base-load.html', 'Base load', 'The demand that never goes away.'),
   ('example-office-analysis.html', 'Worked example', 'Peaks against capacity in one office.'),
   ('how-it-works.html', 'How the analyser works', 'Including how headroom is worked out.')],
  'Agreed supply capacity in kVA, kW to kVA via power factor, headroom from half-hourly peaks with a safety margin, and checking heat pumps and EV charging.'))

# ── READING A HEATMAP ───────────────────────────────────────────────────
PAGES.append(guide_page(
  'reading-a-heatmap.html',
  'How to read a half-hourly electricity heatmap',
  'How to read a half-hourly heatmap',
  'A heatmap shows every half hour of a year on one chart. Once you know what to look for, problems are easy to spot.',
  'How to read a half-hourly electricity heatmap: what the axes and colours mean, what normal looks like, and the patterns that point to waste.',
  '''
<p class="answer">A half-hourly heatmap has one column for each day and one row for each half hour, with darker colours for higher demand. Normal use shows as a dark band during opening hours. Anything dark outside that band, such as at night, at weekends or in holidays, is worth checking.</p>

<h2 id="axes">What you're looking at</h2>
<ul><li><strong>Across:</strong> days, from the start of the period to the end.</li><li><strong>Down:</strong> time of day, from midnight at the top to midnight at the bottom.</li><li><strong>Colour:</strong> demand in that half hour, from pale (low) to dark (high).</li></ul>
<p>A year contains about 17,500 half hours. That's far too many numbers to read in a table, but the heatmap shows them all at once, which is why it's often the quickest way to understand a building.</p>

<figure class="figure"><img src="images/heatmap-office.png" width="2464" height="896" alt="Heatmap of an office year: a dark weekday band, pale nights, and weekends that are sometimes busy" loading="lazy"><figcaption>An office (made-up data). The weekday band is clear, and some Saturdays are as busy as weekdays.</figcaption></figure>

<h2 id="normal">What normal looks like</h2>
<p>For a building used on weekdays, you'd expect a dark horizontal band during working hours, regular pale gaps at weekends, and pale nights. Winter is often slightly darker than summer. The edges of the band show when the building actually starts and stops using electricity each day, which isn't always when the doors open and close.</p>

<h2 id="patterns">Patterns worth checking</h2>
<div class="table-wrap"><table><thead><tr><th>What you see</th><th>What it usually means</th></tr></thead><tbody>
<tr><td>A pale block where it should be blank, such as a holiday week</td><td>Heating or ventilation running to the normal schedule with nobody in</td></tr>
<tr><td>Thin stripes in the evening on the same weekdays</td><td>Regular evening use, such as lettings, classes or cleaning</td></tr>
<tr><td>The dark band starting well before opening</td><td>Heating or ventilation set to start too early</td></tr>
<tr><td>Nights that get darker from a certain date</td><td>New equipment, or something left on, has raised the base load</td></tr>
<tr><td>A single dark column</td><td>One unusual day, such as an event, a fault or a reading error</td></tr>
<tr><td>Grey or striped gaps</td><td>Missing data (not zero use)</td></tr></tbody></table></div>

<h2 id="hospital">Reading a 24-hour site</h2>
<p>A hospital's main supply has no closed hours, so there is no pale weekend gap. Look instead for the overall darkness of the night rows (the base load), any date after which nights get darker, wide summer bands from cooling, and bands of higher import when a CHP engine is off. Separately metered clinics and offices on the site should still show the weekday pattern.</p>

<h2 id="next">Putting a cost on what you see</h2>
<p>The heatmap shows you where to look, and the figures tell you how much it matters. In the analyser, click any day to compare its half hours with a typical day. Then use the out-of-hours and unusual-day findings to put a cost on what you've spotted.</p>
''',
  [('axes', "What you're looking at"), ('normal', 'What normal looks like'), ('patterns', 'Patterns worth checking'), ('hospital', 'Reading a 24-hour site'), ('next', 'Putting a cost on what you see')],
  [('What is a carpet plot?', 'Another name for the same chart: one column per day and one row per half hour, coloured by demand.'),
   ('Why are some days grey?', "They have no valid readings. Missing data is shown as missing rather than as zero, so gaps don't look as if the building was switched off."),
   ('Can I see one day in detail?', 'Yes. In the analyser, click any day on the heatmap to compare its half hours with a typical day of the same kind.')],
  [('example-office-analysis.html', 'Worked example', 'An admin building, explained finding by finding.'),
   ('moving-away-from-chp.html', 'Moving away from CHP', 'Spotting engine outages in your import data.'),
   ('glossary.html', 'Glossary', 'The terms used in these guides.')],
  'How to read a half-hourly heatmap (days across, time of day down, colour for demand) and the patterns that point to waste.'))

# ── PROVING A SAVING ────────────────────────────────────────────────────
PAGES.append(guide_page(
  'proving-savings.html',
  'How to prove an energy saving worked, with half-hourly data',
  'Proving a saving worked',
  "You've changed a setting or replaced some equipment. Half-hourly data can show whether it made a difference, as long as you compare like with like.",
  'How to use half-hourly data to show whether a change saved energy: matched before-and-after periods, the right measure, and what can mislead.',
  '''
<p class="answer">Compare a period before the change with a matching period after it. Use the same days of the week, the same types of day (open, closed, holiday) and enough weeks to even out day-to-day variation. Then look at the part of demand the change should affect, such as base load or out-of-hours use, rather than the total bill.</p>

''' + photo('board-review', 'A team reviewing charts and printed reports around a meeting table, with solar panels and battery units outside the window', 'A saving is easier to sign off when the before-and-after comparison is fair.') + '''
<h2 id="match">Compare like with like</h2>
<ul><li><strong>Compare the same types of day.</strong> Compare weekdays with weekdays and holidays with holidays. A before period with several bank holidays in it will make the after period look better or worse than it really is.</li><li><strong>Use enough data.</strong> Four to eight weeks either side is usually enough to show a real change. A single week can be thrown off by one unusual day.</li><li><strong>Keep the periods close together.</strong> The closer they are, the less the weather and the seasons get in the way.</li><li><strong>Leave out the change itself.</strong> Skip the days when the work was being carried out.</li></ul>

<h2 id="measure">Measure the right thing</h2>
<p>Choose the measure the change should affect:</p>
<div class="table-wrap"><table><thead><tr><th>Change</th><th>Look at</th></tr></thead><tbody>
<tr><td>Heating or ventilation schedules</td><td>Out-of-hours use, and demand around opening and closing</td></tr>
<tr><td>Switching off equipment overnight</td><td>Base load</td></tr>
<tr><td>LED lighting</td><td>Demand during opening hours</td></tr>
<tr><td>Holiday settings in the building controls</td><td>Use during closures</td></tr></tbody></table></div>
<p>Total consumption mixes the effect of your change with everything else that happened, such as changes in occupancy, the weather or new equipment. A genuine saving can get lost in it, and so can a change that didn't work.</p>

<h2 id="weather">Weather and seasons</h2>
<p>Electric heating and cooling depend on the weather. If the period before the change was colder than the period after, some of the drop is down to the weather. For heating changes, compare the same weeks a year apart as a cross-check, or adjust for weather using degree days if you have them.</p>

<h2 id="analyser">In the analyser</h2>
<ul><li><strong>Did a change make a difference?</strong> on the Base load tab compares matched weeks either side of a date you choose.</li><li><strong>Compare periods</strong> on the Heatmap tab shows any two periods side by side.</li><li><strong>Persistent changes</strong> on the Unusual days tab flags lasting shifts automatically, so you can check whether a change shows up when you'd expect.</li></ul>
<p>If you need a formal measurement and verification of savings, for example for a funded project or an energy performance contract, the International Performance Measurement and Verification Protocol (IPMVP) sets out recognised methods.</p>
''',
  [('match', 'Compare like with like'), ('measure', 'Measure the right thing'), ('weather', 'Weather and seasons'), ('analyser', 'In the analyser')],
  [('How long should I wait before checking?', 'Four to eight weeks of data after the change, compared with the same length of time before it, is usually enough to see a real change.'),
   ('Why has our bill not gone down?', 'A saving in one place can be hidden by changes elsewhere, such as occupancy, weather, prices or new equipment. Compare the specific measure the change should affect.'),
   ('Can this replace a formal M&amp;V report?', "It's a good check, but formal measurement and verification (for example under IPMVP) agrees the baseline, adjustments and reporting up front.")],
  [('base-load.html', 'Base load', 'The measure most switch-off changes affect.'),
   ('out-of-hours-electricity.html', 'Out-of-hours use', 'The measure schedule changes affect.'),
   ('hospital-energy-efficiency.html', 'Energy efficiency in hospitals', 'The changes worth proving.')],
  'Proving a saving with half-hourly data: matched before-and-after periods, the right measure for the change, weather effects, and the analyser tools.'))

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
GLOSSARY = [
  ('Balancing Services Use of System (BSUoS)', 'A charge that covers the National Energy System Operator\'s cost of balancing the electricity system. A fixed rate per MWh, set in advance for six-month periods. <a href="non-energy-charges.html#bsuos">More</a>.'),
  ('Capacity Market (CM)', 'A scheme that pays providers to keep enough reliable capacity available. Businesses pay for it according to their electricity use between 4pm and 7pm on working days from November to February. <a href="non-energy-charges.html#cm">More</a>.'),
  ('Climate Change Levy (CCL)', 'A tax on energy used by businesses, charged per kWh. Holders of a climate change agreement pay a reduced rate. <a href="non-energy-charges.html#ccl">More</a>.'),
  ('Contracts for Difference (CfD)', 'Contracts that give low-carbon generators a fixed price. Suppliers pay a levy that rises when wholesale prices are low and falls, even to zero, when they are high. <a href="non-energy-charges.html#cfd">More</a>.'),
  ('Distribution Use of System (DUoS)', 'Charges for using the local distribution network, set by your network operator. They combine unit rates that vary by time band, capacity charges and fixed daily charges. <a href="non-energy-charges.html#duos">More</a>.'),
  ('Non-energy costs', 'Everything in an electricity price apart from the wholesale energy: network charges, policy costs and taxes. <a href="business-electricity-price.html">More</a>.'),
  ('Nuclear RAB levy', 'A levy on suppliers that funds the building of new nuclear power stations under the Regulated Asset Base model, starting with Sizewell C. <a href="non-energy-charges.html#rab">More</a>.'),
  ('Red, amber and green bands', 'The time bands most network operators use for distribution unit rates, with a different price in each. Each operator sets its own times. <a href="non-energy-charges.html#duos">More</a>.'),
  ('Renewables Obligation (RO)', 'A scheme requiring suppliers to present certificates for each MWh they supply, or pay a buy-out price. The cost is passed on per unit. <a href="non-energy-charges.html#ro">More</a>.'),
  ('Transmission Network Use of System (TNUoS)', 'Charges for using the national high-voltage transmission network. For business sites, mainly a fixed charge per site per day, banded by agreed capacity or consumption. <a href="non-energy-charges.html#tnuos">More</a>.'),
  ('Wholesale price', 'The price suppliers pay for electricity on the wholesale market, often called the commodity cost. <a href="electricity-prices-ten-years.html#wholesale">More</a>.'),
  ('Agreed supply capacity', 'The maximum demand, in kVA, an electricity connection is set up for. It appears on larger electricity bills and is also called authorised or available capacity. <a href="supply-capacity.html">More</a>.'),
  ('Annualised figure', 'A yearly figure scaled up from the valid readings available. It is used when the data covers less than a full year or has gaps.'),
  ('Base load', 'The level of demand a building rarely drops below: what never switches off. The analyser measures it as the 5th percentile of half-hourly demand. <a href="base-load.html">More</a>.'),
  ('Closed-hours excess', 'Electricity used while a building should be closed, above its base load. The analyser ranks sites by it. <a href="out-of-hours-electricity.html">More</a>.'),
  ('Coverage', 'The share of expected half-hourly readings that are present and valid.'),
  ('Degree days', 'A measure of how cold (heating degree days) or warm (cooling degree days) a period was. Used to compare energy use across periods with different weather.'),
  ('DNO', "Distribution network operator. The company that runs the local electricity network and your site's connection to it. The first two digits of your MPAN show which one. <a href=\"mpan-profile-class.html#bottom\">More</a>."),
  ('Half-hourly (HH) data', 'A record of the electricity used in every half hour: 48 readings a day.'),
  ('Heatmap', 'A chart of every half hour in a period, with one column per day and one row per half hour, coloured by demand. Also called a carpet plot. <a href="reading-a-heatmap.html">More</a>.'),
  ('kVA', 'Kilovolt-ampere. A measure of apparent power, and the unit supply capacity is set in. kVA = kW ÷ power factor.'),
  ('kW', 'Kilowatt. A measure of power: the rate electricity is being used at a given moment. Divide a half-hourly reading in kWh by 0.5 to get the average kW for that half hour.'),
  ('kWh', 'Kilowatt-hour. A measure of energy, and what you are billed for. Using 1 kW for one hour is 1 kWh.'),
  ('Load factor', 'Average demand divided by peak demand. A low load factor means demand has short, high peaks.'),
  ('Market-wide half-hourly settlement (MHHS)', 'The move to settle every electricity meter in Great Britain using half-hourly data. <a href="half-hourly-settlement.html">More</a>.'),
  ('MPAN', 'Meter point administration number. The 13-digit number on the bottom line of the supply number on an electricity bill. It identifies the supply point. <a href="mpan-profile-class.html">More</a>.'),
  ('Peak demand', 'The highest half-hourly average demand in a period, usually in kW or kVA.'),
  ('Power factor', 'The ratio of real power (kW) to apparent power (kVA), between 0 and 1. Equipment such as motors lowers it.'),
  ('Profile class', 'The first two digits of the top line of the supply number. 00 means the supply is settled half-hourly; 01 to 08 mean use is estimated from standard profiles. <a href="mpan-profile-class.html#top">More</a>.'),
  ('Settlement', "The process that works out how much electricity each supplier's customers used, and when, so suppliers pay the right amount for it."),
  ('Time-of-use tariff', 'A tariff with different unit rates at different times of day, such as day and night rates.'),
]
GLOSSARY += [
  ('Combined heat and power (CHP)', 'An engine, usually gas-fired, that generates electricity on site and recovers its waste heat for heating and hot water. Common on hospital estates; its carbon case has weakened as the grid has cleaned up. <a href="moving-away-from-chp.html">More</a>.'),
  ('Coefficient of performance (COP)', 'How much heat a heat pump delivers for each unit of electricity it uses at a given moment. A COP of 3 means 3 kWh of heat for 1 kWh of electricity. The seasonal average is the SCOP.'),
  ('Distribution network operator (DNO)', 'The company that owns and runs the local electricity network and agrees your supply capacity and any generation connection.'),
  ('EFPMS', 'The Estates and Facilities Performance Management System: the mandatory annual estates and facilities return for NHS Wales, including energy and CHP. <a href="estates-returns-and-benchmarking.html#efpms">More</a>.'),
  ('ERIC', 'The Estates Returns Information Collection: the mandatory annual estates and facilities return for NHS trusts in England, including energy use and costs. <a href="estates-returns-and-benchmarking.html#eric">More</a>.'),
  ('G99', 'The engineering recommendation that sets how most generators, including larger solar systems and batteries, apply to the network operator to connect. <a href="solar-planning-and-grid.html">More</a>.'),
  ('Green Plan', 'An NHS organisation\'s board-approved plan for reducing its carbon emissions and environmental impact, in line with the NHS net zero targets.'),
  ('Heat decarbonisation plan (HDP)', 'A plan for replacing fossil fuel heating with low carbon alternatives, building by building, often required for public sector funding bids. <a href="heat-decarbonisation.html#plan">More</a>.'),
  ('Health Technical Memorandum (HTM)', 'Guidance on the design and operation of healthcare buildings and engineering services, such as HTM 03-01 (ventilation), HTM 04-01 (water safety) and HTM 06-01 (electrical services).'),
  ('NHS Carbon Footprint', 'The emissions the NHS in England controls directly, including energy used in its buildings. The target is net zero by 2040. The Carbon Footprint Plus adds the supply chain, with a 2045 target. <a href="nhs-net-zero-targets.html">More</a>.'),
  ('NHS Net Zero Building Standard', 'The NHS England standard for new buildings and major upgrades that need HM Treasury business case approval, covering energy and whole-life carbon. <a href="nhs-net-zero-targets.html#england">More</a>.'),
  ('Power purchase agreement (PPA)', 'A contract to buy electricity from a generator at an agreed price, often from a solar system a funder owns on your site. <a href="paying-for-solar.html">More</a>.'),
  ('Public Sector Decarbonisation Scheme (PSDS)', 'The UK government grant scheme, run by Salix, that funded heat and energy projects in English public buildings from 2020. No new funding is being committed beyond awarded projects. <a href="decarbonisation-funding.html#england">More</a>.'),
]
GLOSSARY.sort(key=lambda t: t[0].lower())
NAV_PARENT['glossary.html'] = 'guides.html'
PAGES.append(Page(
  'glossary.html', 'Glossary of half-hourly electricity terms',
  'Plain definitions of half-hourly electricity, bill and healthcare estates terms: base load, kW, kVA, MPAN, CHP, COP, ERIC, EFPMS, HTM, PSDS, DUoS, TNUoS and more.',
  page_hero('Guide', 'Glossary', 'Simple definitions of the terms used in half-hourly electricity data and on this site.',
            crumbs=[HOME, GUIDES, ('Glossary', 'glossary.html')], image='glossary')
  + guide(updated_line() + '<p class="answer">Half-hourly (HH) data is a record of the electricity a meter measures in every half hour: 48 readings a day, usually in kWh. The terms you will meet most often are kWh (energy, what you are billed for), kW (how fast electricity is being used at a given moment), base load (the demand that never switches off) and kVA (the unit your supply capacity is set in).</p>'
          + '<dl class="glossary">' + ''.join(
      f'<div id="{re.sub(r"[^a-z0-9]+", "-", t.lower().split(" (")[0]).strip("-")}"><dt>{t}</dt><dd>{d}</dd></div>' for t, d in GLOSSARY) + '</dl>')
  + cta('See the terms in your own data', "It's free, there's no sign-up, and nothing is uploaded."),
  crumbs=[HOME, GUIDES, ('Glossary', 'glossary.html')], article=True, section='Guides',
  summary='Definitions: base load, closed-hours excess, kW, kWh, kVA, power factor, MPAN, profile class, agreed supply capacity, settlement, MHHS, DUoS, TNUoS, BSUoS, Renewables Obligation, CfD, Capacity Market, nuclear RAB, CCL, red/amber/green bands and more.',
  schema=[{'@type': 'DefinedTermSet', 'name': 'Half-hourly electricity glossary', 'hasDefinedTerm': [
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
       ('sectors.html', 'Other settings', 'Acute, community, clinics, ambulance and private.')],
      f'{short}: what normal half-hourly demand looks like, what to check first, how to set the hours, and the capacity and solar questions.',
      crumbs=[HOME, SECTORS, (short, file)]))

SETTINGS_CARDS = [(f, s, lead) for f, s, _, lead, *_ in SECTOR_DATA] + [
    ('private-hospitals.html', 'Private and independent hospitals', 'The same engineering, different targets, finance and reporting duties.'),
]

PAGES.append(Page(
  'sectors.html', 'Healthcare settings: what to look for in your data | Healthcare Energy Insights',
  'What half-hourly electricity data shows in acute hospitals, community and mental health sites, health centres and clinics, ambulance stations and private hospitals.',
  page_hero('Healthcare settings', 'What to look for in your setting', 'Each part of a healthcare estate uses electricity differently. Choose yours to see what normal looks like, what to check first and how to set it up in the analyser.',
            crumbs=[HOME, SECTORS], image='sectors') +
  '<section class="section"><div class="section-inner">' +
  photo('estate-hospital', 'Illustration of a hospital estate with clinical buildings, solar on roofs and car park canopies, plant compounds and a substation', cls='figure figure-wide', lazy=False) +
  '<div class="link-grid">' +
  ''.join(link_card(f, s, lead, 'Read more') for f, s, lead in SETTINGS_CARDS) +
  '</div></div></section>' + cta('Check your whole estate', 'Load every meter at once and the analyser ranks the sites, so you know which to look at first.'),
  crumbs=[HOME, SECTORS], section='Sectors', summary='Index of healthcare settings pages.'))

GUIDE_GROUPS = [
  ('Decarbonising the estate', [
    ('healthcare-estates-decarbonisation.html', 'The estates challenge', 'Targets, heat, CHP, capacity and funding in one place, and where to start.'),
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
    ('example-office-analysis.html', 'Worked example: an admin building', 'What the analyser found in a year of data from one office building.'),
    ('reading-a-heatmap.html', 'How to read a heatmap', 'Every half hour of a year on one chart, and the patterns to look for.'),
    ('base-load.html', 'Base load', 'What always runs, how to measure it and how to reduce it.'),
    ('out-of-hours-electricity.html', 'Out-of-hours electricity use', 'Clinics, offices and other buildings with set hours.'),
    ('supply-capacity.html', 'Supply capacity and kVA', 'The basics of capacity, power factor and headroom.'),
    ('proving-savings.html', 'Proving a saving worked', 'How to compare before and after fairly.'),
    ('half-hourly-settlement.html', 'Half-hourly settlement (MHHS)', 'What the move to half-hourly settlement means.'),
    ('mpan-profile-class.html', 'Reading your MPAN', 'Profile class, network region and meter type.'),
    ('electricity-benchmarks.html', 'Electricity benchmarks', 'Typical kWh per m² by building type.'),
  ]),
  ('Prices and bills', [
    ('business-electricity-price.html', "What's in a non-domestic electricity price", 'Wholesale, network, policy, tax and supplier costs.'),
    ('non-energy-charges.html', 'Non-energy charges explained', 'TNUoS, DUoS, BSUoS, levies and taxes.'),
    ('electricity-prices-ten-years.html', 'Ten years of electricity prices', 'What organisations paid from 2015 to 2026, and why.'),
    ('non-energy-costs-outlook.html', 'Where non-energy costs are heading', 'Published forecasts and decisions for 2027 and beyond.'),
    ('glossary.html', 'Glossary', 'kW, kVA, ERIC, HTM, PSDS, CHP and other terms.'),
  ]),
]
GUIDE_LIST = [g for _, items in GUIDE_GROUPS for g in items]
NAV_PARENT['get-your-data.html'] = 'guides.html'
PAGES.append(Page(
  'guides.html', 'Guides for healthcare estates: decarbonisation, solar and half-hourly data',
  'Plain guides for NHS and private healthcare estates teams: net zero targets, funding, heat pumps, moving away from CHP, electrical capacity, solar and half-hourly electricity data.',
  page_hero('Guides', 'Guides for healthcare estates', 'Clear answers to the questions estates, facilities and energy teams ask about decarbonisation, solar and half-hourly data.',
            crumbs=[HOME, GUIDES], image='guides') +
  '<section class="section"><div class="section-inner">' +
  ''.join(f'<h2 class="section-title" style="margin-top:40px">{g}</h2><div class="link-grid">' + ''.join(link_card(f, t, d) for f, t, d in items) + '</div>'
          for g, items in GUIDE_GROUPS) +
  '<p class="note" style="margin-top:32px">Looking for your setting? See <a href="sectors.html" style="color:var(--blue);text-decoration:underline">what to look for by healthcare setting</a>.</p></div></section>'
  + cta('Ready to look at your own data?', "It's free, there's no sign-up, and nothing is uploaded."),
  crumbs=[HOME, GUIDES], section='Guides', summary='Index of guides.'))
