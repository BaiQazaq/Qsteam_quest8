# 7. Write a function to print all paths between two vertices in a graph using DFS.

# In this implementation, the Graph class has methods to add edges (add_edge) and print all paths between 
# two vertices using DFS (print_all_paths_dfs). The dfs_util function is a recursive helper function that performs the DFS traversal, 
# and when the destination node is reached, it adds the current path to the result.

# The example usage demonstrates creating a simple undirected graph and printing all paths between two specified vertices. 
# You can modify the add_edge calls to create your own graph for testing. The output will display all paths between the specified vertices.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def print_all_paths_dfs(self, start, end):
        if start not in self.graph or end not in self.graph:
            return []

        def dfs_util(current, path):
            visited.add(current)
            path.append(current)

            if current == end:
                result.append(path.copy())
            else:
                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        dfs_util(neighbor, path)

            path.pop()
            visited.remove(current)

        result = []
        visited = set()
        dfs_util(start, [])
        return result

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

start_node = 0
end_node = 3

all_paths = g.print_all_paths_dfs(start_node, end_node)

print("All Paths between", start_node, "and", end_node, ":")
for path in all_paths:
    print(path)
