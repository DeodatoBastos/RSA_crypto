from math import gcd
from random import randint
from typing import Tuple, List, Dict

from utils import fast_exp_mod
from primes import generate_prime_number


def message_codification(message: str) -> int:
    DICTIONARY: Dict[str, int] = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17,
                                  "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25,
                                  "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "X": 32, "W": 33,
                                  "Y": 34, "Z": 35, " ": 36, ".": 37}

    letters: List[str] = list(message)
    plaintext: int = sum([DICTIONARY[letter] for letter in letters])

    return plaintext


def choose_public_exponent(n: int) -> int:
    """
        Generate an integer which is invertible modulus phi_n
    Args:
        n: the modulus value

    Returns:
        e: invertible integer modulus phi_n
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
        t: inverse of e modulus n
    """

    t: int = 0
    new_t: int = 1
    r: int = n
    new_r: int = e

    while new_r != 0:
        quotient: int = r // new_r

        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if t < 0:
        t += n

    return t


def generate_keypair() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
        Generate a key pair using RSA cryptography

    Returns:
       return a Tuple of (public_key, private_key)
    """

    a: int = 15
    b: int = 20

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
        public_key: public key used in encryption
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
        private_key: private key used in decryption
        ciphertext: message to be decrypted

    Returns:
        plaintext: returns the decrypted message
    """

    d: int
    n: int

    d, n = private_key
    plaintext: int = fast_exp_mod(ciphertext, d, n)
    return plaintext
