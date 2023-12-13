# 10. Implement a DFS-based solution to find the connected components of a graph.

# In this implementation, the Graph class has methods to add edges (add_edge) and find connected 
# components using DFS (find_connected_components_dfs). The dfs_util function is a recursive helper function that performs the DFS traversal.
#  For each unvisited node, it starts a new connected component and explores all the nodes in that component.

# The example usage demonstrates creating a simple undirected graph and finding its connected components. 
# You can modify the add_edge calls to create your own graph for testing. The output will display the connected components of the graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def find_connected_components_dfs(self):
        connected_components = []
        visited = set()

        def dfs_util(node, component):
            visited.add(node)
            component.append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor, component)

        for node in self.graph:
            if node not in visited:
                component = []
                dfs_util(node, component)
                connected_components.append(component)

        return connected_components

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)

connected_components = g.find_connected_components_dfs()

print("Connected Components:")
for component in connected_components:
    print(component)

print(g.graph)