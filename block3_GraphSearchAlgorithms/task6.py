# # 6. Implement an algorithm to find the level of each node in a graph using BFS.
# In this implementation, the Graph class has methods to add edges (add_edge) and find the levels of each node using BFS (find_levels_bfs).
# The BFS algorithm is used to traverse the graph, and the level of each node is updated during the traversal.

# The find_levels_bfs function returns a dictionary where keys are nodes, and values are their respective levels. 
# The example usage demonstrates creating a simple undirected graph and finding the levels of each node starting from a specified node. 
# You can modify the add_edge calls to create your own graph for testing. The output will display the level of each node.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph

    def find_levels_bfs(self, start):
        if start not in self.graph:
            return None

        levels = {}
        visited = set()
        queue = deque([(start, 0)])  # (node, level)
        visited.add(start)

        while queue:
            current_node, level = queue.popleft()
            levels[current_node] = level

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))
                    visited.add(neighbor)

        return levels

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)

start_node = 0

node_levels = g.find_levels_bfs(start_node)

print("Node Levels:")
for node, level in node_levels.items():
    print(f"Node {node}: Level {level}")
