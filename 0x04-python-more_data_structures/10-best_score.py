#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    score_best = ""
    for key, value in a_dictionary.items():
        if value >= score:
            score = value
            score_best = key
    return score_best
