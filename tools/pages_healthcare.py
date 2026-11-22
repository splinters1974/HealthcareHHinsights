"""
Healthcare decarbonisation guides: the estates challenge (the hub page), net
zero targets in England, Scotland and Wales, funding routes, heat
decarbonisation, moving away from gas CHP, electrical capacity, solar on
healthcare estates, energy efficiency, estates returns and benchmarking.

Written for NHS and independent-sector estates, facilities and energy
managers: plain words, terms explained on first use, every figure sourced and
dated. Policy and funding change quickly, so REVIEW EVERY SIX MONTHS, and
straight away when a funding round opens or closes. CHECKED is when the
sources were last read.

Nothing here is NHS guidance. Pages say so where it matters, and link to the
NHS England, Scottish Government and Welsh Government sources.
"""
from kit import long_date, photo
from pages_guides import GUIDES, HOME, guide_page

CHECKED = '2026-11-18'


def ref(*n):
    return f'<sup><a href="#sources">{",".join(str(x) for x in n)}</a></sup>'


def srcs(items):
    return ('<div class="sources"><h2 id="sources">Sources</h2>'
            f'<p class="help">Checked {long_date(CHECKED)}.</p><ol>'
            + ''.join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in items) + '</ol></div>')


NOT_NHS = ('<div class="note"><strong>Independent guidance.</strong> Hospital Energy Insights is not part of, or endorsed by, the NHS, '
           'NHS England, the Scottish Government or the Welsh Government. We summarise their published policy and link to it. '
           'Always check the source and your own organisation\'s policies before relying on it.</div>')

# ── Sources used on more than one page ─────────────────────────────────
S = {
    'nz': ('NHS England: Delivering a net zero NHS', 'https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/'),
    'nz5': ('NHS England: Five years of a greener NHS, progress and forward look', 'https://www.england.nhs.uk/long-read/five-years-greener-nhs-progress-forward-look/'),
    'nzbs': ('NHS England: NHS Net Zero Building Standard', 'https://www.england.nhs.uk/estates/nhs-net-zero-building-standard/'),
    'scot': ('Scottish Government: NHS Scotland climate emergency and sustainability strategy 2022 to 2026 (sustainable buildings and land)',
             'https://www.gov.scot/publications/nhs-scotland-climate-emergency-sustainability-strategy-2022-2026/pages/8/'),
    'scot25': ('Scottish Government: NHS Scotland climate emergency and sustainability annual report 2025',
               'https://www.gov.scot/publications/nhs-scotland-climate-emergency-sustainability-annual-report-2025/pages/3/'),
    'wales': ('Welsh Government: NHS Wales decarbonisation strategic delivery plan 2025 to 2030, Part 6: buildings and land',
              'https://www.gov.wales/nhs-wales-decarbonisation-strategic-delivery-plan-2025-2030-buildings-and-land-html'),
    'walest': ('Hywel Dda University Health Board: decarbonisation action plan reporting (NHS Wales interim targets)',
               'https://hduhb.nhs.wales/about-us/performance-targets/performance-documents/2022-2023-qualitative-reporting-decarbonisation-action-plans/'),
    'eric': ('NHS England Digital: Estates Returns Information Collection, summary page and dataset for ERIC 2025/26',
             'https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection/summary-page-and-dataset-for-eric-2025-26'),
    'eric24': ('Building Better Healthcare: ERIC 2024/25 shows £15.9bn maintenance backlog (31 October 2025)',
               'https://buildingbetterhealthcare.com/data-released-by-nhs-digital-shows-15-9bn-backlog'),
    'psds': ('Salix Finance: Public Sector Decarbonisation Scheme update', 'https://www.salixfinance.co.uk/news/public-sector-decarbonisation-scheme'),
    'psds4': ('Salix Finance: Phase 4 Public Sector Decarbonisation Scheme, project criteria',
              'https://salixfinance.co.uk/phase-4-public-sector-decarbonisation-scheme-project-criteria'),
    'hdp': ('Salix Finance: Guidance on the preparation of heat decarbonisation plans (Phase 4 Low Carbon Skills Fund)',
            'https://www.salixfinance.co.uk/sites/default/files/2023-03/Heat%20Decarbonisation%20Plan%20Guidance%20Phase%204%20LCSF.pdf'),
    'gbe100': ('NHS England: £100 million from Great British Energy for NHS trusts to install solar panels and battery storage (21 March 2025)',
               'https://www.england.nhs.uk/blog/100-million-funding-from-great-british-energy-for-nhs-trusts-to-install-solar-panels-and-battery-storage-systems/'),
    'gbe1': ('Great British Energy: first anniversary announcement (15 May 2026)', 'https://www.gbe.gov.uk/node/131'),
    'clean': ('GOV.UK: Clean energy upgrades for hospitals and military sites (February 2026)',
              'https://www.gov.uk/government/news/clean-energy-upgrades-for-hospitals-and-military-sites'),
    'tewv': ('Tees, Esk and Wear Valleys NHS Foundation Trust: new clean energy upgrades at our trust (6 February 2026)',
             'https://www.tewv.nhs.uk/new-clean-energy-upgrades-at-our-trust/'),
    'phu': ('Portsmouth Hospitals University NHS Trust: extra solar panels funded by Great British Energy (27 October 2025)',
            'https://www.porthosp.nhs.uk/about-us/news/portsmouth-hospitals-university-nhs-trust-awarded-pound-17m-funding-extra-solar-panels-will-help-support-investment-frontline-ca'),
    'lpp': ('GOV.UK: Local Power Plan', 'https://www.gov.uk/government/publications/local-power-plan/local-power-plan-accessible-webpage'),
    'scotfoi': ('Scottish Government: NHS Scotland estate decarbonisation project information, FOI release (19 May 2026)',
                'https://www.gov.scot/publications/foi-202600513595/'),
    'scotdev': ('Salix Finance: Scottish Government opens clean heat fund for public sector', 'https://www.salixfinance.co.uk/news/scotland-clean-heat-fund'),
    'walesloan': ('Salix Finance: Wales Funding Programme (Salix loans and Invest to Save)', 'https://www.salixfinance.co.uk/loans/welsh-loans'),
    'wges': ('Welsh Government: Energy Service impact report 2024 to 2025', 'https://www.gov.wales/energy-service-impact-report-2024-2025-html'),
    'ghg26': ('Department for Energy Security and Net Zero: Greenhouse gas reporting, conversion factors 2026',
              'https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2026'),
    'netb': ('NHS England: NHS Estates Technical Bulletin 2026/1, generating energy efficiency savings through controlling theatre ventilation (July 2026)',
             'https://www.england.nhs.uk/wp-content/uploads/2026/07/PRN02301-netb-2026-1-energy-savings-in-theatres-v1.1.pdf'),
    'hnz': ('Department for Energy Security and Net Zero: Heat network zoning, overview of proposals (January 2026)',
            'https://assets.publishing.service.gov.uk/media/697876793fd50ac304b7979b/heat-network-zoning-proposals-overview-slidedeck.pdf'),
    'brid': ('Renewable Energy Installer: Bridlington Hospital heat pump and solar project',
             'https://renewableenergyinstaller.co.uk/?p=39506'),
    'notts': ('Building Better Healthcare: UK\'s last coal-heated hospital switches to clean energy after £34.8m overhaul',
              'https://buildingbetterhealthcare.com/uk-s-last-coal-heated-hospital-switches-to-clean'),
    'nottsv': ('Vital Energi: UK\'s last coal-heated hospital completes switch to clean energy (11 May 2026)',
               'https://www.vitalenergi.co.uk/media/press-releases/uk-s-last-coal-heated-hospital-completes-switch-to-clean-energy/'),
    'efpms': ('NHS Wales Shared Services Partnership, Specialist Estates Services: Estates and Facilities Performance Management System (EFPMS)',
              'https://nwssp.nhs.wales/ourservices/specialist-estates-services/our-services/facilities-management/'),
    'efpmsdef': ('NWSSP Specialist Estates Services: EFPMS data definitions and completion notes 2025/26',
                 'https://nwssp.nhs.wales/ourservices/specialist-estates-services/specialist-estates-services-documents/ses-miscellaneous-documents/efpms-25-26-data-definitions-pdf/'),
    'ericstd': ('NHS standards directory: Estates Return Information Collection', 'https://standards.nhs.uk/published-standards/estates-return-information-collection'),
    'eui': ('Buildings (MDPI): Energy use intensity in England\'s NHS acute hospitals, 2018 to 2025', 'https://www.mdpi.com/2075-5309/16/9/1782/htm'),
    'esos': ('GOV.UK: How to comply with the Energy Savings Opportunity Scheme (ESOS) Phase 4',
             'https://www.gov.uk/government/publications/comply-with-the-energy-savings-opportunity-scheme-esos-phase-4/how-to-comply-with-the-energy-savings-opportunity-scheme-esos-phase-4'),
    'esosbs': ('Burges Salmon: ESOS Phase 4 key dates', 'https://www.burges-salmon.com/?p=18371'),
    'ihpn': ('Independent Healthcare Providers Network: Net Zero Commitment', 'https://www.ihpn.org.uk/net-zero-commitment/'),
    'supp': ('NHS England: Greener NHS, suppliers and the net zero supplier roadmap', 'https://www.england.nhs.uk/greenernhs/get-involved/suppliers/'),
    'crp27': ('NHS England: 2027 NHS carbon reduction plan requirements for the procurement of NHS goods, services and works',
              'https://www.england.nhs.uk/long-read/2027-nhs-carbon-reduction-plan-requirements-for-the-procurement-of-nhs-goods-services-and-works/'),
}


def sources_for(*keys):
    return srcs([S[k] for k in keys])


def n(keys, key):
    """Position of a source in this page's list, for the superscript."""
    return keys.index(key) + 1


PAGES = []

# ── THE HUB: THE ESTATES CHALLENGE ─────────────────────────────────────
K = ['nz', 'nz5', 'scot25', 'wales', 'eric', 'eric24', 'phu', 'psds', 'gbe1', 'ghg26']
PAGES.append(guide_page(
  'healthcare-estates-decarbonisation.html',
  'Decarbonising healthcare estates: the challenge and where to start',
  'Decarbonising healthcare estates',
  'Net zero targets, a funding landscape that has changed shape, grid connections that take years, and buildings that never close. Here is the challenge in one place, and a practical order to tackle it in.',
  'The decarbonisation challenge for NHS and private healthcare estates in England, Scotland and Wales: targets, heat, CHP, grid capacity, funding, and where half-hourly data fits in.',
  f'''
<p class="answer">For most hospital estates the biggest single source of carbon is heat from burning gas, in boilers and CHP. Replacing it means moving to electric heat pumps and heat networks, which needs electrical capacity, money and time. The practical order is: measure what you use and when, cut waste, check your electrical headroom, add on-site generation where it pays, then replace fossil heat as plant reaches the end of its life.</p>
<p class="help">Looking for the numbers alone? See <a href="nhs-estates-energy-facts.html">NHS estates energy facts and figures</a>.</p>
{NOT_NHS}
{photo('estate-hospital', 'Illustration of a hospital estate with solar on the roofs and car park canopies, plant compounds, battery storage and a substation')}

<h2 id="scale">The scale of it</h2>
<p>NHS trusts in England spent about £14.4 billion running their estates in 2025/26, and the Estates Returns Information Collection (ERIC) records the estate's energy use at around 11 billion kWh a year.{ref(n(K,'eric'))} The NHS is the single biggest energy user in the public sector, with an energy bill estimated at around £1.3 billion that has almost doubled since 2019.{ref(n(K,'phu'))} The backlog of maintenance in the English estate was estimated at £15.9 billion in 2024/25, and much of it sits in the same boiler houses, pipework and switchrooms that decarbonisation depends on.{ref(n(K,'eric24'))}</p>
<p>In Scotland, building energy for heat and power remains the largest contributor to the emissions covered by NHS Scotland's 2040 net zero target.{ref(n(K,'scot25'))} The picture is similar in England and Wales.</p>

<h2 id="pressures">Five pressures at once</h2>
<h3>1. Targets with dates</h3>
<p>The NHS in England has committed to net zero by 2040 for the emissions it controls directly, with an 80% cut by 2028 to 2032.{ref(n(K,'nz'))} NHS England reports that these emissions have already fallen by over 68% since 1990 and that it remains on track for the interim target.{ref(n(K,'nz5'))} Scotland and Wales have their own dates, and Wales has a firm end date for fossil-fuelled CHP. See <a href="nhs-net-zero-targets.html">net zero targets across the UK</a>.</p>
<h3>2. Funding has changed shape</h3>
<p>The Public Sector Decarbonisation Scheme (PSDS) funded a large share of hospital heat projects in England from 2020, but no further money is being committed beyond projects already awarded. Phase 4 projects run to March 2028.{ref(n(K,'psds'))} Newer money is smaller and more targeted, such as Great British Energy's solar programme for NHS sites.{ref(n(K,'gbe1'))} Projects increasingly need to pay for themselves, or use loans, partnerships and power purchase agreements. See <a href="decarbonisation-funding.html">funding routes</a>.</p>
<h3>3. The grid connection</h3>
<p>Heat pumps replace gas with electricity, so a site's peak electrical demand rises, usually in the coldest weeks. Many hospitals already run close to their agreed supply capacity, and upgrading a connection can take years. Removing a gas CHP engine can add hundreds of kilowatts to grid import on its own. See <a href="hospital-electrical-capacity.html">electrical capacity for electrification</a>.</p>
<h3>4. Buildings that never close</h3>
<p>Acute hospitals run around the clock, with theatres, imaging, sterile services, labs and wards that cannot be switched off for a works programme. Every change is planned around clinical risk, infection control and resilience, which slows delivery and raises cost.</p>
<h3>5. Falling grid carbon changes old answers</h3>
<p>The UK government's electricity carbon factor for 2026 reporting is about 0.13 kg CO₂e per kWh, down from 0.177 for 2025.{ref(n(K,'ghg26'))} That makes on-site gas CHP look worse on carbon than it did when many systems were installed, and makes electric heat look better every year. See <a href="moving-away-from-chp.html">moving away from gas CHP</a>.</p>

<h2 id="order">A practical order of work</h2>
<ol>
<li><strong>Measure.</strong> Load 12 months of half-hourly electricity data for every meter into the <a href="analyser/">analyser</a>. You will see base load, day and night use, out-of-hours use in clinics and admin buildings, and each site's peaks against its agreed supply capacity.</li>
<li><strong>Cut waste first.</strong> Controls, ventilation schedules, theatre setback, LED lighting and steam losses are usually the cheapest carbon to remove, and they reduce the size of everything you buy afterwards. See <a href="hospital-energy-efficiency.html">energy efficiency in hospitals</a>.</li>
<li><strong>Know your headroom.</strong> Before you design a heat pump scheme, know how much spare electrical capacity each site has, in which months, with and without CHP running.</li>
<li><strong>Generate where it pays.</strong> Hospitals use electricity all day, every day, so they use almost all of the output of a well-sized solar system. Use the <a href="solar-calculator.html">solar calculator</a> with your own half-hourly profile. See <a href="solar-on-healthcare-estates.html">solar on healthcare estates</a>.</li>
<li><strong>Plan the heat.</strong> Write or refresh a heat decarbonisation plan that matches each boiler, CHP engine and steam system to its replacement date. See <a href="heat-decarbonisation.html">heat decarbonisation</a>.</li>
<li><strong>Fund and procure.</strong> Match each project to a funding route and a compliant procurement route, and build the business case from measured data rather than estimates.</li>
</ol>

<h2 id="data">Where half-hourly data fits</h2>
<p>Half-hourly data is the evidence behind almost every step above. It shows the real base load you are paying for, proves whether a controls change worked, gives the peak demand a DNO will ask about, and sets the share of solar output a site will use. It is also data you already have: your electricity supplier records it for billing. See <a href="get-your-data.html">how to get your half-hourly data</a>.</p>
''' + sources_for(*K),
  [('scale', 'The scale of it'), ('pressures', 'Five pressures at once'), ('order', 'A practical order of work'), ('data', 'Where half-hourly data fits')],
  [('What is the biggest source of carbon on a hospital estate?', 'Usually gas burned for heat and hot water, in boilers and CHP engines. Grid electricity is a smaller and falling share as the grid gets cleaner.'),
   ('Where should an estates team start?', 'With measurement and waste: load your half-hourly data, fix controls and schedules, and check electrical headroom before designing heat pump schemes. It costs little and makes every later project smaller.'),
   ('Does this apply to private hospitals?', 'The engineering is the same. The targets and funding differ: independent providers set their own targets, many through the IHPN commitment, and use private finance. See our page on private and independent hospitals.')],
  [('nhs-net-zero-targets.html', 'Net zero targets', 'England, Scotland and Wales, side by side.'),
   ('hospital-electrical-capacity.html', 'Electrical capacity', 'Headroom for heat pumps, and the CHP effect.'),
   ('decarbonisation-funding.html', 'Funding routes', 'What is still available, and what replaced PSDS.')],
  'The decarbonisation challenge for healthcare estates: gas heat is the biggest source; targets, PSDS ending, grid capacity, 24/7 operation and falling grid carbon; a six-step order of work starting with half-hourly data.',
  crumbs=[HOME, ('Decarbonisation', 'healthcare-estates-decarbonisation.html')]))

# ── NET ZERO TARGETS ───────────────────────────────────────────────────
K = ['nz', 'nz5', 'nzbs', 'scot', 'scot25', 'wales', 'walest', 'supp', 'crp27', 'ihpn']
PAGES.append(guide_page(
  'nhs-net-zero-targets.html',
  'NHS net zero targets in England, Scotland and Wales',
  'Net zero targets for healthcare across the UK',
  'The NHS in England, NHS Scotland and NHS Wales each have their own targets and dates. Here they are side by side, with what each means for the estate.',
  'NHS net zero targets compared: England 2040 and 2045, NHS Scotland 2040 with renewable heat by 2038, NHS Wales 34% by 2030 and no fossil CHP after 2035, plus the supplier roadmap and private sector commitments.',
  f'''
<p class="answer">The NHS in England aims for net zero by 2040 for the emissions it controls directly, and 2045 for the emissions it can influence. NHS Scotland aims for net zero by 2040, with all NHS-owned buildings using renewable heat by 2038. NHS Wales is working to a 34% reduction by 2030 as part of a Welsh public sector net zero ambition, with all fossil-fuelled CHP to be decommissioned by 2035.</p>
{NOT_NHS}

<h2 id="compare">Side by side</h2>
<div class="table-wrap"><table><thead><tr><th>Nation</th><th>Headline target</th><th>What it means for buildings</th></tr></thead><tbody>
<tr><td>England</td><td>Net zero by 2040 for the NHS Carbon Footprint (direct emissions), 80% cut by 2028 to 2032. Net zero by 2045 for the Carbon Footprint Plus (supply chain), 80% cut by 2036 to 2039.{ref(n(K,'nz'))}</td><td>New buildings and major upgrades that need HM Treasury business case approval must follow the NHS Net Zero Building Standard.{ref(n(K,'nzbs'))}</td></tr>
<tr><td>Scotland</td><td>Net zero by 2040 or earlier, net zero supply chain by 2045.{ref(n(K,'scot25'))}</td><td>Cut building emissions by at least 75% against 1990, renewable heating for all NHS-owned buildings by 2038, the whole estate net zero by 2040 or earlier.{ref(n(K,'scot'))}</td></tr>
<tr><td>Wales</td><td>Interim cuts of 16% by 2025 and 34% by 2030, contributing to a Welsh public sector that is collectively net zero by 2030.{ref(n(K,'walest'))}</td><td>No new fossil-fuelled CHP, existing CHP kept efficient until life expired, and all fossil CHP decommissioned by 2035.{ref(n(K,'wales'))}</td></tr>
</tbody></table></div>

<h2 id="england">England</h2>
<p>The two targets were set in 2020 against a 1990 baseline. The NHS Carbon Footprint covers emissions the NHS controls directly, including the energy used in its buildings. The Carbon Footprint Plus adds the supply chain, medicines and other emissions the NHS can influence.{ref(n(K,'nz'))} NHS England reports that direct emissions have fallen by over 68% since 1990, and that it remains on track for the interim 80% target by 2032.{ref(n(K,'nz5'))}</p>
<p>For estates teams, this shows up in three places: the trust's Green Plan, the heat decarbonisation plan behind any capital bid, and the NHS Net Zero Building Standard for new buildings and major upgrades.{ref(n(K,'nzbs'))}</p>

<h2 id="scotland">Scotland</h2>
<p>NHS Scotland brought its net zero date forward from 2045 to 2040. Its strategy commits to cutting emissions from buildings by at least 75% against 1990, using renewable heating systems in all NHS-owned buildings by 2038, and making the whole estate net zero by 2040 or earlier.{ref(n(K,'scot'))} New facilities must either use renewable heat from the start or have a clear plan to do so by 2038. The 2025 annual report describes power purchase agreements as a core part of the strategy, because renewable electricity cuts the cost of electrified heat and transport.{ref(n(K,'scot25'))}</p>

<h2 id="wales">Wales</h2>
<p>NHS organisations in Wales work to the NHS Wales Decarbonisation Strategic Delivery Plan, now updated for 2025 to 2030. It sets interim reductions of 16% by 2025 and 34% by 2030.{ref(n(K,'walest'))} The buildings section is specific about plant: no further fossil-fuelled CHP is to be installed, existing CHP should run at maximum efficiency until life expired, decommissioning is preferred over major refurbishment such as engine replacement, and all fossil CHP is to be decommissioned by 2035. It also asks for seasonal reviews of building controls such as BMS settings, timers and thermostats.{ref(n(K,'wales'))}</p>

<h2 id="suppliers">Suppliers and private providers</h2>
<p>Since April 2024, NHS England has required a carbon reduction plan for all new procurements, and every NHS procurement since April 2022 has carried at least a 10% weighting for net zero and social value.{ref(n(K,'supp'))} From 1 April 2027, a stricter carbon reduction plan standard applies to larger contracts and new frameworks.{ref(n(K,'crp27'))} That matters to independent hospitals delivering NHS work, and to every contractor quoting for estate projects.</p>
<p>Independent healthcare providers have their own sector commitment, led by the Independent Healthcare Providers Network, to reach net zero by 2035.{ref(n(K,'ihpn'))} See <a href="private-hospitals.html">private and independent hospitals</a>.</p>

<h2 id="data">What this means for your data</h2>
<p>Every one of these targets is reported from measured energy use. Half-hourly electricity data gives you the electricity side at the finest detail available, and shows whether changes you make are working. Load it into the <a href="analyser/">analyser</a> with your carbon factor, and the reports show kWh and tonnes of CO₂e by site.</p>
''' + sources_for(*K),
  [('compare', 'Side by side'), ('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales'), ('suppliers', 'Suppliers and private providers'), ('data', 'What this means for your data')],
  [('When does the NHS in England have to reach net zero?', 'By 2040 for the emissions it controls directly (the NHS Carbon Footprint), with an 80% cut by 2028 to 2032, and by 2045 for the emissions it can influence (the Carbon Footprint Plus).'),
   ('What is NHS Scotland\'s target for heating?', 'All NHS-owned buildings are to use renewable heating systems by 2038, with the whole estate net zero by 2040 or earlier.'),
   ('Can NHS Wales install new gas CHP?', 'No. The NHS Wales decarbonisation plan says no further fossil-fuelled CHP will be installed, existing units should run until life expired, and all fossil CHP should be decommissioned by 2035. Renewable CHP is still supported.')],
  [('healthcare-estates-decarbonisation.html', 'The estates challenge', 'Everything in one place, and where to start.'),
   ('moving-away-from-chp.html', 'Moving away from CHP', 'Why the carbon case has changed.'),
   ('decarbonisation-funding.html', 'Funding routes', 'England, Scotland and Wales.')],
  'NHS England net zero 2040 (direct) and 2045 (supply chain); NHS Scotland net zero 2040, renewable heat in NHS-owned buildings by 2038, buildings minus 75%; NHS Wales 16% by 2025 and 34% by 2030, no new fossil CHP and all decommissioned by 2035; supplier carbon reduction plans; IHPN 2035.',
  crumbs=[HOME, GUIDES, ('Net zero targets', 'nhs-net-zero-targets.html')]))

# ── FUNDING ────────────────────────────────────────────────────────────
K = ['psds', 'psds4', 'gbe100', 'gbe1', 'clean', 'tewv', 'lpp', 'scotfoi', 'scotdev', 'walesloan', 'wges', 'scot25']
PAGES.append(guide_page(
  'decarbonisation-funding.html',
  'Funding for NHS and healthcare decarbonisation projects in 2026',
  'Funding healthcare decarbonisation',
  'PSDS is tapering out, and the money that replaces it is smaller, more targeted and less often a straight grant. Here is what is available in England, Scotland and Wales, and how projects are being paid for now.',
  'Funding routes for hospital decarbonisation in 2026: the end of new PSDS money, Great British Energy solar for NHS sites, Scottish and Welsh schemes, and funded models such as PPAs and energy performance contracts.',
  f'''
<p class="answer">In England, the Public Sector Decarbonisation Scheme is not funding new projects beyond those already awarded, and Phase 4 projects run to March 2028.{ref(n(K,'psds'))} The main new public money for NHS estates is targeted: Great British Energy's solar and battery funding, and the clean energy upgrades announced for 82 trusts in February 2026.{ref(n(K,'gbe1'),n(K,'clean'))} Scotland and Wales run their own schemes. Beyond grants, more projects now use power purchase agreements, energy performance contracts and other funded models that pay back from savings.</p>
{NOT_NHS}

<h2 id="england">England</h2>
<h3>Public Sector Decarbonisation Scheme (PSDS)</h3>
<p>PSDS has paid for heat pumps, insulation, LED lighting, solar and controls across the public sector since 2020, including many hospital energy centres. The government has confirmed it will commit no further funding beyond projects already awarded. Those projects remain funded, with Phase 4 running until 31 March 2028.{ref(n(K,'psds'))} If your trust holds a Phase 4 award, delivery to time and budget is now the priority. Phase 4 also set a maximum grant carbon cost of £510 per tonne of CO₂e saved over a project's life, a useful benchmark for comparing any future project.{ref(n(K,'psds4'))}</p>
<h3>Great British Energy and NHS England solar funding</h3>
<p>In March 2025, £100 million from Great British Energy was announced for NHS trusts to install solar panels and battery storage: 132 projects at 78 trusts, covering around 200 sites.{ref(n(K,'gbe100'))} By May 2026, 162 NHS sites in England had completed solar installations through the programme, and a further £25 million was announced for up to 40 more NHS sites.{ref(n(K,'gbe1'))} These rounds have had short application windows and tight delivery deadlines, so trusts with surveyed, ready-to-go roofs and car parks have been best placed.</p>
<h3>Clean energy upgrades, February 2026</h3>
<p>In February 2026 the government announced that 82 NHS trusts, alongside eight military sites and a prison, would share £74 million for clean energy and efficiency upgrades, including £9 million delivered with Great British Energy for batteries and solar.{ref(n(K,'clean'),n(K,'tewv'))}</p>
<h3>The Local Power Plan</h3>
<p>Published in February 2026 and backed by Great British Energy, the Local Power Plan uses a mix of grants, loans and local investment, and aims to open up long-term power purchase agreements between community energy groups and public buildings.{ref(n(K,'lpp'))} Large, constant hospital loads make good partners for that kind of arrangement.</p>

<h2 id="scotland">Scotland</h2>
<p>NHS boards were funded through the Scottish Green Public Sector Estate Decarbonisation Scheme, which has now closed. The Scottish Government says health boards can now apply for capital funding to Scotland's Public Sector Heat Decarbonisation Fund, administered by Salix, and that estate decarbonisation has also been funded from the health portfolio's capital budget.{ref(n(K,'scotfoi'))} A separate Public Sector Clean Heat Development Fund offered up to £30,000 a project for early development work, with applications closing in September 2026.{ref(n(K,'scotdev'))} NHS Scotland also treats renewable power purchase agreements as a core part of its strategy.{ref(n(K,'scot25'))}</p>

<h2 id="wales">Wales</h2>
<p>The Wales Funding Programme, run by Salix for the Welsh Government, includes Invest to Save, which offers interest-free finance to public bodies without borrowing powers, such as health boards.{ref(n(K,'walesloan'))} The Welsh Government Energy Service gives technical, commercial and procurement support, and had supported 57 installed projects for NHS Wales health boards and trusts by its 2024 to 2025 report.{ref(n(K,'wges'))}</p>

<h2 id="models">Funded and partnership models</h2>
<ul>
<li><strong>Power purchase agreement (PPA).</strong> A funder pays for, owns and maintains a solar system on your site, and you buy its electricity at an agreed rate. No capital, but a long contract. It suits constant-load sites like hospitals. See <a href="paying-for-solar.html">paying for solar</a>.</li>
<li><strong>Energy performance contract (EPC).</strong> A contractor designs, installs and often maintains a package of measures, and guarantees the savings. Frameworks such as RE:FIT are commonly used to procure them.</li>
<li><strong>Energy services or heat-as-a-service.</strong> A partner builds and runs an energy centre and sells heat and power to the site over a long term.</li>
<li><strong>Your own capital.</strong> The cheapest money if you have it. Measured half-hourly data and a clear payback make the case at a capital planning group far stronger.</li>
</ul>

<h2 id="ready">Being ready when money appears</h2>
{photo('hc-strategy-meeting', 'An estates, finance and clinical team reviewing a hospital decarbonisation roadmap and site plans', 'Funding rounds reward trusts that can show their data, plans and surveys straight away.')}
<p>Recent rounds have rewarded trusts that could move quickly. What helps most:</p>
<ol>
<li>A current heat decarbonisation plan, with each site's plant and replacement dates.</li>
<li>Twelve months of half-hourly data for every meter, analysed, so you can show base load, peaks and headroom straight away.</li>
<li>Agreed supply capacities and any known DNO constraints, site by site.</li>
<li>Roof and car park surveys for solar, with a first estimate from the <a href="solar-calculator.html">solar calculator</a>.</li>
<li>A procurement route agreed in advance, such as a framework your organisation can use.</li>
</ol>
''' + sources_for(*K),
  [('england', 'England'), ('scotland', 'Scotland'), ('wales', 'Wales'), ('models', 'Funded and partnership models'), ('ready', 'Being ready when money appears')],
  [('Is the Public Sector Decarbonisation Scheme still open?', 'No new money is being committed. Projects already awarded remain funded, with Phase 4 running until 31 March 2028.'),
   ('What funding is there for solar on NHS sites?', 'Great British Energy has funded solar at hundreds of NHS sites since 2025, with a further £25 million announced in May 2026 for up to 40 more sites. Rounds have been short, so have surveys and data ready. PPAs avoid the need for capital altogether.'),
   ('Can health boards in Wales borrow for energy projects?', 'Health boards do not have borrowing powers, so the Wales Funding Programme offers Invest to Save, interest-free finance for public bodies without them.')],
  [('paying-for-solar.html', 'Paying for solar', 'Buying, leasing or a PPA.'),
   ('heat-decarbonisation.html', 'Heat decarbonisation', 'What a fundable heat project looks like.'),
   ('nhs-net-zero-targets.html', 'Net zero targets', 'England, Scotland and Wales.')],
  'Healthcare decarbonisation funding: PSDS no new commitments (Phase 4 to March 2028, £510/tCO2e cap); GBE £100m NHS solar (2025), 162 sites done and £25m for 40 more (May 2026); £74m for 82 trusts (Feb 2026); Scotland Public Sector Heat Decarbonisation Fund; Wales Invest to Save; PPAs and EPCs.',
  crumbs=[HOME, GUIDES, ('Funding', 'decarbonisation-funding.html')]))

# ── HEAT DECARBONISATION ───────────────────────────────────────────────
K = ['hdp', 'scot', 'nzbs', 'brid', 'notts', 'hnz', 'psds4']
PAGES.append(guide_page(
  'heat-decarbonisation.html',
  'Heat decarbonisation for hospitals: heat pumps, steam and flow temperatures',
  'Heat decarbonisation for hospitals',
  'Replacing gas boilers and CHP on a hospital estate is the biggest single step towards net zero, and the hardest. Here is how teams are approaching it, and the data you need first.',
  'How to decarbonise heat on hospital estates: heat decarbonisation plans, heat pumps, flow temperatures, steam, hot water safety, heat recovery and heat networks, and the electrical capacity each needs.',
  f'''
<p class="answer">Hospital heat is usually decarbonised in stages: cut demand, lower the temperatures the heating system runs at, add heat pumps for the base of the heat load, recover waste heat from cooling and ventilation, and keep existing boilers for peaks and resilience until they can be retired. Steam and hot water need separate solutions. Every stage adds electrical load, so check headroom early.</p>
{NOT_NHS}
{photo('hc-heat-pump-plant-room', 'Two engineers with tablets in a hospital plant room beside an air source heat pump and a building management screen', 'Heat pumps work best at low flow temperatures, so controls and the heating system matter as much as the plant.')}

<h2 id="plan">Start with a heat decarbonisation plan</h2>
<p>A heat decarbonisation plan sets out how an organisation will replace fossil fuel heating with low carbon alternatives, building by building. Salix's guidance for public sector plans asks for a whole building approach, and includes a section on whether the electricity supply can support a switch to electric heating.{ref(n(K,'hdp'))} A plan written now, while there is less grant money about, is still the document funders, boards and contractors ask for first.</p>

<h2 id="temperatures">Flow temperatures decide almost everything</h2>
{photo('hc-thermal-survey', 'A surveyor in a hard hat reading a thermal image of a hospital building on a tablet', 'A thermal survey shows where heat is escaping, so the worst buildings can be improved before heat pumps are sized.')}
<p>Many hospital heating systems were designed for boilers running at around 80°C. Heat pumps are most efficient at much lower temperatures, so the questions are how far you can lower the flow temperature, and what has to change to do it. Common steps are:</p>
<ul>
<li>balancing the system and fixing controls, so it is not overheating some areas to reach others</li>
<li>improving insulation and glazing in the worst buildings first</li>
<li>adding or replacing emitters in areas that cannot be kept warm at lower temperatures</li>
<li>splitting high-temperature users onto their own supply</li>
</ul>
<p>New healthcare buildings in England must follow the NHS Net Zero Building Standard, which pushes towards all-electric, low-temperature systems from the start.{ref(n(K,'nzbs'))}</p>

<h2 id="special">Steam, hot water and other special cases</h2>
<ul>
<li><strong>Steam.</strong> Older estates still distribute steam for sterilisation, humidification and kitchens. Moving to local electric steam generators at the point of use can remove long, lossy steam mains.</li>
<li><strong>Domestic hot water.</strong> Hot water in healthcare buildings is stored and circulated at high temperatures to control Legionella, under HTM 04-01. Heat pumps can pre-heat it, but it normally needs a top-up stage, and the design must keep water safety first.</li>
<li><strong>Simultaneous heating and cooling.</strong> Hospitals cool imaging, IT and theatres while heating wards. A water-source heat pump can take heat from the chilled water system and use it for heating. At Nottingham City Hospital, a 160 kW heat pump recovers waste heat as part of a £34.8 million programme that also added air source heat pumps, solar and a site-wide LED upgrade.{ref(n(K,'notts'))}</li>
</ul>

<h2 id="examples">What it looks like in practice</h2>
<p>At Bridlington Hospital, 20-year-old gas boilers and a gas CHP unit supplied the heating and hot water. The project decommissioned the CHP, removed a boiler and installed a 600 kW air source heat pump system sized to meet all of the hospital's heating and hot water demand, alongside a 750 kWp solar system.{ref(n(K,'brid'))} In Scotland, renewable heat for all NHS-owned buildings by 2038 means every board is planning work of this kind.{ref(n(K,'scot'))}</p>

<h2 id="networks">Heat networks</h2>
<p>In England, heat network zoning will identify areas where heat networks are expected to be the lowest-cost low carbon heat, and certain buildings in a zone may be required to connect within set timescales. Large public buildings such as hospitals are typical anchor loads.{ref(n(K,'hnz'))} If your site is in a likely zone, a connection may be part of your plan, and your own energy centre may become a source of heat for others.</p>

<h2 id="electric">The electrical side</h2>
<p>A heat pump's electrical input is roughly its heat output divided by its efficiency at that moment. On a cold day, a scheme delivering 1 MW of heat at an efficiency of 2.5 draws about 400 kW of electricity, around 420 kVA at a power factor of 0.95. That load arrives in the weeks when the site's electrical demand is already at its highest. Load your half-hourly data into the <a href="analyser/">analyser</a>, enter the agreed supply capacity, and use the headroom check to test a constant extra load. See <a href="hospital-electrical-capacity.html">electrical capacity</a>.</p>
<p>When comparing options, the Phase 4 PSDS cap of £510 of grant per tonne of CO₂e saved over a project's life is a useful yardstick for value.{ref(n(K,'psds4'))}</p>
''' + sources_for(*K),
  [('plan', 'Start with a plan'), ('temperatures', 'Flow temperatures'), ('special', 'Steam and hot water'), ('examples', 'In practice'), ('networks', 'Heat networks'), ('electric', 'The electrical side')],
  [('Can a heat pump heat a whole hospital?', 'Sometimes. Bridlington Hospital installed a 600 kW air source heat pump system sized for all its heating and hot water. On larger acute sites, heat pumps more often cover the base load first, with existing boilers kept for peaks and resilience.'),
   ('Why do flow temperatures matter?', 'Heat pumps get more efficient as the temperature they have to produce falls. Lowering the heating system temperature, by fixing controls, insulating and upgrading emitters, cuts running costs and the electrical load.'),
   ('How much electricity will heat pumps need?', 'Roughly the heat output divided by the efficiency. As an illustration, 1 MW of heat at an efficiency of 2.5 needs about 400 kW of electricity, in the coldest weeks when demand is already highest.')],
  [('hospital-electrical-capacity.html', 'Electrical capacity', 'Is there room for the heat pumps?'),
   ('moving-away-from-chp.html', 'Moving away from CHP', 'What to do with existing engines.'),
   ('hospital-energy-efficiency.html', 'Energy efficiency', 'Cut demand before sizing plant.')],
  'Hospital heat decarbonisation: heat decarbonisation plans (whole building approach, electrical capacity section), lowering flow temperatures, steam to point-of-use, hot water safety under HTM 04-01, heat recovery from cooling, heat network zoning, and the electrical load (1 MW heat at efficiency 2.5 needs about 400 kW).',
  crumbs=[HOME, GUIDES, ('Heat decarbonisation', 'heat-decarbonisation.html')]))

# ── MOVING AWAY FROM CHP ───────────────────────────────────────────────
K = ['ghg26', 'wales', 'brid', 'efpmsdef', 'nz']
PAGES.append(guide_page(
  'moving-away-from-chp.html',
  'Moving away from gas CHP in hospitals: carbon, cost and electrical capacity',
  'Moving away from gas CHP',
  'Gas CHP was a sound carbon choice for many hospitals ten years ago. As the grid has cleaned up, the sums have changed. Here is why, what to do with the engines you have, and the electrical surprise waiting when one stops.',
  'Why gas CHP no longer saves carbon against grid electricity in most hospitals, how the 2026 carbon factors change the comparison, NHS Wales policy, options for existing engines and the effect on grid import and capacity.',
  f'''
<p class="answer">Gas combined heat and power (CHP) saves carbon only when the grid electricity it replaces is more carbon-intensive than burning the extra gas. With the UK grid factor at about 0.13 kg CO₂e per kWh for 2026 reporting, a typical gas CHP engine now emits more than buying electricity from the grid and making the heat in a boiler.{ref(n(K,'ghg26'))} It can still cut costs when gas is cheap relative to electricity, and it adds resilience, but it does not lead to net zero. When a CHP engine stops, the site's grid import rises by its full electrical output, which is often the first capacity problem a trust meets.</p>
{NOT_NHS}

<h2 id="carbon">Why the carbon case has changed</h2>
<p>Here is a simple comparison, per kWh of gas burned in an engine with typical efficiencies. It is illustrative: your engine's own efficiencies, and how much of its heat you use, will change the answer.</p>
<div class="table-wrap"><table><thead><tr><th>Assumption or result</th><th class="num">Value</th></tr></thead><tbody>
<tr><td>Natural gas, kg CO₂e per kWh (gross calorific value), 2026 factors</td><td class="num">0.182</td></tr>
<tr><td>Grid electricity, kg CO₂e per kWh, 2026 factors</td><td class="num">0.131</td></tr>
<tr><td>CHP electrical efficiency / heat efficiency (assumed)</td><td class="num">35% / 45%</td></tr>
<tr><td>Boiler efficiency for the alternative (assumed)</td><td class="num">90%</td></tr>
<tr><td><strong>CHP:</strong> 1 kWh of gas gives 0.35 kWh of electricity and 0.45 kWh of heat</td><td class="num">0.182 kg</td></tr>
<tr><td><strong>Grid plus boiler:</strong> 0.35 kWh from the grid, 0.5 kWh of gas for the heat</td><td class="num">0.137 kg</td></tr>
<tr><td><strong>Heat pump instead of boiler:</strong> 0.35 kWh from the grid, plus 0.18 kWh to make 0.45 kWh of heat at an efficiency of 2.5</td><td class="num">0.069 kg</td></tr>
</tbody></table></div>
<p>On these assumptions, the CHP route emits about a third more than grid electricity and a boiler, and more than twice as much as grid electricity and a heat pump. Factors are from the UK government's 2026 conversion factors.{ref(n(K,'ghg26'))} With the 2025 grid factor of 0.177, the CHP route was still about a fifth worse. Ten years ago, when the grid factor was far higher, CHP came out ahead, which is why so many were installed.</p>
<p>Some engineers argue that CHP displaces the gas power stations at the margin of the grid rather than the average mix, which flatters CHP. That debate is real, but NHS carbon reporting uses the average, location-based factors, so that is what your Green Plan figures will show.</p>

<h2 id="policy">What the policies say</h2>
<p>NHS Wales has the clearest position: no further fossil-fuelled CHP will be installed, existing CHP should be maintained at maximum efficiency until life expired, decommissioning is preferred over major refurbishment such as an engine replacement, and all fossil CHP is to be decommissioned by 2035. Renewable CHP is still supported.{ref(n(K,'wales'))} In England, the 2040 net zero target for direct emissions leaves no room for gas CHP in the long run, because the gas it burns is a direct emission.{ref(n(K,'nz'))}</p>

<h2 id="options">Options for the engine you have</h2>
<ol>
<li><strong>Run it well to the end of its life.</strong> If it is reliable and its heat is fully used, keep it running efficiently while the replacement is planned.</li>
<li><strong>Do not re-engine by default.</strong> A major overhaul can lock in another decade of gas. Price the alternatives at the same time.</li>
<li><strong>Change how it runs.</strong> Running only when electricity prices are high, and heat is needed, can keep the cost benefit while cutting run hours.</li>
<li><strong>Plan its replacement.</strong> Heat pumps for the base heat load, heat recovery from cooling, and boilers for peaks, as at Bridlington Hospital, where the CHP was decommissioned and a 600 kW air source heat pump system installed.{ref(n(K,'brid'))}</li>
<li><strong>Think about resilience separately.</strong> CHP is sometimes counted on for resilience. Standby generators, batteries and supply arrangements may do that job better once the engine goes.</li>
</ol>

<h2 id="capacity">The capacity surprise</h2>
{photo('hc-heat-pump-plant-room', 'Two engineers with tablets in a hospital plant room beside an air source heat pump and a building management screen', 'Replacing CHP heat with heat pumps moves the load onto the electricity supply.')}
<p>While a CHP engine runs, the site's main meter only records what the CHP does not supply. So the half-hourly data you get from your supplier understates the site's real electrical demand by the engine's output. When the engine is off for maintenance, trips, or is removed, grid import jumps by that amount. If a 1 MW engine stops, the site needs about 1 MW more from the grid, roughly 1,050 kVA at a power factor of 0.95.</p>
<p>To see this in your own data:</p>
<ul>
<li>Load the main import meter into the <a href="analyser/">analyser</a> and look at the heatmap. Engine outages show as bands of higher import.</li>
<li>If you have the CHP generation meter's data, load it as a separate meter and add the two together to see the site's true demand.</li>
<li>Run the headroom check against the agreed supply capacity with the engine's output as a test load. If the answer is negative, removing the CHP needs a connection upgrade or a matching cut in demand.</li>
</ul>
<p>Welsh estates already report CHP units as part of their EFPMS return, so the data on engine sizes and run hours often exists.{ref(n(K,'efpmsdef'))}</p>
''' + sources_for(*K),
  [('carbon', 'Why the carbon case has changed'), ('policy', 'What the policies say'), ('options', 'Options for the engine you have'), ('capacity', 'The capacity surprise')],
  [('Does gas CHP still save carbon?', 'In most cases, no, when measured with the UK government\'s average grid factor. At 2026 factors a typical gas engine emits about a third more than buying grid electricity and making the heat in a boiler. It can still save money, depending on gas and electricity prices.'),
   ('Should we replace our CHP engine when it wears out?', 'Not by default. Price a heat pump and heat recovery scheme at the same time. In Wales, policy prefers decommissioning to major refurbishment and plans to end fossil CHP by 2035.'),
   ('Why does grid import rise when CHP stops?', 'The main meter only sees what the CHP does not supply. When the engine stops, the site draws its full output from the grid instead, so peaks rise and headroom shrinks.')],
  [('hospital-electrical-capacity.html', 'Electrical capacity', 'How to test headroom with your data.'),
   ('heat-decarbonisation.html', 'Heat decarbonisation', 'What replaces the CHP heat.'),
   ('nhs-net-zero-targets.html', 'Net zero targets', 'Including NHS Wales and CHP.')],
  'Gas CHP versus grid in 2026: gas 0.182 and grid 0.131 kgCO2e/kWh; with 35%/45% CHP efficiencies, CHP 0.182 kg vs grid plus boiler 0.137 kg vs grid plus heat pump 0.069 kg per kWh of gas; NHS Wales decommission fossil CHP by 2035; removing CHP raises grid import by its output (1 MW is about 1,050 kVA).',
  crumbs=[HOME, GUIDES, ('Moving away from CHP', 'moving-away-from-chp.html')]))

# ── ELECTRICAL CAPACITY ────────────────────────────────────────────────
K = ['hdp', 'nzbs']
PAGES.append(guide_page(
  'hospital-electrical-capacity.html',
  'Electrical capacity for hospital electrification: heat pumps, EV charging and CHP',
  'Electrical capacity for electrification',
  'Heat pumps, EV charging and the end of CHP all need more electricity at the same time of year. Half-hourly data shows how much room each site really has, before anyone draws a scheme.',
  'How to check whether a hospital or healthcare site has the electrical capacity for heat pumps, EV charging and CHP removal, using half-hourly data, agreed supply capacity in kVA and a winter headroom check.',
  f'''
<p class="answer">Your agreed supply capacity, in kVA, is the most your site may draw from the network. Compare it with your busiest half hours, converted from kW to kVA, and the gap is your headroom. Check it in winter, when heat pumps add the most load, and with any CHP switched off. If the headroom is smaller than the new load, you need to cut demand elsewhere, add on-site generation or storage, or apply to your network operator for more capacity, which can take a long time.</p>

<h2 id="find">Find the numbers</h2>
<ul>
<li><strong>Agreed supply capacity (kVA)</strong> is on your electricity bill or in your connection agreement. Large hospitals may have several supplies, each with its own capacity.</li>
<li><strong>Half-hourly data</strong> for each supply, for at least 12 months, so the winter peaks are in it. See <a href="get-your-data.html">getting your data</a>.</li>
<li><strong>Power factor.</strong> Your bill may show reactive power charges. If you don't know your power factor, 0.95 is a common working assumption.</li>
</ul>

<h2 id="check">Run the check</h2>
<ol>
<li>Load each supply's file into the <a href="analyser/">analyser</a> and enter its agreed capacity and power factor on the Capacity tab.</li>
<li>Look at the busiest half hours and the months they fall in. On some hospital sites the electrical peak is in summer, from cooling, but heat pumps will create a new winter peak.</li>
<li>Enter the new load as a test load, for example the electrical input of a heat pump scheme or the output of a CHP engine you plan to remove, and keep a safety margin, such as 10%.</li>
<li>Download the PDF. It gives your capital planning group and your network operator the same evidence.</li>
</ol>

<h2 id="sizing">Rough sizes of new loads</h2>
<div class="table-wrap"><table><thead><tr><th>New load</th><th>Rough electrical demand</th></tr></thead><tbody>
<tr><td>Heat pumps delivering 1 MW of heat on a cold day, efficiency 2.5</td><td>About 400 kW (420 kVA at 0.95)</td></tr>
<tr><td>Removing a 1 MW gas CHP engine</td><td>About 1 MW more import (1,050 kVA at 0.95)</td></tr>
<tr><td>Ten 7 kW staff car chargers running together</td><td>70 kW</td></tr>
<tr><td>Two 50 kW rapid chargers for fleet vehicles</td><td>100 kW</td></tr>
</tbody></table></div>
<p>These are illustrations. Your designer will size the real loads, and smart charging and controls can reduce what is needed at the peak.</p>

<h2 id="options">If the headroom isn't there</h2>
{photo('hc-battery-ev-charging', 'Two engineers beside a battery storage unit and electric vehicle chargers at a hospital car park', 'Batteries and smart charging can keep new loads within the agreed capacity.')}
<ul>
<li><strong>Cut the peak first.</strong> Controls, chiller sequencing and ventilation schedules often take tens of kilowatts off the busiest half hours. See <a href="hospital-energy-efficiency.html">energy efficiency</a>.</li>
<li><strong>Generate on site.</strong> Solar reduces daytime import, but it does little on winter evenings when heat pump demand is high. Batteries can move energy into those hours.</li>
<li><strong>Manage new loads.</strong> Smart EV charging and heat pump controls can stay within a limit, using thermal storage to shift heat.</li>
<li><strong>Apply early.</strong> Connection upgrades can take years. The Salix guidance on heat decarbonisation plans asks for the electricity loading capacity to support a switch to electric heating, so an early application belongs in the plan.{ref(n(K,'hdp'))}</li>
</ul>

<h2 id="resilience">Resilience</h2>
<p>Hospitals keep standby generators and resilient supply arrangements for essential services. Moving heat to electricity means heat now depends on those arrangements too. Make sure the electrical resilience design, usually under HTM 06-01 in England, is reviewed alongside any heat pump scheme, and that new buildings meet the NHS Net Zero Building Standard.{ref(n(K,'nzbs'))}</p>
''' + sources_for(*K),
  [('find', 'Find the numbers'), ('check', 'Run the check'), ('sizing', 'Rough sizes of new loads'), ('options', "If the headroom isn't there"), ('resilience', 'Resilience')],
  [('What is agreed supply capacity?', 'The maximum your site may draw from the electricity network, in kVA, set in your connection agreement and shown on many bills. Going over it can bring charges and puts the supply at risk.'),
   ('Why check headroom in winter?', 'Heat pumps draw the most electricity in the coldest weeks. A site whose peak is in summer, from cooling, can still run out of capacity once heat is electrified.'),
   ('Does my half-hourly data include the CHP?', 'No. The main meter records what the site draws from the grid, which is what the CHP does not supply. Add the CHP generation meter\'s data to see true demand.')],
  [('supply-capacity.html', 'Supply capacity and kVA', 'The basics of capacity and power factor.'),
   ('moving-away-from-chp.html', 'Moving away from CHP', 'The capacity effect of removing an engine.'),
   ('heat-decarbonisation.html', 'Heat decarbonisation', 'Sizing the heat pumps.')],
  'Hospital electrical headroom: agreed supply capacity (kVA) minus winter peak (kW/power factor); test heat pump input (1 MW heat at efficiency 2.5 is about 400 kW), CHP removal (1 MW is about 1,050 kVA) and EV charging; options if short; resilience and HTM 06-01.',
  crumbs=[HOME, GUIDES, ('Electrical capacity', 'hospital-electrical-capacity.html')]))

# ── SOLAR ON HEALTHCARE ESTATES ───────────────────────────────────────
K = ['gbe100', 'gbe1', 'phu', 'scot25', 'nz']
PAGES.append(guide_page(
  'solar-on-healthcare-estates.html',
  'Solar for NHS trusts, health boards and private hospitals',
  'Solar on healthcare estates',
  'Hospitals use electricity all day, every day, so they use almost all of their solar output. Here is how to size it from your own data, where it goes on a hospital site, and how it is being paid for.',
  'Solar PV for hospitals and healthcare estates: why 24/7 sites use most of their solar, roofs, car park canopies and ground mounts, helipads and plant, grid connection, funding and sizing from half-hourly data.',
  f'''
<p class="answer">Solar suits hospitals because demand never stops, so a well-sized system's output is almost all used on site, saving the full unit price. Clinics and admin buildings closed at weekends use less of it. The way to size a system is to measure your own share used on site from half-hourly data, then model the roof, car parks and land in the <a href="solar-calculator.html">solar calculator</a>.</p>
{photo('hc-rooftop-solar-install', 'Two installers checking solar panels on a hospital roof')}

<h2 id="why">Why it suits healthcare</h2>
<ul>
<li><strong>Constant demand.</strong> Wards, theatres, imaging, sterile services and ventilation run every day of the year, weekends included.</li>
<li><strong>Space.</strong> Large flat roofs, surface and multi-storey car parks and land on the estate can all take panels.</li>
<li><strong>Price certainty.</strong> Every kWh generated and used on site is one not bought at volatile grid prices.</li>
<li><strong>Carbon.</strong> Grid electricity is part of the NHS Carbon Footprint, so solar used on site counts directly towards the 2040 target.{ref(n(K,'nz'))}</li>
</ul>

<h2 id="share">The number that matters: share used on site</h2>
<p>Solar you use yourself saves your full unit price. Solar you export earns a few pence. The solar calculator values export at 5p/kWh, so at a 25p unit price a kWh used is worth five times a kWh exported. On a 24/7 hospital the share used is often 90% or more, until the system gets large enough to cover the site's whole daytime demand on a sunny Sunday. On a health centre or admin building closed at weekends it is often 55 to 80%.</p>
<p>Rather than guess, measure it. Load the site's half-hourly data into the <a href="analyser/">analyser</a>, open its Solar tab and press <strong>Size solar for this site</strong>. The calculator opens with your share used at each system size, so the payback is based on your own profile. See <a href="solar.html">sizing solar from half-hourly data</a>.</p>

<h2 id="where">Where it goes on a hospital site</h2>
{photo('hc-private-hospital-carport', 'A private hospital entrance with solar panels on the roof and a solar car park canopy', 'Roofs and car park canopies together: the canopy costs more per kWp, but uses space that is otherwise only parking.')}
<ul>
<li><strong>Roofs.</strong> Hospital roofs carry plant, flues, access routes and sometimes helipads, so the usable share can be lower than on a warehouse. Structural checks are needed on older buildings.</li>
<li><strong>Car park canopies.</strong> More expensive per kWp because of the steelwork, but they use space that is otherwise only parking, give shade and shelter, and sit well with EV charging. See <a href="solar-cost.html">what solar costs</a>.</li>
<li><strong>Ground mounts.</strong> The cheapest per kWp where the estate has land, often with a private wire to the main site.</li>
<li><strong>Helipads.</strong> Glint and glare from panels near a helicopter landing site needs assessing, and will usually be raised at planning stage.</li>
</ul>

<h2 id="grid">Grid connection and resilience</h2>
<p>Most hospital systems need approval from the network operator under the G99 process before they connect, and the operator may limit how much you can export. On a 24/7 site, export is often small anyway. Solar on its own does not keep a hospital running in a power cut: grid-connected systems switch off when the grid fails unless they are designed with batteries and controls to work alongside standby generators. See <a href="solar-planning-and-grid.html">planning, grid connection and other hurdles</a>.</p>

<h2 id="funding">Paying for it</h2>
<p>Great British Energy has become the main source of new public money for NHS solar: £100 million announced in March 2025 for 132 projects at 78 trusts,{ref(n(K,'gbe100'))} 162 NHS sites completed by May 2026 with £25 million more for up to 40 sites,{ref(n(K,'gbe1'))} and a scheme worth up to £255 million across schools, NHS and military sites.{ref(n(K,'phu'))} In Scotland, renewable power purchase agreements are a core part of NHS Scotland's strategy.{ref(n(K,'scot25'))} Power purchase agreements, where a funder owns the system and you buy its electricity, avoid the need for capital altogether. See <a href="paying-for-solar.html">paying for solar</a> and <a href="decarbonisation-funding.html">funding routes</a>.</p>
''' + sources_for(*K),
  [('why', 'Why it suits healthcare'), ('share', 'Share used on site'), ('where', 'Where it goes'), ('grid', 'Grid and resilience'), ('funding', 'Paying for it')],
  [('How much of its solar does a hospital use?', 'A 24/7 hospital often uses 90% or more of a well-sized system\'s output. Clinics and admin buildings closed at weekends often use 55 to 80%. Measure your own figure from half-hourly data in the analyser.'),
   ('Will solar keep the hospital running in a power cut?', 'Not on its own. Grid-connected systems switch off when the grid fails. Backup needs batteries and controls designed to work with the site\'s standby generators.'),
   ('Is there funding for solar on NHS sites?', 'Great British Energy has funded solar at hundreds of NHS sites since 2025, with a further £25 million announced in May 2026 for up to 40 more. Power purchase agreements avoid capital altogether.')],
  [('solar.html', 'Sizing solar from your data', 'How the analyser feeds the calculator.'),
   ('solar-calculator-method.html', 'How the solar calculator works', 'Method and assumptions.'),
   ('paying-for-solar.html', 'Paying for solar', 'Buying, leasing or a PPA.')],
  'Solar on healthcare estates: 24/7 hospitals use 90%+ of a well-sized system, clinics 55 to 80%; measure share used on site in the analyser and pass it to the solar calculator; roofs, car park canopies, ground mounts, helipad glare; G99 and resilience; GBE NHS solar funding and PPAs.',
  crumbs=[HOME, GUIDES, ('Solar on healthcare estates', 'solar-on-healthcare-estates.html')]))

# ── ENERGY EFFICIENCY ──────────────────────────────────────────────────
K = ['netb', 'wales', 'nottsv', 'notts', 'nz']
PAGES.append(guide_page(
  'hospital-energy-efficiency.html',
  'Energy efficiency in hospitals: where the quick wins are',
  'Energy efficiency in hospitals',
  'Before buying new plant, take out the waste. On a hospital estate the biggest savings are usually in ventilation, controls, lighting and steam, and half-hourly data shows where to start.',
  'Practical energy efficiency for hospitals and healthcare sites: theatre ventilation setback, BMS schedules, LED lighting, steam and pipework, chillers and plant rooms, and how to prove the savings with half-hourly data.',
  f'''
<p class="answer">The cheapest carbon to remove on a hospital estate is usually energy wasted by plant running when it isn't needed: theatre ventilation overnight, air handling in empty outpatient areas, lights on 24 hours, and heat lost from steam and hot water pipework. Fix controls and schedules first, then lighting and insulation, then larger plant. Every kilowatt saved also makes the heat pumps and connection upgrades you need later smaller.</p>
{photo('hc-efficient-ward', 'A bright hospital ward corridor with a nurse, a porter and a wall-mounted building systems display', 'Wards run around the clock; the offices, outpatients and corridors around them often do not need to.')}

<h2 id="theatres">Theatre ventilation</h2>
<p>Operating theatres need high air change rates when in use, and many systems run that way around the clock. HTM 03-01 already allows theatre ventilation to be switched off or set back when theatres are not in use, but NHS England says this is not widely implemented. Its Estates Technical Bulletin 2026/1, published in July 2026, sets out how to do it safely, and should be read alongside HTM 03-01.{ref(n(K,'netb'))} Any change needs your ventilation authorising engineer and infection prevention team involved.</p>

<h2 id="controls">Controls and schedules</h2>
<p>Building management system (BMS) settings drift. Outpatient departments, offices, education centres and restaurants on a hospital site keep set hours, but their heating, cooling and air handling often run on the main hospital's 24-hour schedule. NHS Wales asks for seasonal reviews of BMS settings, heating timers and thermostats for exactly this reason.{ref(n(K,'wales'))} At Nottingham City Hospital, the contractor reports that the BMS upgrade alone saved more than 7 million kWh of gas a year, nearly five times the guaranteed figure.{ref(n(K,'nottsv'))}</p>
<p>In the <a href="analyser/">analyser</a>, set each non-clinical building's real opening hours and it will show use outside them, priced at your rates.</p>

<h2 id="lighting">Lighting</h2>
<p>Many hospital areas are lit around the clock. LED replacement, with presence and daylight controls in corridors, stairs, car parks and plant rooms, is usually among the shortest paybacks available. Nottingham City Hospital's programme replaced more than 6,600 fittings.{ref(n(K,'notts'))}</p>

<h2 id="heat">Steam, hot water and pipework</h2>
<ul>
<li>Failed steam traps and uninsulated valves and flanges waste heat around the clock.</li>
<li>Long steam mains to a few users can cost more in losses than they deliver.</li>
<li>Pumps and fans without variable speed drives run at full speed whatever the demand.</li>
</ul>

<h2 id="base">Base load</h2>
<p>A hospital's base load, the demand it never drops below, is mostly essential. But it also hides chillers short-cycling, plant left on after a refurbishment, and equipment nobody owns. A step up in base load after works is a common sign. The analyser flags lasting changes and unusual days. See <a href="base-load.html">base load</a>.</p>

<h2 id="prove">Proving it worked</h2>
{photo('hc-energy-control-room', 'An estates team in an energy monitoring room, with screens showing campus energy use, carbon and building performance', 'Half-hourly data shows when energy is used. A walk round shows why.')}
<p>Change one thing at a time where you can, and compare matched weeks before and after with the analyser's before-and-after view. Measured savings are what boards, funders and Green Plan reports want. See <a href="proving-savings.html">proving a saving worked</a>.</p>
''' + sources_for(*K),
  [('theatres', 'Theatre ventilation'), ('controls', 'Controls and schedules'), ('lighting', 'Lighting'), ('heat', 'Steam and pipework'), ('base', 'Base load'), ('prove', 'Proving it worked')],
  [('Can theatre ventilation be turned down overnight?', 'HTM 03-01 allows theatre ventilation to be switched off or set back when theatres are not in use, and NHS England\'s Estates Technical Bulletin 2026/1 explains how to do it safely. Involve your ventilation authorising engineer and infection prevention team.'),
   ('What is the quickest energy saving in a hospital?', 'Usually fixing controls and schedules so that non-clinical areas stop running on the 24-hour hospital timetable. It costs little and the half-hourly data shows the result within weeks.'),
   ('How do we prove a saving?', 'Compare matched periods before and after the change with half-hourly data, one change at a time where possible.')],
  [('base-load.html', 'Base load', 'What always runs.'),
   ('proving-savings.html', 'Proving a saving worked', 'Before and after, fairly.'),
   ('heat-decarbonisation.html', 'Heat decarbonisation', 'The next step after efficiency.')],
  'Hospital energy efficiency: theatre ventilation setback (HTM 03-01, NHS Estates Technical Bulletin 2026/1), BMS schedules for non-clinical areas, LED with controls, steam traps and insulation, variable speed drives, base load steps, and proving savings with half-hourly data.',
  crumbs=[HOME, GUIDES, ('Energy efficiency', 'hospital-energy-efficiency.html')]))

# ── ESTATES RETURNS AND BENCHMARKING ──────────────────────────────────
K = ['ericstd', 'eric', 'eui', 'efpms', 'efpmsdef', 'scot25']
PAGES.append(guide_page(
  'estates-returns-and-benchmarking.html',
  'ERIC, EFPMS and benchmarking energy use in NHS estates',
  'Estates returns and benchmarking',
  'Every NHS trust in England and every health board in Wales already reports its energy use each year. Here is how those returns work, and how half-hourly data adds the detail they leave out.',
  'How NHS estates report energy: ERIC in England, EFPMS in Wales and annual sustainability reports in Scotland, energy use per square metre, and how half-hourly data explains the annual numbers.',
  f'''
<p class="answer">In England, NHS trusts report estates costs and energy use each year through the Estates Returns Information Collection (ERIC). In Wales, health boards and trusts report through the Estates and Facilities Performance Management System (EFPMS). Scottish boards publish annual climate emergency and sustainability reports. These returns give annual totals. Half-hourly data shows when the energy was used, which is what you need to reduce it.</p>

<h2 id="eric">ERIC in England</h2>
<p>ERIC is a mandatory collection of estates and facilities data from NHS organisations providing NHS-funded secondary care.{ref(n(K,'ericstd'))} The 2025/26 collection reported a total cost of running the NHS estate of £14.4 billion, and a Director of Estates must sign off each trust's return.{ref(n(K,'eric'))} The site-level data is public, so you can compare your sites with similar ones elsewhere. Researchers using ERIC data found average energy use intensity in acute hospital sites of about 211 kWh per square metre in 2024/25, with gas around three quarters of the total.{ref(n(K,'eui'))}</p>

<h2 id="efpms">EFPMS in Wales</h2>
<p>EFPMS is the comprehensive collection of estates and facilities data set up by the Welsh Government to improve the management of the NHS estate in Wales, run by NHS Wales Shared Services Partnership's Specialist Estates Services.{ref(n(K,'efpms'))} The return includes energy from utilities and local generation, renewable energy, and a section on CHP units.{ref(n(K,'efpmsdef'))}</p>

<h2 id="scotland">Scotland</h2>
<p>Scottish health boards publish annual climate emergency and sustainability reports, and the Scottish Government publishes a national report, which shows building energy for heat and power as the largest source of emissions in NHS Scotland's net zero target.{ref(n(K,'scot25'))}</p>

<h2 id="compare">Comparing your sites fairly</h2>
<ul>
<li><strong>Compare like with like.</strong> An acute hospital with theatres and imaging uses far more per square metre than a community hospital or a health centre.</li>
<li><strong>Use the same floor area basis</strong> as the return, and the same period.</li>
<li><strong>Separate electricity and heat.</strong> A site with CHP buys less electricity and more gas, which moves both figures.</li>
</ul>
<p>Enter each site's floor area in the <a href="analyser/">analyser</a> to see electricity per square metre alongside the half-hourly detail.</p>

<h2 id="hh">What half-hourly data adds</h2>
{photo('hc-energy-control-room', 'An estates team in an energy monitoring room, with screens showing campus energy use, carbon and building performance')}
<p>An annual return tells you a site used, say, 6 GWh of electricity. Half-hourly data shows that 2 GWh of it was base load, that the peak is creeping towards the supply limit, that a ward block's ventilation stopped turning down at night after a refurbishment, and how much of a solar system's output the site would use. That is the evidence that turns a benchmark into a project.</p>
''' + sources_for(*K),
  [('eric', 'ERIC in England'), ('efpms', 'EFPMS in Wales'), ('scotland', 'Scotland'), ('compare', 'Comparing fairly'), ('hh', 'What half-hourly data adds')],
  [('What is ERIC?', 'The Estates Returns Information Collection: a mandatory annual return of estates and facilities data, including energy, from NHS trusts in England. The data is published.'),
   ('What is EFPMS?', 'The Estates and Facilities Performance Management System, the mandatory estates and facilities return for NHS Wales, which includes energy, renewables and CHP.'),
   ('Can I benchmark against other hospitals?', 'Yes. ERIC site data is public. Compare sites of the same type, on the same floor area basis, and separate electricity from gas.')],
  [('electricity-benchmarks.html', 'Electricity benchmarks', 'Typical kWh per square metre by building type.'),
   ('hospital-energy-efficiency.html', 'Energy efficiency', 'Where the savings usually are.'),
   ('get-your-data.html', 'Getting your data', 'What to ask your supplier for.')],
  'NHS estates reporting: ERIC (England, mandatory, £14.4bn estate running cost 2025/26, acute EUI about 211 kWh/m² in 2024/25), EFPMS (Wales, includes CHP), Scottish board sustainability reports; comparing fairly; what half-hourly data adds.',
  crumbs=[HOME, GUIDES, ('Estates returns and benchmarking', 'estates-returns-and-benchmarking.html')]))

# ── PRIVATE AND INDEPENDENT HOSPITALS ─────────────────────────────────
from pages_guides import SECTORS  # noqa: E402
K = ['esos', 'esosbs', 'ihpn', 'supp', 'crp27', 'ghg26']
PAGES.append(guide_page(
  'private-hospitals.html',
  'Energy and net zero for private and independent hospitals',
  'Private and independent hospitals',
  'The engineering is the same as in the NHS: 24-hour wards, theatres, imaging and a big heat load. The targets, the money and the reporting duties are different.',
  'Energy, carbon and solar for private and independent hospitals in the UK: ESOS Phase 4, SECR, NHS supplier carbon reduction plans, the IHPN net zero 2035 commitment, and funded solar.',
  f'''
<p class="answer">Most independent hospital groups have to report energy and carbon under ESOS and, for larger companies, SECR. Those delivering NHS work also need carbon reduction plans under the NHS supplier roadmap, with a stricter standard for larger contracts from April 2027. Many have signed the IHPN commitment to reach net zero by 2035. Half-hourly data gives the electricity side of all of these, and the evidence for solar and efficiency projects.</p>

<h2 id="esos">ESOS Phase 4</h2>
<p>The Energy Savings Opportunity Scheme applies to large undertakings and groups that contain one. The qualification date for Phase 4 is 31 December 2026,{ref(n(K,'esos'))} and organisations that qualify must complete their assessment and notify compliance by 5 December 2027. A large undertaking is broadly one with 250 or more employees, or with turnover above £44 million and a balance sheet above £38 million.{ref(n(K,'esosbs'))} Twelve months of half-hourly data for every site makes the energy audit faster and more accurate, and shows the savings opportunities ESOS asks you to identify.</p>

<h2 id="secr">SECR</h2>
<p>Larger companies report their UK energy use and emissions in their annual report under Streamlined Energy and Carbon Reporting (SECR), using the government's conversion factors. The electricity factor for 2026 reporting fell to about 0.13 kg CO₂e per kWh, so reported Scope 2 emissions fall even if use does not change.{ref(n(K,'ghg26'))} Say which year's factors you used.</p>

<h2 id="nhs-work">Delivering NHS work</h2>
<p>Since April 2024, NHS England has required a carbon reduction plan for all new procurements, and all NHS procurements carry at least a 10% weighting for net zero and social value.{ref(n(K,'supp'))} From 1 April 2027 a stricter carbon reduction plan standard applies to contracts worth £5 million a year or more and to new frameworks.{ref(n(K,'crp27'))} A credible plan, backed by measured site data and projects, is now part of winning NHS work.</p>

<h2 id="ihpn">The sector commitment</h2>
<p>The Independent Healthcare Providers Network has set a sector-wide ambition for independent providers to reach net zero by 2035, five years ahead of the NHS's 2040 target for its direct emissions.{ref(n(K,'ihpn'))}</p>

<h2 id="projects">What projects look like</h2>
{photo('hc-private-hospital-dusk', 'A private hospital at dusk with rooftop solar, a solar car park canopy and electric vehicle chargers')}
<ul>
<li><strong>Solar.</strong> Private hospitals run around the clock, so they use most of a well-sized system's output. Power purchase agreements avoid capital; buying outright gives the best lifetime return and may qualify for capital allowances. See <a href="paying-for-solar.html">paying for solar</a> and the <a href="solar-calculator.html">solar calculator</a>.</li>
<li><strong>Heat.</strong> The same heat pump, flow temperature and hot water questions as NHS sites. See <a href="heat-decarbonisation.html">heat decarbonisation</a>.</li>
<li><strong>Efficiency.</strong> Theatre ventilation setback, BMS schedules for outpatient and consulting areas, and LED lighting. See <a href="hospital-energy-efficiency.html">energy efficiency</a>.</li>
</ul>

<h2 id="data">Using the analyser across a group</h2>
<p>Load one file per meter for every hospital in the group. The analyser ranks sites, shows base load and peaks against capacity for each, and produces a portfolio PDF and Excel export you can use in your ESOS audit, SECR narrative or carbon reduction plan. The analysis runs in your browser, so commercially sensitive data never leaves your computer.</p>
''' + sources_for(*K),
  [('esos', 'ESOS Phase 4'), ('secr', 'SECR'), ('nhs-work', 'Delivering NHS work'), ('ihpn', 'The sector commitment'), ('projects', 'What projects look like'), ('data', 'Using the analyser across a group')],
  [('Do private hospitals have to comply with ESOS?', 'If the group, or any UK company in it, is a large undertaking on 31 December 2026, yes. Compliance must be notified by 5 December 2027.'),
   ('Do NHS suppliers need a carbon reduction plan?', 'Yes, for all new NHS procurements since April 2024, with a stricter standard for contracts worth £5 million a year or more and new frameworks from 1 April 2027.'),
   ('Is solar worthwhile for a private hospital?', 'Usually, because demand runs all day every day, so most of the output is used on site. Measure your own share used from half-hourly data and model the site in the solar calculator.')],
  [('solar-on-healthcare-estates.html', 'Solar on healthcare estates', 'Roofs, car parks and land.'),
   ('nhs-net-zero-targets.html', 'Net zero targets', 'NHS targets and the supplier roadmap.'),
   ('hospital-energy-efficiency.html', 'Energy efficiency', 'Where the savings usually are.')],
  'Private and independent hospitals: ESOS Phase 4 (qualification 31 Dec 2026, notify by 5 Dec 2027), SECR, NHS supplier carbon reduction plans (all procurements since April 2024; 2027 standard for contracts of £5m a year or more), IHPN net zero by 2035, solar and efficiency.',
  crumbs=[HOME, SECTORS, ('Private and independent hospitals', 'private-hospitals.html')]))

# ── FACTS AND FIGURES ───────────────────────────────────────────────────
# Every figure here is already sourced on one of the guides above; this page
# gathers them for people (and answer engines) looking for the numbers.
# Update it whenever one of those guides changes a figure.
K = ['eric', 'phu', 'eric24', 'nz', 'nz5', 'scot', 'scot25', 'walest', 'wales', 'nzbs', 'ghg26',
     'psds', 'psds4', 'gbe100', 'gbe1', 'clean', 'netb', 'supp', 'crp27', 'ihpn', 'esos']


def _row(figure, what, *keys):
    return f'<tr><td class="num" style="white-space:nowrap"><strong>{figure}</strong></td><td>{what}{ref(*[n(K, k) for k in keys])}</td></tr>'


def _table(label, rows):
    return (f'<div class="table-wrap"><table aria-label="{label}"><thead><tr><th class="num">Figure</th><th>What it is</th></tr></thead><tbody>'
            + ''.join(rows) + '</tbody></table></div>')


PAGES.append(guide_page(
  'nhs-estates-energy-facts.html',
  'NHS estates energy: key facts and figures for 2026',
  'NHS estates energy: facts and figures',
  'The numbers estates teams, boards and suppliers ask for most, in one place: the size of the estate, net zero dates, carbon factors, funding and the biggest single savings. Each one is sourced and dated.',
  'Key figures on NHS estates energy for 2026: estate cost and energy use, net zero dates in England, Scotland and Wales, carbon factors, funding and theatre savings.',
  f'''
<p class="answer">NHS trusts in England spent about £14.4 billion running their estates in 2025/26 and used around 11 billion kWh of energy.{ref(n(K, 'eric'))} The NHS in England aims for net zero by 2040 for the emissions it controls, NHS Scotland by 2040 with renewable heat in all NHS-owned buildings by 2038, and NHS Wales has interim targets of a 34% cut by 2030 and no fossil CHP after 2035.{ref(n(K, 'nz'), n(K, 'scot'), n(K, 'walest'), n(K, 'wales'))} The grid electricity carbon factor for 2026 reporting is about 0.13 kg CO₂e per kWh.{ref(n(K, 'ghg26'))}</p>
{NOT_NHS}
<p class="help">Figures checked {long_date(CHECKED)}. Each links to its source below; the guides linked in each section explain what the numbers mean for an estate.</p>

<h2 id="estate">The size of the estate</h2>
{_table('The size of the NHS estate', [
  _row('£14.4bn', 'Cost of running the NHS estate in England, 2025/26 (ERIC)', 'eric'),
  _row('~11bn kWh', 'Energy used by the NHS estate in England in a year (ERIC)', 'eric'),
  _row('~£1.3bn', 'Estimated NHS energy bill, almost double its 2019 level', 'phu'),
  _row('£15.9bn', 'Backlog maintenance in the English NHS estate, 2024/25', 'eric24'),
])}
<p>See <a href="estates-returns-and-benchmarking.html">ERIC, EFPMS and benchmarking</a>.</p>

<h2 id="targets">Net zero targets</h2>
{_table('NHS net zero targets', [
  _row('2040', 'England: net zero for the NHS Carbon Footprint (emissions it controls), with an 80% cut by 2028 to 2032', 'nz'),
  _row('2045', 'England: net zero for the Carbon Footprint Plus, including the supply chain', 'nz'),
  _row('68%+', 'England: reported fall in directly controlled emissions since 1990', 'nz5'),
  _row('2038', 'Scotland: renewable heating in all NHS-owned buildings', 'scot'),
  _row('2040', 'Scotland: whole NHS estate net zero, or earlier', 'scot'),
  _row('34%', 'Wales: interim emissions cut by 2030 (16% by 2025)', 'walest'),
  _row('2035', 'Wales: all fossil-fuelled CHP decommissioned; no new fossil CHP installed', 'wales'),
  _row('2035', 'Independent sector: IHPN ambition for providers to reach net zero', 'ihpn'),
])}
<p>See <a href="nhs-net-zero-targets.html">NHS net zero targets in England, Scotland and Wales</a>.</p>

<h2 id="carbon">Carbon factors and CHP</h2>
{_table('Carbon factors', [
  _row('0.13', 'kg CO₂e per kWh of grid electricity, UK government factor for 2026 reporting (0.177 for 2025)', 'ghg26'),
])}
<p>At that factor, a typical gas CHP engine now emits more than buying grid electricity and making the heat in a boiler. Our worked comparison puts the CHP route about a third higher, and more than twice grid electricity with a heat pump; see <a href="moving-away-from-chp.html">moving away from gas CHP</a> for the assumptions.</p>

<h2 id="funding">Funding</h2>
{_table('Funding for NHS decarbonisation', [
  _row('2027/28', 'Public Sector Decarbonisation Scheme: no new rounds beyond this; Phase 4 projects run to 31 March 2028', 'psds'),
  _row('£510', 'PSDS Phase 4 cap on grant per tonne of CO₂e saved over a project\'s life', 'psds4'),
  _row('£100m', 'Great British Energy funding for NHS trust solar and batteries (March 2025): 132 projects at 78 trusts', 'gbe100'),
  _row('162', 'NHS sites in England with completed solar through the programme by May 2026, with £25m more for up to 40 sites', 'gbe1'),
  _row('£74m', 'Clean energy and efficiency upgrades shared by 82 NHS trusts, eight military sites and a prison (February 2026)', 'clean'),
])}
<p>See <a href="decarbonisation-funding.html">funding for healthcare decarbonisation</a>.</p>

<h2 id="savings">The biggest single saving</h2>
{_table('Theatre ventilation savings', [
  _row('132 to 286 MWh', 'Energy saved per operating theatre each year by switching off or setting back ventilation when empty', 'netb'),
  _row('~3,300', 'Operating theatres in England', 'netb'),
  _row('25 to 30 min', 'Active ventilation needed before a theatre is used after a long shutdown', 'netb'),
])}
<p>See <a href="base-load.html#theatres">theatre ventilation and base load</a> and the <a href="example-hospital-analysis.html">worked example</a>, where a failed setback costs a community hospital about £31,000 a year.</p>

<h2 id="rules">Reporting and procurement rules</h2>
{_table('Reporting and procurement', [
  _row('10%', 'Minimum weighting for net zero and social value in NHS procurements since April 2022', 'supp'),
  _row('April 2024', 'Carbon reduction plan required for all new NHS procurements', 'supp'),
  _row('1 April 2027', 'Stricter carbon reduction plan standard for contracts of £5m a year or more and new frameworks', 'crp27'),
  _row('31 Dec 2026', 'ESOS Phase 4 qualification date for large undertakings, including private hospital groups', 'esos'),
])}
<p>See <a href="private-hospitals.html">private and independent hospitals</a>.</p>
''' + sources_for(*K),
  [('estate', 'The size of the estate'), ('targets', 'Net zero targets'), ('carbon', 'Carbon factors and CHP'), ('funding', 'Funding'), ('savings', 'The biggest single saving'), ('rules', 'Reporting and procurement')],
  [('How much energy does the NHS use?', 'NHS trusts in England used around 11 billion kWh of energy in a year, according to the Estates Returns Information Collection, and spent about £14.4 billion running their estates in 2025/26.'),
   ('When does the NHS have to reach net zero?', 'In England, 2040 for emissions the NHS controls directly and 2045 including the supply chain. NHS Scotland aims for 2040, with renewable heat in all NHS-owned buildings by 2038. NHS Wales has interim targets of 16% by 2025 and 34% by 2030.'),
   ('What is the grid carbon factor for 2026?', 'About 0.13 kg CO2e per kWh in the UK government conversion factors for 2026 reporting, down from 0.177 for 2025.'),
   ('How much energy does theatre ventilation setback save?', 'NHS England estimates 132 to 286 MWh per operating theatre each year, across about 3,300 theatres in England.')],
  [('healthcare-estates-decarbonisation.html', 'The estates challenge', 'What these numbers mean, and where to start.'),
   ('nhs-net-zero-targets.html', 'Net zero targets', 'The targets in full.'),
   ('example-hospital-analysis.html', 'Worked example', 'The figures on one hospital.')],
  'Sourced key figures for NHS estates energy (checked November 2026): £14.4bn estate cost and ~11bn kWh energy (ERIC 2025/26), £15.9bn backlog, net zero 2040/2045 England, 2040 Scotland with renewable heat by 2038, Wales 34% by 2030 and no fossil CHP after 2035, grid factor 0.13 kg/kWh (2026), PSDS ending, GBE £100m NHS solar, theatre setback 132-286 MWh per theatre.'))

PAGES[0].section = 'Guides'
