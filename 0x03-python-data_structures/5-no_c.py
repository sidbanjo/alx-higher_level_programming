#!/usr/bin/python3
def no_c(my_string):
    mod_string = ""
    x = 0
    for i in my_string:
        if i == "c" or i == "C":
            continue
        else:
            mod_string[x] = i
            x++
    return mod_string
