#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Factorize the number and sum up the factors
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
