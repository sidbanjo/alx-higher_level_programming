#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("")
    up_str = ""
    for i in str:
        x = ord(i)
        if x in range(97, 123):
            up_str += chr(x - 32)
        else:
            up_str += i
    print(up_str)
