"""
https://www.reddit.com/r/learnpython/comments/q4hz6c/so_im_a_little_stuck_any_advice_12ampm_input/
"""

def time12h_to_24h(time_str: str) -> int:
    afternoon = time_str[-2:].lower() == "pm"
    hours = int(time_str[:-2]) % 12
    return int(afternoon) * 12 + hours


def main() -> None:
    assert(time12h_to_24h("12am") == 0)
    assert(time12h_to_24h("2am") == 2)
    assert(time12h_to_24h("12pm") == 12)
    assert(time12h_to_24h("11pm") == 23)
    print("oll korrekt!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
