import streamlit as st
import math

# Define calculator operations
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

# Define calculator layout
st.set_page_config(page_title="Calculator", page_icon=":iphone:", layout="wide")
st.title("Calculator")

# Import CSS
st.markdown('<link rel="stylesheet" type="text/css" href="style.css">', unsafe_allow_html=True)

button_labels = [
    ["(", ")", "C", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["±", "0", ".", "=", "%", "^", "√"]
]

# Define button mapping
button_map = {
    "C": "clear",
    "÷": "/",
    "×": "*",
    "^": "**",
    "√": "square_root",
    "=": "calculate"
}

# Generate calculator buttons
col_width = st.sidebar.get_column_width() // len(button_labels[0])
for row in button_labels:
    button_row = st.empty()
    for label in row:
        operation = button_map.get(label, label)
        if operation == "calculate":
            button = button_row.button(label, key=operation, width=col_width*2)
        elif operation == "clear":
            button = button_row.button(label, key=operation, width=col_width)
        else:
            button = button_row.button(label, key=operation, width=col_width)
        st.markdown(f'<style>div.stButton > button[key="{operation}"] {{background-color: #f0f0f0; color: #333333;}}</style>', unsafe_allow_html=True)

# Define input field for calculator
input_field = st.text_input("Enter calculation", key="input")

# Handle user input and display result
if button and operation == "clear":
    input_field.value = ""
elif button and operation == "calculate":
    try:
        result = eval(input_field.value)
        input_field.value = str(result)
    except (SyntaxError, ValueError, ZeroDivisionError) as e:
        input_field.value = str(e)
