import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2

def percentage(num1, num2):
    return num1 * (num2 / 100)

def exponent(num1, num2):
    return num1 ** num2

def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number!")
    return math.sqrt(num)

def calculate(operation, num1, num2=None):
    if operation == "+":
        return add(num1, num2)
    elif operation == "-":
        return subtract(num1, num2)
    elif operation == "*":
        return multiply(num1, num2)
    elif operation == "/":
        return divide(num1, num2)
    elif operation == "%":
        return percentage(num1, num2)
    elif operation == "^":
        return exponent(num1, num2)
    elif operation == "sqrt":
        return square_root(num1)
    else:
        raise ValueError("Invalid operation!")


st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
