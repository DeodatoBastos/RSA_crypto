def fast_exp_mod(a: int, e: int, n: int = 1) -> int:
    """
        A faster algorithm to compute a power to e modulus n, i.e., a^e (mod n)
    Args:
        a: base of exponential
        e: power of exponential
        n: modulus

    Returns:
        P: value congruent of a power to e modulus n, i.e., P === a^e (mod n)

    """
    A: int = a
    P: int = 1
    E: int = e

    while True:
        if E == 0:
            return P

        if E & 1 == 1:
            P = (A * P) % n
            E = (E - 1) >> 1
        else:
            E = E >> 1

        A = (A * A) % n
