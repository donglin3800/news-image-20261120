#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news front page (1024x1024 PNG).

One image, five verified stories, drawn with Pillow only. Every fact on
the page was checked against reports published on 19-20 November 2026
(see README.md for the sources). The page is drawn early on 20 November
UTC, so stories that closed on Thursday 19 November are dated as such
on the page itself.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 232)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (24, 68, 128)
GREY = (90, 86, 76)
RULE = (18, 18, 18)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines fitting `width` px."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, width, leading, color=INK):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def headline(draw, x, y, text, fnt, width, leading):
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=INK)
        y += leading
    return y


def kicker(draw, x, y, text):
    f = font(SANS_B, 19)
    draw.text((x, y), text, font=f, fill=RED)
    return y + 26


def box(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], outline=RULE, width=2)


def flag_strips(draw, x, y, w, h):
    """Three small flag strips: China, USA, Russia."""
    third = w // 3
    # China: red field, five small yellow stars.
    draw.rectangle([x, y, x + third - 8, y + h], fill=(222, 41, 16))
    for sx, sy, r in [(x + 16, y + 16, 7), (x + 38, y + 12, 4),
                      (x + 48, y + 26, 4), (x + 38, y + 40, 4),
                      (x + 20, y + 38, 4)]:
        draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 222, 0))
    # USA: red and white stripes with a blue canton.
    ux = x + third
    for i in range(7):
        col = (178, 34, 52) if i % 2 == 0 else (255, 255, 255)
        draw.rectangle([ux, y + i * h // 7, ux + third - 8,
                        y + (i + 1) * h // 7], fill=col)
    draw.rectangle([ux, y, ux + third // 2, y + h // 2], fill=(30, 50, 120))
    # Russia: white, blue, red horizontal bands.
    rx = x + 2 * third
    for i, col in enumerate([(255, 255, 255), (0, 57, 166), (213, 0, 50)]):
        draw.rectangle([rx, y + i * h // 3, rx + third - 8,
                        y + (i + 1) * h // 3], fill=col)
    draw.rectangle([x, y, x + w - 8, y + h], outline=RULE, width=2)


def cyclone(draw, cx, cy, r):
    """Spiral storm: concentric arcs in deep blue."""
    for k in range(5):
        rr = r * (1 - k * 0.16)
        draw.arc([cx - rr, cy - rr, cx + rr, cy + rr],
                 start=20 + k * 55, end=300 + k * 55,
                 fill=(24, 68, 128), width=7)
    draw.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # Double outer rule.
    d.rectangle([14, 14, W - 14, H - 14], outline=RULE, width=3)
    d.rectangle([22, 22, W - 22, H - 22], outline=RULE, width=1)

    # Masthead.
    title = "THE WORLD IN ONE PAGE"
    tf = font(SERIF_B, 62)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 34), title, font=tf, fill=INK)
    d.line([40, 118, W - 40, 118], fill=RULE, width=3)
    sub = "FRIDAY 20 NOVEMBER 2026  ·  THE DAY'S NEWS IN ONE IMAGE"
    sf = font(SANS_B, 22)
    sw = d.textlength(sub, font=sf)
    d.text(((W - sw) / 2, 128), sub, font=sf, fill=INK)
    d.line([40, 164, W - 40, 164], fill=RULE, width=1)

    # --- Lead story: Shenzhen summit (full width, y 178-418) ---
    box(d, 36, 178, 952, 240)
    y = kicker(d, 52, 190, "SHENZHEN  ·  THE SUMMIT")
    y = headline(d, 52, y, "Three leaders, one declaration",
                 font(SERIF_B, 40), 620, 48)
    y = para(d, 52, y + 4,
             "Xi Jinping, Donald Trump and Vladimir Putin meet in "
             "Shenzhen and sign a joint declaration pledging UN reform, "
             "nuclear limits and more oil output. No Ukraine or Gaza "
             "breakthrough; Trump flies home for a White House briefing.",
             font(SANS, 20), 620, 25)
    flag_strips(d, 700, 218, 272, 118)

    # --- Row 2: ICJ verdict | Cyclone Akvan (y 432-672) ---
    box(d, 36, 432, 466, 240)
    y = kicker(d, 52, 444, "THE HAGUE  ·  WORLD COURT")
    y = headline(d, 52, y, "Myanmar guilty of genocide",
                 font(SERIF_B, 28), 434, 34)
    y = para(d, 52, y + 6,
             "The International Court of Justice finds Myanmar guilty of "
             "genocide against the Rohingya, the first state it has ever "
             "held responsible. Nine to six; about 10,000 killed in 2017; "
             "reparations ordered.",
             font(SANS, 19), 434, 24)

    box(d, 522, 432, 466, 240)
    y = kicker(d, 538, 444, "ODISHA, INDIA  ·  WEATHER")
    y = headline(d, 538, y, "Cyclone Akvan hits India",
                 font(SERIF_B, 28), 434, 34)
    y = para(d, 538, y + 6,
             "Severe Cyclone Akvan lands near Gopalpur around noon, "
             "winds 90-100 km/h, gusts to 110. Over 100,000 people in "
             "shelters; red alerts in 11 districts.",
             font(SANS, 19), 300, 24)
    cyclone(d, 905, 578, 58)

    # --- Row 3: Anthropic debut | Wall Street sell-off (y 686-886) ---
    box(d, 36, 686, 466, 200)
    y = kicker(d, 52, 698, "NEW YORK  ·  TECHNOLOGY")
    y = headline(d, 52, y, "Anthropic's debut fades",
                 font(SERIF_B, 28), 434, 34)
    d.text((52, y + 4), "ANT  $97.17", font=font(SANS_B, 36), fill=INK)
    d.text((322, y + 12), "+17%", font=font(SANS_B, 28), fill=BLUE)
    y = para(d, 52, y + 56,
             "Opens $111.50, up 34% on the $83 IPO price; briefly near "
             "$2 trillion. The offering closes today.",
             font(SANS, 19), 434, 24)

    box(d, 522, 686, 466, 200)
    y = kicker(d, 538, 698, "WALL STREET  ·  MARKETS")
    y = headline(d, 538, y, "Sixth straight fall",
                 font(SERIF_B, 28), 434, 34)
    d.text((538, y + 4), "DOW  -2.19%", font=font(SANS_B, 36), fill=RED)
    y = para(d, 538, y + 56,
             "Dow falls 1,101 points to 49,097, its first close below "
             "50,000 since June. S&P 500 -2.02%, Nasdaq -2.25%.",
             font(SANS, 19), 434, 24)

    # --- Footer ---
    d.line([40, 900, W - 40, 900], fill=RULE, width=1)
    foot = ("Drawn early on Friday 20 November 2026 (UTC). The summit, the court "
            "verdict, the market close and the Anthropic debut are Thursday "
            "19 November's news as reported overnight; the cyclone landfall "
            "is today. Sources: The Times, UN News, CNN, Le Monde, India "
            "Meteorological Department, Nasdaq, Invezz.")
    para(d, 40, 912, foot, font(SANS, 16), 944, 22, color=GREY)

    img.save("entry.png", format="PNG")
    print("wrote entry.png")


if __name__ == "__main__":
    main()
