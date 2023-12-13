# 2. Implement a Depth-First Search(DFS) algorithm for a graph.

# In this implementation, the Graph class has methods to add edges (add_edge) and perform Depth-First Search (dfs). 
# The dfs method takes a starting node as an argument and returns the DFS traversal order as a list.

# The dfs_recursive function is a recursive helper function that performs the actual DFS traversal. 
# It marks the current node as visited, appends it to the result list, and recursively explores its neighbors.

# The example usage demonstrates creating a simple graph and performing DFS starting from a specific node. 
# You can modify the add_edge calls to create your own graph for testing. The output will display the DFS traversal order.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start):
        visited = {node: False for node in self.graph}
        result = []

        def dfs_recursive(node):
            visited[node] = True
            result.append(node)

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        return result

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_node = 2
dfs_result = g.dfs(start_node)

print(f"DFS starting from node {start_node}:")
print(dfs_result)
