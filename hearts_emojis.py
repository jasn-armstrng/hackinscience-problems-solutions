from rich import print as rprint
import unicodedata


def print_heart_emojis() -> None:
    # Define the range to cover all emojis (including extended ones).
    # Note: As of Unicode 13.0, the highest code point for emojis is 0x1FADF
    for i in range(1, 0x1FADF + 1):
        try:
            # Get the name of the character
            character_name = unicodedata.name(chr(i))

            # Check if 'HEART' is in the name
            if 'HEART' in character_name:
                print(chr(i), end='')
        except ValueError:
            # This is raised when the character has no name, so we just skip it
            pass


def main() -> None:
    print_heart_emojis()


if __name__ == "__main__":
    main()
