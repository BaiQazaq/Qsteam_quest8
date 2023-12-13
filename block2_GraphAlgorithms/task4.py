# 4. Implement a method to detect a cycle in a directed graph.

# Detecting a cycle in a directed graph can be done using Depth-First Search (DFS) as well. 
# During DFS traversal, if you encounter a node that is already in the current recursion stack, then a cycle exists. 

# In this implementation, the Graph class is similar to the undirected graph version, 
# with additional checks for the presence of the current vertex in the recursion stack. 
# The is_cyclic_util function is a recursive utility function that performs DFS and returns True if a cycle is detected.

# The example usage demonstrates creating a simple directed graph and checking whether it contains a cycle. 
# You can modify the add_edge calls to create your own graph for testing.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, recursion_stack):
        visited[v] = True
        recursion_stack[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor]:
                # If the neighbor is in the current recursion stack, a cycle exists
                return True

        recursion_stack[v] = False
        return False

    def is_cyclic(self):
        # Initialize the visited and recursion_stack arrays
        visited = {vertex: False for vertex in self.graph}
        recursion_stack = {vertex: False for vertex in self.graph}

        # Perform DFS traversal for each unvisited vertex
        for vertex in self.graph:
            if not visited[vertex]:
                if self.is_cyclic_util(vertex, visited, recursion_stack):
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
