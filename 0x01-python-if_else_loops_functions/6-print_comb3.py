#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if x == i:
            continue
        elif x < i:
            continue
        else:
            if i == 8 and x == 9:
                print("{}{}".format(i, x))
            else:
                print("{}{}".format(i, x), end=", ")
