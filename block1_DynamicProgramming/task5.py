# 5. Solve the 0-1 knapsack problem using dynamic programming.

# In this implementation, the knapsack function uses dynamic programming to build a 2D table (dp) where dp[i][w] 
# represents the maximum value that can be obtained with the first i items and a knapsack capacity of w. 
# It iterates through each item and capacity combination to fill the table and find the optimal solution.

# The example usage demonstrates finding the maximum value for a given knapsack capacity with the given weights and values. 
# You can replace weights, values, and knapsack_capacity with your own values.

def knapsack(weights, values, capacity):
    """
    Solve the 0-1 knapsack problem using dynamic programming.

    Parameters:
    - weights: A list of weights of the items.
    - values: A list of values of the items.
    - capacity: The maximum weight capacity of the knapsack.

    Returns:
    - The maximum value that can be obtained within the given capacity.
    """
    n = len(weights)

    # Initialize a table to store the solutions to subproblems
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is less than or equal to the capacity
            if weights[i - 1] <= w:
                # Choose the maximum value between including and excluding the current item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight is greater than the capacity, exclude it
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
knapsack_capacity = 5

result = knapsack(weights, values, knapsack_capacity)

print(f"The maximum value for the given knapsack capacity is: {result}")
