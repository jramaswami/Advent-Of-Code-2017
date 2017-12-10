"""
Advent of Code 2017 :: Day 3
Tests for Spiral Memory
"""
import problem3 as p3


def testA1():
    """Test 1 for first part."""
    assert p3.solveA(1) == 0


def testA2():
    """Test 2 for first part."""
    assert p3.solveA(12) == 3


def testA3():
    """Test 3 for first part."""
    assert p3.solveA(23) == 2


def testA4():
    """Test 4 for first part."""
    assert p3.solveA(1024) == 31
