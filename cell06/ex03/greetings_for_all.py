#!/usr/bin/env python3

def greetings(name=None):
    if not name:
        print("Heelo, noble stanger.")
    elif not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}")

greetings('Alexandra')
greetings('Will')
greetings()
greetings(42)