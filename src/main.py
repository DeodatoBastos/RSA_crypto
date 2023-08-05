from typing import Tuple
from sys import stdout

from crypto import message_codification, generate_keypair, encrypt, decrypt

if __name__ == "__main__":
    MESSAGE: str = "NAO SOU NADA. NUNCA SEREI NADA. NAO POSSO QUERER SER NADA. A " + \
              "PARTE ISSO TENHO EM MIM TODOS OS SONHOS DO MUNDO. ESTOU HOJE " + \
              "VENCIDO COMO SE SOUBESSE A VERDADE. ESTOU HOJE PERPPLEXO COMO " + \
              "QUEM PENSOU E ACHOU E ESQUECEU."

    plaintext: int = message_codification(MESSAGE)

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
    i: int = 1

    while second_decrypted_plaintext != decrypted_plaintext and i < 100_000:
        stdout.write("\rTrial number %i to crack the ciphertext" % i)
        stdout.flush()
        second_public_key, second_private_key = generate_keypair()
        second_decrypted_plaintext: int = decrypt(second_private_key, ciphertext)
        i += 1

    print("\nDecrypted plaintext with other private key: ", second_decrypted_plaintext)
    print("Number of trials: ", i)
    print("Public key: ", second_public_key, "\nPrivate Key: ", second_private_key)
