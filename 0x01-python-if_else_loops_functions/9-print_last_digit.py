#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        num = -1 * number
    else:
        num = number
    while num > 10:
        num %= 10

    print("{}".format(num), end="")
    return num
