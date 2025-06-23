#!/usr/bin/env python3

print("Enter a number")
inputLine = input()

num = int(inputLine)

for i in range(10): # will loop from 0 to 9
    print(f"{i} x {num} = {i*num}")