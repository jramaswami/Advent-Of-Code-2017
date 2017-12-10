"""
Advent of Code 2017 :: Day 6
Memory Reallocation
"""
from collections import defaultdict
from operator import itemgetter


INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


def redistribute(memory, index):
    """Redistribute blocks from memory bank at given index."""
    val = memory[index]
    memory[index] = 0
    while val:
        index += 1
        if index >= len(memory):
            index = 0
        memory[index] += 1
        val -= 1
    return memory


def solveA(memory):
    """Solve first part of problem."""
    states = defaultdict(bool)
    states[tuple(memory)] = True
    count = 0
    while True:
        # find max and index
        max_i, _ = max(enumerate(memory), key=itemgetter(1))
        # redistribute
        memory = redistribute(memory, max_i)
        count += 1
        memory_state = tuple(memory)
        if memory_state in states:
            return count
        states[memory_state] = True


def solveB(memory):
    """Solve second part of problem."""
    states = defaultdict(int)
    count = 0
    states[tuple(memory)] = count
    while True:
        # find max and index
        max_i, _ = max(enumerate(memory), key=itemgetter(1))
        # redistribute
        memory = redistribute(memory, max_i)
        count += 1
        memory_state = tuple(memory)
        if memory_state in states:
            return count - states[memory_state]
        states[memory_state] = count


def main():
    """Main program."""
    print('The solution to part A is', solveA(INPUT))
    print('The solution to part B is', solveB(INPUT))


if __name__ == '__main__':
    main()
