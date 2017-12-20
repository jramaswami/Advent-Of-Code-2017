"""
Advent of Code 2017 :: Day 20
Particle Swarm
"""
import re
import itertools
from collections import namedtuple, defaultdict

PATTERN = re.compile('-?\d+')

Position = namedtuple('Position', ['x', 'y', 'z'])
Position.__add__ = lambda s, o: Position(s.x + o.x, s.y + o.y, s.z + o.z)
Position.distance = lambda s: abs(s.x) + abs(s.y) + abs(s.z)


class Particle:
    def __init__(self, index, pos, vel, acc):
        self.index = index
        self.pos = pos
        self.prev_pos = None
        self.vel = vel
        self.acc = acc
        self.destroyed = False

    def move(self):
        """Move particle"""
        self.prev_pos = self.pos
        self.vel = self.vel + self.acc
        self.pos = self.pos + self.vel

    def dist_to_origin(self):
        """Return distance to origin."""
        return self.pos.distance()

    def getting_closer(self, other):
        """Returns true if self and other are getting closer."""
        prev_d = abs(self.prev_pos.x - other.prev_pos.x) + \
                 abs(self.prev_pos.y - other.prev_pos.y) + \
                 abs(self.prev_pos.z - other.prev_pos.z)
        curr_d = abs(self.pos.x - other.pos.x) + \
                 abs(self.pos.y - other.pos.y) + \
                 abs(self.pos.z - other.pos.z)
        if curr_d < prev_d:
            return True
        return False
        
    def __repr__(self):
        return "Postion({}, pos=({},{},{}) vel=({},{},{}), acc=({},{},{})".format(
            repr(self.index), 
            self.pos.x, self.pos.y, self.pos.z,
            self.vel.x, self.vel.y, self.vel.z,
            self.acc.x, self.acc.y, self.acc.z)

    def __lt__(self, other):
        sdist = self.dist_to_origin()
        odist = other.dist_to_origin()
        if sdist == odist:
            return self.acc < other.acc
        else:
            return sdist < odist


def solve_a(particles):
    """Solve first part of puzzle."""
    while True:
        for p in particles:
            p.move()
        
        min_acc = min(p.acc.distance() for p in particles)
        min_particle = min(p for p in particles)
        if min_particle.acc.distance() == min_acc:
            return min_particle.index


def remove_collisions(particles):
    """Remove particles that are colliding."""
    positions = defaultdict(list)
    for p in particles:
        positions[p.pos].append(p)

    for pos, ps in positions.items():
        if len(ps) > 1:
            for p in ps:
                p.destroyed = True
    
    return [p for p in particles if not p.destroyed]


def tick(particles):
    """Move particles."""
    for p in particles:
        p.move()
    return particles


def solve_b(particles):
    """Solve second part of puzzle."""
    prev_len = 0
    while True:
        particles = tick(particles)
        particles = remove_collisions(particles)
        if not any(p0.getting_closer(p1) for p0, p1 in itertools.product(particles, repeat=2)):
            return len(particles)


def parse_particle(index, line):
    """Returns particle."""
    numbers = [int(n) for n in PATTERN.findall(line)]
    if len(numbers) != 9:
        print('ERROR', line)
    pos = Position(numbers[0], numbers[1], numbers[2])
    vel = Position(numbers[3], numbers[4], numbers[5])
    acc = Position(numbers[6], numbers[7], numbers[8])
    return Particle(index, pos, vel, acc)
    
    
def main():
    """Main program."""
    import sys
    lines = sys.stdin.read().strip().split('\n')
    particles_a = [parse_particle(i, ln) for i, ln in enumerate(lines)]
    particles_b = [parse_particle(i, ln) for i, ln in enumerate(lines)]
    solution_a = solve_a(particles_a)
    print('The solution to part A is', solution_a)
    solution_b = solve_b(particles_b)
    print('The solution to part B is', solution_b)


if __name__ == '__main__':
    main()