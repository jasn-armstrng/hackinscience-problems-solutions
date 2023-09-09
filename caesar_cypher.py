# https://www.hackinscience.org/exercises/caesar-cypher

A, Z = 65, 90   # Upper and lower bounds for Ascii uppercase letter
a, z = 97, 122  # Upper and lower bounds for Ascii lowercase letter
dist = 26       # No. of letters in the English alphabet.

def caesar_cypher_encrypt(message: str, key: int) -> str:
    """
    Encrypts a given message using the Caesar cipher.

    Parameters:
    - message (str): The plaintext message to be encrypted.
    - key (int): The number of positions each letter in the message should be
      shifted.

    Returns:
    - str: The encrypted message.

    Notes:
    - Only alphabetic characters are encrypted. Numbers, symbols, and other
      characters remain unchanged.
    - The function is case-sensitive, meaning 'A' and 'a' are shifted within
      their respective alphabets.
    """
    cypher: list = []
    for i in message:
        char_val = ord(i)
        if A <= char_val <= Z:
            cypher.append(chr(((char_val - A + key) % dist) + A))
        elif a <= char_val <= z:
            cypher.append(chr(((char_val - a + key) % dist) + a))
        else:
            cypher.append(i)
    return ''.join(cypher)

def caesar_cypher_decrypt(cypher: str, key: int) -> str:
    """
    Decrypts a given cyphertext using the Caesar cipher.

    Parameters:
    - cypher (str): The encrypted message to be decrypted.
    - key (int): The number of positions each letter in the cypher should be
      shifted back to obtain the original message.

    Returns:
    - str: The decrypted message.

    Notes:
    - Only alphabetic characters are decrypted. Numbers, symbols, and other
      characters remain unchanged.
    - The function is case-sensitive, meaning 'A' and 'a' are shifted within
      their respective alphabets.
    """
    message: list = []
    for i in cypher:
        char_val = ord(i)
        if A <= char_val <= Z:
            message.append(chr(((char_val - A - key) % dist) + A))
        elif a <= char_val <= z:
            message.append(chr(((char_val - a - key) % dist) + a))
        else:
            message.append(i)
    return ''.join(message)

def test_encrypt_decrypt() -> None:
    assert caesar_cypher_decrypt("Udymts nx xzujw inxht !", 31) == "Python is super disco !"
    assert caesar_cypher_encrypt("Python is super disco !", 31) == "Udymts nx xzujw inxht !"
    print("All tests have passed!")

def main() -> None:
    test_encrypt_decrypt()

if __name__ == "__main__":
    main()
