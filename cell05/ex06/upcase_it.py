#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    string = sys.argv[1]
    string = string.upper()
    print(string)
else:
    print("none")
