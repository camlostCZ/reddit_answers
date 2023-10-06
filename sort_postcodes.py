"""
https://www.reddit.com/r/learnpython/comments/1715jov/sorting_post_codes/

Requires: Python 3.9+
"""

import re

from pprint import pprint


SAMPLE = ["DE1","DE10","DE11","DE12","DE2","DE3","DE4","B4","B5","B6"]


def sort_postal_codes(codes: list[str]) -> list[str]:
    rex = re.compile(r"^([^\d]+)(.*)$")

    # Split codes into individual lists
    data = {}
    for each in codes:
        if (m := rex.search(each)):
            key, value = m.groups()
            if key in data:
                data[key].append(int(value))
            else:
                data[key] = [int(value)]

    # Sort the lists
    for key in data:
        data[key] = sorted(data[key])

    # Build a new, sorted list
    result = []
    for key in sorted(data.keys()):
        for each in data[key]:
            result.append(f"{key}{each}")
    return result


def main():
    codes = sort_postal_codes(SAMPLE)
    pprint(codes)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by the user.")
