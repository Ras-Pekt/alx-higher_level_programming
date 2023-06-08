#!/usr/bin/python3
import sys
import calculator_1 as calc

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        result = calc.add(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    elif sys.argv[2] == '-':
        result = calc.sub(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    elif sys.argv[2] == '*':
        result = calc.mul(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    elif sys.argv[2] == '/':
        result = calc.div(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
