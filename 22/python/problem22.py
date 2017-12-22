"""
Advent of Code 2017 :: Day 22
Sporifica Virus
"""
from collections import namedtuple, defaultdict
import tqdm
import pyperclip


Position = namedtuple('Position', ['row', 'col'])
Position.__add__ = lambda s, o: Position(s.row + o.row, s.col + o.col)
Position.__sub__ = lambda s, o: Position(s.row - o.row, s.col - o.col)

DirectionsT = namedtuple('Directions', ['up', 'down', 'right', 'left'])
Directions = DirectionsT(Position(-1, 0), Position(1, 0), 
                        Position(0, 1), Position(0, -1))


StateT = namedtuple('StateT', ['Clean', 'Weakened', 'Infected', 'Flagged'])
State = StateT(0, 1, 3, 4)


LOGGING = False


def log(*msg):
    """Logging"""
    if LOGGING:
        print(*msg)


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
            self.turn_right

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
        log(pos, 'to', self.infected[pos]) 
        if self.infected[pos] == State.Infected:
            self.infections_caused += 1

    def burst(self):
        """Perform one burst."""
        log('virus pos', self.virus.pos, self.infected[self.virus.pos])
        if self.infected[self.virus.pos] == State.Infected:
            log(self.virus.pos, 'turning right')
            self.virus.turn_right()
        else:
            log(self.virus.pos, 'turning left')
            self.virus.turn_left()
        self.next_state(self.virus.pos)
        self.virus.move()


def solve_a(bursts, memory_string):
    """Solve first part of puzzle."""
    cluster = Cluster(memory_string)
    log(cluster.infected)
    for _ in tqdm.tqdm(range(bursts)):
       cluster.burst()
    return cluster.infections_caused


def main():
    """Main program."""
    import sys
    memory_string = sys.stdin.read()
    solution_a = solve_a(10000, memory_string)
    print('The solution to Part A is', solution_a)
    pyperclip.copy(str(solution_a))


if __name__ == '__main__':
    main()