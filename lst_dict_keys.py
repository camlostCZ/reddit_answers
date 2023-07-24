"""
https://www.reddit.com/r/learnpython/comments/158a781/efficient_way_to_return_dict_keys_where_last/
"""

from typing import Callable, Generator

SAMPLE = {
    "a": [1, 2 ,3, 1.5],
    "b": [2, 3, 4, 6],
    "c": [7, 4, 5, 1.7],
    "d": [3, 3, 3, 3],
    "e": []
}


def filter_dict(data: dict[str, list[int]], filter: Callable) -> Generator[str, None, None]:
    for key, value in data.items():
        if filter(value):
            yield key


def main():
    # Either this:
    #keys = filter_dict(SAMPLE, lambda x: x and x[-1] < 2)
    # ... or that:
    keys = (x for x, v in SAMPLE.items() if v and v[-1] < 2)

    for each in keys:
        print(each)


if __name__ == "__main__":
    main()
