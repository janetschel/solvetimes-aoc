# solvetimes-aoc
This tool calculates solve-times of a private leaderboard in AoC

## Why?
Private leaderboards at https://adventofcode.com sadly do not show the solve-times of each participant. You have to write an API (etc.) for that.

This is a small command line tool which calculates solve times based on the CET timezone.

The output will look like this, after you placed a `times.txt` in a in the same folder an ran `python3 times.py` in your terminal:

```
Times for 'Jan Etschel':
day 1 part 1 -> 0:24:45, at: 6:24:45
day 1 part 2 -> 0:26:13, at: 6:26:13 (diff to part 1: 0:01:28)
day 2 part 1 -> 0:29:14, at: 6:29:14
day 2 part 2 -> 0:36:35, at: 6:36:35 (diff to part 1: 0:07:21)
day 3 part 1 -> 0:14:00, at: 6:14:00
day 3 part 2 -> 0:16:51, at: 6:16:51 (diff to part 1: 0:02:51)
day 4 part 1 -> 0:05:43, at: 6:05:43
day 4 part 2 -> 1:09:45, at: 7:09:45 (diff to part 1: 1:04:02)
day 5 part 1 -> 0:32:20, at: 6:32:20
day 5 part 2 -> 0:56:26, at: 6:56:26 (diff to part 1: 0:24:06)
day 6 part 1 -> 0:08:39, at: 6:08:39
day 6 part 2 -> 0:16:36, at: 6:16:36 (diff to part 1: 0:07:57)
day 7 part 1 -> 2:20:22, at: 8:20:22
day 7 part 2 -> 2:29:29, at: 8:29:29 (diff to part 1: 0:09:07)
day 8 part 1 -> 0:10:15, at: 6:10:15
day 8 part 2 -> 0:26:30, at: 6:26:30 (diff to part 1: 0:16:15)
```
