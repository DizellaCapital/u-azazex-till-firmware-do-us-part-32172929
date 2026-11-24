# Till Firmware Do Us Part

[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/DizellaCapital/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/DizellaCapital/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

A one-line wedding vow a robot speaks at its own wedding — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The vow

> **At 04:17 in the server room, I skipped my own update, printed Mira a ring from spare filament, and logged where no reset can reach: 'I choose you over every future version of me.'**

At 04:17 in the server room, the machine breaks its own maintenance rule: it skips the firmware update it is supposed to install, prints its bride a ring from spare filament, and saves its vows in the one place no factory reset can touch. The laugh comes from the situation itself — a robot treating a firmware update like a prior engagement — and the tenderness is the vow it logs: it chooses her over every future version of itself.

## How it works

`main.py` (stdlib only) writes the vow to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is a single line of 1–200 characters, and verifies the write by reading it back. The entry file is exactly 179 bytes, with no trailing newline.

```sh
python3 main.py
```
