"""
https://www.reddit.com/r/learnpython/comments/pgv7dt/adjacent_value_from_next_column/
"""

import csv

FILENAME = "sample.csv"

def main() -> None:
    with open(FILENAME, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            print(f"{row['column 1']}:{row['column 2']}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
