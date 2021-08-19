"""
https://www.reddit.com/r/learnpython/comments/p6fcm9/please_help_been_stuck_on_this_for_2_days/
"""

from typing import Generator

SOURCE_PATH = "./arg-covid19.csv"


def parse_src_file(path: str, delimiter=',') -> Generator[str, None, None]:
    with open(path) as src:
        for line in src:
            record = [x.strip() for x in line.replace('"', '').split(delimiter)]
            if len(record) == 5:
                yield record


def main():
    data = parse_src_file(SOURCE_PATH)
    for item in data:
        country, code, day, year, count = item
        print(f"{country},{code},{day} {year},{count}")


if __name__ == "__main__":
    main()
