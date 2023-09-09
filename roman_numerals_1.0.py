# Very rough version 1
def units_to_roman(number: int) -> str:
    if number == 9: return 'IX'
    elif number > 5:
        return 'V' + (number - 5) * 'I'
    elif number == 5:
        return 'V'
    elif number == 4:
        return 'IV'
    else:
        return number * 'I'

def tenths_to_roman(number: int) -> str:
    if number == 9:
        return 'XC'
    elif number > 5:
        return 'L' + (number - 5) * 'X'
    elif number == 5:
        return 'L'
    elif number == 4:
        return 'XL'
    else:
        return number * 'X'

def hundredths_to_roman(number: int) -> str:
    if number == 9:
        return 'CM'
    elif number > 5:
        return 'D' + (number - 5) * 'C'
    elif number == 5:
        return 'D'
    elif number == 4:
        return 'CD'
    else:
        return number * 'C'

def thousands_to_roman(number: int) -> str:
    return number * 'M'

conversion_dict = {
    '0': units_to_roman,
    '1': tenths_to_roman,
    '2': hundredths_to_roman,
    '3': thousands_to_roman
}

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
    #   2. In a list tore each place value
    #   3. Apply the rules for each place value
    output  = ""
    stack   = []
    counter = 0
    while number > 0:
        function = conversion_dict.get(str(counter))
        if counter > 2:
            stack.append(function(number))
            break
        else:
            stack.append(function(number % 10))
        number = number//10
        counter += 1

    while stack:
       output += stack.pop()
    return output
