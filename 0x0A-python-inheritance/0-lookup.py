#!/usr/bin/python3
"""All attributes of a class
"""

def lookup(obj):
    """Returs the attributes of a given obj
    """
    return list(obj.__dict__.keys())
