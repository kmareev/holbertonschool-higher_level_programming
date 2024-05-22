#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_num = {
        'I' : 1,'V' : 5,'X' : 10,'L' : 50,
        'C' : 100,'D' : 500,'M' : 1000
    }

    prev_value = 0
    total = 0

    for c in roman_string:
        if c not in roman_num:
            return 0

        current_value = roman_num[c]

        if current_value > prev_value:
            total -= prev_value
        else:
            total += prev_value

        prev_value = current_value

    total += current_value
    return total
