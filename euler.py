"""
https://www.reddit.com/r/pythonhelp/comments/y2zfep/since_my_coding_instructor_called_the_q_dumb_and/
"""

from fractions import Fraction
from math import factorial


def compute(n: int) -> Fraction:
    result = Fraction(1, 1)
    for i in range(2, n + 1):
        result = result + Fraction(1, factorial(i))
    return result


def main():
    for x in range(1, 25):
        result = compute(x)
        print(f"{x} -> {float(result)}")


main()
