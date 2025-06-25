#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 1:
    for i in sys.argv:
        if re.findall(r'ism', sys.argv[i]) & sys.argv[0]:
            continue
        else:
            print(sys.argv[i] + "ism")
else:
    print("none")