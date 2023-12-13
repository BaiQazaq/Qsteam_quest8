# 9. Write a program to detect a cycle in a graph using DFS.

# In this implementation, the Graph class has methods to add edges (add_edge) and check for a cycle using DFS (has_cycle_dfs). 
# The dfs_util function is a recursive helper function that performs the DFS traversal. 
# If a visited node is encountered that is already in the recursion stack, it indicates the presence of a back edge and hence a cycle.

# The example usage demonstrates creating a simple directed graph and checking if it has a cycle. 
# You can modify the add_edge calls to create your own graph for testing. The output will indicate whether the graph has a cycle or not.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle_dfs(self):
        visited = set()
        recursion_stack = set()

        def dfs_util(node):
            visited.add(node)
            recursion_stack.add(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    if dfs_util(neighbor):
                        return True
                elif neighbor in recursion_stack:
                    return True

            recursion_stack.remove(node)
            return False

        for node in self.graph:
            if node not in visited:
                if dfs_util(node):
                    return True

        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

has_cycle = g.has_cycle_dfs()

if has_cycle:
    print("The graph has a cycle.")
else:
    print("The graph does not have a cycle.")
