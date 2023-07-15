"""
https://www.reddit.com/r/pythonhelp/comments/vgxklf/simple_read_replace_write_html_file/
"""

PATH_FILE = "./resources/sample.html"
REPLACE_WHAT = "Ping List"
REPLACE_WITH = "NOC"


def main() -> None:
    with open(PATH_FILE) as f:
        content = f.read()

    data = content.replace(REPLACE_WHAT, REPLACE_WITH)

    with open(PATH_FILE, "w") as f:
        f.write(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
