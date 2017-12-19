"""
Advent of Code 2017 :: Day 19
A Series of Tubes
"""
from collections import namedtuple
import pyperclip


Position = namedtuple('Position', ['row', 'col'])
Position.__add__ = lambda s, o: Position(s.row + o.row, s.col + o.col)
Position.__sub__ = lambda s, o: Position(s.row - o.row, s.col - o.col)

class Maze:
    def __init__(self, input_string):
        self.steps = 0
        self.maze = [line for line in input_string.split('\n')]
        height = len(self.maze)
        width = len(self.maze[0])
        self.visited = visited = [[False for _ in range(width)] for _ in range(height)]
        self.message = []

    def find_start(self):
        """Find the start point of maze"""
        col = self.maze[0].index('|')
        return Position(0, col)

    def get_neighbors_4(self, pos):
        "Gets the neighbors of given cell: right, left, down, up."
        directions = [Position(0, -1), Position(0, 1), Position(-1, 0), Position(1, 0)]
        return [pos + dirn for dirn in directions if self.inbounds(pos + dirn)]

    def inbounds(self, pos):
        """Returns true if position is inside maze."""
        width = len(self.maze[0])
        height = len(self.maze)
        return pos.row >= 0 and pos.row < height and pos.col >= 0 and pos.col < width

    def maze_char(self, pos):
        """Returns the char at that position."""
        return self.maze[pos.row][pos.col]

    def visit(self, pos):
        """Sets visited to true for given pos."""
        self.visited[pos.row][pos.col] = True

    def is_visited(self, pos):
        """Returns if position has been visited."""
        return self.visited[pos.row][pos.col]

    def next_move(self, pos, dirn):
        """Get the next move."""
        next_pos = pos + dirn
        if self.inbounds(next_pos) and self.maze_char(next_pos) != ' ':
            return (next_pos, dirn)
        else:
            for next_pos in self.get_neighbors_4(pos):
                if self.maze_char(next_pos) != ' ' and not self.is_visited(next_pos):
                    return (next_pos, next_pos - pos)
        return (None, None)

    def run_maze(self):
        """Run through the maze."""
        pos = self.find_start()
        dirn = Position(1, 0)
        while pos:
            self.visit(pos)
            self.steps += 1
            if self.maze_char(pos).isalpha():
                self.message.append(self.maze_char(pos))
            pos, dirn = self.next_move(pos, dirn)

    def solution_a(self):
        """Return the solution to part A."""
        return ''.join(self.message)

    def solution_b(self):
        """Return the solution to part B."""
        return self.steps

def main():
    """Main program."""
    import sys
    maze = Maze(sys.stdin.read())
    maze.run_maze()
    print('The solution to Part A is', maze.solution_a())
    print('The solution to Part B is', maze.solution_b())
    pyperclip.copy(str(maze.solution_b()))


if __name__ == '__main__':
    main()