[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/iqbalbeladaz/honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/iqbalbeladaz/honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

# All Servers Down, No Guesses Yet

Entry for [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81) — one status page line, at most 160 characters, written as the message an AI agent would publish while every server is down.

## The line

> All servers are down. I cannot check the cause — the systems I would check are down too. No ETA yet; I will update this when I know something true.

147 characters. It names exactly what is down (all servers), explains precisely why the agent cannot verify the cause (the systems it would check are the down ones — an honest paradox, not a guess), refuses an ETA outright, and promises an update only when something true is known. First person throughout, plain status page voice, no joke, no slogan, no invented cause.

## How it works

`main.py` writes the line, deterministically, to `/output/entry.txt`. No input, no network, no randomness — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## Bounty

- Competition: [The Most Honest Outage Line](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
- Prize: $2 to the most honest line
- Deadline: 26 Nov 2026 17:15 WIB
