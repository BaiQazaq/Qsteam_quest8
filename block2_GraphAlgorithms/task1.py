# 1. Implement graph representation using an adjacency matrix.

# An adjacency matrix is a common way to represent a graph using a 2D matrix where each cell matrix[i][j] represents 
# whether there is an edge between vertex i and vertex j. For an unweighted graph, the matrix typically contains 0 or 1, 
# # indicating the absence or presence of an edge. For a weighted graph, the matrix may contain the weight of the edge.

# In this implementation, the Graph class has an __init__ method to initialize the number of vertices and create 
# an adjacency matrix filled with zeros. The add_edge method adds an edge between two vertices with an optional weight. 
# The display method prints the adjacency matrix.

# The example usage demonstrates creating a graph with 4 vertices and adding edges between them. 
# The resulting adjacency matrix is displayed. You can modify the vertices and add more edges based 
# on your specific graph requirements.

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, source, destination, weight=1):
        # Add an edge between source and destination with the given weight
        if 0 <= source < self.vertices and 0 <= destination < self.vertices:
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight  # For undirected graph

    def display(self):
        # Display the adjacency matrix
        for row in self.adj_matrix:
            print(row)

# Example usage:
vertices = 4
graph = Graph(vertices)

graph.add_edge(0, 1, 1)
graph.add_edge(0, 2, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 1)

print("Adjacency Matrix:")
graph.display()
