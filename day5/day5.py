#!/usr/bin/env python3

from typing import Iterable
import argparse
import fileinput

class Inventory:
    def __init__(self, ranges: list[range], ids: list[int]) -> None:
        self.ranges = sorted(ranges, key=lambda r: r.start)
        self.ids = ids

    def part1(self) -> list[int]:
        fresh = []
        for _id in self.ids:
            if any(_id in _range for _range in self.ranges):
                fresh.append(_id)
        return fresh

    def part2(self) -> int:
        disjoint: list[range] = []
        for cur in self.ranges:
            if (
                disjoint
                and (prev := disjoint[-1])
                and cur.start in prev
            ):
                disjoint[-1] = range(min(prev.start, cur.start), max(prev.stop, cur.stop))
            else:
                disjoint.append(cur)
        return sum(len(r) for r in disjoint)

    @staticmethod
    def from_strings(r: Iterable[str]) -> 'Inventory':
        ranges = []
        for line in r:
            if line.strip() == '':
                break
            start, stop = [int(x) for x in line.split('-')]
            ranges.append(range(start, stop + 1))

        ids = []
        for line in r:
            ids.append(int(line))

        return Inventory(ranges, ids)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', required=True, type=int, choices=[1, 2])
    ap.add_argument('file', nargs='?', default='-')
    args = ap.parse_args()

    with fileinput.input([args.file]) as r:
        inv = Inventory.from_strings(r)
        if args.part == 1:
            print(len(inv.part1()))
        else:
            print(inv.part2())
