#!/usr/bin/env python3

userInput = input()

for char in userInput:
    if char.isupper():
        char = char.lower()
    else:
        char = char.upper()
    print(char, end="")

print()
