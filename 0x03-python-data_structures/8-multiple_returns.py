#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    character = ""
    if sentence == "":
        character = None
    else:
        length = len(sentence)
        character = sentence[0]
    return (length, character)