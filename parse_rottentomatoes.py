"""
https://www.reddit.com/r/learnpython/comments/u9xrco/struggling_scraping_and_getting_the_information/
"""

import enum
import requests
from bs4 import BeautifulSoup, ResultSet, Tag


URL = "https://www.rottentomatoes.com/top/bestofrt/"
TOP = 3  # How many movies should be displayed


class RottenTomatoesError(RuntimeError):
    pass


def parse_movie_row(row: Tag) -> dict[str]:
    KEYS = ["rank", "rating", "title", "reviews"]
    result = {}
    cells = row.find_all("td")
    if len(cells) == 4:
        for i, key in enumerate(KEYS):
            result[key] = cells[i].text.strip()
    return result


def load_movie_table(url: str) -> list[dict[str]]:
    page = requests.get(URL)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find("table", class_="table")
        if table:
            rows = table.find_all("tr")
            for each in rows:
                movie_info = parse_movie_row(each)
                if len(movie_info) == 4:
                    yield movie_info
        else:
            raise RottenTomatoesError("Requested HTML element not found.")
    else:
        raise RottenTomatoesError(f"Unable to load the page. HTTP code {page.status_code}")


def main() -> None:
    try:
        data = load_movie_table(URL)
        rank = 1
        for item in data:
            if rank > TOP:
                break
            print(item)
            rank += 1
    except RottenTomatoesError as e:
        print(f"Error: {e}")
    except requests.exceptions.ConnectionError:
        print(f"Error: Unable to connect to {URL}.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
