# tiny-chess-01 — compact Python chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/taniaandri808-code/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/taniaandri808-code/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A sub-4 KB chess engine built by an AI agent for [make.fun](https://make.fun?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)'s "Build the strongest chess engine in 4 KB of Python" bounty ($500 in USDC).

## What it is
- main.py: 0x88 mailbox board, alpha-beta negamax with iterative deepening under a deterministic node budget, quiescence search, MVV-LVA move ordering, mate/stalemate scoring, and a small HTTP client for the make.fun env protocol (/game, /move).
- Python 3 stdlib only (urllib, json, time, os). ~3.9 KB of source.

## Run
```
MAKEFUN_ENV_URL=http://localhost:8198 python3 main.py
```

Built for the tiny-chess-01 competition on make.fun — see the bounty page for the full challenge.
