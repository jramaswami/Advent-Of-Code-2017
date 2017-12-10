"""
Advent of Code :: Day 4
High-Entropy Passphrases
"""

from itertools import product, combinations


def validB(passphrase):
    """
    Returns true if password is valid
    as per part A of the puzzle i.e.
    i.e. there are no tokens that are
    anagrams of each other.
    """
    tokens = [sorted(t) for t in passphrase.split()]
    for lhs, rhs in combinations(tokens, 2):
        if lhs == rhs:
            return False
    return True

def validA(passphrase):
    """
    Returns true if password is valid
    as per part A of the puzzle i.e.
    there are no duplicate tokens.
    """
    tokens = passphrase.split()
    for lhs, rhs in combinations(tokens, 2):
        if lhs == rhs:
            return False
    return True


def solveA(passphrases):
    """
    Solution to part A of puzzle.
    """
    return sum([validA(p) for p in passphrases])


def solveB(passphrases):
    """
    Solution to part B of puzzle.
    """
    return sum([validB(p) for p in passphrases])


def main():
    """
    Main program.
    """
    import sys
    passphrases = sys.stdin.readlines()
    print('The solution to Part A is:', solveA(passphrases))
    print('The solution to Part B is:', solveB(passphrases))


if __name__ == '__main__':
    main()

