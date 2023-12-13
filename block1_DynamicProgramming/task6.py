# 6. Write a dynamic programming solution for the longest common subsequence problem.

# The Longest Common Subsequence (LCS) problem involves finding the length of the longest subsequence that is common to two given sequences.

# In this implementation, the longest_common_subsequence function uses dynamic programming to build a 2D table (dp) where dp[i][j] 
# represents the length of the longest common subsequence of the first i elements of sequence X and the first j elements of sequence Y. 
# It iterates through each pair of elements in the sequences, updating the table based on whether the characters match or not.

# The example usage demonstrates finding the length of the Longest Common Subsequence for the given sequences "ABCBDAB" and "BDCAB". 
# You can replace sequence1 and sequence2 with your own sequences.

def longest_common_subsequence(X, Y):
    """
    Solve the Longest Common Subsequence (LCS) problem using dynamic programming.

    Parameters:
    - X: The first sequence.
    - Y: The second sequence.

    Returns:
    - The length of the longest common subsequence.
    """
    m, n = len(X), len(Y)

    # Initialize a table to store the solutions to subproblems
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage:
sequence1 = "ABCBDAB"
sequence2 = "BDCAB"

result = longest_common_subsequence(sequence1, sequence2)

print(f"The length of the Longest Common Subsequence is: {result}")
