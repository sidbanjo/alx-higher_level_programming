#!/usr/bin/python3
def uppercase(str):
    for i in str:
        x = ord(i)
        print("{}".format(chr(x - 32) if x in range(97, 123) else i), end="")
        if i == str[-1]:
            print("\n")
