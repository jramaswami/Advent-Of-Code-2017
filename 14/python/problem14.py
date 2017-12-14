"""
Advent of Code 2017 :: Day 14
Disk Defragmentation
"""
from operator import xor
from functools import reduce
from collections import deque


INPUT = 'amgozmfv'

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


def complete_knot_hash(input_string):
    """Returns completed knot hash."""
    twist_lengths = input_to_lengths(input_string)
    string_circle = list(range(256))
    knot_hash_loop(twist_lengths, string_circle)
    dense_hash = condense_hash(string_circle)
    return dense_hash


def solve_a(input_string):
    return sum((sum('{0:b}'.format(h).count('1')
                    for h in complete_knot_hash(input_string + '-' + str(i))) 
                for i in range(128)))
                

def get_neighbors_4(row, col):
    "Gets the neighbors of given cell: right, left, down, up."
    if col + 1 < 128:
        yield (row, col + 1)
    if col - 1 >= 0:
        yield (row, col - 1)
    if row + 1 < 128:
        yield (row + 1, col)
    if row - 1 >= 0:
        yield (row - 1, col)


def solve_b(input_string):
    memory = [''.join(format(h, '08b') 
                      for h in complete_knot_hash(input_string + '-' + str(i))) 
              for i in range(128)]
    visited = [[False for _ in range(128)] for _ in range(128)]
    region_count = 0
    for row in range(128):
        for col in range(128):
            if memory[row][col] == '0' or visited[row][col]:
                continue
            region_count += 1
            queue = deque()
            queue.append((row, col))
            while queue:
                row_u, col_u = queue.popleft()
                for row_v, col_v in get_neighbors_4(row_u, col_u):
                    if memory[row_v][col_v] == '1' and not visited[row_v][col_v]:
                        visited[row_v][col_v] = True
                        queue.append((row_v, col_v))
    return region_count
    

def main():
    """Main program."""
    print('Solution to part A is', solve_a(INPUT))
    print('Solution to part A is', solve_b(INPUT))


if __name__ == '__main__':
    main()
