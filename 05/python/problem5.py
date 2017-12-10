"""
Advent of Code 2017 :: Day 5
A Maze of Twisty Trampolines, All Alike
"""


def printInstructions(instructions, index):
    for idx, ist in enumerate(instructions):
        if idx == index:
            print("({})".format(ist), end= " ")
        else:
            print(ist, end=" ")
    print()


def solveA(instructions):
    """Solve first part of day 5 puzzle."""
    jumps = 0
    index = 0
    while index >= 0 and index < len(instructions):
        jump = instructions[index]
        instructions[index] += 1
        index += jump
        jumps += 1
    return jumps


def solveB(instructions):
    """Solve first part of day 5 puzzle."""
    jumps = 0
    index = 0
    while index >= 0 and index < len(instructions):
        jump = instructions[index]
        if jump >= 3:
            instructions[index] -= 1
        else:
            instructions[index] += 1

        index += jump
        jumps += 1
    return jumps


def main():
    """Main program."""
    import sys
    instructions = [int(i) for i in sys.stdin.readlines()]
    print('The solution to part A is', solveA(list(instructions)))
    print('The solution to part B is', solveB(list(instructions)))


if __name__ == '__main__':
    main()
