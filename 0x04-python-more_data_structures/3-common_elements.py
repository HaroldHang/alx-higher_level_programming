#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = { val1 for val1 in set_1 for val2 in set_2 if val1 == val2 }
    return new_set
