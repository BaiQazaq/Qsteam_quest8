# 3. Write a program to detect a cycle in an undirected graph.
# Detecting a cycle in an undirected graph can be done using Depth-First Search (DFS). 
# If, during the DFS traversal, we encounter an already visited node that is not the parent of the current node, 
# then a cycle exists in the graph

# In this implementation, the Graph class has methods to add edges (add_edge), perform DFS traversal (is_cyclic_util), 
# and check for cycles in the graph (is_cyclic). The is_cyclic_util function is a recursive utility 
# function that performs DFS and returns True if a cycle is detected.

# The example usage demonstrates creating a simple undirected graph and checking whether it contains a cycle. 
# You can modify the add_edge calls to create your own graph for testing.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, v):
                    return True
            elif parent != neighbor:
                # If the neighbor is visited and not the parent of the current node, a cycle exists
                return True

        return False

    def is_cyclic(self):
        # Initialize the visited array
        visited = {vertex: False for vertex in self.graph}

        # Perform DFS traversal for each unvisited vertex
        for vertex in self.graph:
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, -1):
                    return True

        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
