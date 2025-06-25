#!/usr/bin/env python3

import sys

count = len(sys.argv)

if count < 2:
    print("none")
else:
    while (count > 1):
        print(sys.argv[count-1])
        count-=1