#!/usr/bin/env python3

import sys

def downcase_it(string):
    return string.lower()

if len(sys.argv) < 2:
    print("none")

for str in sys.argv:
    if str == sys.argv[0]:
        continue
    else:
        print(downcase_it(str))
