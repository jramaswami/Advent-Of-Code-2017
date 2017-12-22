import problem22 as p22

def test_burst():
    """Test burst()"""
    cluster = p22.Cluster('..#\n#..\n...')
    assert cluster.infected[p22.Position(0, 2)] == p22.State.Infected
    assert cluster.infected[p22.Position(1, 0)] == p22.State.Infected
    assert cluster.infected[p22.Position(1, 1)] == p22.State.Clean
    cluster.burst()
    assert cluster.virus.direction == p22.Directions.left
    assert cluster.virus.pos == p22.Position(1,0)
    assert cluster.infected[p22.Position(1,1)] == p22.State.Infected
    assert cluster.infected[cluster.virus.pos] == p22.State.Infected
    prev_pos = cluster.virus.pos
    cluster.burst()
    assert cluster.virus.direction == p22.Directions.up  # turned right
    assert cluster.virus.pos == p22.Position(0, 0) # moved up
    assert cluster.infected[prev_pos] == p22.State.Clean # cleaned
    # four times in a row finds clean and infects

    for _ in range(4):
        assert cluster.infected[cluster.virus.pos] == p22.State.Clean
        prev_pos = cluster.virus.pos
        cluster.burst()
        assert cluster.infected[prev_pos] == p22.State.Infected
    assert cluster.virus.pos == p22.Position(0, 0)
    prev_pos = cluster.virus.pos
    cluster.burst()
    assert cluster.virus.direction == p22.Directions.right
    assert cluster.virus.pos == p22.Position(0, 1)
    assert cluster.infected[prev_pos] == p22.State.Clean
    assert cluster.infections_caused == 5

def test_solve_a():
    assert p22.solve_a(7, '..#\n#..\n...') == 5
    assert p22.solve_a(70, '..#\n#..\n...') == 41
    assert p22.solve_a(10000, '..#\n#..\n...') == 5587

def test_burst_evolved():
    """Test burst()"""
    print("\nEvolved\n")
    cluster = p22.EvolvedCluster('..#\n#..\n...')
    assert cluster.infected[p22.Position(0, 2)] == p22.State.Infected
    assert cluster.infected[p22.Position(1, 0)] == p22.State.Infected
    assert cluster.infected[p22.Position(1, 1)] == p22.State.Clean
    cluster.burst()
    assert cluster.virus.direction == p22.Directions.left
    assert cluster.virus.pos == p22.Position(1,0)
    assert cluster.infected[p22.Position(1,1)] == p22.State.Weakened
    assert cluster.infected[cluster.virus.pos] == p22.State.Infected
    prev_pos = cluster.virus.pos
    cluster.burst()
    assert cluster.virus.direction == p22.Directions.up
    assert cluster.virus.pos == p22.Position(0,0)
    assert cluster.infected[prev_pos] == p22.State.Flagged
    assert cluster.infected[cluster.virus.pos] == p22.State.Clean


def test_solve_b():
    assert p22.solve_b(100, '..#\n#..\n...') == 26
    assert p22.solve_b(10000000, '..#\n#..\n...') == 2511944
