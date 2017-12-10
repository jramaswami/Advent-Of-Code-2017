"""
Advent of Code 2017 :: Day 1 :: Tests
"""
import problem1 as p1

def test_A1():
    """Test against 1122"""
    assert p1.solveA("1122") == 3

def test_A2():
    """Test against 1111"""
    assert p1.solveA("1111") == 4

def test_A3():
    """Test against 1234"""
    assert p1.solveA("1234") == 0

def test_A4():
    """Test against 91212129"""
    assert p1.solveA("91212129") == 9

def test_B1():
    """Test against 1212"""
    assert p1.solveB("1212") == 6

def test_B2():
    """Test against 1221"""
    assert p1.solveB("1221") == 0

def test_B3():
    """Test against 123425"""
    assert p1.solveB("123425") == 4

def test_B4():
    """Test against 123123"""
    assert p1.solveB("123123") == 12

def test_B5():
    """Test against 12131415"""
    assert p1.solveB("12131415") == 4
