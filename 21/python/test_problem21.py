"""
Advent of Code 2017 :: Day 21
Tests for Fractal Art
"""
import problem21 as p21


def test_count_pixels_on():
    """Test count_pixels_on()"""
    assert p21.count_pixels_on(['.#.', '..#', '###']) == 5

def test_enhance():
    """Test enhance()"""
    rules = p21.read_rules(['../.# => ##./#../...',
                           '.#./..#/### => #..#/..../..../#..#'])
    matrix = ['.#.', '..#', '###']
    matrix1 = p21.enhance(matrix, rules)
    assert matrix1 == ['#..#','....','....','#..#']
    matrix2 = p21.enhance(matrix1, rules)
    assert matrix2 == ['##.##.','#..#..','......','##.##.','#..#..','......']
    assert p21.count_pixels_on(matrix2) == 12