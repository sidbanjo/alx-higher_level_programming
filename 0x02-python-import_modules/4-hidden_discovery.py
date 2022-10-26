#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    namelist = dir(hidden_4)
    namelist.sort()
    for x in namelist:
        if x[0:2] == "__":
            continue
        else:
            print(f"{x}")
