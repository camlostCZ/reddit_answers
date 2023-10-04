import requests

from lxml import etree


URL = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"

HEADERS = {
    "user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
}


def stringify_children(node) -> str:
    """
    https://stackoverflow.com/a/24151860

    Args:
        node (lxml.ElementTree): HTML element

    Returns:
        Text representation of node.
    """
    s = node.text
    if s is None:
        s = ''
    for child in node:
        s += etree.tostring(child, encoding='unicode')
    return s


def main() -> None:
    r = requests.get(URL)
    tree = etree.fromstring(r.content, parser=etree.HTMLParser())

    try:
        el_table = tree.xpath("//th/a[contains(@title, 'Summer Olympic Games')]/ancestor::table")[0]
        print(stringify_children(el_table))
    except IndexError:
        print("Error: Table was not found.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by the user.")
