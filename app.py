import streamlit as st
import math

st.title("Advanced Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

add_btn = st.button("Addition")
sub_btn = st.button("Subtraction")
mul_btn = st.button("Multiplication")
div_btn = st.button("Division")
pow_btn = st.button("Power")
sin_btn = st.button("Sin")
cos_btn = st.button("Cos")
tan_btn = st.button("Tan")

if sin_btn:
    result = math.sin(num1)
    st.success(f"The Sin of {num1} is {result:.2f}")
elif cos_btn:
    result = math.cos(num1)
    st.success(f"The Cos of {num1} is {result:.2f}")
elif tan_btn:
    result = math.tan(num1)
    st.success(f"The Tan of {num1} is {result:.2f}")
else:
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
    else:
        result = None

    if result is not None:
        st.success(f"Result is {result}")

    
    
    
    
    
    
    
    

 
st.write("---")
st.write("created by __")
st.write("       Shib Kumar Saraf ")
