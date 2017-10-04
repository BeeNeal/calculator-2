"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculate(user_input):
    """prefix calculator that evaluates user user_input

    enter operator and evaluate following numbers"""

    tokens = user_input.split(" ")
    answer = "I don't understand."

    for i in tokens[1:]:
        try:
            float(i)
        except:
            return answer

    try:
        num1 = float(tokens[1])
    except:
        pass
    try:
        num2 = float(tokens[2])
    except:
        pass
    try:
        num3 = float(tokens[3])
    except:
        pass

    if tokens[0] == "+":
        answer = add(num1, num2)

    elif tokens[0] == "-":
        answer = subtract(num1, num2)

    elif tokens[0] == "*":
        answer = multiply(num1, num2)

    elif tokens[0] == "/":
        answer = divide(num1, num2)

    elif tokens[0] == "square":
        answer = square(num1)

    elif tokens[0] == "cube":
        answer = cube(num1)

    elif tokens[0] == "pow":
        answer = power(num1, num2)

    elif tokens[0] == "mod":
        answer = mod(num1, num2)

    elif tokens[0] == "add_mult":
        answer = add_mult(num1, num2, num3)

    elif tokens[0] == "add_cubes":
        answer = add_cubes(num1, num2)




    return answer

def run_calc():
    """loop through calculator"""

    while True: # user_input != "q":
        user_input = raw_input("Please enter your expression: ")
        if user_input == "q":
            break
        print calculate(user_input)


run_calc()
