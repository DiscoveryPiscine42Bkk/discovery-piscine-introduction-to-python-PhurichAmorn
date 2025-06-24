#!/usr/bin/env python3

numInput = input("Give me a number: ")

try:
    num = float(numInput)
    if num.is_integer() is False:
        num += 1
    
    print(int(num))

except ValueError:
    print("Invalid Input Number")
