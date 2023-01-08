#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if last > 5:
    print(f"last digit of {number:d} is {number % 10} and is greater than 5")
elif last == 0:
    print(f"last digit of {number:d} is {last} and is 0")
if last < 6 and last != 0:
    print(f"last digit of {number:d} is {last} and is less than 6 and not 0")
