# 4. Implement a dynamic programming solution for the rod cutting problem.

# In this implementation, the rod_cutting function uses dynamic programming to build a table (dp) where dp[i] 
# represents the maximum obtainable value for a rod of length i. 
# It iterates through each possible rod length and calculates the maximum value by considering all possible cuts.

# The example usage demonstrates finding the maximum obtainable value for a rod of length 4 with given lengths and values. 
# You can replace rod_lengths, rod_values, and rod_length with your own values.

def rod_cutting(lengths, values, n):
    """
    Solve the rod cutting problem using dynamic programming.

    Parameters:
    - lengths: A list of possible rod lengths.
    - values: A list of values corresponding to each rod length.
    - n: The total length of the rod.

    Returns:
    - The maximum obtainable value by cutting up the rod.
    """
    # Initialize a table to store the solutions to subproblems
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_value = float('-inf')
        for j in range(len(lengths)):
            if i >= lengths[j]:
                max_value = max(max_value, values[j] + dp[i - lengths[j]])
        dp[i] = max_value

    return dp[n]

# Example usage:
rod_lengths = [1, 2, 3, 4, 5, 6, 7, 8]
rod_values = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 4

result = rod_cutting(rod_lengths, rod_values, rod_length)

print(f"The maximum obtainable value for a rod of length {rod_length} is: {result}")
