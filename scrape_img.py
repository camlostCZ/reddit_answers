"""
https://www.reddit.com/r/learnpython/comments/p4s9sx/can_someone_help_me_debug_my_code_i_am_building/
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions

from typing import Generator


URL_SEARCH = "https://www.istockphoto.com/cs/search/2/image?family=creative&phrase="
CLASS_MASK = "MosiacAsset-module__thumb_"
PATH_BROWSER = "resources/msedgedriver.exe"


def init_browser(driver_path: str, headless: bool = True) -> webdriver:
    options = EdgeOptions()
    options.use_chromium = True
    if headless:
        options.add_argument('headless')
        options.add_argument('disable-gpu')
    return Edge(executable_path=driver_path, options=options)


def search_site(phrase: str, search_url: str, driver: webdriver) -> Generator[str, None, None]:
    query = phrase.replace(' ', '%20')
    url = f"{search_url}{query}"
    driver.get(url)

    xpath = f"//img[starts-with(@class, '{CLASS_MASK}')]"
    try:
        for elem in driver.find_elements_by_xpath(xpath):
            yield elem.get_attribute("src")
    except Exception as e:
        print(e)


def main() -> None:
    driver = init_browser(PATH_BROWSER)

    urls = search_site("lion", URL_SEARCH, driver)
    for item in urls:
        print(f"Found image URL: {item}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
