# # 5. Write a program to check for a path between two nodes in a graph using BFS.
# In this implementation, the Graph class has methods to add edges (add_edge) and check for a path between two nodes using BFS (has_path_bfs). 
# The BFS algorithm is used to explore the graph from the start node, and if the end node is reached during the traversal, 
# it returns True. Otherwise, it returns False.

# You can modify the add_edge calls to create your own graph for testing. 
# The output will indicate whether there is a path from the start node to the end node.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def has_path_bfs(self, start, end):
        if start not in self.graph or end not in self.graph:
            return False

        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current_node = queue.popleft()

            if current_node == end:
                return True

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return False

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

start_node = 0
end_node = 3

has_path = g.has_path_bfs(start_node, end_node)

if has_path:
    print(f"There is a path from {start_node} to {end_node}.")
else:
    print(f"There is no path from {start_node} to {end_node}.")
