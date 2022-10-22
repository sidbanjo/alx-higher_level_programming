#!/usr/bin/python3
import sys


def inf_add():
    ar = sys.argv
    ar_len = len(ar)
    _add = 0

    if ar_len < 2:
        pass
    else:
        for x in range(1, ar_len):
            _add += int(ar[x])
    print(_add)


if __name__ == "__main__":
    inf_add()
