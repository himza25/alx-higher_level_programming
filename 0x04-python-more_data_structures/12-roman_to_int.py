#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for i in roman_string:
        curr_value = roman_dict[i]
        if curr_value > prev_value:
            total += curr_value - 2 * prev_value
        else:
            total += curr_value
        prev_value = curr_value

    return total
