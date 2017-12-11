"""
Advent of Code 2017 :: Day 11
Tests for Hex Ed
"""
import problem11 as p11

def test_solve_a():
    """Tests for first part of puzzle."""
    assert p11.solve_a('ne,ne,ne') == 3
    assert p11.solve_a('ne,ne,sw,sw') == 0
    assert p11.solve_a('ne,ne,s,s') == 2
    assert p11.solve_a('se,sw,se,sw,sw') == 3

def test_solve_b():
    """Tests for second part of puzzle."""
    assert p11.solve_b('ne,ne,ne') == 3
    assert p11.solve_b('ne,ne,sw,sw') == 2
    assert p11.solve_b('ne,ne,s,s') == 2
    assert p11.solve_b('se,sw,se,sw,sw') == 3
