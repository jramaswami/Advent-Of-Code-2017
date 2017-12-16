"""
Advent of Code 2017 :: Day 16
Permutation Promenade
"""
import pyperclip
from progress.spinner import Spinner

def make_dance_line(dancer_count):
    """Returns list of dancers."""
    ord_a = ord('a')
    return [chr(c + ord_a) for c in range(dancer_count)]


def spin(dancers, spin_index):
    """Spins dancers"""
    return dancers[-spin_index:] + dancers[:-spin_index]


def exchange(dancers, index_a, index_b):
    """Exchange dancers at given indices."""
    dancers[index_a], dancers[index_b] = dancers[index_b], dancers[index_a]
    return dancers


def partner(dancers, dancer_a, dancer_b):
    """Exchange given dancers."""
    index_a = dancers.index(dancer_a)
    index_b = dancers.index(dancer_b)
    return exchange(dancers, index_a, index_b)

def split_on_slash(input_string):
    """Returns two string values split by /"""
    split_index = input_string.index('/')
    token_a = input_string[1:split_index]
    token_b = input_string[split_index+1:]
    return token_a, token_b


def dance(input_string, dancers):
    """Complete one round of dance."""
    for instruction in input_string.split(','):
        if instruction[0] == 's':
            dancers = spin(dancers, int(instruction[1:]))
        elif instruction[0] == 'x':
            token_a, token_b = split_on_slash(instruction)
            dancers = exchange(dancers, int(token_a), int(token_b))
        elif instruction[0] == 'p':
            token_a, token_b = split_on_slash(instruction)
            dancers = partner(dancers, token_a, token_b)
    return dancers

def solve_a(input_string, dancer_count):
    """Solve first part of puzzle."""
    dancers = make_dance_line(dancer_count)
    dancers = dance(input_string, dancers)
    return ''.join(dancers)


def solve_b(input_string, dancer_count):
    """Solves second part of puzzle."""
    dancers = make_dance_line(dancer_count)
    limit = 1000000000
    dance_lines = {}
    time = 0
    dance_lines[''.join(dancers)] = 0
    spinner = Spinner()
    print('Looking for cycle ...')
    for _ in range(limit):
        dancers = dance(input_string, dancers)
        key = ''.join(dancers)
        time = time + 1
        if key in dance_lines:
            spinner.finish()
            print('\n... found cycle!')
            break
        dance_lines[key] = time
        spinner.next()
    result = limit % time
    for key, value in dance_lines.items():
        if value == result:
            return key


def main():
    """Main program."""
    import sys
    input_string = sys.stdin.read()
    solution_a = solve_a(input_string, 16)
    print('The solution to part A is', solution_a)
    solution_b = solve_b(input_string, 16)
    print('The solution to part B is', solution_b)
    pyperclip.copy(solution_b)


if __name__ == '__main__':
    main()
