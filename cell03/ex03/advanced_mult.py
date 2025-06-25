#!/usr/bin/env python3

import sys

if len(sys.argv) > 1: # check for the arguments
    print("none")
else:
    i = 0
    while i <= 10:
        num = 0
        print(f"Table de {i}: ", end=" ")
        while num <= 10:
            print(f"{i*num}", end = " ")
            if num == 10:
                print(end = "\n")
            num += 1
        i += 1
