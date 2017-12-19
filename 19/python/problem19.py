"""
Advent of Code 2017 :: Day 19
A Series of Tubes
"""
from collections import namedtuple

Pos = namedtuple(Pos, ['row', 'col'])
Pos.__add__ = lambda s, o: Pos(s.row + o.row, s.col + o.col)

def get_neighbors_4(row, col, height, width):
    "Gets the neighbors of given cell: right, left, down, up."
    if col + 1 < width:
        yield (row, col + 1)
    if col - 1 >= 0:
        yield (row, col - 1)
    if row + 1 < height:
        yield (row + 1, col)
    if row - 1 >= 0:
        yield (row - 1, col)


def find_start(maze):
    """Find the start point of maze"""
    col = maze[0].index('|')
    return (0, col)


def next_move(position, maze, visited):
    row, col = position
    char = maze[row][col]
    next_pos = None
    if char == '|':
        if row > 0 and not visited[row-1][col]:
            next_pos = (row - 1, col)
        else:
            next_pos = (row + 1, col)
    elif char == '-':
        if not visited[row][col-1]:
            next_pos = (row, col - 1)
        else:
            next_pos = (row, col + 1)
    else:
        width = len(maze[0])
        height = len(maze)
        for row_v, col_v in get_neighbors_4(row, col, height, width):
            if maze[row_v][col_v] != ' ' and not visited[row_v][col_v]:
                next_pos = (row_v, col_v) 
    
    if not next_pos or maze[next_pos[0]][next_pos[1]] == ' ':
        return (-1, -1)
    else:
        return next_pos


def solve_a(maze):
    """Solve first part of puzzle."""
    message = []
    width = len(maze[0])
    height = len(maze)
    visited = [[False for _ in range(width)] for _ in range(height)]
    row, col = find_start(maze)
    visited[row][col] = True
    direction = (-1, 0)
    while True:
    while row >= 0 and col >= 0:
        print(row, col, maze[row][col])
        row, col = next_move((row, col), maze, visited)
        visited[row][col] = True
        if maze[row][col].isalpha():
            message.append(maze[row][col])
    return ''.join(message)


def main():
    """Main program."""
    import sys
    maze = [line[:-1] for line in sys.stdin]
    for row in maze:
        print(row)
    print('The solution to Part A is', solve_a(maze))


if __name__ == '__main__':
    main()