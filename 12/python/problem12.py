"""
Advent of Code 2017 :: Day 12
Digital Plumber
"""
from collections import defaultdict, deque

def read_graph(input_string):
    """Reads from from list of lines."""
    graph = defaultdict(list)
    for line in input_string.strip().split('\n'):
        node_u, graph_text = line.split(' <-> ')
        graph[int(node_u)] = [int(i) for i in graph_text.split(', ')]
    return graph

def component_count(root, graph):
    """Counts number of components connected to root."""
    count = 0
    visited = defaultdict(bool)
    queue = deque()
    queue.append(root)
    visited[root] = True
    while queue:
        node_u = queue.popleft()
        count += 1
        for node_v in graph[node_u]:
            if not visited[node_v]:
                visited[node_v] = True
                queue.append(node_v)
    return count


def count_components(graph):
    """Counts number of components in graph."""
    count = 0
    visited = defaultdict(bool)
    for root in graph.keys():
        if visited[root]:
            continue
        count += 1
        queue = deque()
        queue.append(root)
        visited[root] = True
        while queue:
            node_u = queue.popleft()
            for node_v in graph[node_u]:
                if not visited[node_v]:
                    visited[node_v] = True
                    queue.append(node_v)
    return count

def main():
    """Main program."""
    import sys
    graph = read_graph(sys.stdin.read())
    print('The solution to part A is', component_count(0, graph))
    print('The solution to part B is', count_components(graph))


if __name__ == '__main__':
    main()
