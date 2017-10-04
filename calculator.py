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
    num1 = float(tokens[1])
    try:
        num2 = float(tokens[2])
        num2 = float(tokens[3])
    except:
        pass
    # print tokens
    for i in tokens[1:]:
        try:
            float(i)
        except:
            return answer

    if tokens[0] == "+":
        answer = add(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "-":
        answer = subtract(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "*":
        answer = multiply(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "/":
        answer = divide(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "square":
        answer = square(float(tokens[1]))

    elif tokens[0] == "cube":
        answer = cube(float(tokens[1]))

    elif tokens[0] == "pow":
        answer = power(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "mod":
        answer = mod(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "add_mult":
        answer = add_mult(float(tokens[1]), float(tokens[2]), float(tokens[3]))

    elif tokens[0] == "add_cubes":
        answer = add_cubes(float(tokens[1]), float(tokens[2]))




    return answer

def run_calc():
    """loop through calculator"""

    while True: # user_input != "q":
        user_input = raw_input("Please enter your expression: ")
        if user_input == "q":
            break
        print calculate(user_input)


run_calc()
