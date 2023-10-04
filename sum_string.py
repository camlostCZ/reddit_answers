"""
https://www.reddit.com/r/learnpython/comments/15k8no7/learning_python_with_codewars_and_was_wondering/
"""

TESTS = [
    ("1203", "78", "1281"),
    ("7203", "9978", "17181"),
    ("999", "999", "1998"),
    ("0", "0", "0")
]


def sum_strings(s1: str, s2: str) -> str:
    result = ""
    top_len = max(len(s1), len(s2))
    digits = list(zip(s1.zfill(top_len), s2.zfill(top_len)))
    carry = 0
    for d1, d2 in digits[::-1]: # Common way to reverse a list
        carry, remain = divmod(int(d1) + int(d2) + carry, 10)
        result = str(remain) + result
    result = carry * "1" + result
    return result


def main():
    for num1, num2, result in TESTS:
        total = sum_strings(num1, num2)
        print(f"Computed: {num1} + {num2} = {total} (expected {result})")
        assert total == result


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by the user.")
