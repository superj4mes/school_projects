#!/usr/bin/python3

import random
import string
import sys

def check_input(input):
    try:
        # Try to parse int
        val = int(input)
        if val <= 0 :
            val = 8
        return val
    except ValueError:
        try:
            # Try to parse float
            val = round(float(input))
            if val <= 0 :
                val = 8
            return val
        except ValueError:
            # if neither success input is string
            val = 8
            return val

# user input password length
userInput = sys.argv[-1]
# function tryparse to return right value
length = check_input(userInput)
# save string library of alphabets and digits in variable
letters = string.ascii_letters + string.digits
# join random letters to form password
result_str = ''.join([random.choice(letters) for i in range(length)])
# print password
print(result_str)
