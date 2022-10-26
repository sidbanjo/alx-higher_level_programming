#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def _calc():
    ar = sys.argv
    ar_len = len(ar)
    funcs = {"+": add, "-": sub, "*": mul, "/": div}

    if ar_len != 4 :
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(ar[1])
        b = int(ar[3])
        op = ar[2]
        if op not in funcs.keys():
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            for key, value in funcs.items():
                if key == op:
                    print(f"{a} {key} {b} = {value(a, b)}")


if __name__ == "__main__":
    _calc()
