"""
Advent of Code 2017 :: Day 20
Tests for Particle Swarm
"""
import problem20 as p20

def test_solve_a():
    """Test solve_a()"""
    p0 = p20.parse_particle(0, 'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>')
    p1 = p20.parse_particle(1, 'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>')
    assert p20.solve_a([p0, p1]) == 0


def test_solve_b():
    """Test solve_b()"""
    p0 = p20.parse_particle(0, '<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>')
    p1 = p20.parse_particle(1, 'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>')
    p2 = p20.parse_particle(2, 'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>')
    p3 = p20.parse_particle(3, 'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>')
    particles = [p0, p1, p2, p3]
    assert p20.solve_b(particles) == 1