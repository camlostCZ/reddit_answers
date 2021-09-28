"""
https://www.reddit.com/r/learnpython/comments/pxc2w2/what_am_i_doing_wrong/
"""

def end_zeroes(num: int) -> int:
    result = 0
    while num % 10 == 0:
        result += 1
        num = num // 10
    return result


assert(end_zeroes(1) == 0)
assert(end_zeroes(-100) == 2)
assert(end_zeroes(14504500000) == 5)
