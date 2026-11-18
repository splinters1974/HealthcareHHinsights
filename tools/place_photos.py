"""
Healthcare photos (from the Healthcare HH Insights Google Drive folder, Nov 2026).

    python3 tools/place_photos.py /path/to/drive-folder

Takes the numbered PNGs, saves each as a page photo (site/images/photos/hc-*.jpg
and -800.jpg), a page header (site/images/heroes/<page>.jpg, -900, WebP) and a
link and share card (site/images/guides/<page>.jpg, 1200 x 630, and -600).
Then rebuild with tools/build_pages.py. Needs Pillow.

The pictures are illustrations of made-up sites. Keep NHS logos out of any
replacement.
"""
import os
import sys

from PIL import Image

ROOT = os.path.join(os.path.dirname(__file__), '..', 'site', 'images')
PHOTOS = {  # drive number -> photo name
    '01': 'hc-public-hospital-solar', '02': 'hc-private-hospital-carport', '03': 'hc-heat-pump-plant-room',
    '04': 'hc-efficient-ward', '05': 'hc-energy-control-room', '06': 'hc-rooftop-solar-install',
    '07': 'hc-battery-ev-charging', '08': 'hc-strategy-meeting', '09': 'hc-thermal-survey', '10': 'hc-private-hospital-dusk',
}
# page -> (photo, horizontal focus 0..1 for the wide crops)
PAGES = {
    'acute-hospitals': ('01', 0.5), 'sectors': ('01', 0.5), 'nhs-net-zero-targets': ('01', 0.35),
    'private-hospitals': ('02', 0.6), 'solar': ('02', 0.5),
    'heat-decarbonisation': ('03', 0.6), 'moving-away-from-chp': ('03', 0.85),
    'hospital-energy-efficiency': ('04', 0.5), 'community-and-mental-health': ('04', 0.35),
    'how-it-works': ('05', 0.5), 'estates-returns-and-benchmarking': ('05', 0.4),
    'solar-on-healthcare-estates': ('06', 0.5), 'solar-planning-and-grid': ('06', 0.7),
    'hospital-electrical-capacity': ('07', 0.4), 'ambulance-stations-and-fleet': ('07', 0.75),
    'healthcare-estates-decarbonisation': ('08', 0.5), 'decarbonisation-funding': ('10', 0.55), 'guides': ('06', 0.5),
    'health-centres-and-clinics': ('09', 0.6),
}


def crop(im, w, h, fx):
    """Crop to w:h around horizontal focus fx, then resize."""
    tw = min(im.width, round(im.height * w / h))
    th = round(tw * h / w)
    left = max(0, min(im.width - tw, round(fx * im.width - tw / 2)))
    top = max(0, (im.height - th) // 2)
    return im.crop((left, top, left + tw, top + th)).resize((w, h), Image.LANCZOS)


def main(src):
    ims = {}
    for n, name in PHOTOS.items():
        f = next(x for x in os.listdir(src) if x.startswith(n) and x.lower().endswith('.png'))
        im = Image.open(os.path.join(src, f)).convert('RGB')
        ims[n] = im
        im.save(os.path.join(ROOT, 'photos', f'{name}.jpg'), quality=82, optimize=True, progressive=True)
        im.resize((800, round(im.height * 800 / im.width)), Image.LANCZOS).save(
            os.path.join(ROOT, 'photos', f'{name}-800.jpg'), quality=80, optimize=True, progressive=True)
    for page, (n, fx) in PAGES.items():
        im = ims[n]
        # Header: wide strip, no upscaling past the source width.
        for width, suffix in [(im.width, ''), (900, '-900')]:
            hero = crop(im, width, round(width * 0.42), fx)
            hero.save(os.path.join(ROOT, 'heroes', f'{page}{suffix}.jpg'), quality=80, optimize=True, progressive=True)
            hero.save(os.path.join(ROOT, 'heroes', f'{page}{suffix}.webp'), quality=78, method=6)
        card = crop(im, 1200, 630, fx)
        card.save(os.path.join(ROOT, 'guides', f'{page}.jpg'), quality=82, optimize=True, progressive=True)
        card.resize((600, 315), Image.LANCZOS).save(os.path.join(ROOT, 'guides', f'{page}-600.jpg'), quality=80, optimize=True, progressive=True)
    print(f'wrote {len(PHOTOS)} photos and {len(PAGES)} headers and cards')


if __name__ == '__main__':
    main(sys.argv[1])
