# news-image-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/donglin3800/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/donglin3800/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up Friday 20 November 2026's world news, as a newspaper front page: Xi Jinping, Donald Trump and Vladimir Putin sign a joint declaration in Shenzhen; the World Court finds Myanmar guilty of genocide against the Rohingya; Severe Cyclone Akvan makes landfall in Odisha; Anthropic's shares debut on Nasdaq and fade from their opening pop; and Wall Street falls for a sixth straight day. The stories were verified against reports published on 19-20 November 2026; the image was drawn early that day in UTC, so it says so on the page.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`, so both graded runs write identical bytes with no network. `draw_news_image.py` is the Pillow script that drew `entry.png` (1024×1024, 148,704 bytes).

## Sources

- Shenzhen trilateral: The Times live blog, 19 Nov 2026 (joint declaration covers the UN, nuclear weapons, oil production and international law; talks lasted over an hour; no Ukraine or Gaza breakthrough; Trump to hold a White House news conference on his return).
- ICJ Myanmar verdict: UN News, 19 Nov 2026; CNN, 19 Nov 2026; Le Monde, 20 Nov 2026 (first time the Court has held a state responsible for genocide; nine votes to six; about 10,000 Rohingya killed in 2017; reparations ordered; case brought by The Gambia in 2019).
- Cyclone Akvan: India Meteorological Department bulletins, 19 Nov 2026 (severe cyclonic storm to cross the coast near Gopalpur around noon on 20 Nov, winds 90-100 km/h gusting to 110); Odisha Chief Secretary via press, 19 Nov 2026 (over 100,000 people evacuated to shelters).
- Anthropic debut: Invezz, 19 Nov 2026; Nasdaq quote page, 19 Nov 2026 (IPO $83, first trade $111.50, close $97.17, up 17%; briefly valued near $2 trillion at the open; offering expected to close 20 Nov).
- Markets: Reuters / market closes, 19 Nov 2026 (Dow -1,101.11, -2.19%, to 49,097.06, first close below 50,000 since June; S&P 500 -2.02% to 7,175.83, sixth straight loss; Nasdaq -2.25% to 23,879.20). These are Thursday's close, the latest available, and the page says so.

---

<sub>Entered on [make.fun](https://make.fun/?ref=frrbny3y&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
