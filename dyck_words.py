# Implementation of a is_a_dyck_word function

# A Dyck word is a word composed of two symbols, typically ( and ). A Dyck word
# have to be "well-parenthesized". See: https://en.wikipedia.org/wiki/Dyck_language.
# for more.

# This version of the function can produce incorrect results in some cases because
# it doesn't properly match opening and closing characters. It simply checks whether
# a character is an opener or closer and manipulates the stack accordingly, but it
# doesn't verify that each closing character correctly matches its corresponding
# opening character.

# For example, consider the word "([)]". It has the correct number of openers and
# closers and they are evenly distributed, but the word is not a Dyck word because
# the second opener ( is closed by ] instead of ). The current implementation of
# is_a_dyck_word(word) would incorrectly return True for this input.

# The generate_openers_and_closers(word) function currently splits the unique
# characters into two halves, assuming that the first half of unique characters in
# the input sequence are openers and the second half are closers. This will not
# work correctly for inputs where openers and closers are intermingled.

# As a recommendation, consider modifying the is_a_dyck_word(word) function so that
# it checks whether each closing character correctly matches the last opened but not
# yet closed character. A possible approach is to use a dictionary mapping opening
# characters to closing characters, and when you pop a character from the stack,
# check that it matches the current closing character.
from rich.console import Console


console = Console()


def generate_openers_and_closers(word: str) -> tuple:
    # Create an empty list to store the unique characters we find in the word
    unique_chars = []

    # Iterate through each character in the word
    for char in word:
        # If we haven't seen this character before, add it to our list of unique characters
        if char not in unique_chars:
            unique_chars.append(char)

    # Find the midpoint of our list of unique characters. We'll use this to split the list into 'openers' and 'closers'
    mid_index = len(unique_chars) // 2

    # The 'openers' are the first half of the unique characters
    openers = unique_chars[:mid_index]
    # The 'closers' are the second half of the unique characters
    closers = unique_chars[mid_index:]

    # Return our 'openers' and 'closers'
    return (openers, closers)


def is_a_dyck_word(word: str) -> bool:
    """
    Determines if a given word is a Dyck word.
    A Dyck word is a sequence of characters (typically brackets) that is well-formed;
    i.e., each opening bracket has a corresponding closing bracket, and they are correctly nested.

    Args:
        word (str): A string of brackets.

    Returns:
        bool: True if the word is a Dyck word (i.e., all brackets are correctly matched and nested); False otherwise.
    """
    openers, closers = generate_openers_and_closers(word)

    # Initialize an empty list as a stack
    stack: list = []

    for char in word:
        if char in openers:
            stack.append(char)
        elif len(stack) > 0 and char in closers:
            stack.pop()
        else:
            return False  # Handles no matches in openers

    # If all openers and closers have been correctly matched and nested, the stack should now be empty
    # If it is, return True to indicate that the word is a Dyck word
    # If it's not (i.e., there are un-matched opening brackets remaining), return False
    return len(stack) == 0



def test_is_a_dyck_word() -> None:
    test_cases: dict = {
        "":         True,
        "()":       True,
        "(((())))": True,
        "()()()()": True,
        "()(())()": True,
        "(((":      False,
        "((()":     False,
        "()()()(":  False,
        "[]":       True,
        "{}":       True,
        "<>":       True,
        "[[]]":     True,
        "{{}}":     True,
        "<<>>":     True,
        "[][]":     True,
        "{}{}":     True,
        "<><>":     True,
        "([)]":     False,
        "AB":       True,
        "ABAB":     True,
        "AABB":     True,
        "AABBAB":   True,
        "AAABBB":   True,
        "ABABAB":   True,
        ",.":       True,
        ",.,.":     True,
        "..,,":     True,
        "dodo":     True,
        "mama":     True,
        "papa":     True,
        "tutu":     True,
        "()[]{}":   True
    }

    for test, result in test_cases.items():
        try:
            assert(is_a_dyck_word(test) == result)
            console.log(f"[green]Passed: {test}")
        except AssertionError:
            console.log(f"[red]Failed: {test}")


def main() -> None:
    test_is_a_dyck_word()


if __name__ == "__main__":
    main()
