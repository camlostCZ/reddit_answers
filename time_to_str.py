"""
https://www.reddit.com/r/pythonhelp/comments/159mhua/can_anyone_please_explain_whats_wrong_with_my_code/
"""

TESTS = [
    (30, "30s"),
    (60, "1m"),
    (90, "1m 30s"),
    (3600, "1h"),
    (3601, "1h 1s"),
    (3661, "1h 1m 1s"),
    (90042, "25h 42s"),
    (0, "0s")
]


def getHoursMinutesSeconds(total_secs: int) -> tuple[int, int, int]:
    hours = total_secs // 3600
    secs = total_secs % 3600
    mins = secs // 60
    secs = total_secs % 60
    return (hours, mins, secs)        


def format_time(hours: int, mins: int, secs: int) -> str:
    result = ""
    if hours > 0:
        result = f"{hours}h"
    if mins > 0:
        result = " ".join((result, f"{mins}m"))
    if secs > 0 or result == "":
        result = " ".join((result, f"{secs}s"))
    return result.strip()


def main():
    for (total_secs, expected) in TESTS:
        hours, mins, secs = getHoursMinutesSeconds(total_secs)
        result = format_time(hours, mins, secs)
        print(f"Total seconds: {total_secs} -> formatted: {result}")
        try:
            assert result == expected
        except AssertionError:
            print(f"Test failed for {total_secs} - expected result: {expected}.")
            return


if __name__ == "__main__":
    main()
