#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = int(repr(number)[-1])
if last > 5 and number > 0:
    print(f"Last digit of {number} is {last} and is greater than 5")
if number == 0 and last == 0:
    print(f"Last digit of {number} is {last} and is 0")
if number < 0 and last < 6 and last != 0:
    print(f"Last digit of {number} is -{last} and is less than 6 and not 0")
