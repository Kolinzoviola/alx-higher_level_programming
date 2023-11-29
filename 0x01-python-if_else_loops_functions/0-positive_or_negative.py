#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:      # conditional statement
    print(f'{number} is positive')      # this is printed if positive
if number < 0:      # condition statement for another block of code
    print(f'{number} is negative')  # printed if Negative
if number == 0:     # condition for number == 0
    print(f'{number} is zero')      # printed if true
