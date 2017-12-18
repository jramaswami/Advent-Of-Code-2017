"""
Advent of Code 2017 :: Day 18
Tests for Duet
"""
import problem18 as p18

TEST_PROGRAM_A = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

TEST_PROGRAM_B="""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""


def test_machine_set():
    """Tests Duet Machine set()"""
    machine = p18.DuetMachine()
    machine.set('a', '1')
    assert machine.registers['a'] == 1
    assert machine.instruction_ptr == 1
    machine.set('b', '-2')
    assert machine.registers['b'] == -2
    assert machine.instruction_ptr == 2

def test_machine_sndA():
    """Tests Duet Machine sndA()"""
    machine = p18.DuetMachine()
    machine.set('a', '1')
    machine.sndA('a')
    assert machine.freq == 1
    assert machine.instruction_ptr == 2

def test_machine_rcvA():
    """Tests Duet Machine sndA()"""
    machine = p18.DuetMachine()
    machine.set('a', '1')
    machine.sndA('a')
    machine.rcv('b')
    assert machine.freq == 1
    assert machine.instruction_ptr == 3
    machine.set('b', '4')
    machine.rcv('b')
    assert machine.prev_freq == 1
    assert machine.freq == 0
    assert machine.instruction_ptr == 5
    machine.sndA('b')
    machine.rcv('0')
    assert machine.prev_freq == 1
    assert machine.freq == 4
    assert machine.instruction_ptr == 7
    machine.rcv('7')
    assert machine.prev_freq == 4
    assert machine.freq == 0
    assert machine.instruction_ptr == 8

def test_machine_add():
    """Test DuetMachine add()"""
    machine = p18.DuetMachine()
    machine.set('a', '1')
    machine.add('a', '2')
    assert machine.registers['a'] == 3
    assert machine.instruction_ptr == 2
    machine.add('a', 'a')
    assert machine.registers['a'] == 6
    assert machine.instruction_ptr == 3

def test_machine_mul():
    """Test DuetMachine mul()"""
    machine = p18.DuetMachine()
    machine.set('b', '2')
    machine.mul('b', '2')
    assert machine.registers['b'] == 4
    assert machine.instruction_ptr == 2
    machine.set('c', '5')
    machine.mul('b', 'c')
    assert machine.registers['b'] == 20
    assert machine.instruction_ptr == 4

def test_machine_mod():
    """Test DuetMachine mod()"""
    machine = p18.DuetMachine()
    machine.set('b', '5')
    machine.mod('b', '2')
    assert machine.registers['b'] == 1
    assert machine.instruction_ptr == 2
    machine.set('b', '8')
    machine.set('c', '5')
    machine.mod('b', 'c')
    assert machine.registers['b'] == 3
    assert machine.instruction_ptr == 5

def test_machine_jgz():
    """Test DuetMachine jgz()"""
    machine = p18.DuetMachine()
    machine.set('a', '2')
    machine.jgz('b', 'a')
    assert machine.instruction_ptr == 2
    machine.set('b', '5')
    machine.jgz('b', 'a')
    assert machine.instruction_ptr == 5
    machine.set('a', '-2') # 5
    machine.jgz('0', 'a') # 6
    assert machine.instruction_ptr == 7
    machine.jgz('3', 'a') # 7
    assert machine.instruction_ptr == 5

def test_machine_run():
    """Tests Duet Machine run()"""
    machine = p18.DuetMachine()
    machine.load_program(TEST_PROGRAM_A)
    machine.runA()
    assert machine.first_rcv == 4

def test_duet_run():
    """Tests DuetRunner run()"""
    duet = p18.DuetRunner()
    duet.load_program(TEST_PROGRAM_B)
    duet.run()
    assert duet.machine1.send_count == 3