#!/usr/bin/python3
def uppercase(str):
    str += " "
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 124: 
            print("{:c}".format(ord(str[i]) - 32), end="")
        else:
            print("{:c}".format(ord(str[i])), end="")
