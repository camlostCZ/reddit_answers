"""
https://www.reddit.com/r/pythonhomework/comments/urqmff/need_help_writing_a_number_counter_program/
"""

import random

from collections import Counter


POPULATION_SIZE = 500
MIN_NUMBER = 0
MAX_NUMBER = 99


def generate_population(min_n: int, max_n: int, size: int) -> list[int]:
    result = []
    for _ in range(size):
        result.append(random.randint(min_n, max_n))
    return result


def main() -> None:
    numbers = generate_population(MIN_NUMBER, MAX_NUMBER, POPULATION_SIZE)
    counts = Counter(numbers)
    missing = set(range(MIN_NUMBER, MAX_NUMBER + 1)) - set(counts.keys())

    print("Number of occurences of individual numbers:")
    for k in sorted(counts.keys()):
        print(f"{k:2}:  {counts[k]}")

    print("\n\nMissing numbers:")
    print(", ".join(map(str, list(missing))))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
