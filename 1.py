"""
Solution to problem 1
https://projecteuler.net/problem=1
"""
from typing import List


def sum_of_multiples_below(multiples: List[int], below: int) -> int:
    """Get the sum of of all multiples of multiples less than below.

    Args:
        multiples: the values to use multiples of
        below: the upper value that multiples should not exceed

    Returns:
        The sum of all multiples less than below
    """
    seen = set()
    total = 0

    for multiple in multiples:
        multiplier = 1
        val = multiplier * multiple

        while val < below:
            if val not in seen:
                seen.add(val)
                total += val
            val = multiplier * multiple
            multiplier += 1

    return total

print(sum_of_multiples_below([3, 5], 1000))
