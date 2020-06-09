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
    max_prime = 0

    # divide out 2
    while num % 2 == 0:
        num = int(num / 2)
        max_prime = 2

    # the highest possible prime factor
    max_factor = int(math.sqrt(num) + 1)

    # counter for going through candidate prime numbers
    i = 3
    while max_prime < max_factor and num > 1:
        while num % i == 0:
            max_prime = i
            num = int(num / i)
            max_factor = int(math.sqrt(num) + 1)
        i += 2

    if num == 1:
        return max_prime

    return num


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
