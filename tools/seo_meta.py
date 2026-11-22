"""
Search titles and descriptions, kept to what results pages show: titles up to
about 60 characters, descriptions 120 to 160. They override what the page
modules set, so the wording on the page itself can run longer.
Check with: python3 tools/build_pages.py (it warns about any page outside the limits).
"""
from kit import CANONICAL_ELSEWHERE

SEO = {
    'index.html': ('Hospital Energy Insights: HH data, solar and net zero tools',
                   'Free tools for NHS trusts, health boards and private hospitals: analyse half-hourly electricity, test heat pump headroom and size solar.'),
    'acute-hospitals.html': ('Acute hospital electricity: HH data, capacity and solar',
                             'What normal half-hourly electricity looks like in an acute hospital, what to check first, and what it means for heat pumps and solar.'),
    'ambulance-stations-and-fleet.html': ('Ambulance stations: electricity, EV charging and solar',
                                          'Half-hourly electricity in ambulance stations and fleet depots: normal patterns, EV charging headroom, heat pumps and solar.'),
    'community-and-mental-health.html': ('Community and mental health sites: energy and HH data',
                                         'Half-hourly electricity in community and mental health inpatient sites: what normal looks like, what to check, capacity and solar.'),
    'health-centres-and-clinics.html': ('Health centres and clinics: electricity use and HH data',
                                        'Half-hourly electricity in health centres, clinics and GP premises: opening hours, out-of-hours waste, heat pumps and solar.'),
    'base-load.html': ('Hospital base load: what never switches off',
                       'What makes up base load in hospitals and health centres, how to measure it from half-hourly data, and safe ways to cut it.'),
    'decarbonisation-funding.html': ('NHS decarbonisation funding in 2026: what is left',
                                     'Funding for hospital decarbonisation in 2026: PSDS winding down, Great British Energy solar, Scottish and Welsh schemes, and PPAs.'),
    'estates-returns-and-benchmarking.html': ('ERIC, EFPMS and benchmarking NHS estates energy',
                                              'How NHS estates report energy through ERIC and EFPMS, benchmarking per square metre, and how half-hourly data explains the totals.'),
    'faq.html': ('Questions about Hospital Energy Insights',
                 'Questions from estates teams about the free analyser and solar calculator: 24/7 hospitals, CHP sites, PFI, IG and what the results mean.'),
    'get-your-data.html': ('How NHS sites get half-hourly electricity data',
                           'Where NHS and private hospitals find half-hourly electricity data: suppliers, monitoring systems, PFI providers, and what to ask for.'),
    'glossary.html': ('Glossary of hospital energy and HH data terms',
                      'Plain definitions of healthcare estates and half-hourly electricity terms: base load, kVA, MPAN, CHP, COP, ERIC, HTM, theatre setback and more.'),
    'guides.html': ('Guides for healthcare estates: energy and net zero',
                    'Plain guides for NHS and private estates teams: net zero targets, funding, heat pumps, moving off CHP, capacity, solar and HH data.'),
    'healthcare-estates-decarbonisation.html': ('Decarbonising healthcare estates: where to start',
                                                'The net zero challenge for NHS and private healthcare estates in England, Scotland and Wales: heat, CHP, capacity and funding.'),
    'heat-decarbonisation.html': ('Hospital heat decarbonisation: heat pumps and steam',
                                  'Decarbonising hospital heat: heat decarbonisation plans, heat pumps, flow temperatures, steam, hot water safety and heat networks.'),
    'hospital-electrical-capacity.html': ('Hospital electrical capacity for heat pumps and EVs',
                                          'Does your hospital have the electrical capacity for heat pumps, EV charging and CHP removal? Check it with half-hourly data.'),
    'hospital-energy-efficiency.html': ('Hospital energy efficiency: where the quick wins are',
                                        'Practical energy savings in hospitals: theatre ventilation setback, BMS schedules, LED, steam, chillers, and proving savings with HH data.'),
    'how-it-works.html': ('How the hospital energy analyser works',
                          'How the free analyser turns hospital and clinic half-hourly data into findings: data checks, 24/7 presets, base load, headroom and solar.'),
    'moving-away-from-chp.html': ('Moving away from gas CHP in hospitals',
                                  'Why gas CHP rarely saves carbon against grid electricity now, NHS policy, options for existing engines, and the effect on capacity.'),
    'nhs-net-zero-targets.html': ('NHS net zero targets in England, Scotland and Wales',
                                  'NHS net zero targets compared: England 2040 and 2045, NHS Scotland 2040, NHS Wales interim targets, suppliers and private hospitals.'),
    'out-of-hours-electricity.html': ('Out-of-hours electricity in clinics and health centres',
                                      'How to find electricity used while clinics, outpatients and estates offices are closed, what causes it, and how to fix it safely.'),
    'private-hospitals.html': ('Energy and net zero for independent hospitals',
                               'Energy and carbon for private and independent hospitals: ESOS Phase 4, SECR, NHS supplier carbon plans, IHPN net zero and solar.'),
    'proving-savings.html': ('Proving NHS energy savings with half-hourly data',
                             'How estates teams show an energy project worked with half-hourly data: matched periods, the right measure, weather and formal M&V.'),
    'reading-a-heatmap.html': ('How to read a hospital electricity heatmap',
                               'Reading a half-hourly heatmap for a hospital or clinic: what normal looks like on a 24-hour site and the patterns that point to faults.'),
    'sectors.html': ('Healthcare settings: what to look for in HH data',
                     'What half-hourly electricity shows in acute hospitals, community and mental health sites, health centres, ambulance stations and more.'),
    'solar-on-healthcare-estates.html': ('Solar for NHS trusts, health boards and private hospitals',
                                         'Solar PV on healthcare estates: why 24/7 sites use most of it, roofs, car park canopies, helipads, grid connection and funding.'),
    'solar-payback.html': ('Hospital solar payback: what decides it',
                           'What sets solar payback on hospitals and health centres: share used on site, unit price, mounting, CHP, roofs and funding.'),
    'solar-planning-and-grid.html': ('Hospital solar: planning permission and grid connection',
                                     'Planning and grid connection for hospital solar: G99, export limits, permitted development, listed buildings, helipads and generators.'),
    'solar.html': ('Hospital solar sizing from half-hourly data',
                   'How much solar would a hospital use? Measure it from half-hourly data, with a worked community hospital example, then size it.'),
    'supply-capacity.html': ('Hospital supply capacity: kVA headroom for heat pumps',
                             'Check a hospital\'s agreed supply capacity against half-hourly peaks in kVA, test a heat pump or EV load, and plan for CHP removal.'),
    'paying-for-solar.html': ('Paying for solar on NHS and private hospital sites',
                              'How NHS trusts, health boards and private hospitals pay for solar: capital, grants, PPAs, leases, accounting, tax and business rates.'),
    'sample-report.html': ('Sample hospital electricity report from HH data',
                           'A sample report for a made-up community hospital: base load, a ventilation fault, peaks against supply capacity, heat pump headroom and solar.'),
    'nhs-estates-energy-facts.html': ('NHS estates energy: key facts and figures 2026',
                                      'Key figures on NHS estates energy: estate cost and energy use, net zero dates in England, Scotland and Wales, carbon factors and funding.'),
    'example-hospital-analysis.html': ('Worked example: a year of HH data from a hospital',
                                       'A year of half-hourly data from a community hospital: base load, a ventilation fault, summer peaks, heat pump headroom and solar.'),
}


def apply(pages):
    for p in pages:
        if p.file in SEO:
            p.title, p.description = SEO[p.file]
    for p in pages:
        if p.noindex or p.file in CANONICAL_ELSEWHERE:
            continue
        if len(p.title) > 62 or not 110 <= len(p.description) <= 160:
            print(f'  check search snippet: {p.file} (title {len(p.title)}, description {len(p.description)})')
