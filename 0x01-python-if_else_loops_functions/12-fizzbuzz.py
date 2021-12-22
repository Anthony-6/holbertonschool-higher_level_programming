#!/usr/bin/env python3
def fizzbuzz():
    for numero in range(1, 101):
        Fizz = numero % 3 == 0
        Buzz = numero % 5 == 0
        FizzBuzz = Fizz and Buzz == 0
        if FizzBuzz == 1:
            print('Fizz'.format(FizzBuzz), end=" ")
        elif Fizz == 1:
            print('FizzBuzz'.format(Fizz), end=" ")
        elif Buzz == 1:
            print('Buzz'.format(Buzz), end=" ")
        else:
            print('{}'.format(numero), end=" ")
