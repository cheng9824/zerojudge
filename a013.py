def roman_to_number(roman):
    value = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    for i in range(len(roman)):
        a = value[roman[i]]

        if i < len(roman) - 1:
            b = value[roman[i + 1]]

            if a < b:
                result -= a
            else:
                result += a
        else:
            result += a

    return result

def number_to_roman(number):
    roman_value = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''

    for value, roman in roman_value.items():
        while number >= value:
            number -= value
            result += roman

    return result

while True:
    line = input()

    if line == '#':
        break

    a, b = line.split()

    c = roman_to_number(a)
    d = roman_to_number(b)

    e = abs(c - d)

    if e == 0:
        print('ZERO')
    else:
        print(number_to_roman(e))