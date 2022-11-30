#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = str(number)[-1]
if int(lastDig) == 0:
    print(f"Last digit of {number} is {lastDig} and is 0")
elif number > 0 and int(lastDig) < 6:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0")
elif int(lastDig) > 5 and number > 0:
    print(f"Last digit of {number} is {lastDig} and is greater than 5")
else:
    print(f"Last digit of {number} is -{lastDig} and is less than 6 and not 0")