"""
Advent of Code 2017 :: Day 25
The Halting Problem
"""
from collections import namedtuple, defaultdict

Branch = namedtuple('Branch', ['write', 'move', 'next_state'])


def parse_program(input_string):
    lines = input_string.strip().split('\n')
    begin_state = lines[0][-2]
    steps_start = lines[1].index('after') + 6
    steps_end = lines[1].index('steps') - 1
    steps = int(lines[1][steps_start:steps_end])
    branches = {}
    line_index = 3
    while line_index < len(lines):
        state = lines[line_index][-2:-1]
        zero_branch = parse_branch(lines, line_index + 1)
        one_branch = parse_branch(lines, line_index + 5)
        branches[state] = (zero_branch, one_branch)
        line_index += 10
    return begin_state, steps, branches


def parse_branch(lines, line_index):
    """Parse a branch"""
    write = int(lines[line_index+1][-2:-1])
    token = lines[line_index+2].split()[-1]
    if token.startswith('right'):
        move = 1
    elif token.startswith('left'):
        move = -1
    else:
        print('Error: sould be left or right: ', token)
    next_state = lines[line_index + 3][-2:-1]
    return Branch(write, move, next_state)


def run_program(start_state, steps, branches):
    tape = defaultdict(int)
    cursor = 0
    state = start_state
    for _ in range(steps):
        curr_val = tape[cursor]
        branch = branches[state][curr_val]
        tape[cursor] = branch.write
        cursor += branch.move
        state = branch.next_state
    return sum(tape.values())


def main():
    """Main program."""
    import sys
    input_string = sys.stdin.read()
    start_state, steps, branches = parse_program(input_string)
    checksum = run_program(start_state, steps, branches)
    print('The solution is', checksum)


if __name__ =='__main__':
    main()