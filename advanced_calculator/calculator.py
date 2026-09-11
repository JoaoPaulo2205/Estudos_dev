import math
import os

"""operações basicas"""

def add (value1, value2):
    return value1 + value2

def subtract (value1, value2):
    return value1 - value2

def multiply (value1, value2):
    return value1 * value2

def divide (value1, value2):
    return value1 / value2

def remainder (value1, value2):
    return math.fmod(value1,value2)

def validate_operation(operator) -> bool: 
    if operator in ["+", "-", "*", "/", "%"]:
        return True
    return False

def calculate(val1, val2, op):
    if op == "+":
        return add(val1, val2)
    elif op == "-":
        return subtract(val1, val2)
    elif op == "*":
        return multiply(val1, val2)
    elif op == "/":
        return divide(val1, val2)
    elif op == "%":
        return remainder(val1, val2)

print("Welcome to the calculator\n")

while True:
    print("what would you like to calculate?")
    print("1) +\n" \
    "2) -\n" 
    "3) *\n" \
    "4) /\n" \
    "5) %\n"
    "your choice: ", end="")

    operation = input()
    if (validate_operation(operation)):
        print(f"selected operation: {operation}\n")

        print("insert the numbers to be calculated:")
        print("first: ", end="")
        number1 = float(input())

        print("\nsecond: ", end="")
        number2 = float(input())
        print("")

        print(f"calculating {number1} {operation} {number2}")
        result = calculate(number1, number2, operation)

        print(f"{number1} {operation} {number2} = {result}\n")
        print("calculate again? (Y/N) ", end="")

        repeat = input()

        if repeat in ["Y", "y"]:
            os.system('clear')
            continue

        elif repeat in ["N", "n"]:
            print("shuting down!")
            break
        else:
            print("invalid option, shuting down!")
            break
    else:
        print(f"the operation {operation} is invalid! try again!\n\n")

