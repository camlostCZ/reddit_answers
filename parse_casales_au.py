"""
https://www.reddit.com/r/learnpython/comments/uf33hg/please_help_me_with_bs4_this_piece_of_code_worked/
"""

import bs4, requests
import re

URL = 'https://www.carsales.com.au/cars/used/toyota/rav4/victoria-state/'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}

MAPPING = [
    ("data-webm-networkid", "id"),
    ("data-webm-bodystyle", "style"),
    ("data-webm-make", "make"),
    ("data-webm-model", "model"),
    ("data-webm-state", "state"),
    ("data-webm-price", "price")
]


def fetch_car_info(elem: bs4.Tag) -> dict[str, str]:
    result = {}

    if (elem_title := c.find("h3", recursive=True)):
        result["title"] = elem_title.text.strip()

    for m in MAPPING:
        if m[0] in elem.attrs:
            result[m[1]] = elem.attrs[m[0]]
    return result


page = requests.get(URL, headers=HEADERS)
page.raise_for_status()
soup = bs4.BeautifulSoup(page.content, 'html.parser')

total_cars = 0
cars = []
for elem in soup.find_all("div", class_="listing-items"):
    cards = elem.find_all("div", class_=re.compile("^listing-item card (topspot|showcase)"))
    for c in cards:
        item = fetch_car_info(c)
        cars.append(item)
        total_cars += 1

print(f"Number of cars: {total_cars}")
for item in sorted(cars, key=lambda x: int(x["price"])):
    print(item)
