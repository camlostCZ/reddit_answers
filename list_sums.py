"""
https://www.reddit.com/r/learnpython/comments/mbpvxp/need_to_return_20_20_19_16_10_0/
"""

import random

from typing import Iterable


def method1(data: Iterable[int]) -> list[int]:
    result = []
    total = sum(data)
    for item in data:
        result.append(total)
        total = total - item
    result.append(total)
    return result



#ls = sorted(random.sample(range(100), 50))
ls = [0, 1, 3, 6, 10]
print(", ".join(map(str, ls)))
sums = method1(ls)
print(", ".join(map(str, sums)))
