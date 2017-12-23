"""
Advent of Code 2017 :: Day 23
Coprocessor Conflagration
"""
from math import sqrt
from collections import defaultdict


LOGGING = False


class Machine:
    """Represents the computer to run the program."""
    def __init__(self, registers=defaultdict(int)):
        self.instruction_ptr = 0
        self.instructions = []
        self.registers = registers
        self.instruction_ctr = defaultdict(int)
        self.halt = False

    def log(self, *msg):
        """Log msg to console."""
        if LOGGING:
            print(self.instruction_ptr, ':', *msg)

    def load_program(self, program):
        """Load program from string."""
        self.instructions = []
        for line in program.split('\n'):
            # remove comments
            instr = line.split(';')[0]
            self.instructions.append(instr.strip().split())
        self.instruction_ptr = 0

    def runnable(self):
        """Returns True if program is runnable."""
        return not self.halt

    def run(self):
        """Run program."""
        self.log('Running ...')
        while self.runnable():
            self.tick()

    def tick(self):
        """Complete on instruction."""
        if not self.runnable():
            return
        tokens = self.instructions[self.instruction_ptr]
        func = getattr(self, tokens[0])
        if len(tokens) == 3:
            func(tokens[1], tokens[2])
        elif len(tokens) == 2:
            func(tokens[1])
        elif len(tokens) == 1:
            func()
        else:
            self.log("ERROR", tokens)
        if self.instruction_ptr < 0 or self.instruction_ptr >= len(self.instructions):
            self.halt = True
        self.log([(k, v) for k, v in self.registers.items()])

    def get_value(self, arg):
        """Returns value of given argument"""
        sign = 1
        if arg[0] == '-': 
            sign = -1
            arg = arg[1:]
        if arg.isnumeric():
            return sign * int(arg)
        else:
            return self.registers[arg]

    def set(self, reg, arg):
        """set instruction"""
        val = self.get_value(arg)
        self.log("set({}, {}={})".format(reg, arg, val))
        self.registers[reg] = val
        self.instruction_ptr += 1
    
    def add(self, reg, arg):
        """add instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        self.log("add({}={}, {}={})".format(reg, val1, arg, val2))
        self.registers[reg] = val1 + val2
        self.instruction_ptr += 1

    def sub(self, reg, arg):
        """sub instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        self.log("sub({}={}, {}={})".format(reg, val1, arg, val2))
        self.registers[reg] = val1 - val2
        self.instruction_ptr += 1

    def mul(self, reg, arg):
        """mul instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        self.log("mul({}={}, {}={})".format(reg, val1, arg, val2))
        self.registers[reg] = val1 * val2
        self.instruction_ctr['mul'] +=1 
        self.instruction_ptr += 1

    def mod(self, reg, arg):
        """mod instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        self.log("mod({}={}, {}={})".format(reg, val1, arg, val2))
        self.registers[reg] = val1 % val2
        self.instruction_ptr += 1

    def jgz(self, arg1, arg2):
        """jgz instruction"""
        val1 = self.get_value(arg1)
        off = self.get_value(arg2)
        self.log("jgz({}={}, {}={})".format(arg1, val1, arg2, off))
        if val1 > 0:
            self.instruction_ptr += off
        else:
            self.instruction_ptr += 1

    def jnz(self, arg1, arg2):
        """jnz instruction"""
        val1 = self.get_value(arg1)
        off = self.get_value(arg2)
        self.log("jnz({}={}, {}={})".format(arg1, val1, arg2, off))
        if val1 != 0:
            self.instruction_ptr += off
        else:
            self.instruction_ptr += 1
    
    def stop(self):
        """halt instruction"""
        self.halt = True

    def nop(self):
        """pass"""
        self.instruction_ptr += 1 


def is_prime(b):
    """Returns 1 if not prime."""
    lim = int(sqrt(b)) + 1
    for d in range(2, b):
        if b % d:
            return 0
    return 1

def solve_b():
    b = (99 * 100) + 100000
    c = b + 17000
    h = 0
    step = 17
    for b0 in range(b, c+1,step):
        f = 1 # 9: set f 1
        for d in range(2, b0):
            if b0 % d == 0:
                f = 0
                break
        if f == 0:  # 25: jnz f 2
            h = h + 1  # 26: sub h -1
    return h


def main():
    """Main program."""
    import sys
    import pyperclip
    program = sys.stdin.read().strip()
    machine = Machine()
    machine.load_program(program)
    machine.run()
    print('The solution to part A is', machine.instruction_ctr['mul'])
    solution_b = solve_b()
    print('The solution to part B is', solution_b)
    pyperclip.copy(str(solution_b))


if __name__ == '__main__':
    main()