#!/usr/bin/env python3
"""Draw the front page: 'THE WORLD TODAY — Friday 27 November 2026'.

One 1024x1024 PNG summing up the world's news of Friday 27 November 2026.
36 real stories, grouped by region, drawn with Pillow only.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

PAPER = (248, 244, 233)
INK = (17, 17, 17)
NAVY = (14, 42, 71)
RED = (163, 22, 33)
GREY = (90, 86, 76)
RULE = (180, 172, 150)

REGIONS = {
    "MIDDLE EAST": (179, 84, 30),
    "EUROPE": (31, 78, 121),
    "AMERICAS": (46, 107, 52),
    "ASIA-PACIFIC": (122, 31, 92),
}

# (region, headline, one-line description, <= ~50 chars so it stays one line)
STORIES = [
    ("MIDDLE EAST", "Iran drone strike hits Kuwait, kills two Italian workers",
     "Tehran denies role; Rome demands answers."),
    ("MIDDLE EAST", "Israel kills 10 in Gaza; Hamas weighs response",
     "Deadly strikes test the fragile ceasefire."),
    ("MIDDLE EAST", "Saudi Jazan refinery attacked; Nepali worker killed",
     "Blast at Red Sea plant raises escalation fears."),
    ("MIDDLE EAST", "Egypt detains driver over Cairo tanker crash",
     "Tanker collision killed 31; safety probed."),
    ("MIDDLE EAST", "Guinea-Bissau junta delays elections to 2028",
     "Military rulers extend transition to 2028."),
    ("MIDDLE EAST", "Ebola outbreak in DR Congo passes 12,000 cases",
     "Health workers race to contain the spread."),
    ("EUROPE", "Depardieu ordered to stand trial over alleged rape",
     "French court sends film star to trial."),
    ("EUROPE", "UK net migration falls to lowest since 1997",
     "Tighter visa rules cut arrivals sharply."),
    ("EUROPE", "Spain's ex-central bank chief picked as next ECB president",
     "Choice signals continuity at eurozone top."),
    ("EUROPE", "Poundland collapses into administration",
     "11,000 jobs at risk as chain fails."),
    ("EUROPE", "Norse Atlantic halts all flights, faces collapse",
     "Budget carrier grounds fleet; travellers stranded."),
    ("EUROPE", "Nearly 100 Labour MPs oppose Rosebank oil field",
     "Backbench revolt pressures Starmer on drilling."),
    ("EUROPE", "Diesel tanker overturns near Ibiza; one dead",
     "Crash spills fuel near tourist coast."),
    ("EUROPE", "French mainstream risks failure in presidential race",
     "Centre parties struggle as extremes dominate."),
    ("EUROPE", "Belgium opens Europe's largest satellite factory",
     "Plant will build 500 satellites a year."),
    ("EUROPE", "UK train stabber convicted of attempted murder of 14",
     "Court finds attacker guilty after rampage."),
    ("AMERICAS", "Trump demands probe of 'fake' GDP figures",
     "Growth revised up to 4.3%; president claims rigged."),
    ("AMERICAS", "Trump tariffs hit 14 trading partners, up to 40%",
     "New duties escalate trade war with allies."),
    ("AMERICAS", "FCC lets SpaceX deploy 1m satellites",
     "Approval paves way for space data centres."),
    ("AMERICAS", "Musk: every US child to get 2 SpaceX shares",
     "Plan to give children a stake in space firm."),
    ("AMERICAS", "Judge: FCC violated ABC's free speech",
     "Court rules regulator overstepped on licences."),
    ("AMERICAS", "Mexico's president criticises DEA tip line",
     "Sheinbaum rebukes US agency over hotline."),
    ("AMERICAS", "FAA ground stop in Miami after FedEx jet leaves runway",
     "Cargo plane skids off tarmac in Miami."),
    ("AMERICAS", "Lottery winner arrested by ICE after $1m win",
     "Jackpot claimant detained in enforcement sweep."),
    ("AMERICAS", "Duran Duran guitarist Andy Taylor dies aged 65",
     "Band mourns founding member after long illness."),
    ("ASIA-PACIFIC", "World Chess: Gukesh vs Sindarov in marathon draw",
     "Game 3 of title match ends level."),
    ("ASIA-PACIFIC", "India court: judicial member must sit on PMLA bench",
     "Top court also scraps Anand Mohan release."),
    ("ASIA-PACIFIC", "Bangkok refinery blast injures nine, three critical",
     "Bangchak shuts all units after explosion."),
    ("ASIA-PACIFIC", "NZ final results: coalition holds 67 of 131 seats",
     "About 400,000 special votes decided it."),
    ("ASIA-PACIFIC", "Sinner pulls out of Australian Open 2027",
     "Knee injury rules out world No. 1."),
    ("ASIA-PACIFIC", "Kim Jong Un vows more nuclear weapons",
     "North Korea ignores Trump's offer of talks."),
    ("ASIA-PACIFIC", "Hong Kong renovation fire kills 168",
     "Deadliest blaze in decades sparks inquiry."),
    ("ASIA-PACIFIC", "Myanmar rejects part of ICJ genocide ruling",
     "Junta dismisses court's Rohingya findings."),
    ("ASIA-PACIFIC", "Nepal declares 4,000 landslide victims dead",
     "Missing declared deceased after monsoon."),
    ("ASIA-PACIFIC", "Zelensky: US too focused on Middle East",
     "Kyiv questions Trump-Putin friendship."),
]

LEAD_HEAD = "Thanksgiving storm halts Macy's 100th parade"
LEAD_DESC = ("First delay in a century: 500,000+ without power, 1,000+ flights "
             "cancelled or delayed as 80 million Americans travel.")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(d, cx, cy, r):
    """Simple schematic globe: circle, meridians, parallels."""
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=NAVY, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=NAVY, width=2)
    d.line([cx, cy - r, cx, cy + r], fill=NAVY, width=2)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          0, 360, fill=NAVY, width=2)
    d.arc([cx - r, cy - r * 1.1, cx + r, cy + r * 0.1],
          0, 360, fill=NAVY, width=1)


def draw_storm(d, x, y, s):
    """Schematic storm cloud with rain and lightning."""
    c = (70, 90, 110)
    d.ellipse([x, y, x + s, y + s * 0.55], fill=c)
    d.ellipse([x + s * 0.25, y - s * 0.28, x + s * 0.85, y + s * 0.35], fill=c)
    d.ellipse([x + s * 0.55, y - s * 0.12, x + s * 1.05, y + s * 0.5], fill=c)
    for rx in [0.2, 0.5, 0.8]:
        d.line([x + s * rx, y + s * 0.62, x + s * rx - 3, y + s * 0.85],
               fill=(40, 90, 160), width=3)
    d.polygon([(x + s * 1.15, y + s * 0.1), (x + s * 0.95, y + s * 0.55),
               (x + s * 1.12, y + s * 0.55), (x + s * 0.92, y + s * 1.0),
               (x + s * 1.28, y + s * 0.45), (x + s * 1.1, y + s * 0.45)],
              fill=(230, 180, 30))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=2)

    # ---- Masthead ----
    f_title = font(SERIF, 58)
    f_sub = font(SANS_B, 15)
    f_date = font(SERIF, 26)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 16), title, font=f_title, fill=NAVY)
    d.line([24, 88, W - 24, 88], fill=INK, width=2)
    d.line([24, 92, W - 24, 92], fill=INK, width=1)
    date = "FRIDAY, 27 NOVEMBER 2026"
    dw = d.textlength(date, font=f_date)
    d.text(((W - dw) / 2, 98), date, font=f_date, fill=RED)
    sub = "THE WORLD IN ONE DAY  •  36 STORIES FROM EVERY REGION"
    sw = d.textlength(sub, font=f_sub)
    d.text(((W - sw) / 2, 130), sub, font=f_sub, fill=INK)
    draw_globe(d, 66, 52, 26)
    draw_globe(d, W - 66, 52, 26)

    # ---- Lead story band ----
    ly0, ly1 = 158, 262
    d.rectangle([16, ly0, W - 16, ly1], fill=(232, 226, 205),
                outline=NAVY, width=2)
    d.text((30, ly0 + 8), "LEAD STORY — UNITED STATES", font=font(SANS_B, 12),
           fill=RED)
    f_lead = font(SERIF, 30)
    d.text((30, ly0 + 26), LEAD_HEAD, font=f_lead, fill=INK)
    f_leadd = font(SANS, 15)
    for i, ln in enumerate(wrap(d, LEAD_DESC, f_leadd, 760)):
        d.text((30, ly0 + 62 + i * 19), ln, font=f_leadd, fill=(40, 40, 40))
    draw_storm(d, 868, ly0 + 22, 62)

    # ---- Three-column story grid ----
    cols = [STORIES[0:12], STORIES[12:24], STORIES[24:36]]
    col_x = [16, 352, 688]
    col_w = 320
    grid_top = 274
    grid_bot = 996
    f_head = font(SANS_B, 13)
    f_desc = font(SANS, 11)

    for ci, stories in enumerate(cols):
        x0 = col_x[ci]
        y = grid_top
        cur_region = None
        for region, head, desc in stories:
            if region != cur_region:
                cur_region = region
                col = REGIONS[region]
                d.rectangle([x0, y, x0 + col_w, y + 19], fill=col)
                d.text((x0 + 8, y + 4), region, font=font(SANS_B, 11),
                       fill=(255, 255, 255))
                y += 24
            lines = wrap(d, head, f_head, col_w - 4)
            for ln in lines:
                d.text((x0 + 2, y), ln, font=f_head, fill=INK)
                y += 15
            dlines = wrap(d, desc, f_desc, col_w - 4)
            for ln in dlines[:1]:
                d.text((x0 + 2, y), ln, font=f_desc, fill=(55, 55, 55))
                y += 13
            y += 4
            d.line([x0, y, x0 + col_w, y], fill=RULE, width=1)
            y += 8
        if y > grid_bot:
            raise SystemExit("column %d overflow: y=%d > %d" % (ci, y, grid_bot))
        if ci < 2:
            d.line([x0 + col_w + 8, grid_top, x0 + col_w + 8, grid_bot],
                   fill=RULE, width=1)

    # ---- Footer ----
    d.line([16, 1000, W - 16, 1000], fill=INK, width=1)
    foot = "All stories first reported on Friday 27 November 2026  •  Sources: Reuters, BBC, NYT and wire reports"
    fw = d.textlength(foot, font=font(SANS, 10))
    d.text(((W - fw) / 2, 1005), foot, font=font(SANS, 10), fill=GREY)

    img.save(OUT, optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
