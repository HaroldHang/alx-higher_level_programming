#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1 , set_2 = list(set_1), list(set_2)
    for val1 in set_1: 
        for val2 in set_2: 
            if val1 == val2:
                set_1.remove(val1)
                set_2.remove(val2)
    set_1.extend(set_2)
    new_set = set(set_1)
    return new_set
