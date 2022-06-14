"""
https://www.reddit.com/r/learnpython/comments/vc5ouw/number_parsing/
"""

import math
import re

NUMBERS_MAP = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
    "hundred": 100,
    "hundreds": 100,
    "thousand": 1000,
    "thousands": 1000,
    "million": 1000000,
    "millions": 1000000
}


class UnknownWordError(IndexError):
    pass


def parse_number_string(
        data: str, 
        mapping: dict[str, int] = NUMBERS_MAP) -> int:
    """
    Parse word numbers to int.
    Example: "two hundred seven" -> 207

    Args:
        data: Number written in words
        mapping: Dictionary used to translate words to values

    Returns:
        Resulting number

    Raises:
        UnknownWordError in case of unknown words
    """
    pattern = re.compile(r"[ -]")
    num_lst = pattern.split(data.lower())

    result = 0
    sub_sum = 0
    for item in num_lst:
        try:
            value = mapping[item]
            if value == 100:
                sub_sum *= value
            elif value != 0:
                zeroes = int(math.log10(value))
                if zeroes > 0 and zeroes % 3 == 0:  # Multiples of 1000
                    result += sub_sum * value
                    sub_sum = 0
                else:
                    sub_sum += value
            else:  # Skip zero
                pass
        except KeyError:
            raise UnknownWordError(f"Unknown word: {item}")
    result += sub_sum

    return result


def main() -> None:
    try:
        assert(parse_number_string("one million two hundred fourteen thousand seven hundred eight") == 1214708)
        assert(parse_number_string("zero thousands four") == 4)
        assert(parse_number_string("zero million") == 0)

        num_str = input("Enter a number by words (ex: twenty one): ")
        number = parse_number_string(num_str)
        print(f"The number is: {number}")
    except UnknownWordError as e:
        print(e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
