"""
Solution to problem 3
https://projecteuler.net/problem=3
"""

import math
from typing import Optional

def largest_prime_factor(n: int) -> Optional[int]:
    """Get the largest prime factor of n."""
    # running number as we divide factors out of it
    num = n

    # handle the case where n is prime
    max_prime = n

    # go through 2
    while num % 2 == 0:
        max_prime = 2
        num = int(num / 2)

    # go through odd numbers
    for i in range(3, int(math.sqrt(num) + 1), 2):
        while num % i == 0:
            max_prime = i
            num = int(num / i)

    return max_prime


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
