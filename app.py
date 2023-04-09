import streamlit as st
import math

# Setting up the calculator layout
st.set_page_config(page_title="Calculator", page_icon=":iphone:", layout="wide")
st.title("Calculator")

col1, col2, col3, col4 = st.beta_columns(4)

with col1:
    num1 = st.number_input("Enter the first number", value=0.0, step=0.01)

with col2:
    num2 = st.number_input("Enter the second number", value=0.0, step=0.01)

# Adding buttons for various operations
add_btn = st.button("+")
sub_btn = st.button("-")
mul_btn = st.button("*")
div_btn = st.button("/")
mod_btn = st.button("%")
pow_btn = st.button("^")
sqrt_btn = st.button("√")
sin_btn = st.button("sin")
cos_btn = st.button("cos")
tan_btn = st.button("tan")
log_btn = st.button("log")
exp_btn = st.button("exp")
clear_btn = st.button("C")

# Performing the selected operation
if sin_btn:
    result = math.sin(num1)
    st.success(f"sin({num1}) = {result:.2f}")
elif cos_btn:
    result = math.cos(num1)
    st.success(f"cos({num1}) = {result:.2f}")
elif tan_btn:
    result = math.tan(num1)
    st.success(f"tan({num1}) = {result:.2f}")
elif sqrt_btn:
    result = math.sqrt(num1)
    st.success(f"√({num1}) = {result:.2f}")
elif log_btn:
    result = math.log10(num1)
    st.success(f"log({num1}) = {result:.2f}")
elif exp_btn:
    result = math.exp(num1)
    st.success(f"exp({num1}) = {result:.2f}")
else:
    if add_btn:
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result:.2f}")
    elif sub_btn:
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result:.2f}")
    elif mul_btn:
        result = num1 * num2
        st.success(f"{num1} * {num2} = {result:.2f}")
    elif div_btn:
        if num2 != 0:
            result = num1 / num2
            st.success(f"{num1} / {num2} = {result:.2f}")
        else:
            st.warning("Division by zero error. Please enter a non-zero number as divisor.")
            result = "Not defined"
    elif mod_btn:
        result = num1 % num2
        st.success(f"{num1} % {num2} = {result:.2f}")
    elif pow_btn:
        result = num1 ** num2
        st.success(f"{num1} ^ {num2} = {result:.2f}")
    else:
        result = None

# Handling cases where the result is not defined
if result is None:
    st.info("Perform an operation to see the result.")

# Adding a clear button to reset the calculator
if clear_btn:
    st.experimental_rerun()

# Importing the CSS file
st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)
