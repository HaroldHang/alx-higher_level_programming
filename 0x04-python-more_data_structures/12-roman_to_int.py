#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I' : '1', 'V' : '5', 'X' : '10', 'L' : '50', 'C' : '100', 'D' : '500', 'M' : '1000'}
    if isinstance(roman_string, str):
        num = 0
        skip = False
        roman_len = len(roman_string)
        for i in range(0, roman_len):
            if skip:
                continue
            else:
                if i == (roman_len - 1):
                    skip = False
                    num += int(roman_num[roman_string[i]])
                elif (roman_string[i] == 'I' and (roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X')) or (roman_string[i] == 'X' and (roman_string[i + 1] == 'L' or roman_string[i + 1] == 'M' or roman_string[i + 1] == 'C')): 
                    num += int(roman_num[roman_string[i + 1]]) - int(roman_num[roman_string[i]])
                    skip = True
                else:
                    skip = False
                    num += int(roman_num[roman_string[i]])
        return num
    else:
        return None