#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if number < 0:
    l_digit *= -1
if l_digit > 5:
    print(F"Last digit of {number} is {l_digit} and is greater than 5")
if l_digit == 0:
    print(F"Last digit of {number} is {l_digit} and is 0")
if l_digit < 6 and last_digit != 0:
    print(F'Last digit of {number} is {l_digit} and is less than 6 and not 0')
