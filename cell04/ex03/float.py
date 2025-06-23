#!/usr/bin/env python3

numInput = input("Give me a number: ")

try:
    num = float(numInput)
    if num.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("The number is not a valid value!")

