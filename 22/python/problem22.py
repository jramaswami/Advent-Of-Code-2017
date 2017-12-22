"""
Advent of Code 2017 :: Day 22
Sporifica Virus
"""
from collections import namedtuple, defaultdict
import tqdm
import pyperclip


Position = namedtuple('Position', ['row', 'col'])
Position.__add__ = lambda s, o: Position(s.row + o.row, s.col + o.col)
Position.move = lambda s, cmplx: Position(s.row + cmplx.imag, s.col + cmplx.real)


DirectionsT = namedtuple('Directions', ['up', 'down', 'right', 'left'])
Directions = DirectionsT(Position(-1, 0), Position(1, 0), 
                        Position(0, 1), Position(0, -1))


StateT = namedtuple('StateT', ['Clean', 'Weakened', 'Infected', 'Flagged'])
State = StateT(0, 1, 2, 3)


class Sporifica:
    """Represents the virus."""
    def __init__(self, init_pos):
        self.pos = init_pos
        self.direction = Directions.up

    def turn_right(self):
        """Turn"""
        turns = {Directions.up: Directions.right, 
                 Directions.left: Directions.up,
                 Directions.down: Directions.left, 
                 Directions.right: Directions.down}  
        self.direction = turns[self.direction]
    
    def turn_left(self):
        """Turn"""
        turns = {Directions.up: Directions.left, 
                 Directions.left: Directions.down,
                 Directions.down: Directions.right, 
                 Directions.right: Directions.up}
        self.direction = turns[self.direction]
    
    def turn(self, state):
        if state == State.Clean:
            self.turn_left()
        elif state == State.Infected:
            self.turn_right()
        elif state == State.Flagged:
            self.direction = Position(self.direction.row * -1, self.direction.col * -1)


    def move(self):
        """Move"""
        self.pos = self.pos + self.direction


class Cluster:
    """Represents cluster."""
    def __init__(self, memory_string):
        self.infected = defaultdict(int)
        self.infections_caused = 0
        self.init_memory_dim = 0
        self.read_memory(memory_string)
        self.center = self.init_memory_dim // 2
        self.virus = Sporifica(Position(self.center, self.center))
    
    def read_memory(self, memory_string):
        lines = memory_string.strip().split('\n')
        self.init_memory_dim = len(lines)
        for rindex, row in enumerate(lines):
            for cindex, col in enumerate(row):
                if col == '#':
                    pos = Position(rindex, cindex)
                    self.infected[pos] = State.Infected

    def next_state(self, pos):
        """Changes state of position."""           
        if self.infected[pos] == State.Infected:
            self.infected[pos] = State.Clean
        else:
            self.infected[pos] = State.Infected
        if self.infected[pos] == State.Infected:
            self.infections_caused += 1

    def burst(self):
        """Perform one burst."""
        self.virus.turn(self.infected[self.virus.pos])
        self.next_state(self.virus.pos)
        self.virus.move()


class EvolvedCluster(Cluster):
    def __init__(self, memory_string):
        super(EvolvedCluster, self).__init__(memory_string)

    def next_state(self, pos):
        """Changes state of position."""           
        self.infected[pos] = (self.infected[pos] + 1) % 4
        if self.infected[pos] == State.Infected:
            self.infections_caused += 1


def solve_a(bursts, memory_string):
    """Solve first part of puzzle."""
    cluster = Cluster(memory_string)
    for _ in tqdm.tqdm(range(bursts)):
       cluster.burst()
    return cluster.infections_caused


def solve_b(bursts, memory_string):
    """Solve first part of puzzle."""
    cluster = EvolvedCluster(memory_string)
    for _ in tqdm.tqdm(range(bursts)):
       cluster.burst()
    return cluster.infections_caused


def solve_a0(bursts, memory_string):
    """Alternate solution for a."""
    infection_count = 0
    rot_left = 1j
    rot_right = -1j
    lines = memory_string.strip().split('\n')
    center = len(lines) // 2
    grid = defaultdict(int)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                posn = col - (row * 1j)
                grid[posn] = 1
    virus_posn = center - (center * 1j)
    virus_dirn = 1j
    for _ in range(bursts):
        # turn
        curr_state = grid[virus_posn]
        if curr_state == 0: # clean
            virus_dirn *= rot_left
            infection_count += 1  # will be infected
        elif curr_state == 1: # infected
            virus_dirn *= rot_right
        # infect
        new_state = (curr_state + 1) % 2
        grid[virus_posn] = new_state
        # move
        virus_posn += virus_dirn
    return infection_count


def solve_b0(bursts, memory_string):
    """Alternate solution for b."""
    infection_count = 0
    rot_left = 1j
    rot_right = -1j
    lines = memory_string.strip().split('\n')
    center = len(lines) // 2
    grid = defaultdict(int)
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                posn = col - (row * 1j)
                grid[posn] = 2
    virus_posn = center - (center * 1j)
    virus_dirn = 1j
    for _ in tqdm.tqdm(range(bursts)):
        # turn
        curr_state = grid[virus_posn]
        if curr_state == 0: # clean
            virus_dirn *= rot_left
        elif curr_state == 1: # weakened
            infection_count += 1 # will be infected
        elif curr_state == 2: # infected
            virus_dirn *= rot_right
        elif curr_state == 3: # flagged
            virus_dirn *= -1
        # infect
        new_state = (curr_state + 1) % 4
        grid[virus_posn] = new_state
        # move
        virus_posn += virus_dirn
    return infection_count


def main():
    """Main program."""
    import sys
    memory_string = sys.stdin.read()
    solution_a = solve_a0(10000, memory_string)
    print('The solution to Part A is', solution_a)
    solution_b = solve_b0(10000000, memory_string)
    print('The solution to Part B is', solution_b)
    pyperclip.copy(str(solution_b))


if __name__ == '__main__':
    main()