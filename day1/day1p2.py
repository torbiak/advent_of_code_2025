#!/usr/bin/env python3

import fileinput

zeros = 0
cur = 50
modulus = 100
with fileinput.input() as r:
    for line in r:
        dir = line[0]
        ticks = int(line[1:].strip())

        zeros += ticks // modulus
        ticks %= modulus
        if cur != 0 and (dir == 'L' and ticks >= cur or dir == 'R' and cur + ticks >= modulus):
            zeros += 1

        cur += ticks if dir == 'R' else -ticks
        cur %= modulus
print(zeros)
