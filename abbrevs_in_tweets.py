"""
https://www.reddit.com/r/learnpython/comments/150tahf/help_with_tweet_decoder/
"""

import re


MAP_ABBREVIATIONS = {
    "lol": "laughing out loud",
    "brb": "be right back",
    "afaik": "after all I know",
    "tbh": "to be honest",
    "idk": "I don't know",
    "asap": "as soon as possible"
}


def search_abbreviation(txt: str, map: dict[str, str]) -> list[tuple[str, str]]:
    result = []

    # Tokenize text
    words = re.split(r"\b", txt.lower())
    for each in words:
        if each in map:
            result.append((each, map[each]))
    return result


def main() -> None:
    tweet = input("Enter a tweet message (max. 160 chars):\n")
    abbrevs = search_abbreviation(tweet, MAP_ABBREVIATIONS)

    print("\nAbbreviations discovered:")
    for (abb, meaning) in abbrevs:
        print(f"  - {abb}: {meaning}")


if __name__ == "__main__":
    main()
