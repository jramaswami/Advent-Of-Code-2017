"""
Advent of Code 2017 :: Day 15
Dueling Generators
"""

import problem15 as p15


def test_generator():
    """Tests generator()"""
    expected_a = [1092455, 1181022009, 245556042, 1744312007, 1352636452]
    actual_a = list(p15.generator(p15.FACTOR_A, 65, 5))
    assert  actual_a == expected_a
    expected_b = [430625591, 1233683848, 1431495498, 137874439, 285222916]
    actual_b = list(p15.generator(p15.FACTOR_B, 8921, 5))
    assert  actual_b == expected_b

def test_solve_a():
    """Tests solve_a()"""
    # assert p15.solve_a(65, 8921) == 588
    assert p15.solve_a0(65, 8921) == 588

def test_solve_b():
    """Tests solve_a()"""
    assert p15.solve_b0(65, 8921) == 309