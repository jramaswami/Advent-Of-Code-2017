"""
Advent of Code 2017 :: Day 10
Tests for Knot Hash
"""
import problem10 as p10

def test_reverse_slice():
    """Tests for reverse_slice"""
    A = [0, 1, 2, 3, 4]
    p10.reverse_slice(0, 3, A)
    assert A == [2, 1, 0, 3, 4]
    p10.reverse_slice(3, 7, A)
    assert A == [4, 3, 0, 1, 2]


def test_knot_hash():
    """Tests for knot_hash()"""
    A = [0, 1, 2, 3, 4]
    T = [3, 4, 1, 5]
    p10.knot_hash(T[:1], A)
    assert A == [2, 1, 0, 3, 4]
    A = [0, 1, 2, 3, 4]
    p10.knot_hash(T[:2], A)
    assert A == [4, 3, 0, 1, 2]
    A = [0, 1, 2, 3, 4]
    p10.knot_hash(T[:3], A)
    assert A == [4, 3, 0, 1, 2]
    A = [0, 1, 2, 3, 4]
    p10.knot_hash(T[:4], A)
    assert A == [3, 4, 2, 1, 0]
    A = [0, 1, 2, 3, 4]
    p10.knot_hash(T, A)
    assert A == [3, 4, 2, 1, 0]

def test_solution_A():
    """Test solution for part A."""
    assert p10.solve_a() == 38415


def test_input_to_lengths():
    """Tests input_to_lengths()"""
    assert p10.input_to_lengths('1,2,3') == [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]


def test_complete_knot_hash():
    """Tests for complete_knot_hash()"""
    assert p10.complete_knot_hash('') == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert p10.complete_knot_hash('AoC 2017') == '33efeb34ea91902bb2f59c9920caa6cd'
    assert p10.complete_knot_hash('1,2,3') == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert p10.complete_knot_hash('1,2,4') == '63960835bcdc130f0b66d7ff4f6a5a8e'
