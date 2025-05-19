#!/usr/bin/python3
"""
Defines a function minOperations to calculate the minimum operations
needed to achieve exactly n 'H' characters in a text file using only
Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to get n 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible.
    """
    if n <= 1:
        return 0  # If n is less than or equal to 1, it's impossible to achieve

    operations = 0
    factor = 2

    # Factorize n and accumulate the sum of factors as the number of operations
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
