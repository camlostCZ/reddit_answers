"""
primenum.py

Basic tools for work with prime numbers.
"""

from functools import cache     # Requires Python 3.9+

PRIME_NUMBERS = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}


@cache
def is_prime(n: int) -> bool:
    """
    Primality test using 6k+-1 optimization.

    Args:
        n: A positive integer

    Returns:
        True if the argument is a prime number, False otherwise.

    Source:
        https://en.wikipedia.org/wiki/Primality_test
    """
    if n <= 3:
        return n > 1
    if not n % 2 or not n % 3:
        return False
    i = 5
    stop = int(n ** 0.5)
    while i <= stop:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


def _test_is_prime():
    for i in range(50):
        if (res := is_prime(i, set())):
            print(f"{i:2} is a prime number.")
