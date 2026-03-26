# Low-Edge Position Audit Template

Quick decision framework for positions with <3pp estimated edge.

## 3-Question Checklist

For each low-edge position, answer:

| # | Question | YES / NO |
|---|----------|----------|
| 1 | Is the estimate stale (>7 days without re-evaluation)? | |
| 2 | Is the position size <M$30? | |
| 3 | Is the edge <3pp? | |

**If all three are YES → SELL**, unless an override applies (see below).

**If any are NO → HOLD** and re-evaluate next cycle.

## Override: Hold Despite All-YES

Keep the position if ANY of the following are true:

- **Resolution imminent:** `days_to_close < 14`. Let it ride — transaction costs of selling exceed expected loss from a small mispricing this close to resolution.
- **Correlated with a larger position:** Selling would leave a larger position unhedged or reduce a deliberate portfolio correlation. Check if this position offsets risk elsewhere.
- **Information arriving soon:** A known event (earnings, ruling, data release) within 7 days that will sharply resolve uncertainty. Wait for the signal.

## Usage

Run this once per cycle on all positions flagged as low-edge in the briefing. Target: 30 seconds per position.

```
Position: [market name]
Edge: [X]pp  |  Size: M$[Y]  |  Last evaluated: [date]  |  Closes: [date]
Q1: [Y/N]  Q2: [Y/N]  Q3: [Y/N]
Override? [none / imminent / correlated / info-pending]
Decision: [SELL / HOLD]
```
