"""
https://www.reddit.com/r/learnpython/comments/16zey6v/iterating_a_list_with_sublist_in_a_dictionary/
"""

from pprint import pprint


DOOR_FEATURE = {
    "e": "DOOR LOCK CONNECTION TO ENGAGEMENT LIGHT",
    "d": "LEAD LINED",
    "g": "ACOUSTIC DOOR SEAL",
    "f": "180 DOOR VIEWER",
    "a": "HERMETICALLY SEALED",
    "c1": "WITH MECHANICAL HOLD-OPEN DEVICE",
}

SAMPLE = ['e', 'd', 'f',['e', 'd', 'f'],'c1', 'a']


def process_list(lst: list[str | list[str]], source: dict[str, str]) -> list[str | list[str]]:
    result = []
    for item in lst:
        try:
            if isinstance(item, list):
                data = process_list(item, source)
            else:
                    data = source[item]
            result.append(data)
        except KeyError:
            # Skip unknown keys
            pass
    return result


def main():
    data = process_list(SAMPLE, DOOR_FEATURE)
    pprint(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by the user.")
