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

