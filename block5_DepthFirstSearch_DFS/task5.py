# 5. Implement a method to find if a graph is connected using DFS.

# To determine if a graph is connected using Depth-First Search (DFS), 
# you can perform a DFS traversal from a starting node and check if all nodes are visited. 
# If all nodes are visited, the graph is connected; otherwise, it is not.

# In this implementation, the Graph class has methods to add edges (add_edge) and 
# check if the graph is connected using DFS (is_connected_dfs). 
# The dfs_util function is a recursive helper function that performs the DFS traversal starting from an arbitrary node.

# The example usage demonstrates creating a connected graph and a disconnected graph, 
# and then checking if they are connected using the is_connected_dfs method. 
# The output will indicate whether each graph is connected or not.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def is_connected_dfs(self):
        if not self.graph:
            return False  # An empty graph is not connected

        visited = set()

        def dfs_util(node):
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_util(neighbor)

        start_node = next(iter(self.graph))  # Start DFS from an arbitrary node
        dfs_util(start_node)

        # Check if all nodes are visited
        return len(visited) == len(self.graph)

# Example usage:
g_connected = Graph()
g_connected.add_edge(0, 1)
g_connected.add_edge(0, 2)
g_connected.add_edge(1, 2)

g_disconnected = Graph()
g_disconnected.add_edge(0, 1)
g_disconnected.add_edge(2, 3)

print("Is the connected graph connected?", g_connected.is_connected_dfs())
print("Is the disconnected graph connected?", g_disconnected.is_connected_dfs())
