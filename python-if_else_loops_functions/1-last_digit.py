#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Extracts the last digit of hte random number
last_digit = abs(number) % 10
# Adjusts the sign of the last digit if negative
if number < 0:
    last_digit *= -1
print("Last digit of", number, "is", last_digit, end=" ")

if number > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
