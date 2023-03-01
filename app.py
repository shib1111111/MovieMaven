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
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.warning("Division by 0 error. Please enter a non-zero number as divisor.")
            result = "Not defined"
    st.success(f"Result is {result}")

    st.write("---")
st.write("created by __")
st.write("       Shib Kumar Saraf ")
