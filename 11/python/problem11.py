"""
Advent of Code 2017 :: Day 11
Hex Ed
"""
from collections import namedtuple
from functools import reduce
from operator import add
from itertools import accumulate

HexCoordinate = namedtuple('HexCoordinate', ['x', 'y', 'z'])
HexCoordinate.__add__ = lambda s, o: HexCoordinate(s.x + o.x, s.y + o.y, s.z + o.z)


DIRECTIONS = {'n': HexCoordinate(1, -1, 0), 's': HexCoordinate(-1, 1, 0),
              'nw': HexCoordinate(0, -1, 1), 'sw': HexCoordinate(-1, 0, 1),
              'ne': HexCoordinate(1, 0, -1), 'se': HexCoordinate(0, 1, -1)}


def solve_a(input_string):
    """Solves first part of puzzle."""
    new_pos = reduce(add, (DIRECTIONS[s] for s in input_string.split(',')),
                     HexCoordinate(0, 0, 0))
    return max([abs(i) for i in [new_pos.x, new_pos.y, new_pos.z]])


def solve_b(input_string):
    """Solves second part of puzzle."""
    lst = [HexCoordinate(0, 0, 0)]
    lst.extend((DIRECTIONS[s] for s in input_string.split(',')))
    coords = accumulate(lst)
    dists = (max(abs(i) for i in (p.x, p.y, p.z)) for p in coords)
    return max(dists)


def main():
    """Main program."""
    import sys
    input_string = sys.stdin.read()
    print('The solution to part A is', solve_a(input_string.strip()))
    print('The solution to part B is', solve_b(input_string.strip()))


if __name__ == '__main__':
    main()
