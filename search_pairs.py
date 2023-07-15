"""
https://www.reddit.com/r/learnpython/comments/p7hw06/whats_wrong_with_my_code/
"""

from itertools import combinations


def find_pairs_equal_to(number: str, lst: list[int]) -> list[tuple[int, int]]:
    """Simple solutions using for loops.

    Args:
        number (int): Sum used to filter results
        lst (list[int]): Source list of integers

    Returns:
        list[tuple[int, int]]: List of pairs sum of which equals to the number given.
    """
    result = []
    if len(lst) > 1:
        for idx, x in enumerate(lst):
            for y in lst[idx:]:
                if number - x == y:
                    result.append((x, y))

        # Or much less readable:
        # result = [(x, y) for idx, x in enumerate(lst) for y in lst[idx:] if x + y == number]
    return result


def find_pairs_equal_to2(number: int, lst: list[int]) -> list[tuple[int, int]]:
    """The solutions using itertools.combinations().

    Args:
        number (int): Sum used to filter results
        lst (list[int]): Source list of integers

    Returns:
        list[tuple[int, int]]: List of pairs sum of which equals to the number given.
    """
    return [x for x in combinations(lst, 2) if sum(x) == number]


def find_pairs_equal_to_OP(number, ln):
    """Original code as posted by the OP. Doesn't work as expected.
    """
    a = []
    for i in ln:
        for j in ln:
            if i != j:
                if (i + j) == number:
                    a.append(min(i, j))
                    a.append(max(i, j))
    print(a)

def main() -> None:
    lst = [1, 2, 3, 5, 6, 9]
    total = 7
    pairs = find_pairs_equal_to(total, lst)
    for item in pairs:
        a, b = item
        print(f"({a}, {b})")

    print("OP version:")
    find_pairs_equal_to_OP(total, lst)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
