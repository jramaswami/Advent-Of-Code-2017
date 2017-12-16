"""
Advent of Code 2017 :: Day 16
Permutation Promenade
"""
import problem16 as p16


def test_make_dance_line():
    """Test for make_dance_line()"""
    assert p16.make_dance_line(5) == ['a', 'b', 'c', 'd', 'e']

def test_spin():
    """Test for spin()"""
    dancers = p16.make_dance_line(5)
    assert p16.spin(dancers, 3) == ['c', 'd', 'e', 'a', 'b']

def test_exchange():
    """Test for exchange()"""
    dancers = p16.make_dance_line(5)
    assert p16.exchange(dancers, 2, 4) == ['a', 'b', 'e', 'd', 'c']

def test_partner():
    """Test for partner()"""
    dancers = p16.make_dance_line(5)
    assert p16.partner(dancers, 'e', 'c') == ['a', 'b', 'e', 'd', 'c']


def test_split_on_slash():
    """Test for split_on_slash()"""
    assert p16.split_on_slash('x15/12') == ('15', '12')
    assert p16.split_on_slash('pm/d') == ('m', 'd')

def test_solve_a():
    """Test for solve_a()"""
    instructions = 's1,x3/4,pe/b'
    dancers = p16.solve_a(instructions, 5)
    assert dancers == 'baedc'