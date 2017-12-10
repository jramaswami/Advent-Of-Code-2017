"""
Advent of Code :: Day 8
I Heard You Like Registers
"""
from collections import namedtuple, defaultdict
import operator

Instruction = namedtuple('Instruction', ['incr_reg', 'incr_op',
                                         'incr_val', 'pred_reg',
                                         'pred_op', 'pred_val'])



class Computer:
    def __init__(self):
        self.registers = defaultdict(int)
        self.operations = {'<': operator.lt, '>': operator.gt,
                           '<=': operator.le, '>=': operator.ge,
                           '==': operator.eq, '!=': operator.ne,
                           'inc': operator.add, 'dec': operator.sub}
        self.instructions = []
        self.max_val_during = 0

    def translate_operator(self, op_string):
        """Translates operator string into an operator."""
        return self.operations[op_string]


    def load_program(self, input_string):
        """
        Parses input into tokens and puts them into an instruction
        tuple.  For example:
                b inc 5 if a > 1
        is tranlated into
                ('b', operator.add, 5, 'a', operator.gt, 1)
        """
        self.instructions = []
        for line in input_string.split("\n"):
            tokens = line.split()
            self.instructions.append(Instruction(tokens[0],
                                                 self.translate_operator(tokens[1]),
                                                 int(tokens[2]), tokens[4],
                                                 self.translate_operator(tokens[5]),
                                                 int(tokens[6])))


    def evaluate_program(self):
        """Evaluates program."""
        for instruction in self.instructions:
            self._eval(instruction)

    def _eval(self, instruction):
        """Evaluate instruction."""
        pred_reg_val = self.registers[instruction.pred_reg]
        if instruction.pred_op(pred_reg_val, instruction.pred_val):
            inc_reg_val = self.registers[instruction.incr_reg]
            new_reg_val = instruction.incr_op(inc_reg_val, instruction.incr_val)
            self.registers[instruction.incr_reg] = new_reg_val
            self.max_val_during = max(self.max_val_during, new_reg_val)

    def current_max_val(self):
        """Returns maximum value in registers."""
        return max(self.registers.values())

    def during_max_val(self):
        """Returns maximum value in registers at any point of program run."""
        return self.max_val_during


def main():
    """Main program."""
    import sys
    input_string = sys.stdin.read().strip()
    computer = Computer()
    computer.load_program(input_string)
    computer.evaluate_program()
    print('The solution to part A is', computer.current_max_val())
    print('The solution to part A is', computer.during_max_val())


if __name__ == '__main__':
    main()
