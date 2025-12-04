#!/usr/bin/env python3

import fileinput
from typing import Iterable

def current_or_next_double_number(n: int) -> int:
    n_str = str(n)
    halfway = len(n_str) // 2
    if len(n_str) % 2 == 1:
        a = 10**halfway
        b = a
    else:
        a = int(n_str[:halfway])
        b = int(n_str[halfway:])
    repeat = a if b <= a else a + 1
    return repeat * 10**(len(str(repeat))) + repeat

def find_double_numbers(start: int, stop: int) -> Iterable[int]:
    cur = start
    while True:
        cur = current_or_next_double_number(cur)
        if cur > stop:
            break
        yield cur
        cur += 1

def is_multi_number(n: int) -> bool:
    n_str = str(n)
    for stride in range(1, len(n_str) // 2 + 1):
        if len(n_str) % stride != 0:
            continue
        if all(n_str[i] == n_str[i - stride] for i in range(stride, len(n_str))):
            return True
    return False

def find_multi_numbers(start: int , stop: int) -> Iterable[int]:
    for i in range(start, stop + 1):
        if is_multi_number(i):
            yield i

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', choices=[1, 2], type=int, required=True)
    ap.add_argument('file', nargs='*', action='extend')
    args = ap.parse_args()

    _sum = 0
    with fileinput.input(args.file) as r:
        for line in r:
            for _range in line.strip().split(','):
                start, stop = [int(x) for x in _range.split('-')]
                if args.part == 1:
                    _sum += sum(find_double_numbers(start, stop))
                else:
                    _sum += sum(find_multi_numbers(start, stop))

    print(_sum)
