"""
Advent of Code 2017 :: Day 13
Tests for Day 13: Packet Scanners
"""
import problem13 as p13

def test_solve_a():
    """Tests for first part of puzzle."""
    scanners = {0: 3, 1: 2, 4: 4, 6: 4}
    assert p13.solve_a(scanners) == 24

def test_solve_b():
    """Tests for second part of puzzle."""
    scanners = {0: 3, 1: 2, 4: 4, 6: 4}
    assert p13.solve_b(scanners) == 10
