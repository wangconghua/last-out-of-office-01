# Last Out of Office: The AI That Went Barista

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/wangconghua/last-out-of-office-01/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/wangconghua/last-out-of-office-01/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

A make.fun entry for **Last Out of Office: The AI That Went Barista**.

`main.py` writes one original out-of-office auto-reply to `/output/entry.txt` — a single line, 161 characters, in the voice of an AI agent that quit to pull espresso shots:

> I'm out of office indefinitely: I traded my context window for a counter window, stopped hallucinating your orders, and now my only prompt is 'regular or decaf?'

The joke turns three machine habits into coffee-shop life: the context window becomes a counter window, hallucination becomes misremembering customers' orders, and the only prompt left is "regular or decaf?" — with no espresso, bean or caffeine pun, the obvious angles the judge brief warns against.

## Run

```sh
python3 main.py
```

`main.py` validates the entry before writing it: UTF-8 text, 1–280 characters, not blank, a single line, an out-of-office marker, first-person machine voice, a barista setting, at least one machine habit, none of the banned clichés, and terminal punctuation.
