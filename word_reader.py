"""
https://www.reddit.com/r/learnpython/comments/v2udf0/help_solving_a_simple_loop_problem_finding_a
"""

TERMINAL_WORD = ""    # If specified, terminates the user input


def main() -> None:
    acc = ""    # Accumulates words entered by the user
    previous_word = "" if TERMINAL_WORD == "" else TERMINAL_WORD
    while True:
        word = input("Enter a word: ")
        if word == previous_word:
            break

        acc = word if acc == "" else f"{acc} {word}"

        if TERMINAL_WORD == "":    # If not using terminal word, update previous_word
            previous_word = word

    print(f"Words as entered by the user:\n{acc}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
