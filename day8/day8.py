#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Iterable, Literal
import argparse
import fileinput
import math

@dataclass(slots=True, frozen=True)
class Box:
    x: int
    y: int
    z: int

def dist(a: Box, b: Box) -> int:
    # To get the actual distance we'd take the square root, but since we're
    # just using the distance as a metric we don't need to.
    return (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2

def connect_boxes(lines: Iterable[str], part: Literal[1, 2]) -> int:
    boxes: list[Box] = []
    for line in lines:
        x, y, z = [int(n) for n in line.split(',')]
        boxes.append(Box(x, y, z))

    circuits: list[set[Box]] = []
    box_to_circuit: dict[Box, int] = {}

    dists: list[tuple[int, Box, Box]] = []
    for i, a in enumerate(boxes):
        for j in range(i + 1, len(boxes)):
            b = boxes[j]
            dists.append((dist(a, b), a, b))
    dists.sort()

    connections_to_make = 10 if len(boxes) < 100 else 1000
    nconnections = 0
    for _, a, b in dists:
        a_i = box_to_circuit.get(a)
        b_i = box_to_circuit.get(b)
        if a_i is None and b_i is not None:
            # Add loner to circuit
            circuits[b_i].add(a)
            if part == 2 and len(circuits[b_i]) == len(boxes):
                return a.x * b.x
            box_to_circuit[a] = b_i
        elif b_i is None and a_i is not None:
            # Add loner to circuit, the other way.
            circuits[a_i].add(b)
            if part == 2 and len(circuits[a_i]) == len(boxes):
                return a.x * b.x
            box_to_circuit[b] = a_i
        elif a_i is None and b_i is None:
            # Make new circuit
            new_i = len(circuits)
            circuits.append(set([a, b]))
            box_to_circuit[a] = new_i
            box_to_circuit[b] = new_i
        elif a_i == b_i:
            # Already connected
            pass
        elif a_i is not None and b_i is not None:
            # Merge circuits
            circuit_to_remove = circuits[b_i]
            for box in circuit_to_remove:
                box_to_circuit[box] = a_i
            circuits[a_i] |= circuit_to_remove
            circuit_to_remove.clear()
            if part == 2 and len(circuits[a_i]) == len(boxes):
                return a.x * b.x
        else:
            raise RuntimeError('unexpected case')

        nconnections += 1
        if part == 1 and nconnections >= connections_to_make:
            largest_circuit_sizes = sorted([len(c) for c in circuits if c], reverse=True)[:3]
            return math.prod(largest_circuit_sizes)

    raise RuntimeError('expected to hit an end condition')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--part', '-p', required=True, type=int, choices=[1, 2])
    ap.add_argument('file', nargs='?', default='-')
    args = ap.parse_args()

    with fileinput.input(args.file) as r:
        print(connect_boxes(r, args.part))
