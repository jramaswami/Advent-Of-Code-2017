"""
Advent of Code 2017 :: Day 5
Tests for A Maze of Twisty Trampolines, All Alike
"""

import problem5 as p5

def testA1():
    """Test 1 for first part of puzzle."""
    assert p5.solveA([0, 3, 0, 1, -3]) == 5

def testB1():
    """Test 1 for second part of puzzle."""
    assert p5.solveB([0, 3, 0, 1, -3]) == 10

