#!/usr/bin/env python3

import argparse
from typing import cast, Literal, Iterable

class Grid:
    def __init__(self, grid: str) -> None:
        self.grid = bytearray(grid.encode())
        self.width = grid.index('\n')
        self.height = grid.count('\n')

    def get(self, x: int, y: int) -> Literal['.', '@']:
        # Add 1 to skip over newlines.
        i = (self.width + 1) * y + x
        return cast(Literal['.', '@'], chr(self.grid[i]))

    def remove(self, x: int, y: int) -> None:
        i = (self.width + 1) * y + x
        self.grid[i] = ord('.')

    def find_friends(self, x: int, y: int) -> Iterable[tuple[int, int]]:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                fx, fy = x + dx, y + dy
                if fx < 0 or fy < 0 or fx >= self.width or fy >= self.height:
                    continue
                if self.get(fx, fy) == '@':
                    yield (x, y)

    def count_friends(self, x: int, y: int) -> int:
        return sum(1 for _ in  self.find_friends(x, y))

    def count_movable(self) -> int:
        nmovable = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.get(x, y) != '@':
                    #print('.', end='')
                    continue
                if self.count_friends(x, y) < 4:
                    #print('x', end='')
                    nmovable += 1
                else:
                    pass
                    #print('@', end='')
            #print('')
        return nmovable

    def count_removable(self) -> int:
        nremoved = 0
        while True:
            loop_removed = 0
            for y in range(self.height):
                for x in range(self.width):
                    loop_removed += self.remove_friends(x, y)
            if loop_removed == 0:
                break
            nremoved += loop_removed
        return nremoved

    def remove_friends(self, x: int, y: int) -> int:
        nremoved = 0
        if self.get(x, y) != '@' or self.count_friends(x, y) >= 4:
            return nremoved

        self.remove(x, y)
        nremoved += 1
        for fx, fy in self.find_friends(x, y):
            nremoved += self.remove_friends(fx, fy)
        return nremoved

    @staticmethod
    def from_file(filename: str) -> 'Grid':
        with open(filename) as r:
            return Grid(r.read())

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', required=True, choices=[1, 2], type=int)
    ap.add_argument('file')
    args = ap.parse_args()

    grid = Grid.from_file(args.file)

    if args.part == 1:
        print(grid.count_movable())
    else:
        print(grid.count_removable())
