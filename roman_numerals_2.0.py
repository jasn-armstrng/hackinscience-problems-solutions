# Program converts decimals to Roman numerals

# Version 1.0 refactored and a here the function `convert(...)` is a more concise
# implementation of the functions previously implemented to handle the conversion
# of units, tens, hundredths and thousands.
# The stack has also been removed, now the output string is buiilt dynamically as
# the number is processed

# I pictured convert() as a series of processing pipelines that would handle a
# number based on its positional value. The below but rotated 90º

#          ------------------------
# 1s    ->                          -> I, V, IX, ...
#          ------------------------
# 10s   ->                          -> X, L, LXX, ...
#          ------------------------
# 100s  ->                          -> C, D, DCCC, ...
#          ------------------------

# Thousands are processed much faster
#          -------
# 1000s ->         -> M, MM, ...
#          -------

# To do:
# 1. This program assumes that a +ve integer is entered for conversion
# 2.

def to_roman_numeral(number: int) -> str:
    # Rules:
    #   1. If the units part of the number is < 4 it is represented by the equivalent number of 'I's
    #   2. If the units part of the number is 1 less than 5 or 10 it is represented by 'I' followed by the the representations for 5 'V' or 10 'X'
    #   3. If the units part of the number is > 5 and < 9 it is represented by 5 'V' and the equivalent number of 'I's to make up that number
    #   4. If the tenths part of the number is < 40 it is represented by the equivalent number of 'X's
    #   5. If the tenths part of the number is 10 less 50 or 100 it is represented by 'X' followed by the the representations for 50 'L' or 100 'C'
    #   6. If the tenths part of the number is > 50 and < 90 it is represented by 50 'L' and the equivalent number of 'X's to make up that number
    #   7. If the hundredths part of the number is < 400 it is represented by the equivalent number of 'C's
    #   8. If the hundredths part of the number is 100 less 500 or 1000 it is represented by 'C' followed by the the representations for 500 'D' or 100 'M'
    #   9. If the hundredths part of the number is > 500 and < 900 it is represented by 500 'D' and the equivalent number of 'C's to make up that number
    #   10. The thousandths part of the number is represented by the equivalent number of 'M's

    # Actions:
    #   1. Divide the number into units, tenths, hundredths, thousands
    #   2. Convert the number according to its place value
    #   3. Combine the resulting roman numeric strings from action 2
    def convert(number: int, position: int) -> str:
        if position == 3:
            return number * 'M'

        if number == 9:
            a = ['IX', 'XC', 'CM']
            return a[position]
        elif number > 5:
            b = [('V', 'I'), ('L', 'X'), ('D', 'C')]
            return b[position][0] + (number - 5) * b[position][1]
        elif number == 5:
            c = ['V', 'L', 'D']
            return c[position]
        elif number == 4:
            d = ['IV', 'XL', 'CD']
            return d[position]
        else:
            e = ['I', 'X', 'C']
            return e[position] * number

    output: str = ""
    counter: int = 0

    while number > 0:
        if counter > 2:
            output = convert(number, counter) + output
            break
        else:
            output = convert(number % 10, counter) + output
            number = number//10
        counter += 1

    return output


def tests() -> None:
    assert to_roman_numeral(1) == 'I'
    assert to_roman_numeral(2) == 'II'
    assert to_roman_numeral(4) == 'IV'
    assert to_roman_numeral(8) == 'VIII'
    assert to_roman_numeral(16) == 'XVI'
    assert to_roman_numeral(32) == 'XXXII'
    assert to_roman_numeral(111) == 'CXI'
    assert to_roman_numeral(4678) == 'MMMMDCLXXVIII'
    print("All tests have passed")


def main() -> None:
    tests()


if __name__ == "__main__":
    main()
    print(to_roman_numeral(1000))
    print(to_roman_numeral(4468))
