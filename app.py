import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    else:
        result = num1 / num2
    
    st.success(f"Result is {result}")
