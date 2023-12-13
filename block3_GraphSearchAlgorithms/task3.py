# 3. Write a program to find the number of islands using DFS in a matrix.
# Finding the number of islands in a matrix using Depth-First Search (DFS) is a common problem. 
# An island is a group of connected 1s (representing land) in the matrix.

# In this implementation, the num_islands function takes a matrix as input and uses DFS to visit all the connected land 
# cells of each island. It marks the visited cells with "0" to avoid counting the same island multiple times.

# The example usage demonstrates creating a matrix and finding the number of islands. 
# You can modify the matrix variable to test with different input. The output will display the number of islands in the matrix.

def num_islands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    count = 0

    def dfs(row, col):
        if 0 <= row < rows and 0 <= col < cols and matrix[row][col] == "1":
            matrix[row][col] = "0"  # Mark the current cell as visited
            # Explore neighbors
            # print(f"1. row - 1 = {row - 1}, col = {col}")
            dfs(row - 1, col)
            # print(f"2. row + 1 = {row + 1}, col = {col}")
            dfs(row + 1, col)
            # print(f"3. row = {row}, col - 1 = {col - 1}")
            dfs(row, col - 1)
            # print(f"4. row = {row}, col + 1 = {col + 1}")
            dfs(row, col + 1)

    for row in range(rows):
        for col in range(cols):
            # print(f"matrix[{row}][{col}] - {matrix[row][col]}")
            if matrix[row][col] == "1":
                count += 1
                # print(f"matrix[{row}][{col}] - {matrix[row][col]}")
                dfs(row, col)

    return count

# Example usage:
matrix = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

island_count = num_islands(matrix)
print(f"Number of islands: {island_count}")
