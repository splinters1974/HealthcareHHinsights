"""
Solar guides written for healthcare estates: payback, planning and grid
connection, and paying for solar. They replace the general versions copied
from the UK Solar Calculator; its general guides to cost, generation and the
calculator's method stay on this site with a canonical link to the original.

Figures from the solar calculator's method (running costs, degradation, export
rate) match tools/content/solar/solar-calculator-method.html. Hospital figures
come from the worked example (site/samples/example-hospital.csv).

REVIEW EVERY SIX MONTHS: G99 thresholds, permitted development rules, the
business rates exemption, capital allowances, and Great British Energy funding.
"""
from kit import sources
from pages_guides import GUIDES, HOME, guide_page

def ref(*n):
    return f'<sup><a href="#sources">{",".join(str(x) for x in n)}</a></sup>'


def crumbs(short, file):
    return [HOME, GUIDES, (short, file)]


PAGES = []

# ── PAYBACK ─────────────────────────────────────────────────────────────
SRC = [
    ('How the solar calculator works (method and assumptions)', 'solar-calculator-method.html'),
    ('Explanatory Memorandum to SI 2022/405, business rates exemption for renewable plant',
     'https://www.legislation.gov.uk/uksi/2022/405/pdfs/uksiem_20220405_en.pdf'),
    ('GOV.UK: Capital allowances, rates and pools', 'https://www.gov.uk/work-out-capital-allowances/rates-and-pools'),
    ('NHS England Digital: Estates Returns Information Collection (ERIC)',
     'https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection'),
]
PAGES.append(guide_page(
  'solar-payback.html',
  'Hospital solar payback: what decides it and how to shorten it',
  'Solar payback on healthcare sites',
  "Payback is the first question a finance team asks. On a hospital, the answer depends less on panel prices than on how much of the output the site uses, what it pays per unit, and what's happening to the roof and the CHP engine.",
  'What sets solar payback on hospitals and health centres: share used on site, unit price, mounting, CHP, roof condition and funding route, and how to shorten it.',
  f'''
<p class="answer">Solar payback is the number of years until the savings equal the installed cost. On a 24-hour hospital it's usually helped by a high share of output used on site, and held back by lower unit prices on large supply contracts, costly car park canopies and roofs that need work first. Run your own site through the {'<a href="solar-calculator.html">solar calculator</a>'} with the share used on site measured from your half-hourly data, rather than relying on a typical figure.</p>

<h2 id="meaning">What payback does and doesn't tell you</h2>
<p>The calculator reports simple payback: the year when cumulative savings pass the installed cost, without discounting.{ref(1)} It's a fair first filter for a capital bid, but it ignores the 15 to 20 years of savings after break-even, which is where most of a solar system's value sits. For comparing solar with other uses of the same capital, look at the 25-year net benefit the calculator also shows.{ref(1)}</p>
<p>If a funder pays for the system under a power purchase agreement (PPA), there's no payback at all, because you spend no capital. You compare the PPA rate with what you'd otherwise pay per unit. See <a href="paying-for-solar.html">paying for solar</a>.</p>

<h2 id="drivers">What decides payback on a healthcare site</h2>
<div class="table-wrap"><table><thead><tr><th>Factor</th><th>What's different on hospitals</th></tr></thead><tbody>
<tr><td><strong>Share used on site</strong></td><td>Usually high, because wards and plant run through every sunny afternoon and weekend. Our made-up <a href="example-hospital-analysis.html#solar">community hospital</a> uses 99.8% of a 299 kWp system's output. Health centres closed at weekends use less.</td></tr>
<tr><td><strong>Unit price</strong></td><td>Large hospitals often buy at lower unit rates than small businesses, so each kWh saved is worth a little less. Use your real all-in unit rate, not a headline figure.</td></tr>
<tr><td><strong>Mounting</strong></td><td>Flat roofs crowded with plant, flues and walkways fit fewer panels. Car park canopies add space but cost more per kWp because of the steelwork.</td></tr>
<tr><td><strong>CHP</strong></td><td>While a gas CHP engine covers part of the load, solar replaces less grid import. When the engine goes, there's more import to replace. Model the site you'll have.</td></tr>
<tr><td><strong>Roof condition</strong></td><td>If a roof needs replacing within ten years, do it first. Lifting and refitting panels later costs money and time. Roofs feature heavily in NHS backlog maintenance reported through ERIC.{ref(4)}</td></tr>
<tr><td><strong>Location</strong></td><td>Southern England generates more per kWp than Scotland, so the same system pays back sooner in the south.{ref(1)}</td></tr>
</tbody></table></div>

<h2 id="included">What the calculator's payback includes</h2>
<p>The figure covers the installed cost, savings on electricity used on site, export income at 5p/kWh, electricity prices rising 3% a year, panel output falling 1% in year one and 0.4% a year after, one inverter replacement in year 13, and running costs for maintenance, monitoring and insurance rising with inflation.{ref(1)} It doesn't include roof repairs, structural work, any DNO reinforcement charge, finance costs or your own staff time. Those come from a survey and the DNO offer.</p>

<h2 id="public">NHS bodies and private hospitals are different</h2>
<ul>
<li><strong>Business rates.</strong> Hospitals pay business rates, and in England plant used for on-site renewable generation, and batteries used with it, has been exempt from April 2022.{ref(2)} Solar shouldn't add to your rates bill.</li>
<li><strong>Tax relief.</strong> NHS bodies don't pay corporation tax, so capital allowances don't help them. Independent hospital groups that do can claim allowances on solar, which is special rate plant.{ref(3)} Check the position with your tax adviser.</li>
<li><strong>VAT.</strong> How much VAT can be recovered differs between NHS bodies and private companies. Ask your finance team before comparing a purchase with a PPA, because it changes the capital cost.</li>
</ul>

<h2 id="shorten">How to shorten payback</h2>
<ol>
<li><strong>Measure the share used on site</strong> from half-hourly data instead of assuming it. On a 24-hour site the measured figure is often higher than the default.</li>
<li><strong>Size to what you'll use.</strong> A system the site uses entirely usually pays back faster than a bigger one that exports at weekends.</li>
<li><strong>Put the panels on sound roofs first</strong>, and car park canopies where roofs run out or need replacing.</li>
<li><strong>Combine projects.</strong> Doing solar alongside a roof replacement or LED upgrade shares access, scaffolding and design costs.</li>
<li><strong>Check funding first.</strong> A grant or a PPA changes the capital cost, and with it the payback. See <a href="decarbonisation-funding.html">funding for healthcare decarbonisation</a>.</li>
</ol>
''' + sources(SRC),
  [('meaning', 'What payback tells you'), ('drivers', 'What decides payback'), ('included', "What's included"), ('public', 'NHS and private differences'), ('shorten', 'How to shorten it'), ('sources', 'Sources')],
  [('How long does solar take to pay back on a hospital?', 'It depends on the site, but a 24-hour hospital that uses nearly all its output usually does better than an office of the same size. Measure the share used on site from half-hourly data and run the figures in the solar calculator for your roof, region and unit price.'),
   ('Does an NHS trust get tax relief on solar?', 'No. NHS bodies do not pay corporation tax, so capital allowances do not apply. Independent hospital companies can usually claim them.'),
   ('Will solar increase our business rates?', 'Not in England. On-site renewable generation, and batteries used with it, are exempt from business rates from April 2022 under SI 2022/405.'),
   ('Does a battery shorten payback?', 'Rarely on a 24-hour hospital, which already uses most of its solar. A battery adds cost, so it usually lengthens payback unless the array is large enough to export a lot at weekends.')],
  [('solar.html', 'Sizing from HH data', 'Measure the share a hospital would use.'),
   ('paying-for-solar.html', 'Paying for solar', 'Capital, PPAs and funding for NHS and private sites.'),
   ('solar-on-healthcare-estates.html', 'Solar on healthcare estates', 'The wider case and the practical hurdles.')],
  'Solar payback on hospitals: share used on site (99.8% at 299 kWp in the example hospital), unit price, mounting, CHP, roof condition, business rates exemption, NHS versus private tax, and how to shorten payback.',
  crumbs=crumbs('Solar payback', 'solar-payback.html')))

# ── PLANNING AND GRID ───────────────────────────────────────────────────
SRC = [
    ('National Grid Electricity Distribution: G99 connection procedures', 'https://connections.nationalgrid.co.uk/g99-connection-procedures/'),
    ('CLA: Amendments to permitted development rights for solar (December 2023)', 'https://www.cla.org.uk/news/amendments-to-permitted-development-rights-for-solar/'),
    ('Herbert Smith Freehills Kramer: Connections reform, first ready and needed, first connected (2025)',
     'https://www.hsfkramer.com/notes/energy/2025-posts/Clean-Power-2030--Connections-reform----first-ready-and-needed,-first-connected-'),
]
PAGES.append(guide_page(
  'solar-planning-and-grid.html',
  'Hospital solar: planning permission and grid connection',
  'Solar planning and grid connection for healthcare sites',
  "On a hospital the panels are the easy part. The DNO application, listed buildings, helipads, works around clinical areas and the standby generators are what decide the programme.",
  'Planning and grid connection for solar on hospitals and health centres: G99, export limits, permitted development, listed buildings, helipads, generators and timelines.',
  f'''
<p class="answer">Almost every hospital solar system needs approval from the local distribution network operator (DNO) under G99, and that is usually the longest step. Rooftop solar on non-domestic buildings in England is generally permitted development, but listed buildings, conservation areas and car park canopies need more care. Hospital sites add their own checks: glint and glare near helipads, infection control during works, and how the inverters behave when the site runs on its generators.</p>

<h2 id="g99">The grid connection: G99</h2>
<p>Systems above 50 kW three-phase need a full G99 application, a network study and a formal connection offer before they're installed. Smaller commercial systems use a shorter G99 form, and only domestic-scale systems can install first and notify afterwards under G98.{ref(1)} Larger systems are grouped by size, with Type A covering over 50 kW up to 1 MW and Type B from 1 MW to under 10 MW, and testing and paperwork grow with size.{ref(1)}</p>
<p>Allow around 12 weeks for a typical rooftop application to reach an offer, longer where the local network is constrained. Since 2025 the queue for larger connections has been reordered on a "first ready and needed, first connected" basis, so a complete, well-evidenced application matters more.{ref(3)}</p>
<p><strong>Export limits are cheap for hospitals.</strong> If the network can't take full export, the DNO may offer a connection with an export limit, enforced by a control system. A 24-hour hospital exports little of a well-sized system's output, so a limit usually costs very little and can get a quicker, cheaper offer. Your half-hourly data shows how much you'd export at each size; see <a href="solar.html">sizing solar from half-hourly data</a>.</p>

<h2 id="planning">Planning permission</h2>
<p>In England, since December 2023, rooftop solar on non-domestic buildings has been permitted development with no capacity limit. Solar canopies over non-domestic car parks have their own permitted development right, up to 4 metres high and at least 10 metres from homes, but need prior approval from the council before work starts.{ref(2)}</p>
<ul>
<li><strong>Listed buildings</strong> still need listed building consent. Many older hospital and asylum-era sites have listed blocks, so map them before choosing roofs.</li>
<li><strong>Conservation areas and Article 4 directions</strong> can remove or limit permitted development.</li>
<li><strong>Ground-mounted arrays</strong> on spare land usually need full planning permission.</li>
<li><strong>Scotland and Wales</strong> have their own rules. Speak to the planning authority early wherever you are.</li>
</ul>

<h2 id="hospital">Checks specific to hospital sites</h2>
<div class="table-wrap"><table><thead><tr><th>Issue</th><th>What to do</th></tr></thead><tbody>
<tr><td>Helipads</td><td>Commission a glint and glare assessment for any array near the landing site or its approach paths.</td></tr>
<tr><td>Works near clinical areas</td><td>Agree access routes, crane lifts, noise and dust controls with the clinical teams, and carry out an infection prevention and control risk assessment for the works.</td></tr>
<tr><td>Standby generators and essential supplies</td><td>Under G99, inverters disconnect when the grid is lost. If the array feeds a switchboard the generators back up, the designer must make sure it behaves correctly when the site runs on generators, including during the monthly test.</td></tr>
<tr><td>Fire safety</td><td>Involve your fire safety adviser and insurer early. Rooftop systems are expected to follow recognised fire guidance, with isolation and cable routing designed in.</td></tr>
<tr><td>Roof condition</td><td>Get a structural survey, check remaining roof life, and look for asbestos and fragile rooflights, all common on older NHS buildings.</td></tr>
<tr><td>PFI buildings</td><td>The project company's consent is needed for works on a PFI building, and the contract may need a variation. Start that conversation first.</td></tr>
</tbody></table></div>

<h2 id="timeline">A realistic timeline</h2>
<p>A straightforward rooftop project typically takes five to seven months from first estimate to switch-on: about a month for feasibility, two months for survey and design, the DNO application running alongside for about three months, then contract, installation and commissioning. On a hospital, add time for the checks above, for procurement through an approved route, and for any PFI variation. Car park canopies and ground mounts that need planning take longer.</p>
''' + sources(SRC),
  [('g99', 'The grid connection: G99'), ('planning', 'Planning permission'), ('hospital', 'Checks specific to hospitals'), ('timeline', 'A realistic timeline'), ('sources', 'Sources')],
  [('Do we need planning permission for solar on a hospital roof?', 'In England, usually not, because rooftop solar on non-domestic buildings is permitted development. Listed buildings, sites with an Article 4 direction and some protected areas are exceptions, and the rules differ in Scotland and Wales.'),
   ('Do solar car park canopies need planning permission?', 'In England they can be permitted development, within limits on height and distance from homes, but you need the council\'s prior approval before starting.'),
   ('How long does a DNO connection take?', 'Allow around 12 weeks for a typical rooftop application to reach an offer, and longer where the network is constrained or reinforcement is needed.'),
   ('Will installing solar disrupt clinical services?', 'Usually very little, because most of the work happens on the roof. The final connection needs a short, planned shutdown of the supply it connects to. On a hospital, agree the timing with the clinical teams and estates, and keep essential services on their standby supply while the work is done.'),
   ('What happens to the solar when the hospital is on generators?', 'G99 protection disconnects the inverters when the grid supply is lost. How the array behaves on a generator-backed switchboard is a design question to settle with your electrical engineer.')],
  [('solar-on-healthcare-estates.html', 'Solar on healthcare estates', 'The wider case and what to plan for.'),
   ('supply-capacity.html', 'Supply capacity', 'Headroom on your connection.'),
   ('solar-payback.html', 'Solar payback', 'What decides it on a hospital.')],
  'Planning and grid connection for hospital solar: G99 types and timescales, export limits (cheap for 24-hour sites), permitted development in England since December 2023, listed buildings, helipad glint and glare, generators, PFI consent and a typical timeline.',
  crumbs=crumbs('Planning and grid connection', 'solar-planning-and-grid.html')))

# ── PAYING FOR SOLAR ────────────────────────────────────────────────────
SRC = [
    ('NHS England: £100 million from Great British Energy for NHS trusts to install solar panels and battery storage (21 March 2025)',
     'https://www.england.nhs.uk/blog/100-million-funding-from-great-british-energy-for-nhs-trusts-to-install-solar-panels-and-battery-storage-systems/'),
    ('GOV.UK: Local Power Plan (February 2026)', 'https://assets.publishing.service.gov.uk/media/698b50136c8ef8db1fcfd88e/gbe-local-power-plan-2026.pdf'),
    ('CIBSE Journal: Axe falls on Public Sector Decarbonisation Scheme', 'https://www.cibsejournal.com/news/axe-falls-on-public-sector-decarbonisation-scheme/'),
    ('Explanatory Memorandum to SI 2022/405, business rates exemption for renewable plant',
     'https://www.legislation.gov.uk/uksi/2022/405/pdfs/uksiem_20220405_en.pdf'),
    ('GOV.UK: Capital allowances, rates and pools', 'https://www.gov.uk/work-out-capital-allowances/rates-and-pools'),
    ('GOV.UK: Annual Investment Allowance', 'https://www.gov.uk/capital-allowances/annual-investment-allowance'),
]
PAGES.append(guide_page(
  'paying-for-solar.html',
  'Paying for solar on NHS and private hospital sites',
  'Paying for solar on healthcare sites',
  'Capital budgets, grants, power purchase agreements and leases each suit different organisations. For the NHS the questions are about capital limits and accounting as much as returns.',
  'How NHS trusts, health boards and private hospitals pay for solar: capital, Great British Energy funding, PPAs, leases, accounting, tax, VAT and business rates.',
  f'''
<p class="answer">NHS organisations usually pay for solar from their capital allocation, with grant funding where it's available, or through a power purchase agreement (PPA) where a funder owns the system and the trust buys the electricity. Buying gives the most value over the system's life; a PPA needs no capital. Independent hospital groups have the same options plus tax relief on what they buy.</p>

<h2 id="routes">The main routes</h2>
<div class="table-wrap"><table><thead><tr><th>Route</th><th>Capital needed</th><th>Who owns it</th><th>Best for</th></tr></thead><tbody>
<tr><td>Capital purchase</td><td>All of it</td><td>You</td><td>Trusts with capital headroom and a long future on the site</td></tr>
<tr><td>Grant plus capital</td><td>Part</td><td>You</td><td>Projects that fit an open funding round</td></tr>
<tr><td>Power purchase agreement</td><td>None</td><td>The funder, often transferring to you at the end</td><td>Sites short of capital, or with capital earmarked for backlog</td></tr>
<tr><td>Lease or asset finance</td><td>Little or none</td><td>The lessor or lender, then you</td><td>Private hospital groups; check the accounting first in the NHS</td></tr>
</tbody></table></div>

<h2 id="funding">Grant funding for NHS solar</h2>
<p>In March 2025, NHS England announced £100 million from Great British Energy for NHS trusts to install solar panels and battery storage.{ref(1)} Great British Energy's Local Power Plan, published in February 2026, set out further support for local and public sector energy, including solar and batteries on public buildings.{ref(2)} The Public Sector Decarbonisation Scheme, long the main grant for NHS heat and energy projects, isn't being funded for new rounds beyond 2027/28.{ref(3)} Scotland and Wales run their own routes. Rounds open and close quickly, so check the current position on our <a href="decarbonisation-funding.html">funding page</a>.</p>

<h2 id="ppa">Power purchase agreements</h2>
<p>Under an on-site PPA, a funder designs, installs, owns, insures and maintains the system, and you pay for the electricity you use at an agreed rate per kWh, usually below your grid price. Terms typically run 10 to 25 years, with the rate rising each year by a fixed percentage or with inflation. Before signing, check:</p>
<ul>
<li><strong>The rate and the escalator.</strong> A low starting rate rising steeply can end up dearer than the grid.</li>
<li><strong>The accounting.</strong> Ask your finance team early whether the PPA would be treated as a lease, because that can bring it onto the balance sheet and against capital limits.</li>
<li><strong>Roof works and access.</strong> What happens if a roof must be repaired, or a block demolished or rebuilt, during the term.</li>
<li><strong>The end of the term.</strong> Transfer to the trust, extension or removal.</li>
<li><strong>PFI and landlords.</strong> On a PFI building or a leased health centre, the project company or landlord must agree, and the term should fit their contract.</li>
</ul>
<p>Measuring the share used on site from half-hourly data matters for a PPA too: you only pay for what you use, so the funder's offer depends on it.</p>

<h2 id="stall">Why PPAs stall in healthcare, and how to unblock them</h2>
<p>A PPA needs no capital, yet many offers to NHS trusts and independent hospitals never get signed. The reasons are usually the same, and most can be dealt with early:</p>
<ul>
<li><strong>A long commitment the estate strategy can't support.</strong> A 20-year term on a block due for rebuilding in ten years won't get approved. Choose roofs and car parks that the estate strategy keeps, and agree what happens if a building is disposed of.</li>
<li><strong>Nobody owns the decision.</strong> Estates, finance, procurement and the board all have a say, and the offer sits between them. Name one sponsor, agree the procurement route first and set a date for the board paper.</li>
<li><strong>Doubts about the contract.</strong> Rate, escalator, termination, roof access and end-of-term options are unfamiliar to many teams. Ask for a plain-English summary of each, and compare the rate over the full term with a realistic grid price, not today's.</li>
<li><strong>"It only covers a fraction of our electricity."</strong> True, and it's still worth doing. A PPA fixes the price of part of your demand for a long period, which works as a hedge against grid prices as well as a carbon cut. On a 24-hour site, almost all of it is used.</li>
<li><strong>The accounting answer comes late.</strong> If finance only looks at lease treatment once the contract is drafted, the project stops. Ask the question at the start.</li>
</ul>

<h2 id="tax">Tax, VAT and business rates</h2>
<ul>
<li><strong>Business rates.</strong> In England, on-site renewable generation, and batteries used with it, is exempt from business rates from April 2022.{ref(4)}</li>
<li><strong>Capital allowances.</strong> Only relevant to organisations paying corporation tax, such as independent hospital groups. Solar is special rate plant, so the relief is through the 50% first-year allowance for companies or the Annual Investment Allowance, not full expensing.{ref(5, 6)}</li>
<li><strong>VAT.</strong> Recovery differs between NHS bodies and private companies. Confirm the position before comparing buying with a PPA.</li>
</ul>
<p class="note">General information only, not tax or accounting advice. Rules change; check with your finance team or adviser.</p>

<h2 id="choose">Which route suits you?</h2>
<ul>
<li><strong>NHS trust with capital and a grant round open:</strong> buy, and use the grant to close the gap.</li>
<li><strong>NHS trust with capital tied up in backlog:</strong> compare a PPA through an approved procurement route.</li>
<li><strong>Independent hospital group:</strong> compare buying with capital allowances against a PPA.</li>
</ul>
<p>The <a href="solar-calculator.html">solar calculator</a> shows buying and a PPA side by side for your site.</p>
''' + sources(SRC),
  [('routes', 'The main routes'), ('funding', 'Grant funding'), ('ppa', 'Power purchase agreements'), ('stall', 'Why PPAs stall'), ('tax', 'Tax, VAT and rates'), ('choose', 'Which route suits you'), ('sources', 'Sources')],
  [('Is there grant funding for solar on NHS sites?', 'There has been: in March 2025 NHS England announced £100 million from Great British Energy for NHS trust solar and batteries. Funding rounds change often, so check the current position before planning around a grant.'),
   ('Does a PPA count against an NHS trust\'s capital limit?', 'It can, if it is treated as a lease for accounting purposes. Ask your finance team to review the contract terms before you sign.'),
   ('Can NHS trusts claim capital allowances on solar?', 'No, because NHS bodies do not pay corporation tax. Private hospital companies usually can, through the 50% first-year allowance or the Annual Investment Allowance.'),
   ('Can we put solar on a health centre we lease?', 'Yes, with the landlord\'s consent, which for many health centres means NHS Property Services, Community Health Partnerships or a private landlord. Your lease should run longer than the payback period or PPA term, and you should agree who owns the system at the end.'),
   ('Will solar raise our business rates?', 'Not in England, where on-site renewable generation and associated batteries are exempt from business rates from April 2022.')],
  [('decarbonisation-funding.html', 'Funding', 'Current routes in England, Scotland and Wales.'),
   ('solar-payback.html', 'Solar payback', 'What decides it on a hospital.'),
   ('solar-on-healthcare-estates.html', 'Solar on healthcare estates', 'The wider case.')],
  'Paying for hospital solar: capital purchase, grants (GBE £100m for NHS solar announced March 2025; PSDS not funded for new rounds beyond 2027/28), PPAs and their accounting, leases, business rates exemption in England, and tax for private hospitals.',
  crumbs=crumbs('Paying for solar', 'paying-for-solar.html')))
