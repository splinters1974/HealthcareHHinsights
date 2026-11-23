"""Build every logo asset from the designer's dark-background PNG.

Source: tools/brand/hei-logo-source-dark.png (white wordmark, transparent
background). From it this makes:
  - hei-logo-white.png/.webp   footer and other dark backgrounds
  - hei-logo.png/.webp         header and light backgrounds (navy wordmark)
  - hei-pdf-logo.png           calculator PDF header, 800x200 on white
  - favicons, apple-touch-icon, favicon.ico (the round mark only)
  - analyser/src/local/hhiLogo.ts   JPEG on white for the app and its PDFs
  - tools/guide/img/hhi-logo.png    user guide
  - site/images/og-image.png        share card (logo region repainted)

Clean-up applied to the source: near-invisible haze (alpha < 12) removed,
solid pixels made fully opaque, and the dark descenders on the "g" and "y"
of "Energy" recoloured to match the rest of the wordmark. On the
dark-background versions the navy cross is drawn white so it stays visible.

Run: python3 tools/make_brand.py
"""
import base64, io, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
SRC = os.path.join(HERE, 'brand', 'hei-logo-source-dark.png')
BRAND = os.path.join(ROOT, 'site', 'images', 'brand')
WHITE = (247, 251, 255)
INK = (11, 46, 79)          # --ink in site.css
TEXT_X = 560                # wordmark starts right of the divider


def clean():
    a = np.array(Image.open(SRC).convert('RGBA')).astype(int)
    al = a[..., 3]
    al[al < 12] = 0
    al[al >= 244] = 255
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    yy, xx = np.mgrid[:a.shape[0], :a.shape[1]]
    desc = (xx > TEXT_X) & (yy >= 315) & (yy <= 343) & (b > g + 4) & (r < 200) & (al > 0)
    a[desc, :3] = WHITE
    a[..., 3] = al
    im = Image.fromarray(a.astype(np.uint8))
    return im.crop(im.getbbox())


def white_cross(im):
    """The navy cross vanishes on dark backgrounds, so draw it white there."""
    a = np.array(im).astype(int)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    yy, xx = np.mgrid[:a.shape[0], :a.shape[1]]
    # source coordinates less the 35px bbox crop
    box = (xx >= 87) & (xx <= 235) & (yy >= 101) & (yy <= 249)
    m = box & (r < 90) & (b > r + 30) & (g < 125) & (a[..., 3] > 0)
    a[m, :3] = WHITE
    return Image.fromarray(a.astype(np.uint8))


def light(im):
    """Navy wordmark for light backgrounds; the teal 'Insights' stays."""
    a = np.array(im).astype(int)
    xx = np.mgrid[:a.shape[0], :a.shape[1]][1]
    x0 = TEXT_X - 35  # source was cropped by its bbox (left edge 35)
    w = (xx > x0) & (a[..., 0] > 200) & (a[..., 1] > 200) & (a[..., 2] > 200)
    a[w, :3] = INK
    return Image.fromarray(a.astype(np.uint8))


def fit_h(im, h):
    return im.resize((round(im.width * h / im.height), h), Image.LANCZOS)


def on(bg, im, size=None, pad=0):
    canvas = Image.new('RGBA', size or im.size, bg + (255,))
    x = pad if size else 0
    y = (canvas.height - im.height) // 2 if size else 0
    canvas.alpha_composite(im, (x, y))
    return canvas.convert('RGB')


def mark(im):
    """The round icon on its own, square, transparent."""
    a = np.array(im)
    xx = np.mgrid[:a.shape[0], :a.shape[1]][1]
    sub = im.crop((0, 0, TEXT_X - 70, im.height))
    sub = sub.crop(sub.getbbox())
    s = max(sub.size)
    sq = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    sq.alpha_composite(sub, ((s - sub.width) // 2, (s - sub.height) // 2))
    return sq


def main():
    dark = clean()
    lite = light(dark)
    dark = white_cross(dark)
    H = 264  # 2x the 132px the markup reserves
    for name, im in (('hei-logo-white', dark), ('hei-logo', lite)):
        out = fit_h(im, H)
        out.save(os.path.join(BRAND, name + '.png'), optimize=True)
        out.save(os.path.join(BRAND, name + '.webp'), quality=90, method=6)
        print(name, out.size)

    pdf = fit_h(lite, 176)
    on((255, 255, 255), pdf, (800, 200), pad=12).save(os.path.join(BRAND, 'hei-pdf-logo.png'), optimize=True)

    m = mark(lite)
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
    on((255, 255, 255), fit_h(lite, 264)).save(os.path.join(HERE, 'guide', 'img', 'hhi-logo.png'), optimize=True)

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
