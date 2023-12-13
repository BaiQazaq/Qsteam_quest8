# 9. Write a function to perform topological sorting in a directed graph.

# Topological sorting is an ordering of vertices in a directed graph such that for every directed edge u -> v, 
# vertex u comes before v in the ordering

# In this implementation, the Graph class has methods to add edges (add_edge) and perform topological sorting (topological_sort). 
# The dfs function performs Depth-First Search to visit nodes and add them to the stack in reverse order.

# The example usage demonstrates creating a simple directed acyclic graph (DAG) and performing topological sorting. 
# You can modify the add_edge calls to create your own DAG for testing. 
# The output will display the topological ordering of the vertices.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        def dfs(node):
            print("node - ",node)
            nonlocal visited, stack
            visited[node] = True
            for neighbor in self.graph[node]:
                print("neighbor", neighbor)
                print("***", bool(visited[neighbor]))
                if not visited[neighbor]:
                    print("+++")
                    dfs(neighbor)
            stack.append(node)

        visited = {node: False for node in self.graph}
        stack = []

        for node in self.graph:
            if not visited[node]:
                dfs(node)

        return stack[::-1]

# Example usage:
g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

topological_order = g.topological_sort()

print("Topological Sorting:")
print(topological_order)
