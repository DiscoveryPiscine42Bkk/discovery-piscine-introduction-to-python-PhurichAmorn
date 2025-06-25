#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        array = []
        while start <= end:
            array.append(start)
            start += 1

        print(array)

    except ValueError:
        print("Please Enter a valid arguments!")
else:
    print("none")