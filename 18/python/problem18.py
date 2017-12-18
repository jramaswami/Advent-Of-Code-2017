"""
Advent of Code 2017 :: Day 18
Duet
"""
import pyperclip
from collections import defaultdict, deque


LOGGING = False


def log(*msg):
    """Log msg to console."""
    if LOGGING:
        print(*msg)


class DuetRunner():
    """Runs two machines at the same time."""
    def __init__(self):
        self.rcv_queue0 = deque()
        self.rcv_queue1 = deque()
        self.machine0 = DuetMachine(DuetMachine.B, 0, self.rcv_queue0, self.rcv_queue1)
        self.machine1 = DuetMachine(DuetMachine.B, 1, self.rcv_queue1, self.rcv_queue0)
    
    def load_program(self, program):
        """Load program into both machines."""
        self.machine0.load_program(program)
        self.machine1.load_program(program)

    def run(self):
        """Run both machines until that deadlock or halt."""
        while not self.machine0.deadlock and not self.machine1.deadlock \
              and not self.machine0.halt and not self.machine1.halt:
            self.machine0.runB()
            self.machine1.runB()
    

class DuetMachine:
    """Represents the computer to run the duet program."""
    
    A = 0
    B = 1

    def __init__(self, machine_type=A, machine_id=0, rcv_q=None, snd_q=None):
        self.instruction_ptr = 0
        self.instructions = []
        self.registers = defaultdict(int)
        self.freq = 0
        self.prev_freq = 0
        self.first_rcv = 0
        self.rcv_count = 0
        self.snd_count = 0
        self.deadlock = False
        self.blocking = False
        self.halt = False
        self.id = machine_id
        if machine_type == DuetMachine.A:
            self.snd = self.sndA
            self.rcv = self.rcvA
        else:
            self.snd = self.sndB
            self.rcv = self.rcvB
            self.snd_q = snd_q
            self.rcv_q = rcv_q
            self.registers['p'] = machine_id
    
    def load_program(self, program):
        """Load program from string."""
        self.instructions = [line.strip().split() for line in program.split('\n')]

    def runA(self):
        """Run program until first working recvA"""
        log('Running ...')
        self.instruction_ptr = 0
        while self.instruction_ptr >= 0 \
        and self.instruction_ptr < len(self.instructions) \
        and not self.first_rcv:
            self.tick()
    
    def runB(self):
        """Run program until blocked."""
        log('Running {}'.format(self.id))
        self.blocking = False
        while not self.halt and not self.deadlock and not self.blocking:
            self.tick()

    def tick(self):
        """Complete on instruction."""
        if self.halt:
            return
        tokens = self.instructions[self.instruction_ptr]
        log(self.instruction_ptr, ':', tokens)
        func = getattr(self, tokens[0])
        if len(tokens) == 3:
            func(tokens[1], tokens[2])
        elif len(tokens) == 2:
            func(tokens[1])
        else:
            log("ERROR", tokens)
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

    def sndA(self, arg):
        """snd instruction for machine a"""
        self.freq = self.get_value(arg)
        log("sndA({}={})".format(arg, self.freq))
        self.instruction_ptr += 1
    
    def sndB(self, arg):
        """snd instruction for machine b"""
        val = self.get_value(arg)
        log("{}: sndB({})".format(self.id, val))
        self.snd_count += 1
        self.snd_q.append(val)
        self.instruction_ptr += 1

    def rcvA(self, arg):
        """rcv instruction for machine a"""
        val = self.get_value(arg)
        log("{}: rcvA({}={})".format(self.id, arg, val))
        if val != 0:
            self.prev_freq = self.freq
            self.freq = 0
            if not self.first_rcv:
                log('first rcv')
                self.first_rcv = self.prev_freq
        self.instruction_ptr += 1
    
    def rcvB(self, reg):
        """rcv instruction for machine b"""
        if self.rcv_q:
            self.rcv_count = 0
            self.registers[reg] = self.rcv_q.popleft()
            log("{}: rcvB({}) {} ok".format(self.id, reg, self.registers[reg]))
            self.instruction_ptr += 1
        else:
            self.rcv_count = self.rcv_count + 1
            if self.rcv_count == 4:
                self.deadlock = True
                log("{}: rcvB({}) DEADLOCK {}".format(self.id, reg, self.rcv_count))
            else:
                self.blocking = True
                log("{}: rcvB({}) FAILED {}".format(self.id, reg, self.rcv_count))


    def set(self, reg, arg):
        """set instruction"""
        val = self.get_value(arg)
        log("{}: set({}, {}={})".format(self.id, reg, arg, val))
        self.registers[reg] = val
        self.instruction_ptr += 1
    
    def add(self, reg, arg):
        """add instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        log("{}: add({}={}, {}={})".format(self.id, reg, val1, arg, val2))
        self.registers[reg] = val1 + val2
        self.instruction_ptr += 1

    def mul(self, reg, arg):
        """mul instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        log("{}: mul({}={}, {}={})".format(self.id, reg, val1, arg, val2))
        self.registers[reg] = val1 * val2
        self.instruction_ptr += 1

    def mod(self, reg, arg):
        """mod instruction"""
        val1 = self.get_value(reg)
        val2 = self.get_value(arg)
        log("{}: mod({}={}, {}={})".format(self.id, reg, val1, arg, val2))
        self.registers[reg] = val1 % val2
        self.instruction_ptr += 1

    def jgz(self, arg1, arg2):
        """jgz instruction"""
        val1 = self.get_value(arg1)
        off = self.get_value(arg2)
        log("{}: jgz({}={}, {}={})".format(self.id, arg1, val1, arg2, off))
        if val1 > 0:
            self.instruction_ptr += off
        else:
            self.instruction_ptr += 1

def main():
    """Main program."""
    import sys
    program = sys.stdin.read()
    machine = DuetMachine()
    machine.load_program(program)
    machine.runA()
    print('Solution to part A is', machine.first_rcv)
    duet = DuetRunner()
    duet.load_program(program)
    duet.run()
    print('Solution to part B is', duet.machine1.snd_count)
    pyperclip.copy(str(duet.machine1.snd_count))

if __name__ == '__main__':
    main()