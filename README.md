# tiny-chess-01 entry — compact Python chess engine

A sub-4KB chess engine built for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01).

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

- main.py: 0x88 mailbox board, alpha-beta negamax + quiescence, iterative deepening under a deterministic node budget, HTTP client for the make.fun env protocol.
- Python 3 stdlib only. Run: MAKEFUN_ENV_URL=... python3 main.py
