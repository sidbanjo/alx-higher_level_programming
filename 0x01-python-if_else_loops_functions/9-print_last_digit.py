#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = (0 - number) % 10
    else:
        x = number % 10
    print("{}".format(x), end="")
    return x
