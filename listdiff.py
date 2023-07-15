DIFF = 5
TEST_CASES = [
    {"lst": [1, 2, 3, 4, 0, 6, 7, 8, 9], "expected": False},
    {"lst": [1, 2, 3, 3, 2, 1, 0], "expected": True},
    {"lst": [0], "expected": True}
]


def is_list_in_diff(lst: list[int], base: int, diff: int) -> bool:
    return all([abs(base - x) < diff for x in lst])


def main() -> None:
    for each in TEST_CASES:
        lst = each["lst"]
        if len(lst) == 0:
            print("Error: Empty list found. Skipping.")
        else:
            idx_mid = len(lst) // 2
            mid = lst[idx_mid]
            result_left = is_list_in_diff(lst[:idx_mid], mid, DIFF)
            result_right = is_list_in_diff(lst[idx_mid + 1:], mid, DIFF)
            result = result_left and result_right
            assert(result == each["expected"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")