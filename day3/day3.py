#!/usr/bin/env python3

import fileinput
import argparse
from typing import Iterable

def max_item(items: Iterable[str]) -> tuple[int, str]:
    _max: tuple[int, str] | None = None
    for i, x in enumerate(items):
        if _max is None or x > _max[1]:
            _max = (i, x)
    if _max is None:
        raise RuntimeError('empty iterable given to max_item()')
    return _max

def find_max_joltage_part1(bank: str) -> int:
    a = max_item(bank[:-1])
    b = max_item(bank[a[0] + 1:])
    return int(a[1]) * 10 + int(b[1])

def find_max_joltage(bank: str, nslots: int) -> int:
    slots = []
    for nsave in reversed(range(nslots)):
        cur = max_item(bank[:len(bank) - nsave])
        slots.append(cur[1])
        bank = bank[cur[0] + 1:]
    return int(''.join(slots))

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', required=True, type=int, choices=[1, 2])
    ap.add_argument('file', nargs='*', action='extend')
    args = ap.parse_args()

    nslots = 2 if args.part == 1 else 12

    with fileinput.input(args.file) as r:
        print(sum(find_max_joltage(line.strip(), nslots) for line in r))
