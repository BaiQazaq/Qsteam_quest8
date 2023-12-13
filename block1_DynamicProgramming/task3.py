# 3. Solve the coin change problem with dynamic programming

# In this implementation, the coin_change_ways function uses dynamic programming to build a table (dp) where dp[i] 
# represents the number of ways to make change for the amount i. It iterates through each coin denomination and 
# updates the table based on the number of ways to make change using the current coin.

# The example usage demonstrates finding the number of ways to make change for the amount 5 using coin 
# denominations [1, 2, 5]. You can replace coin_denominations and target_amount with your own values.

def coin_change_ways(coins, amount):
    """
    Solve the coin change problem using dynamic programming.

    Parameters:
    - coins: A list of coin denominations.
    - amount: The target amount for which to make change.

    Returns:
    - The number of ways to make change for the given amount.
    """
    # Initialize a table to store the solutions to subproblems
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make change for amount 0 (no coins used)

    # Iterate through each coin denomination
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Example usage:
coin_denominations = [1, 2, 5]
target_amount = 5

result = coin_change_ways(coin_denominations, target_amount)

print(f"There are {result} ways to make change for {target_amount}.")
