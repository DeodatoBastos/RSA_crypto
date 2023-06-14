from time import time
from random import randint, choices, choice
from typing import List, Tuple

from utils import fast_exp_mod


def generate_odd_number(a: int = 0, b: int = 1) -> int:
    """
        Generate an random odd number in (10^a, 10^(b + 1))
    Args:
        a: initial value
        b: final value
    Returns:
        number: The random odd number

    """

    num_digits = randint(a, b)
    first_digits = choices(range(10), k=num_digits - 1)
    last_digit = choice([1, 3, 7, 9])
    number = int(''.join(map(str, first_digits))) * 10 + last_digit
    return number


def miller_rabin_test(n: int, bases: List[int]) -> bool:
    """
        Verify if number n passes in Miller-Rabin primality test
    Args:
        n: number to verify
        bases: list of bases to verify in Miller-Rabin test

    Returns:
        returns true if the test is inconclusive and false otherwise
    """

    if n == 2 or n == 3:
        return True
    if n & 1 == 0:
        return False

    k: int = 0
    q: int = n - 1
    while q & 1 == 0:
        k += 1
        q = q >> 1

    for base in bases:
        r: int = fast_exp_mod(base, q, n)
        i: int = 0

        while True:
            if (i == 0 and r == 1) or (i >= 0 and r == n-1):
                break
            else:
                i += 1
                r = fast_exp_mod(r, 2, n)

            if i >= k:
                return False

    return True


def generate_prime_number(a: int, b: int) -> int:
    """
        Generate a number with is likely to be a prime in (10^a, 10^(b + 1)) interval
    Args:
        a: init of interval
        b: end of interval

    Returns:
        returns a prime number

    """

    bases: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    while True:
        odd_random_number: int = generate_odd_number(a, b)
        if (miller_rabin_test(odd_random_number, bases)):
            break

    return odd_random_number


def generate_prime_number_with_time(a: int, b: int) -> Tuple[int, float]:
    """
        Generate a number with is likely to be a prime in (10^a, 10^(b + 1)) interval
    Args:
        a: init of interval
        b: end of interval

    Returns:
        returns a prime number and how much time was spent to create it

    """
    bases: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    start_time: float = time()

    while True:
        odd_random_number: int = generate_odd_number(a, b)
        if (miller_rabin_test(odd_random_number, bases)):
            break

    end_time: float = time()

    delta_time: float = end_time - start_time

    return odd_random_number, delta_time
