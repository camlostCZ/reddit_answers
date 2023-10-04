"""
https://www.reddit.com/r/pythonhelp/comments/15ivutp/getting_an_unexpected_output_from_this_code_what/
"""

from typing import Any, Callable, Iterable


TRANS_PH = [
    (0, "pH out of range"),
    (3, "Strongly acidic"),
    (6, "Weakly acidic"),
    (9, "Neutral"),
    (12, "Weakly basic"),
    (14, "Strongly basic")
]

TRANS_GRADE = [
    (95, "A"),
    (90, "B"),
    (80, "C"),
    (70, "D"),
    (60, "E")
]


def transform_data(value: Any, fn: Callable, trans: Iterable[tuple[Any, Any]], default: Any) -> Any:
    for item in trans:
        limit, result = item
        if fn(value, limit):
            return result
    return default


def pH2Category(pH):
    if (pH < 0) or (pH > 14):
        category = "pH out of range"

    elif (0 <= pH) and (pH < 3):
        category = "Strongly acidic"

    elif (3 <= pH) and (pH < 6):
        category = "Weakly acidic"

    elif (6 <= pH) and (pH < 9):
        category = "Neutral"

    elif (9 <= pH) and (pH < 12):
        category = "Weakly basic"

    else:
        category = "strongly basic"
    return category


#test for lemon acidity value
print(pH2Category(2.3))

print("\nTransform pH value:")
print(transform_data(2.3, lambda x, y: x < y, TRANS_PH, "pH out of range"))

print("\nTransform grade:")
print(transform_data(56, lambda x, y: x > y, TRANS_GRADE, "F aka failed"))
