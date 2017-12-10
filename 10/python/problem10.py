"""
Advent of Code 2017 :: Day 10
Knot Hash
"""

INPUT = [189, 1, 111, 246, 254, 2, 0, 120, 215, 93, 255, 50, 84, 15, 94, 62]


def reverse_slice(slice_start, slice_end, string_circle):
    """Reverses a slice of the string_circle."""
    if slice_end >= len(string_circle):
        slice_end = slice_end % len(string_circle)
        slice_val = string_circle[slice_start:] + string_circle[0:slice_end]
        slice_val_rev = slice_val[::-1]
        delta = len(string_circle) - slice_start
        string_circle[slice_start:] = slice_val_rev[:delta]
        string_circle[:slice_end] = slice_val_rev[delta:]
    else:
        slice_val = string_circle[slice_start:slice_end]
        string_circle[slice_start:slice_end] = slice_val[::-1]


def knot_hash(twist_lengths, string_circle):
    """Returns knot hash."""
    skip_size = 0
    curr_pos = 0
    for twist_length in twist_lengths:
        reverse_slice(curr_pos, curr_pos+twist_length, string_circle)
        curr_pos = (curr_pos + twist_length + skip_size) % len(string_circle)
        skip_size += 1


def solve_a():
    """Solves first part of puzzle."""
    A = list(range(256))
    knot_hash(INPUT, A)
    return A[0] * A[1]


def main():
    """Main program."""
    print('The solution to part A is', solve_a())


if __name__ == '__main__':
    main()
