"""
https://www.reddit.com/r/learnpython/comments/wy5wba/how_to_count_occurrences_of_a_word_in_a_list/
"""

from collections import Counter
import re

TOP_COUNT = 26
TITLE_PATTERN = r"<h3 [^>]+>([^<]+)<\/h3>"
PATH_SOURCE = "sample.html"


def load_title(path: str, pattern: str = TITLE_PATTERN):
    pat_space = re.compile(r"\s+", re.MULTILINE)
    with open(path, encoding="utf8") as f:
        data = f.read()
        matches = re.finditer(pattern, data, re.MULTILINE)

        for m in matches:
            title = m.group(1)
            result = pat_space.sub(" ", title).strip().lower()
            yield result


def text_to_words(txt: str):
    pat_delim = re.compile(r"\b")
    return pat_delim.split(txt)


def main() -> None:
    titles = load_title(PATH_SOURCE)
    words = text_to_words(" ".join(titles))

    word_counter = Counter(words)
    for o, n in word_counter.most_common(TOP_COUNT):
        print(f"{o}:  {n}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
