"""
https://www.reddit.com/r/learnpython/comments/uuf3bu/can_i_print_something_only_if_it_meets_a_condition/
"""

from string import ascii_uppercase


def get_upper_triangle(letter: str) -> list[str]:
    result = []
    size = (ord(letter) - ord('A')) + 1
    for i, item in enumerate(ascii_uppercase[:size]):
        line = [' '] * size
        line[size - i - 1] = item

        # Join line and tail of the same line reversed
        # Example: "..A" + ".." -> "..A.."
        # Example: ".B." + "B." -> ".B.B."
        result.append("".join(line + list(reversed(line))[1:]))
    return result


def get_diamond(letter: str) -> list[str]:
    triangle = get_upper_triangle(letter)
    return triangle + list(reversed(triangle))[1:]


def main() -> None:
    letter = input("Enter a letter: ").upper()
    for line in get_diamond(letter):
        print(line)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
