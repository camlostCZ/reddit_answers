"""
Trailing Zeroes in Factorial
https://www.reddit.com/r/learnpython/comments/p5glzg/factorial_trailing_zeros_spoj_nzec_error/
"""

import math


def trailing0_fact(n: int) -> int:
    result = 0
    if n > 4:
        power = int(math.log(n, 5))
        result = 0
        for i in range(1, power + 1):
            result += n // (5 ** i)
    return result
    

def main() -> None:
    assert(trailing0_fact(0) == 0)
    assert(trailing0_fact(5) == 1)
    assert(trailing0_fact(149) == 35)
    assert(trailing0_fact(1051) == 261)
    print("All OK")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
