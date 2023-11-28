#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdgt = number % 10
else:
    lastdgt = number % -10
if lastdgt == 0:
    print(f"Last digit of {number} is {lastdgt} and is 0")
elif lastdgt < 6:
    print(f"Last digit of {number} is {lastdgt} and is less than 6 and not 0")
elif lastdgt > 5:
    print(f"Last digit of {number} is {lastdgt} and is greater than 5")
