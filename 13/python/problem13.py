"""
Advent of Code 2017 :: Day 13
Day 13: Packet Scanners
"""


def solve_a(scanners):
    """Solves first part of puzzle."""
    severity = 0
    for depth, scan_range in scanners.items():
        if depth == 0:
            continue
        period = (scan_range - 1) * 2
        if depth % period == 0:
            severity += depth * scan_range
    return severity


def is_safe_offset(offset, scanners):
    """Returns True if offset is safe."""
    severity = 0
    for depth, scan_range in scanners.items():
        period = (scan_range - 1) * 2
        if (depth + offset) % period == 0:
            return False
    return True


def solve_b(scanners):
    """Solves second part of puzzle."""
    offset = 1
    while True:
        if is_safe_offset(offset, scanners):
            return offset
        offset += 1


def main():
    """Main program."""
    import sys
    scanners = dict([map(int, line.strip().split(': ')) for line in sys.stdin])
    print('Solution to part A is', solve_a(scanners))
    print('Solution to part B is', solve_b(scanners))


if __name__ == '__main__':
    main()
