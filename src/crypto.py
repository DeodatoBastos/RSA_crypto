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
