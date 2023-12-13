# 9. Implement the minimum cost path problem in a 2D matrix.

# The minimum cost path problem involves finding the path from the top-left corner to 
# the bottom-right corner of a 2D matrix with the minimum sum of costs.

# In this implementation, the min_cost_path function uses dynamic programming to build a 2D table dp, 
# where dp[i][j] represents the minimum cost of the path from the top-left corner to cell (i, j). 
# It iterates through the matrix, filling in the table by considering the costs of moving either from the top or from the left.

# The example usage demonstrates finding the minimum cost path in a 3x3 matrix. 
# You can replace cost_matrix with your own cost matrix.

def min_cost_path(matrix):
    """
    Solve the Minimum Cost Path problem in a 2D matrix using dynamic programming.

    Parameters:
    - matrix: A 2D matrix where matrix[i][j] represents the cost of moving from cell (i, j) to (i+1, j) or (i, j+1).

    Returns:
    - The minimum cost of the path from the top-left to the bottom-right corner.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])

    # Initialize a table to store the solutions to subproblems
    dp = [[0] * cols for _ in range(rows)]

    # Fill in the first row and first column of the table
    dp[0][0] = matrix[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]

    # Fill in the rest of the table
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])

    return dp[rows-1][cols-1]

# Example usage:
cost_matrix = [
    [1, 3, 1],
    [2, 8, 5],
    [4, 2, 1]
]

result = min_cost_path(cost_matrix)

print(f"The minimum cost of the path is: {result}")

 