# Hospital Energy Insights

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

### Search and duplicate content

- **Search titles and descriptions** live in `tools/seo_meta.py` (titles up to
  60 characters, descriptions 120 to 160). The build warns about any page
  outside those limits.
- **Pages copied from the sister sites** (supplier data guides, MPAN, prices,
  non-energy charges, benchmarks, and the general solar cost,
  generation and method guides) stay for the journey, but their canonical link
  points at the original on Half Hourly Insights or the UK Solar Calculator, and
  they're left out of the sitemap and llms.txt. The list is
  `CANONICAL_ELSEWHERE` in `tools/kit.py`. Rewrite a page for healthcare before
  taking it off that list.
- **The worked example** uses the made-up `site/samples/example-hospital.csv`
  (`python3 tools/make_samples.py`). Its figures are locked in
  `analyser/tests/website-claims.test.ts`, so a change to the file or the engine
  fails the tests instead of leaving the page out of date.

### Keeping pages current

Funding, policy and price pages are reviewed every six months, other guides
every year. `python3 tools/review_due.py` lists what's due; the build also
warns about anything overdue. After checking a page's figures against their
sources, update its date in `tools/review.json`. Change a figure on a guide and
the same figure on `nhs-estates-energy-facts.html` in the same commit.

## Who runs it

Run by Kinetic Energy Consulting, as with the UK Solar Calculator and Half
Hourly Insights. Named contact: Paul Johnston. Not affiliated with or endorsed
by the NHS. These are set at the top of `tools/kit.py`.

## Before going live

- **Domain:** hospitalenergy.co.uk, registered at Porkbun (22 Nov 2026) and set as `SITE_URL` in `tools/kit.py`. DNS at Porkbun: `ALIAS` at the apex to `apex-loadbalancer.netlify.com`, `CNAME www` to `healthcarehhinsights.netlify.app`. Then submit the sitemap in Google Search Console and Bing Webmaster Tools.
- **Netlify:** the `healthcarehhinsights` project deploys `main` (publish directory `site`). Add hospitalenergy.co.uk as the primary domain and www as an alias under Domain management, so Netlify issues the HTTPS certificate.
- **Google Maps key:** the calculator's map mode uses the UK Solar Calculator's Maps API key. Add the new domain to that key's allowed referrers in Google Cloud, or the map will not load.
- **Email shown:** `enquiries@hospitalenergy.co.uk` (`CONTACT_EMAIL` in `tools/kit.py`), a Porkbun email forward to the owner's inbox.
- **Enquiry form:** posts to a Formspree form (`FORM_ENDPOINT` in `tools/pages_core.py`), currently the Half Hourly Insights one. Create a Formspree form for this site that delivers to the owner's inbox, and put its ID in `FORM_ENDPOINT`. The delivery address lives in Formspree, so it never appears in the page code.
- **Leads:** calculator report requests and customer-edition details are emailed through EmailJS to `LEAD_EMAIL` in `tools/kit.py` (and `analyser/src/local/editionLead.ts`), now `enquiries@hospitalenergy.co.uk`.
- **Images:** add photos to `site/images/heroes/` and `site/images/photos/` (see `tools/make_heroes.py`). Keep NHS logos out of every image.
