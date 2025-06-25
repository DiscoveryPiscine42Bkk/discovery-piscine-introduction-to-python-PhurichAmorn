#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 1:
    string = sys.argv[1]
    match = re.findall(r'z', string)
    if match:
        for i in match:
            print("z", end="")
        print()
    else:
        print("none")
    
else:
    print("none")