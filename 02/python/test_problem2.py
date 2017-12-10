"""
Advent of Code 2017 :: Day 2
Tests for Corruption Checksum
"""
import problem2 as p2

def testA1():
    """Test 1 for Part A."""
    spreadsheet = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
    assert p2.solveA(spreadsheet) == 18

def testB1():
    """Test 1 for Part B."""
    spreadsheet = [[5,9,2,8],[9,4,7,3],[3,8,6,5]]
    assert p2.solveB(spreadsheet) == 9
