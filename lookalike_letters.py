"""
https://www.reddit.com/r/learnpython/comments/150pyz8/replacing_letters_with_lookalike_letters/
"""

import random

CHAR_MAP = {
    "a": "аạąäàáą",
    "e": "èéêë",
    "i": "ìíîï",
    "o": "òóôõö",
    "u": "ùúûü",
    "y": "ýÿ",
    "l": "ł",
    "r": "řȑȓ"
}


def replace_lookalike_chars(txt: str, map: dict[str, str]) -> str:
    result = ""
    for ch in txt:
        letter = ch
        if ch in map:   # Do we have a replacement?
            letter = random.choice(map[ch])
        result += letter
    return result


def main() -> None:
    msg = input("Enter a message: ")
    result = replace_lookalike_chars(msg, CHAR_MAP)
    print(f"Result:\n{result}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
