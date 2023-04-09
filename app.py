import streamlit as st
import math

st.set_page_config(page_title="Calculator", page_icon=":iphone:", layout="wide")

st.title("Calculator")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Enter the first number", value=0.0, step=0.1)
with col2:
    num2 = st.number_input("Enter the second number", value=0.0, step=0.1)

row1 = st.row_container()
add_btn, sub_btn, mul_btn, div_btn, pow_btn = row1.button_group(["+", "-", "×", "÷", "xⁿ"])
row2 = st.row_container()
sin_btn, cos_btn, tan_btn, exp_btn, log_btn = row2.button_group(["sin", "cos", "tan", "eˣ", "log"])

result = None

if sin_btn:
    result = math.sin(num1)
    st.success(f"sin({num1}) = {result:.2f}")
elif cos_btn:
    result = math.cos(num1)
    st.success(f"cos({num1}) = {result:.2f}")
elif tan_btn:
    result = math.tan(num1)
    st.success(f"tan({num1}) = {result:.2f}")
elif exp_btn:
    result = math.exp(num1)
    st.success(f"e^{num1} = {result:.2f}")
elif log_btn:
    result = math.log(num1)
    st.success(f"log({num1}) = {result:.2f}")
elif add_btn:
    result = num1 + num2
    st.success(f"{num1} + {num2} = {result:.2f}")
elif sub_btn:
    result = num1 - num2
    st.success(f"{num1} - {num2} = {result:.2f}")
elif mul_btn:
    result = num1 * num2
    st.success(f"{num1} × {num2} = {result:.2f}")
elif div_btn:
    if num2 != 0:
        result = num1 / num2
        st.success(f"{num1} ÷ {num2} = {result:.2f}")
    else:
        st.warning("Division by 0 error. Please enter a non-zero number as divisor.")
        result = "Not defined"
elif pow_btn:
    result = num1 ** num2
    st.success(f"{num1}^{num2} = {result:.2f}")

if result is None:
    st.info("Please select an operation.")
