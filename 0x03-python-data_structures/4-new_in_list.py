#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mod_list = []
    i = 0
    for x in my_list:
        mod_list[i] = x
        i++
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list
    else:
        mod_list[idx] = element
        return mod_list
