# 8. Implement a method to find leaf nodes in a graph using DFS.

# In this implementation, the Graph class has methods to add edges (add_edge) and find leaf nodes using DFS (find_leaf_nodes_dfs). 
# The dfs_util function is a recursive helper function that performs the DFS traversal, 
# and when a leaf node is encountered (a node with no unvisited neighbors), it is added to the leaf_nodes set.

# The example usage demonstrates creating a simple undirected graph and finding the leaf nodes starting from a specified node. 
# You can modify the add_edge calls to create your own graph for testing. The output will display the leaf nodes in the graph.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def find_leaf_nodes_dfs(self, start):
        if start not in self.graph:
            return None

        visited = set()
        leaf_nodes = set()

        def dfs_util(node):
            visited.add(node)
            is_leaf = True

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    is_leaf = False
                    dfs_util(neighbor)

            if is_leaf:
                leaf_nodes.add(node)

        dfs_util(start)
        return leaf_nodes

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)

start_node = 0

leaf_nodes = g.find_leaf_nodes_dfs(start_node)

print("Leaf Nodes in the graph:")
print(leaf_nodes)
