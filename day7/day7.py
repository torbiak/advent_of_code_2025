#!/usr/bin/env python3

import fileinput
import argparse
from typing import Iterable
from collections import defaultdict

def part1(manifold: Iterable[str]) -> int:
    beams: set[int] = set()
    nsplits = 0
    for line in manifold:
        if not beams:
            beams.add(line.index('S'))
            continue
        next_beams: set[int] = set()
        for beam in beams:
            if line[beam] == '^':
                nsplits += 1
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)
            else:
                next_beams.add(beam)
        beams = next_beams
    return nsplits

def part2(manifold: Iterable[str]) -> int:
    particles_at: dict[int, int] = defaultdict(int)
    for line in manifold:
        if not particles_at:
            particles_at[line.index('S')] = 1
            continue
        next_particles: dict[int, int] = defaultdict(int)
        for i, count in particles_at.items():
            if line[i] == '^':
                next_particles[i-1] += count
                next_particles[i+1] += count
            else:
                next_particles[i] += count
        particles_at = next_particles
    return sum(particles_at.values())

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', required=True, choices=[1, 2], type=int)
    ap.add_argument('file', nargs='?', default='-')
    args = ap.parse_args()

    with fileinput.input(args.file) as r:
        if args.part == 1:
            print(part1(r))
        else:
            print(part2(r))
