# 7. Implement a program for the longest increasing subsequence.

# In this implementation, the longest_increasing_subsequence function uses dynamic programming to build an array dp where dp[i] 
# represents the length of the longest increasing subsequence ending at index i. 
# It iterates through each pair of indices in the array, updating the table based on whether 
# the element at the current index is greater than the element at the previous index.

# The example usage demonstrates finding the length of the Longest Increasing Subsequence 
# for the given sequence [10, 22, 9, 33, 21, 50, 41, 60, 80]. You can replace sequence with your own array.

def longest_increasing_subsequence(nums):
    """
    Solve the Longest Increasing Subsequence (LIS) problem using dynamic programming.

    Parameters:
    - nums: The input array.

    Returns:
    - The length of the longest increasing subsequence.
    """
    if not nums:
        return 0

    n = len(nums)

    # Initialize a table to store the solutions to subproblems
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
sequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]

result = longest_increasing_subsequence(sequence)

print(f"The length of the Longest Increasing Subsequence is: {result}")
