#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0
    len_tup_a = len(tuple_a)
    len_tup_b = len(tuple_b)
    if len_tup_a == 0:
        if len_tup_b == 0:
            return (a, b)
        elif len_tup_b == 1:
            return (tuple_b[0], b)
        else:
            return (tuple_b[0], tuple_b[1])
    elif len_tup_a == 1:
        if len_tup_b == 0:
            return (tuple_a[0], b)
        elif len_tup_b == 1:
            a = tuple_a[0] + tuple_b[0]
            return (tuple_b[0], b)
        else:
            a = tuple_a[0] + tuple_b[0]
            return (a, tuple_b[1])
    else:
        if len_tup_b == 0:
            return (tuple_a[0], tuple_a[1])
        elif len_tup_b == 1:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1]
            return (tuple_b[0], b)
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + tuple_b[1]
            return (a, b)
