#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        n = True
    except:
        n = False
    return n
