#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:                                      #
    number = abs(number)                            # this function check if number is positive or negative, if it's negative, it's going to convert into a positive number 
    last_number = number % 10                       # and after this, it's use modulo to get the last digit and after, it's convert the last digit into a negative number.
    number = -abs(number)                           #
    mod_number = -abs(last_number)                  #
if number > 0
    last_number = number % 10
    mod_number = last_number
if last_number > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'.format(number, mod_number))
if last_number == 0:
    print('Last digit of {:d} is {:d} and is zero'.format(number, mod_number))
if last_number < 6 and number > 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.format(number, mod_number))
