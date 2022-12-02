#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    mods = dir(hidden_4)
    for i in range(0, len(mods)):
        if mods[i][0] == "_":
            continue
        else:
            print(mods[i])
