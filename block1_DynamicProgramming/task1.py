# 1. Implement Fibonacci series using dynamic programming.

# In this implementation, the fibonacci_dynamic function uses a list fib to store the Fibonacci numbers up to the desired index n. 
# It initializes the list with base cases (0 and 1),
# and then iteratively calculates the subsequent Fibonacci numbers using the dynamic programming approach.

# The example usage demonstrates finding the 7th Fibonacci number. 
# You can replace n with any non-negative integer to find the corresponding Fibonacci number. 
# Dynamic programming significantly reduces redundant calculations compared to the naive recursive approach, 
# making it more efficient for larger values of n.

def fibonacci_dynamic(n):
    """
    Compute the nth Fibonacci number using dynamic programming.

    Parameters:
    - n: The index of the desired Fibonacci number.

    Returns:
    - The nth Fibonacci number.
    """
    fib = [0] * (n + 1)

    # Base cases
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example usage:
n = 7
result = fibonacci_dynamic(n)

print(f"The {n}-th Fibonacci number is: {result}")
