#!/usr/bin/python3
import sys


def arguments():
    ar = sys.argv
    ar_len = len(ar) - 1

    if ar_len == 0:
        print(f"{ar_len} arguments.")
    elif ar_len == 1:
        print(f"{ar_len} argument:")
        print(f"1: {ar[1]}")
    else:
        print(f"{ar_len} arguments:")
        for x in range(1, ar_len + 1):
            print(f"{x}: {ar[x]}")


if __name__ == "__main__":
    arguments()
