"""Build every logo asset from the two supplied Hospital Energy Insights PNGs.

Sources (transparent, 900 x 300, used as supplied, no recolouring):
  tools/brand/hei-logo-light.png   dark wordmark, for white and light backgrounds
  tools/brand/hei-logo-dark.png    white wordmark, for the navy footer and share card

From them this makes:
  - hei-logo.png/.webp         header and light backgrounds (from light)
  - hei-logo-white.png/.webp   footer and other dark backgrounds (from dark)
  - hei-pdf-logo.png           calculator PDF header, 800x200 on white
  - favicons, apple-touch-icon, favicon.ico (the round mark only)
  - analyser/src/local/hhiLogo.ts   JPEG on white for the app and its PDFs
  - tools/guide/img/hhi-logo.png    user guide
  - site/images/og-image.png        share card (logo region repainted)

The only clean-up is trimming the empty margin and dropping near-invisible
haze (alpha < 12), so edges stay crisp on coloured backgrounds.

To change the logo: replace the two source files and run
    python3 tools/make_brand.py && python3 tools/build_pages.py
then rebuild the analyser (cd analyser && npm run build) and the user guide
(python3 tools/build_guide.py). Header and footer markup sizes are printed
below; update LOGO_W / LOGO_WHITE_W in tools/kit.py if they change.
"""
import base64, io, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
SRC_LIGHT = os.path.join(HERE, 'brand', 'hei-logo-light.png')
SRC_DARK = os.path.join(HERE, 'brand', 'hei-logo-dark.png')
BRAND = os.path.join(ROOT, 'site', 'images', 'brand')
MARK_RIGHT = 364            # the round mark ends before the divider line (source px)


def load(path, right=None):
    im = Image.open(path).convert('RGBA')
    if right:
        im = im.crop((0, 0, right, im.height))
    a = np.array(im)
    a[a[..., 3] < 12] = 0
    im = Image.fromarray(a)
    return im.crop(im.getbbox())


def fit_h(im, h):
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def on(bg, im, size=None, pad=0):
    canvas = Image.new('RGBA', size or im.size, bg + (255,))
    x = pad if size else 0
    y = (canvas.height - im.height) // 2 if size else 0
    canvas.alpha_composite(im, (x, y))
    return canvas.convert('RGB')


def square(im):
    s = max(im.size)
    sq = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    sq.alpha_composite(im, ((s - im.width) // 2, (s - im.height) // 2))
    return sq


def main():
    lite = load(SRC_LIGHT)
    dark = load(SRC_DARK)
    H = 264  # 2x the 132px the markup reserves
    for name, im in (('hei-logo', lite), ('hei-logo-white', dark)):
        out = fit_h(im, H)
        out.save(os.path.join(BRAND, name + '.png'), optimize=True)
        out.save(os.path.join(BRAND, name + '.webp'), quality=90, method=6)
        print(f'{name}: {out.size}, markup width at 132px high = {round(out.width / 2)}')

    pdf = fit_h(lite, 176)
    on((255, 255, 255), pdf, (800, 200), pad=12).save(os.path.join(BRAND, 'hei-pdf-logo.png'), optimize=True)

    m = square(load(SRC_LIGHT, right=MARK_RIGHT))
    for s in (16, 32, 48, 192):
        m.resize((s, s), Image.LANCZOS).save(os.path.join(BRAND, f'favicon-{s}.png'), optimize=True)
    for s, name in ((512, 'favicon-512.png'), (180, 'apple-touch-icon.png')):
        inner = m.resize((round(s * 0.86),) * 2, Image.LANCZOS)
        c = Image.new('RGBA', (s, s), (255, 255, 255, 255))
        c.alpha_composite(inner, ((s - inner.width) // 2,) * 2)
        c.convert('RGB').save(os.path.join(BRAND, name), optimize=True)
    m.resize((48, 48), Image.LANCZOS).save(os.path.join(ROOT, 'site', 'favicon.ico'),
                                            sizes=[(16, 16), (32, 32), (48, 48)])

    app = on((255, 255, 255), fit_h(lite, 264))
    buf = io.BytesIO(); app.save(buf, 'JPEG', quality=90, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    with open(os.path.join(ROOT, 'analyser', 'src', 'local', 'hhiLogo.ts'), 'w') as f:
        f.write('/**\n * Hospital Energy Insights logo (round mark with the wordmark), as on the\n'
                ' * website. JPEG on white, for the app header and PDFs. Made by\n'
                ' * tools/make_brand.py.\n */\n'
                f'export const HHI_LOGO_ASPECT = {app.width}/{app.height};\n\n'
                f"export const HHI_LOGO = 'data:image/jpeg;base64,{b64}';\n")
    app.save(os.path.join(HERE, 'guide', 'img', 'hhi-logo.png'), optimize=True)

    og_card(dark)


def og_card(dark):
    """Repaint the logo area of the share card from the source photo.

    The card is the dusk photo scaled to 1200 wide, cropped at y=135, under
    a flat navy overlay (0.378 x photo + (6.7, 28.4, 48.7)).
    """
    path = os.path.join(ROOT, 'site', 'images', 'og-image.png')
    og = Image.open(path).convert('RGB')
    ph = Image.open(os.path.join(ROOT, 'site', 'images', 'photos', 'hc-private-hospital-dusk.jpg')).convert('RGB')
    ph = ph.resize((1200, round(ph.height * 1200 / ph.width)), Image.LANCZOS).crop((0, 135, 1200, 765))
    base = np.clip(np.array(ph).astype(float) * 0.378 + np.array([6.7, 28.4, 48.7]), 0, 255).astype(np.uint8)
    box = (55, 45, 620, 225)
    og.paste(Image.fromarray(base).crop(box), box[:2])
    og = og.convert('RGBA')
    logo = fit_h(dark, 150)
    og.alpha_composite(logo, (70, 58))
    og.convert('RGB').save(path, optimize=True)


if __name__ == '__main__':
    main()
