#!/usr/bin/python3
"""
0-rain module

Provides a function to calculate how much rainwater can be
retained between walls represented by non-negative integer heights.
"""


def rain(walls):
    """
    Calculate the total amount of rainwater retained.

    Args:
        walls (list): List of non-negative integers representing wall heights.

    Returns:
        int: Total units of rainwater retained.

    If the list is empty or too short, returns 0.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Compute max to the left of each position
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Compute max to the right of each position
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Sum trapped water at each position
    total = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level > walls[i]:
            total += water_level - walls[i]

    return total
