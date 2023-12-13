# 2. 

# In this implementation, the factorial_dynamic function uses a list factorial_values to store 
# the factorial values up to the desired number n. 
# It initializes the list with the base case (factorial of 0 is 1), and then iteratively calculates 
# the subsequent factorials using the dynamic programming approach.

# The example usage demonstrates finding the factorial of the number 5. 
# You can replace number with any non-negative integer to find the corresponding factorial. 
# The dynamic programming approach here is more about storing intermediate results than optimizing the computation of factorials, 
# which can be efficiently done using iteration.

def factorial_dynamic(n):
    """
    Compute the factorial of a number using dynamic programming.

    Parameters:
    - n: The number for which to compute the factorial.

    Returns:
    - The factorial of the given number.
    """
    if n < 0:
        return None

    factorial_values = [1] * (n + 1)

    for i in range(2, n + 1):
        factorial_values[i] = i * factorial_values[i - 1]

    return factorial_values[n]

# Example usage:
number = 5
result = factorial_dynamic(number)

print(f"The factorial of {number} is: {result}")
