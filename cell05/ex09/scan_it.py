#!/usr/bin/env python3

import sys
import re

if len(sys.argv) < 2:
    print("none")
else:
    search = sys.argv[1]
    string = sys.argv[2]

    found = re.findall(rf'\b{search}\b', string)

    print(len(found))