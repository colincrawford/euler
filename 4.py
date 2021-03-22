"""
Solution to problem 4
https://projecteuler.net/problem=4
"""
from typing import Optional
import itertools

def is_palindrome(n: int) -> bool:
    """Determine if a number is a palindrome.

    Args:
        n: The number to evaluate

    Returns:
        Whether or not the number is a palindrome
        ex:
            10001 is a palindrome
            12345 is not a palindrome
    """
    s = str(n)
    return s == s[::-1]

def largest_palindrome(digits: int) -> Optional[int]:
    """Find the largest palindrome product of two numbers digits long.

    Args:
        digits: The max number of digits for each factor
    """
    max_num = int("9" * digits)
    min_num = int("1" + ("0" * (digits - 1)))

    # build a generator for every combo of values with digits
    def i_with_combos(i):
        # we only need to compare i to the numbers below it
        return zip(itertools.repeat(i), range(i, min_num + 1, -1))
    number_combos = map(i_with_combos, range(max_num, min_num + 1, -1))

    max_palindrome = None
    for combo in number_combos:
        for a, b in combo:
            product = a * b
            if not is_palindrome(product):
                continue
            if not max_palindrome or product > max_palindrome:
                max_palindrome = product
            break

    return max_palindrome

if __name__ == '__main__':
    print(largest_palindrome(digits=3))
