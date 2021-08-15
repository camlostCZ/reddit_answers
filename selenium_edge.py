"""
Selenium Test
https://www.reddit.com/r/learnpython/comments/p2r9mv/trouble_getting_edge_to_run_headless/
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge, EdgeOptions

from typing import Generator


PATH_BROWSER = "resources/msedgedriver.exe"


def main() -> None:
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    driver = Edge(executable_path=PATH_BROWSER, options=options)

    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")