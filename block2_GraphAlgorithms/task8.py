# 8. Implement an algorithm to find articulation points in a graph.

# An articulation point (or cut vertex) in a graph is a vertex whose removal increases the number 
# of connected components in the graph

# In this implementation, the Graph class has methods to add edges (add_edge) and 
# find articulation points (find_articulation_points). The dfs function performs Depth-First Search to find articulation points. 
# The disc_time array stores the discovery time of each vertex, the low_time array stores the earliest discovered vertex that 
# can be reached from the subtree rooted at that vertex, and the children array stores the number of children of each vertex.

# The example usage demonstrates creating a simple undirected graph and finding its articulation points. 
# You can modify the add_edge calls to create your own graph for testing. 
# The output will display the articulation points in the graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_articulation_points(self):
        articulation_points = set()
        visited = {node: False for node in self.graph}
        disc_time = {node: float('inf') for node in self.graph}
        low_time = {node: float('inf') for node in self.graph}
        parent = {node: None for node in self.graph}
        children = {node: 0 for node in self.graph}

        def dfs(node):
            nonlocal articulation_points
            children[node] = 0
            visited[node] = True
            disc_time[node] = self.time
            low_time[node] = self.time
            self.time += 1

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    children[node] += 1
                    parent[neighbor] = node
                    dfs(neighbor)
                    low_time[node] = min(low_time[node], low_time[neighbor])

                    if low_time[neighbor] >= disc_time[node] and parent[node] is not None:
                        articulation_points.add(node)

                    if parent[node] is None and children[node] > 1:
                        articulation_points.add(node)

                elif neighbor != parent[node]:
                    low_time[node] = min(low_time[node], disc_time[neighbor])

        for node in self.graph:
            if not visited[node]:
                dfs(node)

        return articulation_points

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)

articulation_points = g.find_articulation_points()

print("Articulation Points in the graph:")
print(articulation_points)
