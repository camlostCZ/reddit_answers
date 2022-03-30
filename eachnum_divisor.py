"""
https://www.reddit.com/r/learnpython/comments/q77bv2/how_do_i_approach_to_program_the_solution_for/
"""

from typing import Iterable

def lcm(arr: Iterable[int]) -> int:
    result = 0
    factors = set()
    for num in arr[::-1]:
        primes = prime_factors(num)
        if result == 0:
            result = num
            factors.update(primes)
        else:
            # For each prime not in factors:
            # - multiply result with prime
            # - add prime to factors
            pass
        
    return result


assert(lcm(range(1, 11)) == 2520)

print(lcm(range(1, 21)))
