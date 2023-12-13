# 8. Solve the matrix chain multiplication problem using dynamic programming.

# The matrix chain multiplication problem involves finding the most efficient way to multiply 
# a given sequence of matrices, minimizing the total number of scalar multiplications

# In this implementation, the matrix_chain_multiplication function uses dynamic programming to build a 2D table dp, 
# where dp[i][j] represents the minimum number of scalar multiplications needed to multiply matrices from i to j. 
# It iterates through the length of the chain and computes the optimal cost for each subchain.

# The example usage demonstrates finding the minimum number of scalar multiplications needed 
# to multiply matrices with dimensions [10, 30, 5, 60]. You can replace matrix_dimensions with your own list of matrix dimensions.

def matrix_chain_multiplication(dimensions):
    """
    Solve the Matrix Chain Multiplication problem using dynamic programming.

    Parameters:
    - dimensions: A list of dimensions of matrices, where dimensions[i] represents the number of rows of matrix i
                  and dimensions[i+1] represents the number of columns of matrix i.

    Returns:
    - The minimum number of scalar multiplications needed to multiply the matrices.
    """
    n = len(dimensions) - 1

    # Initialize a table to store the solutions to subproblems
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n-1]

# Example usage:
matrix_dimensions = [10, 30, 5, 60]

result = matrix_chain_multiplication(matrix_dimensions)

print(f"The minimum number of scalar multiplications needed is: {result}")
