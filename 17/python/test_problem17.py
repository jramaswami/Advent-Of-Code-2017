"""
Advent of Code 2017 :: Day 17
Spinlock
"""

import problem17 as p17


def test_spin():
    """Tests for spin()"""
    sbuffer = p17.CircularBuffer()
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 2 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 2 3 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 2 4 3 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 5 2 4 3 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 5 2 4 3 6 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 5 7 2 4 3 6 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 5 7 2 4 3 8 6 1.'
    sbuffer.spin(3)
    assert repr(sbuffer) == '0 9 5 7 2 4 3 8 6 1.'


def test_solve_a():
    """Test for solve_a()"""
    assert p17.solve_a(3) == 638


def test_solve_b():
    sbuffer = p17.CircularBuffer()
    for _ in range(2017):
        sbuffer.spin(3)
    assert p17.solve_b(3, 2017) == sbuffer.head.child.value
