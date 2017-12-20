"""
Advent of Code 2017 :: Day 20
Particle Swarm
"""
import re
from collections import namedtuple

PATTERN = re.compile('-?\d+')

Position = namedtuple('Position', ['x', 'y', 'z'])
Position.__add__ = lambda s, o: Position(s.x + o.x, s.y + o.y, s.z + o.z)
Position.distance = lambda s: abs(s.x) + abs(s.y) + abs(s.z)


def move_particle(particle):
    """Returns new particle at new position and velocity."""
    vel = particle.velocity + particle.acceleration
    pos = particle.position + vel
    return Particle(particle.index, pos, vel, particle.acceleration)


Particle = namedtuple('Particle', ['index', 'position', 'velocity', 'acceleration'])
Particle.move = move_particle
Particle.distance = lambda s: s.position.distance()


def solve_a(particles):
    """Solve first part of puzzle."""
    while True:
        moved = [p.move() for p in particles]
        if all((p0.distance() < p1.distance() for p0, p1 in zip(particles, moved))):
            return min(((p.distance(), p) for p in moved))[1]
        particles = moved


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
    particles = [parse_particle(i, ln) for i, ln in enumerate(sys.stdin)]
    solution_a = solve_a(particles)
    print('The solution to part A is', solution_a)    


if __name__ == '__main__':
    main()