#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
if last_digit > 5:
    print(F"Last digit of {number} is {last_digit} and is greater than 5")
if last_digit == 0:
    print(F"Last digit of {number} is {last_digit} and is 0")
if last_digit < 6 and last_digit != 0:
    print(F"Last digit of {number} and is {last_digit} less than 6 and not 0")
