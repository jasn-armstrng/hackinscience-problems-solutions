from collections import Counter
import unicodedata


def remove_non_alphanumeric(input_str):
    """
    Removes all non-alphanumeric characters from a string.

    Parameters:
    input_str (str): The input string from which non-alphanumeric characters need to be removed.

    Returns:
    str: The string with non-alphanumeric characters removed.
    """
    alphanumeric_chars = []

    for ch in input_str:
        if ch.isalnum():
            alphanumeric_chars.append(ch)

    return ''.join(alphanumeric_chars)


def remove_diacritics(input_str: str) -> str:
    """
    Removes diacritics from the given string.

    Parameters:
    input_str (str): The input string from which diacritics need to be removed.

    Returns:
    str: The string with diacritics removed.
    """
    # Normalize the string to 'NFD' form which separates base characters from diacritics
    nfd_form = unicodedata.normalize('NFD', input_str)

    # Use a list comprehension to build a string of base characters, ignoring non-spacing marks
    only_ascii = ''.join(ch for ch in nfd_form if unicodedata.category(ch) != 'Mn')

    return only_ascii


def is_anagram(left: str, right: str) -> bool:
    """
    Determine if two strings are anagrams (ignoring case, diacritics, and non-alphanumeric characters)

    Parameters:
    s1, s2 (str): Strings to compare

    Returns:
    bool: True if s1 and s2 are anagrams, False otherwise
    """
    str_1 = remove_non_alphanumeric(remove_diacritics(left)).lower()
    str_2 = remove_non_alphanumeric(remove_diacritics(right)).lower()

    return Counter(str_1) == Counter(str_2)


def test_is_anagram():
    # Test with simple anagrams
    assert is_anagram("listen", "silent") == True
    assert is_anagram("funeral", "real fun") == True
    assert is_anagram("Madam Curie", "Radium came") == True

    # Test with strings including diacritics
    assert is_anagram("crâné", "crane") == True
    assert is_anagram("éclat", "câtel") == True

    # Test with strings including non-alphanumeric characters
    assert is_anagram("R.E.S.P.E.C.T", "specter") == True
    assert is_anagram("Church of Scientology", "rich-chosen goofy cult") == True

    # Test with non-anagram pairs
    assert is_anagram("hello", "world") == False
    assert is_anagram("Madam Curie", "Marie Curie") == False

    # Test with empty strings
    assert is_anagram("", "") == True
    assert is_anagram("a", "") == False

    # Test with strings of different lengths (non-anagrams)
    assert is_anagram("short", "longer") == False

    # Test with same strings (are anagrams)
    assert is_anagram("same", "same") == True

    print("All tests passed.")


def main() -> None:
    test_is_anagram()


if __name__ ==  "__main__":
    main()
