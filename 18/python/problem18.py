"""
Advent of Code 2017 :: Day 18
Duet
"""

from collections import defaultdict, deque
import pyperclip


LOGGING = False


class DuetRunner():
    """Runs two machines at the same time."""
    def __init__(self):
        self.rcv_queue0 = deque()
        self.rcv_queue1 = deque()
        self.machine0 = DuetMachineB(0, self.rcv_queue0, self.rcv_queue1)
        self.machine1 = DuetMachineB(1, self.rcv_queue1, self.rcv_queue0)
    
    def load_program(self, program):
        """Load program into both machines."""
        self.machine0.load_program(program)
        self.machine1.load_program(program)

    def run(self):
        """Run both machines until that deadlock or halt."""
        while self.machine0.runnable() and self.machine1.runnable():
            self.machine0.run()
            self.machine1.run()
            self.machine0.unblock()
            self.machine1.unblock()


class BaseDuetMachine:
    """Represents the computer to run the duet program."""
    def __init__(self):
        self.instruction_ptr = 0
        self.instructions = []
        self.registers = defaultdict(int)
        self.halt = False

    def log(self, *msg):
        """Log msg to console."""
        if LOGGING:
            print(*msg)

    def load_program(self, program):
        """Load program from string."""
        self.instructions = [line.strip().split() for line in program.split('\n')]
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
        self.log(self.instruction_ptr, ':', tokens)
        func = getattr(self, tokens[0])
        if len(tokens) == 3:
            func(tokens[1], tokens[2])
        elif len(tokens) == 2:
            func(tokens[1])
        else:
            self.log("ERROR", tokens)
        if self.instruction_ptr < 0 or self.instruction_ptr >= len(self.instructions):
            self.halt = True

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

    def mul(self, reg, arg):
        """mul instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        self.log("mul({}={}, {}={})".format(reg, val1, arg, val2))
        self.registers[reg] = val1 * val2
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

class DuetMachineA(BaseDuetMachine):
    """Represents the computer for first part of puzzle."""

    def __init__(self):
        super(DuetMachineA, self).__init__()
        self.freq = 0
        self.prev_freq = 0
        self.first_rcv = 0

    def snd(self, arg):
        """snd instruction for machine a"""
        self.freq = self.get_value(arg)
        self.log("snd({}={})".format(arg, self.freq))
        self.instruction_ptr += 1

    def rcv(self, arg):
        """rcv instruction for machine a"""
        val = self.get_value(arg)
        self.log("rcv({}={})".format(arg, val))
        if val != 0:
            self.prev_freq = self.freq
            self.freq = 0
            if not self.first_rcv:
                self.log('first rcv')
                self.first_rcv = self.prev_freq
                self.halt = True
        self.instruction_ptr += 1


class DuetMachineB(BaseDuetMachine):
    """Represents computer for part B of puzzle."""
    def __init__(self, machine_id, rcv_q, snd_q):
        super(DuetMachineB, self).__init__()
        self.rcv_count = 0
        self.snd_count = 0
        self.deadlock = False
        self.blocking = False
        self.id = machine_id
        self.snd_q = snd_q
        self.rcv_q = rcv_q
        self.registers['p'] = machine_id

    def log(self, *msg):
        """Log message to console."""
        super(DuetMachineB, self).log(self.id, ":", *msg)

    def unblock(self):
        self.blocking = False

    def runnable(self):
        """Returns True if program is runnable."""
        return not self.blocking and not self.deadlock and super(DuetMachineB, self).runnable()

    def snd(self, arg):
        """snd instruction for machine b"""
        val = self.get_value(arg)
        self.log("snd({})".format(val))
        self.snd_count += 1
        self.snd_q.append(val)
        self.instruction_ptr += 1
    
    def rcv(self, reg):
        """rcv instruction for machine b"""
        if self.rcv_q:
            self.rcv_count = 0
            self.registers[reg] = self.rcv_q.popleft()
            self.log("rcv({}) {} ok".format(reg, self.registers[reg]))
            self.instruction_ptr += 1
        else:
            self.rcv_count = self.rcv_count + 1
            if self.rcv_count == 4:
                self.deadlock = True
                self.log("rcvB({}) DEADLOCK {}".format(reg, self.rcv_count))
            else:
                self.blocking = True
                self.log("rcvB({}) FAILED {}".format(reg, self.rcv_count))


def main():
    """Main program."""
    import sys
    program = sys.stdin.read()
    machine = DuetMachineA()
    machine.load_program(program)
    machine.run()
    print('Solution to part A is', machine.first_rcv)
    duet = DuetRunner()
    duet.load_program(program)
    duet.run()
    print('Solution to part B is', duet.machine1.snd_count)
    pyperclip.copy(str(duet.machine1.snd_count))


if __name__ == '__main__':
    main()