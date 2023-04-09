import streamlit as st
import math

st.set_page_config(page_title="Advanced Calculator", page_icon=":heavy_division_sign:")

st.title("Advanced Calculator")

col1, col2 = st.beta_columns([4, 1])

with col1:
    num1 = st.number_input("Enter the first number")
    num2 = st.number_input("Enter the second number")

    add_btn = st.button("+")
    sub_btn = st.button("-")
    mul_btn = st.button("*")
    div_btn = st.button("/")
    pow_btn = st.button("x^y")
    sqrt_btn = st.button("sqrt(x)")
    log_btn = st.button("log(x)")

    sin_btn = st.button("Sin(x)")
    cos_btn = st.button("Cos(x)")
    tan_btn = st.button("Tan(x)")
    clear_btn = st.button("Clear")

with col2:
    st.write("")
    st.write("Result")
    st.write("----")
    if add_btn:
        result = num1 + num2
    elif sub_btn:
        result = num1 - num2
    elif mul_btn:
        result = num1 * num2
    elif div_btn:
        if num2 != 0:
            result = num1 / num2
        else:
            st.warning("Division by 0 error. Please enter a non-zero number as divisor.")
            result = "Not defined"
    elif pow_btn:
        result = num1 ** num2
    elif sqrt_btn:
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            st.warning("Square root of negative number is not defined.")
            result = "Not defined"
    elif log_btn:
        if num1 > 0 and num2 > 1:
            result = math.log(num1, num2)
        else:
            st.warning("Logarithm is not defined for the given inputs.")
            result = "Not defined"
    elif sin_btn:
        result = math.sin(num1)
    elif cos_btn:
        result = math.cos(num1)
    elif tan_btn:
        result = math.tan(num1)
    elif clear_btn:
        num1 = 0
        num2 = 0
        result = 0
    else:
        result = None

    if result is not None:
        st.write(result)

st.write("")
st.write("---")
st.write("created by Shib Kumar Saraf") 
