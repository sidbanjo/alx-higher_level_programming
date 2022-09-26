#!/usr/bin/python3
def print_list_integer(mylist=[]):
    for x in mylist:
        print("{}".format(x))
        if x != mylist[-1]:
            print("\n")
