#!/usr/bin/env python3

import argparse
import fileinput
from typing import Iterable
import math
import re

def part1(lines: Iterable[str]) -> int:
    rows = []
    for line in r:
        rows.append(line.strip().split())
    ops = rows.pop()

    res = 0
    for i, op in enumerate(ops):
        if op == '+':
            res += sum(int(row[i]) for row in rows)
        elif op == '*':
            res += math.prod(int(row[i]) for row in rows)
    return res

def part2(lines: Iterable[str]) -> int:
    rows = []
    for line in r:
        rows.append(line.strip('\n'))
    ops = rows.pop()

    res = 0
    for match in re.finditer(r'[+*]\s+', ops):
        # Intentionally include the separator columns in the width so we don't
        # need a special case for the rightmost problem.
        width = len(match.group(0))
        op = match.group(0).strip()
        start = match.start(0)
        nums = [
             num
             for col in range(start, start + width)
             if (num := extract_num(rows, col)) is not None
         ]
        if op == '+':
            res += sum(nums)
        elif op == '*':
            res += math.prod(nums)
    return res

def extract_num(rows: list[str], col: int) -> int | None:
    digits = ''.join([row[col] for row in rows]).strip()
    if not digits:
        return None
    else:
        return int(digits)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', required=True, type=int, choices=[1, 2,])
    ap.add_argument('file', nargs='?', default='-')
    args = ap.parse_args()

    with fileinput.input(args.file) as r:
        if args.part == 1:
            print(part1(r))
        else:
            print(part2(r))
