"""
Solution to problem 2
https://projecteuler.net/problem=2
"""
from typing import Iterator


def fibonacci_sequence(ceil: int) -> Iterator[int]:
    """Get an iterator of the numbers in the fibonacci sequence below ceil."""
    prev = 0
    curr = 1

    next_val = prev + curr
    while next_val < ceil:
        yield next_val

        prev = curr
        curr = next_val
        next_val = prev + curr

def is_even(n: int) -> bool:
    """Determine if a number is even"""
    return n % 2 == 0

def even_fibonacci_sequence(ceil: int) -> Iterator[int]:
    """Return even numbers from the fibonacci sequence below ceil."""
    return (n for n in fibonacci_sequence(ceil) if is_even(n))

def get_sum_of_even_fibo_numbers_below(ceil: int) -> int:
    return sum(even_fibonacci_sequence(ceil))

if __name__ == '__main__':
    print(get_sum_of_even_fibo_numbers_below(4_000_000))
