#!/usr/bin/python3
""" function that returns a string "Best School" """


def magic_string(n=1):
    magic_string.counter = getattr(magic_string, "counter", 0) + 1
    result = "BestSchool, " * magic_string.counter
    return result.rstrip(", ")
