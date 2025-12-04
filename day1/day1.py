#!/usr/bin/env python3

import fileinput

zeros = 0
cur = 50
with fileinput.input() as r:
    for line in r:
        dir = line[0]
        ticks = int(line[1:].strip())
        if dir == 'L':
            cur -= ticks
        elif dir == 'R':
            cur += ticks
        cur %= 100
        if cur == 0:
            zeros += 1
print(zeros)
