import secrets
import string


def ispunctuation(char: str):
    return char in ['!', '"', '#', '$','%', '&', '\'', '(', ')', '*', '+', ',',
                    '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\/',
                    ']', '^', '_', '`', '{', '|', '}', '~'
                ]

def pwgen(length: int,
          with_digits=True,
          with_uppercase=True,
          with_special_characters=False) -> str:

    if length < 8:
        return("Error: Password length must be >= 8")


    def super_strong() -> str:
        # Generates an alphanumeric password with at least 1 uppercase letter
        # 1 lower case letter and 1 digit, and 1 special character
        alphabet = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 1
                and any(ispunctuation(c) for c in password)):
                break
        return password


    def strong() -> str:
        # Generates an alphanumeric password with at least 1 uppercase letter
        # 1 lower case letter and 1 digits
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 1):
                break
        return password


    def medium(secondary_character_set: str) -> str:
        # Generates an alphanumeric password with at least 1 lowercase letter and
        # (1 digit or 1 uppercase letter)
        alphabet = string.ascii_lowercase + secondary_character_set
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(length))
            if (any(c.islower() for c in password)
                and (sum(c.isdigit() for c in password) >= 1
                     or any(c.isupper() for c in password))):
                break
        return password


    def weak() -> str:
        # Generates a password of lowercase letters
        alphabet = string.ascii_lowercase
        return ''.join(secrets.choice(alphabet) for i in range(length))


    # --------------- Return password for arguments provided -------------------
    if with_digits and with_uppercase and with_special_characters:
        return super_strong()
    elif with_digits and with_uppercase:
        return strong()
    elif with_digits and not with_uppercase:
        return medium(string.digits)
    elif with_uppercase and not with_digits:
        return medium(string.ascii_uppercase)
    else:
        return weak()


def main() -> None:
    print("Weak:", pwgen(8, False, False))
    print("Medium:", pwgen(8, True, False))
    print("Medium:", pwgen(8, False, True))
    print("Strong:", pwgen(8))
    print("Super strong:", pwgen(16, True, True, True))


if __name__ == "__main__":
    main()
