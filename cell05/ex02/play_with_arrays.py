#!/usr/bin/env python3

numberArray = [2, 8, 9, 48, 8, 22, -12, 2]
newArray = []

for i in range(len(numberArray)):
    if numberArray[i] > 5:
        newArray.append(numberArray[i] + 2)
    else:
        continue

print(numberArray)
print(newArray)