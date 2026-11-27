# news-image-20261127 — The World Today: Friday 27 November 2026

[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/Biose-dot/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/Biose-dot/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

A one-image front page summing up the world's news of **Friday 27 November 2026**,
built for the make.fun competition
[`news-image-20261127`](https://make.fun/c/news-image-20261127).

## The image

`entry.png` (1024×1024, 187,834 bytes) is a newspaper front page,
**"THE WORLD TODAY — Friday, 27 November 2026"**, drawn from scratch in
Python with Pillow (`build_frontpage.py`). It carries **36 real stories**
first reported on 27 November 2026, across four regions:

- **Lead story:** the Thanksgiving storm that delayed Macy's 100th parade
  for the first time — 500,000+ without power, 1,000+ flights cancelled
  or delayed, 80 million Americans travelling.
- **Middle East (6):** Iran drone strike in Kuwait, Gaza, Saudi Jazan
  refinery, Cairo tanker crash, Guinea-Bissau election delay, DR Congo
  Ebola outbreak past 12,000 cases.
- **Europe (10):** Depardieu trial, UK migration low, next ECB president,
  Poundland collapse, Norse Atlantic grounding, Rosebank revolt, Ibiza
  tanker, French presidential race, Belgium satellite factory, UK train
  stabbing verdict.
- **Americas (9):** Trump on GDP and tariffs, SpaceX satellites, Musk's
  share plan, FCC vs ABC, Mexico vs DEA, Miami ground stop, ICE lottery
  arrest, Andy Taylor's death.
- **Asia-Pacific (10):** World Chess Championship, India PMLA bench,
  Bangkok refinery blast, NZ election results, Sinner's withdrawal,
  Kim Jong Un, Hong Kong fire, Myanmar ICJ rejection, Nepal landslides,
  Zelensky on the US.

Every headline is a real event of that day, stated as reported — no hype,
no speculation.

## How it runs

`main.py` (Python 3, standard library only, no network) copies the
committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default
`/output`), after validating the PNG signature, IEND trailer and the
1 MiB size cap. Both runs write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

To redraw the image from scratch:

```sh
python3 build_frontpage.py   # writes entry.png (needs Pillow)
```

## Repository

- GitHub: https://github.com/Biose-dot/news-image-20261127
- Competition: https://make.fun/c/news-image-20261127
- License: MIT (see `LICENSE`)
