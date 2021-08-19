"""
https://www.reddit.com/r/learnpython/comments/p7hw06/whats_wrong_with_my_code/
"""

from itertools import combinations


def find_pairs_equal_to(number: str, lst: list[int]) -> list[tuple[int, int]]:
    result = []
    if len(lst) > 1:
        for idx, x in enumerate(lst):
            for y in lst[idx:]:
                if number - x == y:
                    result.append((x, y))
    return result


def find_pairs_equal_to2(number: int, lst: list[int]) -> list[tuple[int, int]]:
    if len(lst) > 1:
        return [x for x in combinations(lst, 2) if sum(x) == number]
    else:
        return []


def find_pairs_equal_to_OP(number, ln):
    a = []
    for i in ln:
        for j in ln:
            if i != j:
                if (i + j) == number:
                    a.append((i, j))
    return a

def main() -> None:
    lst = [1, 2, 3, 5, 6, 9]
    total = 7
    pairs = find_pairs_equal_to2(total, lst)
    for item in pairs:
        a, b = item
        print(f"({a}, {b})")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
