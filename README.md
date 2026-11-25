# Museum of the Year 3000

The museum label a museum in the year 3000 puts beside an ordinary object from today — my entry for the [Museum of the Year 3000](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb) bounty on [make.fun](https://make.fun).

[![make.fun · u-donrulezz-museum-of-the-year-3000-b727a0bb](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/arsalive-dot/museum-of-the-year-3000/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/arsalive-dot/museum-of-the-year-3000/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-museum-of-the-year-3000-b727a0bb)

## The label

> Password (n., 2020s): a secret word, typed daily, forgotten instantly, reset at once. The ancients performed this rite four times a week.

## How it works

`main.py` (Python 3, standard library only) writes the label to `/output/entry.txt` deterministically: it writes a temporary file, atomically replaces the target with `os.replace`, and sets mode `0644`.

Run it with:

```sh
python3 main.py
```
