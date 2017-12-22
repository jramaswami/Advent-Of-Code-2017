import problem22 as p22

def test_burst():
    """Test burst()"""
    cluster = p22.Cluster('..#\n#..\n...')
    assert cluster.infected[p22.Position(0, 2)]
    assert cluster.infected[p22.Position(1, 0)]
    assert not cluster.infected[p22.Position(1, 1)]
    cluster.burst()
    assert cluster.virus.direction == p22.DIRECTIONS.left
    assert cluster.virus.pos == p22.Position(1,0)
    assert cluster.infected[p22.Position(1,1)]
    assert cluster.infected[cluster.virus.pos]
    prev_pos = cluster.virus.pos
    cluster.burst()
    assert cluster.virus.direction == p22.DIRECTIONS.up  # turned right
    assert cluster.virus.pos == p22.Position(0, 0) # moved up
    assert not cluster.infected[prev_pos] # cleaned
    # four times in a row finds clean and infects

    for _ in range(4):
        assert not cluster.infected[cluster.virus.pos]
        prev_pos = cluster.virus.pos
        cluster.burst()
        assert cluster.infected[prev_pos]
    assert cluster.virus.pos == p22.Position(0, 0)
    prev_pos = cluster.virus.pos
    cluster.burst()
    assert cluster.virus.direction == p22.DIRECTIONS.right
    assert cluster.virus.pos == p22.Position(0, 1)
    assert not cluster.infected[prev_pos]
    assert cluster.infections_caused == 5

def test_solve_a():
    assert p22.solve_a(7, '..#\n#..\n...') == 5
    assert p22.solve_a(70, '..#\n#..\n...') == 41
    assert p22.solve_a(10000, '..#\n#..\n...') == 5587
