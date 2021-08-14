"""
Compute date after specified number of days without using any modules.
https://www.reddit.com/r/learnpython/comments/p4au9z/date_calculation/
"""

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def compute_date(today: tuple[int, int, int], days: int) -> tuple[int, int, int]:
    # Faster alternative to a function
    _is_leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    year, month, day = today

    lst_days = [-1] + DAYS_IN_MONTH  # Optimization so that we may use month as the index

    left = days + day - 28  # Get rid of left == 0 situations at the end of the function
    day = 28

    while left + day > lst_days[month]:
        left -= lst_days[month]

        month = month % 12 + 1
        if month == 1:
            year += 1
        elif month == 2:
            # Set 29 days for February if leap year, 28 otherwise
            lst_days[month] = 29 if _is_leap_year(year) else 28

    return (year, month, day + left)


def test_compute_date():
    assert compute_date((2021, 8, 14), 3) == (2021, 8, 17)  # Not crossing current month
    assert compute_date((2021, 8, 14), 21) == (2021, 9, 4)  # Next month
    assert compute_date((2019, 12, 30), 33) == (2020, 2, 1)  # Leap year #1
    assert compute_date((2019, 12, 30), 61) == (2020, 2, 29)  # Leap year #1
    assert compute_date((2019, 12, 30), 427) == (2021, 3, 1)  # More than a year incl. a leap year
    print("All tests passed OK.")


def main() -> None:
    today = input("Enter today's date (ex. 2021-08-14): ")
    number_of_days = int(input("Enter number of days to skip ahead: "))
    year, month, day = compute_date(map(int, today.split('-')), number_of_days)
    print(f"The date after {number_of_days} days(s): {year}-{month:02}-{day:02}")


if __name__ == "__main__":
    try:
        test_compute_date()
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
