#!/usr/bin/env python3

print("Enter the first number:")
num1 = input()

print("Enter the second number:")
num2 = input()

num1 = int(num1)
num2 = int(num2)

result = num1 * num2

print(f"{num1} x {num2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")