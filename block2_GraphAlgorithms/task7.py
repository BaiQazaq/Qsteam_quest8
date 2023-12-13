# 7. Write a program to find all bridges in a given graph.
# # A bridge (or cut-edge) in a graph is an edge that, if removed, increases the number of connected components in the graph.

# In this implementation, the Graph class has methods to add edges (add_edge) and find bridges (find_bridges). 
# The dfs function performs the Depth-First Search to find bridges. 
# The disc_time array stores the discovery time of each vertex, and the low_time array stores the earliest 
# discovered vertex that can be reached from the subtree rooted at that vertex.

# The example usage demonstrates creating a simple undirected graph and finding its bridges. 
# You can modify the add_edge calls to create your own graph for testing. The output will display the bridges in the graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_bridges(self):
        bridges = []
        visited = {node: False for node in self.graph}
        disc_time = {node: float('inf') for node in self.graph}
        low_time = {node: float('inf') for node in self.graph}
        parent = {node: None for node in self.graph}

        def dfs(node):
            nonlocal bridges
            children = 0
            visited[node] = True
            disc_time[node] = self.time
            low_time[node] = self.time
            self.time += 1

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    children += 1
                    parent[neighbor] = node
                    dfs(neighbor)
                    low_time[node] = min(low_time[node], low_time[neighbor])

                    if low_time[neighbor] > disc_time[node]:
                        bridges.append((node, neighbor))

                elif neighbor != parent[node]:
                    low_time[node] = min(low_time[node], disc_time[neighbor])

        for node in self.graph:
            if not visited[node]:
                dfs(node)

        return bridges

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)

bridges = g.find_bridges()

print("Bridges in the graph:")
for bridge in bridges:
    print(bridge)
