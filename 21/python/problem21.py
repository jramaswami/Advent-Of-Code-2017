"""
Advent of Code 2017 :: Day 21
Fractal Art
"""
import pyperclip
import tqdm

def count_pixels_on(matrix):
    """Returns the count of pixels on."""
    return sum(row.count('#') for row in matrix)


def enhance(matrix, rules):
    """Enhance matrix according to rules."""
    
    if len(matrix) % 2 == 0:
        offset = 2
    elif len(matrix) % 3 == 0:
        offset = 3
    else:
        print("ERROR")
        return None

    new_matrix = []
    for row in range(0, len(matrix), offset):
        new_section = ['' for _ in range(offset+1)]
        for col in range(0, len(matrix), offset):
            selection = [matrix[r][col:col+offset] for r in range(row,row+offset)]
            tag = '/'.join(selection)
            new_tag = rules[tag]
            new_selection = new_tag.split('/')
            for index, new_row in enumerate(new_selection):
                new_section[index] = new_section[index] + new_row
        new_matrix.extend(new_section)
    return new_matrix


def rotations(matrix):
    yield [row[::-1] for row in matrix]  # vertical flip
    yield matrix[::-1]  # horizontal flip
    # diagnoal flip
    fmatrix = [[s for s in row] for row in matrix]
    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix)):
            fmatrix[i][j], fmatrix[j][i] = fmatrix[j][i], fmatrix[i][j]
    yield [''.join(row) for row in fmatrix]
    # reverse diagonal flip
    fmatrix = [row[::-1] for row in fmatrix]
    yield [''.join(row) for row in fmatrix[::-1]]
    # rotations cc
    rmatrix = list(matrix)
    for _ in range(3):
        rmatrix = [''.join(row) for row in zip(*rmatrix[::-1])]
        yield rmatrix
    # rotations ccw
    rmatrix = list(matrix)
    for _ in range(3):
        rmatrix = [''.join(row) for row in list(zip(*rmatrix))[::-1]]
        yield rmatrix


def read_rules(lines):
    """Read rules from list of input lines."""
    rules = {}
    for line in lines:
        tokens = line.strip().split(' => ')
        rules[tokens[0]] = tokens[1]
        for rotation in rotations(tokens[0].split('/')):
            rules['/'.join(rotation)] = tokens[1]
    return rules


def main():
    """Main program."""
    import sys
    rules = read_rules(sys.stdin)
    matrix = ['.#.', '..#', '###']
    for round in range(18):
        if round == 5:
            solution_a = count_pixels_on(matrix)
            print('The solution to A is', solution_a)
        matrix = enhance(matrix, rules)
    solution_b = count_pixels_on(matrix)
    print('The solution to B is', solution_b)
    pyperclip.copy(str(solution_b))


if __name__ == '__main__':
    main()