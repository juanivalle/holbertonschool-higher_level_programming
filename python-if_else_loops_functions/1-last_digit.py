#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
las = abs(number) % 10
if las > 5:
    print(f"Last digit of {number} is {las} and is greater than 5")
elif las == 0:
    print(f"Last digit of {number} is {las} and is 0")
else:
    if number < 0:
        print(f"Last digit of {number} is -{las} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {las} and is less than 6 and not 0")
