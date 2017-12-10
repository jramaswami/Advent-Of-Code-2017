"""
Advent of Code 2017 :: Day 9
Tests for Stream Processing
"""
import problem9 as p9

def test_score_stream_A():
    """Tests for first part of puzzle."""
    assert p9.score_stream("{}")[0] == 1
    assert p9.score_stream("{{{}}}")[0] == 6
    assert p9.score_stream("{{},{}}")[0] == 5
    assert p9.score_stream("{{{},{},{{}}}}")[0] == 16
    assert p9.score_stream("{<a>,<a>,<a>,<a>}")[0] == 1
    assert p9.score_stream("{{<ab>},{<ab>},{<ab>},{<ab>}}")[0] == 9
    assert p9.score_stream("{{<!!>},{<!!>},{<!!>},{<!!>}}")[0] == 9
    assert p9.score_stream("{{<a!>},{<a!>},{<a!>},{<ab>}}")[0] == 3

def test_score_stream_B():
    """Tests for second part of puzzle."""
    assert p9.score_stream("<>")[1] == 0
    assert p9.score_stream("<random characters>")[1] == 17
    assert p9.score_stream("<<<<>")[1] == 3
    assert p9.score_stream("<{!>}>")[1] == 2
    assert p9.score_stream("<!!>")[1] == 0
    assert p9.score_stream("<!!!>>")[1] == 0
    assert p9.score_stream("<{o\"i!a,<{i<a>")[1] == 10
