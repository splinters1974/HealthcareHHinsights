# Healthcare HH Insights

Free half-hourly electricity analysis, solar sizing and decarbonisation guides
for NHS and independent healthcare estates in England, Scotland and Wales.

It combines the two sister sites in one journey: the Half Hourly Insights
analyser (upload HH data first) and the UK Solar Calculator (sized from the
measured profile). The analyser runs entirely in the visitor's browser: meter
data is never uploaded.

## The journey

1. **Upload** half-hourly files for each meter (`site/analyser/`).
2. **Understand** base load, day and night use, out-of-hours use in clinics
   and offices, unusual days. New sites start on the 24-hour hospital preset.
3. **Check headroom** against agreed supply capacity for heat pumps, EV
   charging or CHP removal (Capacity tab).
4. **Size solar**: the Solar tab measures the share of output each site would
   use and opens `solar-calculator.html` with it (summary only, after the `#`).
5. **Report**: site and estate PDFs and Excel.

## What's here

| Path | What it is |
| --- | --- |
| `site/` | The published website (Netlify publishes this folder, see `netlify.toml`). |
| `site/analyser/index.html` | The analyser, one self-contained page built from `analyser/`. |
| `site/solar-calculator.html` | The solar calculator, built by `tools/build_calculator.py`. |
| `tools/build_pages.py` | Builds every page in `site/` (and the calculator page). Run `python3 tools/build_pages.py` after any edit. |
| `tools/kit.py` | Site settings (name, domain, contact, lead email), layout, nav, footer and structured data. |
| `tools/pages_healthcare.py` | Decarbonisation hub and healthcare guides, each sourced and dated. |
| `tools/pages_guides.py` | Data guides, glossary, healthcare settings pages and the guides index. |
| `tools/pages_solar.py`, `tools/pages_solarguides.py` | Solar sizing page and the solar guides taken from the UK Solar Calculator (`tools/content/solar/`). |
| `tools/vendor/` | The UK Solar Calculator's own calculator page and stylesheet, kept unchanged so its method stays in step. |
| `analyser/` | Source of the analyser (React, TypeScript, Vite). |

## Updating

```
cd analyser && npm ci && npm test && npm run build   # analyser
python3 tools/build_pages.py                         # pages and calculator
node scripts/check-static-site.mjs                   # links, images, SEO
```

To take a newer calculator from the UK Solar Calculator, copy its
`calculator.html` and `css/shared.css` over the two files in `tools/vendor/`
and rebuild. The build stops if a replacement no longer matches.

## Who runs it

Run by Kinetic Energy Consulting, as with the UK Solar Calculator and Half
Hourly Insights. Named contact: Paul Johnston. Not affiliated with or endorsed
by the NHS. These are set at the top of `tools/kit.py`.

## Before going live

- **Domain:** `SITE_URL` in `tools/kit.py` is set to `https://healthcarehhinsights.co.uk`. Buy it (or change it) and rebuild, then submit the sitemap in Google Search Console and Bing Webmaster Tools.
- **Netlify:** create a site from this repo (publish directory `site`), attach the domain, then merge the redirects in `netlify.toml`.
- **Google Maps key:** the calculator's map mode uses the UK Solar Calculator's Maps API key. Add the new domain to that key's allowed referrers in Google Cloud, or the map will not load.
- **Enquiry form:** the contact form posts to the Half Hourly Insights Formspree form (`FORM_ENDPOINT` in `tools/pages_core.py`). Create a separate form if you want these enquiries kept apart.
- **Leads:** calculator report requests and customer-edition details are emailed through EmailJS to `LEAD_EMAIL` in `tools/kit.py` (and `analyser/src/local/editionLead.ts`).
- **Images:** add photos to `site/images/heroes/` and `site/images/photos/` (see `tools/make_heroes.py`). Keep NHS logos out of every image.
