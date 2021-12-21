#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = abs(number)
    last_number = number % 10
    number = -abs(number)
    Mn = -abs(last_number)
if number > 0:
    last_number = number % 10
if Mn > 5:
    print("Last digit of", number, "is", Mn, "and is greater than 5")
elif Mn == 0:
    print("Last digit of", number, "is", Mn, "and is 0")
elif Mn < 6:
    print("Last digit of", number, "is", Mn, "and is less than 6 and not 0")
