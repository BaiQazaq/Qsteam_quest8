# 5. Write a function to check if a graph is bipartite.

# A graph is bipartite if its vertices can be divided into two disjoint sets such that every edge connects a vertex 
# from one set to a vertex from the other set. This property can be checked using Depth-First Search (DFS). 

# In this implementation, the is_bipartite function uses DFS to assign colors to vertices and checks 
# if adjacent vertices have different colors. If an adjacent vertex has the same color as the current vertex, 
# the graph is not bipartite.

# The example usage demonstrates creating a simple graph and checking whether it is bipartite. 
# You can modify the graph dictionary to test other graphs.

from collections import defaultdict

def is_bipartite(graph):
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
            if colors[neighbor] == 0 and not dfs(neighbor, -color):
                return False
        return True

    colors = defaultdict(int)

    for node in graph:
        if colors[node] == 0 and not dfs(node, 1):
            return False

    return True

# Example usage:
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2, 5],
    5: [3, 4]
}

if is_bipartite(graph):
    print("The graph is bipartite.")
else:
    print("The graph is not bipartite.")
