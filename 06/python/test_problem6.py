"""
Advent of Code 2017 :: Day 6
Tests for Memory Reallocation
"""
import problem6 as p6


def testA1():
    """Test for first part of puzzle."""
    assert p6.solveA([0, 2, 7, 0]) == 5


def testB1():
    """Test for second part of puzzle."""
    assert p6.solveB([0, 2, 7, 0]) == 4
