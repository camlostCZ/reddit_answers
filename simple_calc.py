"""
https://www.reddit.com/r/learnpython/comments/ts9pe9/need_help/
"""

from typing import Optional


VALID_OPERATORS = "+-*/"


def read_input() -> tuple[str, Optional[int], Optional[int]]:
    """
    Read user input. Try to parse it as:
    <int> <operator> <int>

    If a single dot ('.') is entered, it's a valid input with the meaning
    of quit the program.

    Returns:
        Return a tuple of operator and numbers.
    """
    data = input("Calculator:  ")

    result = (None, None, None)
    if data == ".":
        result = (".", None, None)
    for op in VALID_OPERATORS:
        if op in data:
            parts = data.split(op)
            result = (op, ) + tuple(parts)
            # Only 1 operator allowed, so we can end the loop
            break
    return result


def main() -> None:
    while True:
        op, val1, val2 = read_input()
    
        # Based on operator, perform the appropriate operation
        if op == ".":
            break  # Jump out of the loop to quit

        try:
            result = 0
            num1 = int(val1)
            num2 = int(val2)
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 // num2
            else:
                print(f"ERROR: Invalid operation '{op}'")

            # Print the result
            print(f"         ->  {result}")
        except ValueError:
            print(f"ERROR: Invalid input (multiple operators? non-integers?)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
