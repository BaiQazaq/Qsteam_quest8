# 10. Implement a method to find strongly connected components in a directed graph.
# Finding strongly connected components (SCCs) in a directed graph involves identifying groups of vertices where there is 
# a directed path from any vertex to any other vertex within the group. 
# # The Kosaraju's algorithm is commonly used to find SCCs in a directed graph.

# In this implementation, the Graph class has methods to add edges (add_edge) and perform Kosaraju's algorithm (kosaraju). 
# The algorithm consists of two depth-first searches (DFS) passes. 
# The first pass fills a stack with vertices in order of their finishing times in DFS. 
# The second pass traverses the transposed graph (reverse edges) in the order given by the stack and 
# identifies strongly connected components.

# The example usage demonstrates creating a simple directed graph and finding its strongly connected components. 
# You can modify the add_edge calls to create your own directed graph for testing. 
# The output will display the strongly connected components.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def kosaraju(self):
        def dfs_first_pass(node):
            visited_first_pass[node] = True
            for neighbor in self.graph[node]:
                if not visited_first_pass[neighbor]:
                    dfs_first_pass(neighbor)
            stack.append(node)

        def dfs_second_pass(node, scc):
            visited_second_pass[node] = True
            scc.append(node)
            for neighbor in self.graph[node]:
                if not visited_second_pass[neighbor]:
                    dfs_second_pass(neighbor, scc)

        def transpose():
            transposed_graph = defaultdict(list)
            for node in self.graph:
                for neighbor in self.graph[node]:
                    transposed_graph[neighbor].append(node)
            return transposed_graph

        visited_first_pass = {node: False for node in self.graph}
        stack = []

        for node in self.graph:
            if not visited_first_pass[node]:
                dfs_first_pass(node)

        transposed_graph = transpose()

        visited_second_pass = {node: False for node in self.graph}
        strongly_connected_components = []

        while stack:
            node = stack.pop()
            if not visited_second_pass[node]:
                scc = []
                dfs_second_pass(node, scc)
                strongly_connected_components.append(scc)

        return strongly_connected_components

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

sccs = g.kosaraju()

print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
