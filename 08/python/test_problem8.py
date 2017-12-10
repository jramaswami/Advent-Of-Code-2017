"""
Advent of Code :: Day 8
I Heard You Like Registers
"""
import problem8 as p8

def test_a():
    """Test for part 1 of puzzle."""
    test_input = "b inc 5 if a > 1\na inc 1 if b < 5\n" + \
                 "c dec -10 if a >= 1\nc inc -20 if c == 10"
    computer = p8.Computer()
    computer.load_program(test_input)
    computer.evaluate_program()
    assert computer.current_max_val() == 1

def test_b():
    """Test for part 2 of puzzle."""
    test_input = "b inc 5 if a > 1\na inc 1 if b < 5\n" + \
                 "c dec -10 if a >= 1\nc inc -20 if c == 10"
    computer = p8.Computer()
    computer.load_program(test_input)
    computer.evaluate_program()
    assert computer.during_max_val() == 10

