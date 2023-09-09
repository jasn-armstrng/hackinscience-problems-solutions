def from_roman_numeral(roman_numeral: str) -> None:
    """
    Convert a Roman numeral to its decimal (integer) equivalent.

    Args:
        roman_numeral (str): A string representing a Roman numeral.
                             For example: "IX", "XIV", "MMMCMXCIX".

    Returns:
        int: The decimal (integer) equivalent of the given Roman numeral.
             For example: 9, 14, 3999.
    """
    roman_numerals: dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    decimal  = 0
    previous = 0

    for numeral in roman_numeral.upper():  
        next: int = roman_numerals[numeral]

        if previous >= next:
            decimal += previous
        else:
            decimal -= previous
        previous = next 
    decimal += next

    return decimal


def test_from_roman_numeral():
    assert from_roman_numeral('I') == 1
    assert from_roman_numeral('IV') == 4
    assert from_roman_numeral('IX') == 9
    assert from_roman_numeral('LVIII') == 58
    assert from_roman_numeral('CCXLVI') == 246
    assert from_roman_numeral('DCCLXXXIX') == 789
    assert from_roman_numeral('MDCCLXXVI') == 1776
    assert from_roman_numeral('MCMLXXXV') == 1985
    assert from_roman_numeral('MCMXCIV') == 1994
    assert from_roman_numeral('MMCDXXI') == 2421
    assert from_roman_numeral('MMMCMXCIX') == 3999
    print("All tests passed.")


def main() -> None:
    test_from_roman_numeral()


if __name__ == "__main__":
    main()
