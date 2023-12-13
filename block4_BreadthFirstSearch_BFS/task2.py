# 2. Write a program to find the shortest path in an unweighted graph using BFS.

# In this implementation, the Graph class has methods to add edges (add_edge) and find the shortest path using BFS (shortest_path_bfs). 
# The BFS algorithm is used to explore the graph level by level, and when the destination node is reached, 
# the corresponding path is returned.

# The example usage demonstrates creating a simple undirected graph and finding the shortest path between two specified nodes. 
# You can modify the add_edge calls to create your own graph for testing. 
# The output will display the shortest path or indicate if no path is found.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def shortest_path_bfs(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None

        visited = set()
        queue = deque([(start, [])])  # (node, path)

        while queue:
            current_node, path = queue.popleft()

            if current_node == end:
                return path + [end]

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [current_node]))

        return None  # No path found

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)

start_node = 0
end_node = 4

shortest_path = g.shortest_path_bfs(start_node, end_node)

if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path from {start_node} to {end_node} found.")
