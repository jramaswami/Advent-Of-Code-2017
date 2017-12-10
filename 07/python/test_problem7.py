"""
Advent of Code :: Day 7
Recursive Circus
"""
import problem7 as p7

def testA1():
    """Test for part 1 of problem."""
    input_lines = ['pbga (66)', 'xhth (57)', 'ebii (61)', 'havc (66)',
                   'ktlj (57)', 'fwft (72) -> ktlj, cntj, xhth',
                   'qoyq (66)', 'padx (45) -> pbga, havc, qoyq',
                   'tknk (41) -> ugml, padx, fwft', 'jptl (61)',
                   'ugml (68) -> gyxo, ebii, jptl', 'gyxo (61)', 'cntj (57)']
    programs, parents = p7.parse_input(input_lines)
    assert p7.solveA(programs, parents) == 'tknk'

def test_different_index():
    """Tests for different_index()"""
    assert p7.different_index([1, 2, 2, 2]) == 0
    assert p7.different_index([2, 1, 2, 2]) == 1
    assert p7.different_index([2, 2, 1, 2]) == 2
    assert p7.different_index([2, 2, 2, 1]) == 3
