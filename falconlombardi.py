"""
https://www.reddit.com/r/learnpython/comments/uyhnqg/math_question_involving_products_of_primes/
"""

import operator
import itertools as it

from typing import Callable, Generator, Sequence

import primenums


def get_combinations(
        data: Sequence[int],
        filter: Callable[[int], bool]
        ) -> Generator[list[int], None, None]:

    def _multiply(s: Sequence[int]) -> int:
        result = 0 if len(s) == 0 else 1
        for i in s:
            result *= i
        return result

    lst = list(data)
    for n in range(1, len(lst)):
        for comb in it.combinations(lst[1:], n):
            sample = (2,) + tuple(comb)
            product = _multiply(sample)
            if filter(product):
                yield product, sample


def get_primes(num: int) -> Generator[int, None, None]:
    for i in range(2, int(num ** 0.5) + 1):
        if primenums.is_prime(i):
            yield i


def main() -> None:
    number = int(input("Enter a positive integer: "))
    primes = get_primes(number)

    result = get_combinations(list(primes), 
        filter=lambda x: x < number)

    for p, item in result:
        expression = " * ".join(map(str, item))
        print(f"{expression} = {p}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
