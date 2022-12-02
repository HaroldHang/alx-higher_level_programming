#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else :
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
            exit(0)
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
            exit(0)
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
            exit(0)
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
            print(0)
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
