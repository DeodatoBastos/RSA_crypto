from math import gcd
from random import randint

from utils import fast_exp_mod
from primes import Tuple, generate_prime_number


def choose_public_exponent(n: int) -> int:
    """
        Generate an integer which is inversible modulus phi_n
    Args:
        n: the modulus value

    Returns:
        e: inversible integer modulus phi_n
    """

    e: int = randint(2, n)

    while gcd(e, n) != 1:
        e = randint(2, n)

    return e


def compute_private_exponent(e: int, n: int) -> int:
    """
        Generate an integer which is the inverse of e modulus n,
        i.e., d * e (mod n) == 1
    Args:
        e: int value
        n: modulus value

    Returns:
        d: inverse of e modulus n
    """

    d: int
    d, _ = extended_euclidean_algorithm(e, n)

    return d


def extended_euclidean_algorithm(a: int, b: int) -> Tuple[int, int]:
    """
        Calculate the coefficients of a and b in Extended Euclidean Algorithm,
        i.e., a * x + b * y = gcd(a, b)
    Args:
        a: int value
        b: int value

    Returns:
        return a Tuple with the coefficients of a and b, i.e., (x, y).
    """

    if b == 0:
        return 1, 0
    else:
        q: int
        r: int
        s: int
        t: int

        q, r = divmod(a, b)
        s, t = extended_euclidean_algorithm(b, r)
        return t, s - q * t


def generate_keypair() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
        Generate a key pair using RSA cryptography

    Returns:
       return a Tuple of (public_key, private_key)
    """

    a: int = 6
    b: int = 9

    p: int = generate_prime_number(a, b)
    q: int = generate_prime_number(a, b)

    n: int = p * q
    phi_n: int = (p - 1) * (q - 1)

    e: int = choose_public_exponent(phi_n)
    d: int = compute_private_exponent(e, phi_n)

    return (e, n), (d, n)


def encrypt(public_key: Tuple[int, int], plaintext: int) -> int:
    """
        Encrypt the message in plaintext
    Args:
        public_key: public key used in encryptation
        plaintext: message to be encrypted

    Returns:
        ciphertext: returns a encrypted message
    """

    e: int
    n: int
    e, n = public_key
    ciphertext: int = fast_exp_mod(plaintext, e, n)
    return ciphertext


def decrypt(private_key: Tuple[int, int], ciphertext: int) -> int:
    """
        Decrypt the message in ciphertext
    Args:
        private_key: private key used in decryptation
        ciphertext: message to be decrypted

    Returns:
        plaintext: returns the decrypted message
    """

    d: int
    n: int

    d, n = private_key
    plaintext: int = fast_exp_mod(ciphertext, d, n)
    return plaintext
