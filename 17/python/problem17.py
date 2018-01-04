"""
Advent of Code 2017 :: Day 17
Spinlock
"""
import tqdm


INPUT = 344
LIMIT = 50000000


class Node:
    """Represents a node in the linked list."""
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return repr(self)

    def __repr__(self):
        if self.child:
            return "{} {}".format(repr(self.value), repr(self.child))
        return "{}.".format(repr(self.value))


class CircularBuffer:
    """Represents the circular buffer."""
    def __init__(self):
        self.curr = 1
        self.head = Node(0)
        self.tail = self.head
        self.pos = self.head

    def spin(self, steps):
        """Do on round of spinning."""
        actual_steps = steps % self.curr
        for _ in range(actual_steps):
            if self.pos.child:
                self.pos = self.pos.child
            else:
                self.pos = self.head
        new_node = Node(self.curr)
        self.curr += 1
        new_node.child = self.pos.child
        self.pos.child = new_node
        self.pos = new_node

    def __repr__(self):
        return repr(self.head)


def solve_a(steps):
    """Solution to first part of puzzle."""
    sbuffer = CircularBuffer()
    for i in range(2017):
        sbuffer.spin(steps)
    return sbuffer.pos.child.value

def solve_b(steps, limit):
    """Solution to second part of puzzle."""
    index = 0
    curr = 1
    value = 0
    for _ in tqdm.tqdm(range(limit)):
        actual_steps = steps % curr
        index = (index + actual_steps) % curr
        if index == 0:
            value = curr
        index += 1
        curr += 1
    return value

def solve_b0(steps, limit):
    "Better solution to second part of puzzle."""
    index = 0
    curr = 1
    value = 0
    while curr <= limit:
        jump = (curr - index - 1) // steps
        if jump:
            index = index + (jump * steps) + jump 
            curr += jump
        else:
            actual_steps = steps % curr
            index = (index + actual_steps) % curr
            if index == 0:
                value = curr
            curr += 1
            index += 1
        assert index < curr
    return value


def main():
    """Main program."""
    print('The solution to part A is', solve_a(INPUT))
    print('The solution to part B is', solve_b0(INPUT, LIMIT))


if __name__ == '__main__':
    main()
