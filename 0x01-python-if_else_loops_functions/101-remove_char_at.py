#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    if n > len(str) - 1 or n < 0:
        return str
    for i in str:
        if i == str[n]:
            continue
        new_str = new_str + i
    return new_str
