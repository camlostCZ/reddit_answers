"""
https://www.reddit.com/r/learnpython/comments/mei8nd/i_need_explain_for_this_task/
"""

def print_name(name: str, count: int = 1):
    if count > 0:
        print_name(name, count - 1)
        print(f"{count}: {name}")


def main():
    print_name("Invalid", -1)
    print_name("Also Invalid", 0)
    print_name("Once")
    print_name("John IV.", 4)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")