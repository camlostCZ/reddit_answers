"""
https://www.reddit.com/r/learnpython/comments/qenz3k/how_could_i_get_rid_of_the_space_in_the_else/
"""

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 23, 101, 212]


def num_order(n: int) -> str:
    result = "th"
    if n % 100 not in range (11, 14):
        match n % 10:
            case 1: result = "st"
            case 2: result = "nd"
            case 3: result = "rd"
    return str(n) + result

line = ", ".join(num_order(x) for x in NUMBERS)
print(line)
