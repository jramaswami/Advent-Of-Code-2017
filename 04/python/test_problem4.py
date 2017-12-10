"""
Advent of Code :: Day 4
Tests for High-Entropy Passphrases
"""
import problem4 as p4


def testA1():
    """Test 1 for part A."""
    assert p4.validA('aa bb cc dd ee')

def testA2():
    """Test 2 for part A."""
    assert not p4.validA('aa bb cc dd aa')

def testA3():
    """Test 3 for part A."""
    assert p4.validA('aa bb cc dd aaa')

def testB1():
    """Test 1 for part B."""
    assert p4.validB('abcde fghij')

def testB2():
    """Test 2 for part B."""
    assert not p4.validB('abcde xyz ecdab')

def testB3():
    """Test 3 for part B."""
    assert p4.validB('a ab abc abd abf abj')

def testB4():
    """Test 4 for part B."""
    assert p4.validB('iiii oiii ooii oooi oooo')

def testB5():
    """Test 4 for part B."""
    assert not p4.validB('oiii ioii iioi iiio')
