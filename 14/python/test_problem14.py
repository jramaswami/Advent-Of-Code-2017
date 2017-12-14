"""
Advent of Code 2017 :: Day 14
Tests for Disk Defragmentation
"""
import problem14 as p14

def test_solve_a():
    """Tests for first part of puzzle."""
    assert p14.solve_a('flqrgnkx') == 8108

def test_solve_b():
    """Tests for second part of puzzle."""
    assert p14.solve_b('flqrgnkx') == 1242