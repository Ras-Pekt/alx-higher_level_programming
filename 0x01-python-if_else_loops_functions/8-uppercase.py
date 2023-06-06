#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            CH = chr(ord(ch) - 32)
            print("{}".format(CH), end="")
        else:
            print("{}".format(ch), end="")

    print("\n", end="")
