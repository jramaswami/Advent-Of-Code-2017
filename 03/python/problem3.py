"""
Advent of Code 2017 :: Day 3
Spiral Memory
"""
from collections import deque

class Location:
    __slots__ = ['row', 'col']

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def moveRight(self):
        self.col += 1

    def moveLeft(self):
        self.col -= 1

    def moveUp(self):
        self.row -= 1

    def moveDown(self):
        self.row += 1

    def __repr__(self):
        return "Location(row={}, col={})".format(self.row, self.col)

    def __str__(self):
        return repr(self)

# Make use of code from Euler 28
def generate_spiral_diagonals():
    """
    Generator function for the diagonals of a spiral.
    After the first value in the center, the function
    will yield the lower right, lower left, upper left,
    and upper right values of the next spiral
    continuously.
    """
    # First yield the center
    corner_val = 1
    yield (0, corner_val)
    dim_index = 3
    while True:
        for dummy_corner in range(4):
            corner_val = corner_val + dim_index - 1
            yield (dim_index - 1, corner_val)
        dim_index = dim_index + 2


def solveA(location):
    """Solve first part of puzzle."""
    gen = generate_spiral_diagonals()
    prev_steps = prev_corner = 0
    steps, corner = next(gen)
    while corner < location:
        prev_steps, prev_corner = steps, corner
        steps, corner = next(gen)
    delta = min(corner - location, location - prev_corner)
    return steps - delta


def computeValue(location, matrix):
    delta = 0
    moves = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (0, 0)]
    for move in moves:
        row = location.row + move[0]
        col = location.col + move[1]
        if col >= 0 and col < len(matrix[0]) and row >= 0 and row < len(matrix):
            delta += matrix[row][col]
    matrix[location.row][location.col] = delta
    return delta


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(str(i) for i in row))

def addLayer(location, matrix, limit):
    for row in matrix:
        row.append(0)
        row.appendleft(0)
    row = deque([0]* len(matrix[0]))
    matrix.append(row)
    row1 = deque([0]* len(matrix[0]))
    matrix.appendleft(row1)
    # move location to account for appended left and up
    location.moveRight()
    location.moveDown()
    # first move right
    location.moveRight()
    val = computeValue(location, matrix)
    if val > limit:
        return val
    # move up
    while True:
        location.moveUp()
        if location.row < 0:
            location.moveDown()
            break
        val = computeValue(location, matrix)
        if val > limit:
            return val
    # move left
    while True:
        location.moveLeft()
        if location.col < 0:
            location.moveRight()
            break
        val = computeValue(location, matrix)
        if val > limit:
            return val
    # move down
    while True:
        location.moveDown()
        if location.row >= len(matrix):
            location.moveUp()
            break
        val = computeValue(location, matrix)
        if val > limit:
            return val
    # move right
    while True:
        location.moveRight()
        if location.col >= len(matrix[0]):
            location.moveLeft()
            break
        val = computeValue(location, matrix)
        if val > limit:
            return val

    return val

def solveB(limit):
    """Solve second part of puzzle."""
    matrix = deque()
    matrix.append(deque([1]))
    curr = 1
    location = Location(0,0)
    while curr <= limit:
        curr = addLayer(location, matrix, limit)
    return curr

def main():
    """Main program."""
    print("The answer to part A is", solveA(325489))


if __name__ == '__main__':
    main()
