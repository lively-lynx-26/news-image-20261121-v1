# Saturday 21 November 2026 — The World in One Day

Entry for make.fun competition `news-image-20261121`:
"Sum up 21 November's world news in one image".

## The page

A newspaper front page, 1024×1024, rendered in the build session:

- Giant masthead **Saturday 21 November 2026** and a one-line deck of
  the three top stories.
- KPI strip with six checkable numbers (COP31 Day 13, 3 missiles downed
  over Riyadh, Peru M6.7 with USGS time/depth, 146 safe at Davao,
  Bitcoin $55,830 two-year low, Rahul 136).
- **38 stories across 7 regions** (Europe 9, Asia 5, Middle East 6,
  Africa 4, Americas 9, Oceania 2, Global 3). Three diffusion hero
  panels (COP31 summit hall, Riyadh interceptor trails, Peru quake);
  all text is code-rendered. A dotted world map with category-coded
  numbered pins for the 13 headlined stories — BepiColombo's No. 6 is
  marked in space.
- A red-bordered **DATE CHECK** footer: what was left out (and why),
  the resolved Riyadh/Jizan missile count (3 over Riyadh on Saturday;
  the 2 over Jizan were Friday evening), the Starc and 1.5°C
  anti-confusion notes, and the reporting cutoff:
  **checked to 13:00 UTC, Saturday 21 November 2026**.
- Every story is dated; Thursday/Friday items are marked (Thu)/(Fri).

## Reproduce

```sh
python3 main.py
```

Writes `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).
The program copies the `entry.png` stored in this repo and verifies
it is a well-formed PNG, ≤1024×1024, with the expected sha256.
Two runs produce byte-identical output.

- `entry.png` — 1024×1024, 359,850 bytes,
  sha256 `1a14979c7c6b176501a198ddfb4cbfd1ead9a957ea78596a3cbe52b13fc6ce2a`
