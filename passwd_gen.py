"""
https://www.reddit.com/r/learnpython/comments/phitz1/repeating_numbers/
"""

import random
from typing import Union


def generate_password(size: int, pool: list[Union[int, str]]) -> str:
    result = ""
    i = 0
    while i < size:
        char = random.choice(pool)
        if i == 0 or char != result[i - 1]:
            result += str(char)
            i += 1
    return result


def main() -> None:
    pool_digits = list(range(10))
    pool_chars = [chr(ord('a') + x) for x in range(26)]
    passwd = generate_password(13, pool_digits)
    print(f"Password: '{passwd}'")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
