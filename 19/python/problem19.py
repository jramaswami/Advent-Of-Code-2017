"""
Advent of Code 2017 :: Day 19
A Series of Tubes
"""
from collections import namedtuple
import pyperclip


Position = namedtuple('Position', ['row', 'col'])
Position.__add__ = lambda s, o: Position(s.row + o.row, s.col + o.col)
Position.__sub__ = lambda s, o: Position(s.row - o.row, s.col - o.col)

def get_neighbors_4(pos, maze):
    "Gets the neighbors of given cell: right, left, down, up."
    directions = [Position(0, -1), Position(0, 1), Position(-1, 0), Position(1, 0)]
    return [pos + dirn for dirn in directions if inbounds(pos + dirn, maze)]


def find_start(maze):
    """Find the start point of maze"""
    col = maze[0].index('|')
    return Position(0, col)


def inbounds(pos, maze):
    """Returns true if position is inside maze."""
    width = len(maze[0])
    height = len(maze)
    return pos.row >= 0 and pos.row < height and pos.col >= 0 and pos.col < width


def maze_char(pos, maze):
    """Returns the char at that position."""
    return maze[pos.row][pos.col]


def visit(pos, visited):
    """Sets visited to true for given pos."""
    visited[pos.row][pos.col] = True


def is_visited(pos, visited):
    """Returns if position has been visited."""
    return visited[pos.row][pos.col]


def next_move(pos, dirn, maze, visited):
    """Get the next move."""
    next_pos = pos + dirn
    if inbounds(next_pos, maze) and maze_char(next_pos, maze) != ' ':
        return (next_pos, dirn)
    else:
        for next_pos in get_neighbors_4(pos, maze):
            if maze_char(next_pos, maze) != ' ' and not is_visited(next_pos, visited):
                return (next_pos, next_pos - pos)
    return (None, None)

def solve_a(maze):
    """Solve first part of puzzle."""
    message = []
    width = len(maze[0])
    height = len(maze)
    visited = [[False for _ in range(width)] for _ in range(height)]
    pos = find_start(maze)
    dirn = Position(1, 0)
    while pos:
        visit(pos, visited)
        if maze_char(pos, maze).isalpha():
            message.append(maze_char(pos, maze))
        pos, dirn = next_move(pos, dirn, maze, visited)
    return ''.join(message)


def main():
    """Main program."""
    import sys
    maze = [line[:-1] for line in sys.stdin if line.strip()]
    solution_a = solve_a(maze)
    print('The solution to Part A is', solution_a)
    pyperclip.copy(solution_a)


if __name__ == '__main__':
    main()