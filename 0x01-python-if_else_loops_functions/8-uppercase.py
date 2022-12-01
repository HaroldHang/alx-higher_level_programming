#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in range(0, len(str)):
        if ord(str[i]) > 64 and ord(str[i]) < 91:
            string += str[i]
        elif ord(str[i]) > 96 and ord(str[i]) < 124: 
            string += chr(ord(str[i]) - 32)
        else:
            string += str[i]
    print(string)
