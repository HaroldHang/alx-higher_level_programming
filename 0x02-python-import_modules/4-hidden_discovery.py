#!/usr/bin/python3
import compileall
import marshal
if __name__ == "__main__":
    s=compileall.compile_file('hidden_4.pyc')
    print("Hello World")
    print(s)