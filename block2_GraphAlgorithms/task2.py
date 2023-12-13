# 2. Implement graph representation using an adjacency list.
# An adjacency list is another common way to represent a graph. 
# In this representation, each vertex has a list of its adjacent vertices. 
# This is particularly useful for sparse graphs where the number of edges is significantly less than the maximum possible edges. 

# In this implementation, the Graph class has an __init__ method to initialize an empty adjacency list using the defaultdict 
# from the collections module. The add_edge method adds an edge between two vertices with an optional weight. 
# The display method prints the adjacency list.

# The example usage demonstrates creating a graph and adding edges between vertices. 
# The resulting adjacency list is then displayed. You can modify the add_edge calls and 
# add more edges based on your specific graph requirements.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, source, destination, weight=1):
        # Add an edge between source and destination with the given weight
        self.adj_list[source].append((destination, weight))
        self.adj_list[destination].append((source, weight))  # For undirected graph

    def display(self):
        # Display the adjacency list
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

# Example usage:
graph = Graph()

graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)

print("Adjacency List:")
graph.display()
