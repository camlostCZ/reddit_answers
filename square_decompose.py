"""
Square Decompose
https://www.reddit.com/r/learnpython/comments/oyhezt/help_me_with_this_problem_please/
"""

import itertools


def decompose(n: int) -> list[int]:
    """
    Decompose integer so that its square is equal to sum of squares
    of the resulting numbers.

    Args:
        n (int): Source integer.

    Returns:
        list[int]: List of numbers
    """

    square = n ** 2
    lst = []
    for idx in range(2, n):
        lst.extend(itertools.combinations(range(1, n), idx))
    result = [x for x in lst if sum(([y ** 2 for y in x])) == square]
    return sorted(result, key=lambda x: x[-1], reverse=True)


def main():
    """Main function.
    """
    
    for item in decompose(26):
        print(", ".join(map(str, item)))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
