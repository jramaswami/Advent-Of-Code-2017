"""
Advent of Code 2017 :: Day 12
Tests for Digital Plumber
"""
import problem12 as p12

TEST_INPUT = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

def test_a():
    """Test for first part of puzzle."""
    graph = p12.read_graph(TEST_INPUT)
    assert p12.component_count(0, graph) == 6

def test_b():
    """Test for second part of puzzle."""
    graph = p12.read_graph(TEST_INPUT)
    assert p12.count_components(graph) == 2

