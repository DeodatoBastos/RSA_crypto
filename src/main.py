from typing import Dict, List

from crypto import Tuple, generate_keypair, encrypt, decrypt


if __name__ == "__main__":
    MESSAGE: str = "NAO SOU NADA. NUNCA SEREI NADA. NAO POSSO QUERER SER NADA. A " + \
              "PARTE ISSO TENHO EM MIM TODOS OS SONHOS DO MUNDO. ESTOU HOJE " + \
              "VENCIDO COMO SE SOUBESSE A VERDADE. ESTOU HOJE PERPPLEXO COMO " + \
              "QUEM PENSOU E ACHOU E ESQUECEU."

    DICTIONARY: Dict[str, int] = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17,
                                  "I": 18, "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25,
                                  "Q": 26, "R": 27, "S": 28, "T": 29, "U": 30, "V": 31, "X": 32, "W": 33,
                                  "Y": 34, "Z": 35, " ": 36, ".": 37}

    letters: List[str] = list(MESSAGE)
    plaintext: int = sum([DICTIONARY[letter] for letter in letters])

    public_key: Tuple[int, int]
    private_key: Tuple[int, int]
    public_key, private_key = generate_keypair()

    print("Plaintext: ", plaintext)
    print("Public key: ", public_key, "\nPrivate Key: ", private_key)

    ciphertext: int = encrypt(public_key, plaintext)
    print("Ciphertext: ", ciphertext)

    decrypted_plaintext: int = decrypt(private_key, ciphertext)
    print("Decrypted plaintext: ", decrypted_plaintext)

    second_public_key: Tuple[int, int]
    second_private_key: Tuple[int, int]

    second_public_key, second_private_key = generate_keypair()
    second_decrypted_plaintext: int = decrypt(second_private_key, ciphertext)
    print("Decrypted plaintext with other private key: ", second_decrypted_plaintext)
