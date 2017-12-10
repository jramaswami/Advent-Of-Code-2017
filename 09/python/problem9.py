"""
Advent of Code 2017 :: Day 9
Stream Processing
"""

# States
GROUP = 0
GARBAGE = 1
CANCEL = 2

def score_stream(stream):
    """Score the stream"""
    level = 0
    state = []
    garbage_chars = 0
    acc = 0
    for char in stream:
        if state == []:
            if char == '{':
                state.append(GROUP)
                level += 1
            elif char == '<':
                state.append(GARBAGE)
            elif char == '!':
                state.append(CANCEL)
        elif state[-1] == CANCEL:
            state.pop()
        elif state[-1] == GARBAGE:
            if char == '>':
                state.pop()
            elif char == '!':
                state.append(CANCEL)
            else:
                garbage_chars += 1
        elif state[-1] == GROUP:
            if char == '}':
                acc += level
                level -= 1
                state.pop()
            elif char == '{':
                state.append(GROUP)
                level += 1
            elif char == '!':
                state.append(CANCEL)
            elif char == '<':
                state.append(GARBAGE)
    return acc, garbage_chars


def main():
    """Main program."""
    import sys
    input_stream = sys.stdin.read()
    score, garbage_chars = score_stream(input_stream)
    print('Solution to part A is', score)
    print('Solution to part B is', garbage_chars)


if __name__ == '__main__':
    main()
