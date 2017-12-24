"""
Advent of Code 2017 :: Day 24
Electromagnetic Moat
"""
from collections import defaultdict 


class Edge:
    def __init__(self, node_u, node_v):
        self.node_u = node_u
        self.node_v = node_v
        self.visited = False
        self.score = node_u + node_v

    def other_side(self, node_w):
        """Returns other side of edge."""
        if self.node_v == node_w:
            return self.node_u
        else:
            return self.node_v

    def __repr__(self):
        return "({} {})".format(self.node_u, self.node_v)



def dfs_a(graph, node_u, score):
    """DFS search for maximum bridge."""
    max_score = score
    for edge in (e for e in graph[node_u] if not e.visited):
        node_v = edge.other_side(node_u)
        edge.visited = True
        max_score = max(dfs_a(graph, node_v, score + edge.score), max_score)
        edge.visited = False
    return max_score


def dfs_b(graph, node_u, score_t):
    """DFS search for maximum of the longest bridges."""
    max_score_t = score_t
    for edge in (e for e in graph[node_u] if not e.visited):
        node_v = edge.other_side(node_u)
        edge.visited = True
        my_score_t = (score_t[0] + 1, score_t[1] + edge.score)
        max_score_t = max(dfs_b(graph, node_v, my_score_t), max_score_t)
        edge.visited = False
    return max_score_t


def parse_input(input_string):
    """Parse the given input."""
    graph = defaultdict(list)
    for line in input_string.strip().split('\n'):
        node_u, node_v = [int(i) for i in line.split('/')]
        edge = Edge(node_u, node_v)
        graph[node_u].append(edge)
        graph[node_v].append(edge)
    return graph


def main():
    """Main program."""
    import sys
    import pyperclip
    input_string = sys.stdin.read()
    graph = parse_input(input_string)
    solution_a = dfs_a(graph, 0, 0)
    print('The solution to part A is', solution_a)
    solution_b = dfs_b(graph, 0, (0, 0))[1]
    print('The solution to part B is', solution_b)


if __name__ == '__main__':
    main()