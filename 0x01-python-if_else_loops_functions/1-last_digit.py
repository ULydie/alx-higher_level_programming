#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    numb = number * -1
    numb = numb % 10
    numb = numb * -1
else:
    numb = number % 10
    print("Last digit of {}".format(number), end=' ')

if numb > 5:
    print("is {} and is greater than 5".format(numb))
elif numb == 0:
    print("is {} and is 0".format(numb))
elif numb < 6 and numb != 0:
    print("is {} and is less than 6 and not 0".format(numb))
