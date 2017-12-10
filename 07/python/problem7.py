"""
Advent of Code :: Day 7
Recursive Circus
"""
from collections import Counter

class Program:
    __slots__ = ['name', 'weight', 'old_weight', 'children', 'child_weight']

    def __init__(self, name, weight, children=[], child_weight=0):
        self.name = name
        self.weight = weight
        self.children = children
        self.child_weight = child_weight
        self.old_weight = 0

    def __repr__(self):
        return "Program({}, {}, {}, {})".format(self.name, self.weight,
                                                repr(self.children),
                                                self.child_weight)

    def __str__(self):
        return repr(self)


def parse_input(input_lines):
    """
    Builds a parents of programs from given lines of input.
    """
    parents = dict()
    programs = dict()
    for line in input_lines:
        tokens = line.split()
        if len(tokens) > 2:
            # has children
            parent, weight, _, *children = tokens
            weight = int(weight[1:-1])
            programs[parent] = Program(parent, weight,
                                       [c.replace(',', '') for c in children])
            for child in children:
                parents[child.replace(',', '')] = parent
        else:
            # no children
            prog, weight = tokens
            weight = int(weight[1:-1])
            programs[prog] = Program(prog, weight)

    return programs, parents



def solveA(programs, parents):
    """Solves first part of program."""
    return set(programs.keys()).difference(set(parents.keys())).pop()

def solveB(root, programs):
    weigh_tree(root, programs)
    return find_changed(root, programs)


def different_index(values):
    """Return the index of the different value."""
    for index, val in enumerate(values[:-1]):
        if val != values[index + 1]:
            if index == 0 and len(values) > 2:
                if values[1] != values[2]:
                    return 1
            else:
                return index + 1
    return 0


def find_changed(root, programs):
    """Find and return the name of the changed element."""
    if programs[root].old_weight:
        return root
    else:
        for child in programs[root].children:
            changed = find_changed(child, programs)
            if changed:
                return changed
    return None


def weigh_tree(root, programs):
    """Add child weights to tree."""
    if programs[root].children:
        child_weights = [weigh_tree(c, programs) for c in programs[root].children]
        if child_weights.count(child_weights[0]) != len(child_weights):
            # program with wrong weight: find it
            index = different_index(child_weights)
            child_name = programs[root].children[index]
            child = programs[child_name]
            child.old_weight = child.weight
            if index == 0:
                offset = 1
            else:
                offset = -1
            delta = child_weights[index + offset] - child_weights[index]
            child.weight += delta
            child_weights[index] += delta
        programs[root].child_weight = sum(child_weights)
    return programs[root].child_weight + programs[root].weight


def print_tree(root, programs, level):
    """Print the tree."""
    padding = '  ' * level
    line = "{}({}){} #{} {} #{}".format(padding, level, root,
                                        programs[root].weight,
                                        programs[root].children,
                                        programs[root].child_weight)
    print(line)
    for child in programs[root].children:
        print_tree(child, programs, level+1)


def main():
    """Main program."""
    import sys
    input_lines = sys.stdin.readlines()
    programs, parents = parse_input(input_lines)
    root = solveA(programs, parents)
    print('The solution to part A is', root)
    changed = solveB(root, programs)
    print('The solution to part B is', programs[changed].weight)


if __name__ == '__main__':
    main()
