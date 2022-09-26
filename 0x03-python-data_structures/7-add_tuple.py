#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if tuple_a == ():
            ax = 0
        else:
            ax = tuple_a[0]
        ay = 0
    else:
        ax = tuple_a[0]
        ay = tuple_a[1]
    if len(tuple_b) < 2:
        if tuple_b == ():
            bx = 0
        else:
            bx = tuple_b[0]
        by = 0
    else:
        bx = tuple_b[0]
        by = tuple_b[1]
    tup = (ax + bx, ay + by)
    return tup
