#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mod_list = []
    for x in my_list:
        mod_list.append(x)
    if idx < 0:
        return mod_list
    if idx > len(mod_list) - 1:
        return mod_list
    else:
        mod_list[idx] = element
        return mod_list
