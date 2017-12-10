"""
Advent of Code 2017 :: Day 10
Knot Hash
"""
from operator import xor
from functools import reduce

INPUT = "189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62"


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


def knot_hash(twist_lengths, string_circle, curr_pos=0, skip_size=0):
    """Returns knot hash."""
    for twist_length in twist_lengths:
        reverse_slice(curr_pos, curr_pos+twist_length, string_circle)
        curr_pos = (curr_pos + twist_length + skip_size) % len(string_circle)
        skip_size += 1
    return curr_pos, skip_size


def solve_a():
    """Solves first part of puzzle."""
    A = list(range(256))
    T = [int(i) for i in INPUT.split(',')]
    knot_hash(T, A)
    return A[0] * A[1]


def input_to_lengths(input_string):
    """Converts input string to lengths."""
    T = [ord(c) for c in input_string]
    T.extend([17, 31, 73, 47, 23])
    return T

def knot_hash_loop(twist_lengths, string_circle):
    """Knot hash 64 times."""
    curr_pos = skip_size = 0
    for _ in range(64):
        curr_pos, skip_size = knot_hash(twist_lengths, string_circle, curr_pos, skip_size)


def condense_hash(string_circle):
    """Condenses into a dense hash."""
    return [reduce(xor, string_circle[start:start+16]) for start in range(0, 256, 16)]


def hash_to_string(string_circle):
    """Convert hash to a string."""
    return "".join([format(i, '02x') for i in string_circle])


def complete_knot_hash(input_string):
    """Returns completed knot hash."""
    twist_lengths = input_to_lengths(input_string)
    string_circle = list(range(256))
    knot_hash_loop(twist_lengths, string_circle)
    dense_hash = condense_hash(string_circle)
    return hash_to_string(dense_hash)


def solve_b():
    """Solves second part of puzzle."""
    return complete_knot_hash(INPUT)


def main():
    """Main program."""
    print('The solution to part A is', solve_a())
    print('The solution to part B is', solve_b())


if __name__ == '__main__':
    main()
