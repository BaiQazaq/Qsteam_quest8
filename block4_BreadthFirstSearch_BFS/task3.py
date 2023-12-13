# 3. Implement a BFS solution to find the minimum number of edges between two nodes.

# In this implementation, the Graph class has methods to add edges (add_edge) and find the minimum number 
# of edges using BFS (min_edges_bfs). The BFS algorithm is used to explore the graph level by level,
# and when the destination node is reached, the number of edges is returned.

# The example usage demonstrates creating a simple undirected graph and finding the minimum number of edges between two specified nodes. 
# You can modify the add_edge calls to create your own graph for testing. 
# The output will display the minimum number of edges or indicate if no path is found.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def min_edges_bfs(self, start, end):
        if start not in self.graph or end not in self.graph:
            return None

        visited = set()
        queue = deque([(start, 0)])  # (node, edges)

        while queue:
            current_node, edges = queue.popleft()

            if current_node == end:
                return edges

            if current_node not in visited:
                visited.add(current_node)

                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, edges + 1))

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

min_edges = g.min_edges_bfs(start_node, end_node)

if min_edges is not None:
    print(f"Minimum number of edges between {start_node} and {end_node}: {min_edges}")
else:
    print(f"No path between {start_node} and {end_node} found.")

print(g.graph)