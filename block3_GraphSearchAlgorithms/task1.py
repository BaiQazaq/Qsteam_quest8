# 1. Write a Breadth-First Search(BFS) algorithm for a graph

# In this implementation, the Graph class has methods to add edges (add_edge) and perform Breadth-First Search (bfs). 
# The bfs method takes a starting node as an argument and returns the BFS traversal order as a list.

# The algorithm uses a queue to keep track of nodes to visit next. It starts from the specified node, marks it as visited, 
# and iteratively explores its neighbors, adding them to the queue if they haven't been visited yet. 
# The process continues until the queue is empty.

# The example usage demonstrates creating a simple graph and performing BFS starting from a specific node. 
# You can modify the add_edge calls to create your own graph for testing. The output will display the BFS traversal order.

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = {node: False for node in self.graph}
        result = []

        queue = deque([start])
        visited[start] = True

        while queue:
            current_node = queue.popleft()
            result.append(current_node)

            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return result

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start_node = 2
bfs_result = g.bfs(start_node)

print(f"BFS starting from node {start_node}:")
print(bfs_result)
