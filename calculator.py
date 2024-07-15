import streamlit as st
import pandas as pd
import numpy as np
import addition
import subtraction
import multiplication
import division

st.title("WELCOME TO UBAID'S CALCULATOR")
st.header("A simple calculator performs basic Arithmetic Functions")

# Initialize result to None
result = None

a = st.number_input("Enter 1st number")
b = st.number_input("Enter 2nd number")
operation = st.radio('Select an operation \U00002935 ',
                     ['Add \U00002795', 'Subtract \U00002796', 'Multiply \U00002716', 'Divide \U0001F4C9'])

if operation == "Add \U00002795":
    result = addition.add(a, b)
elif operation == "Subtract \U00002796":
    result = subtraction.subtract(a, b)
elif operation == "Multiply \U00002716":
    result = multiplication.multiply(a, b)
elif operation == "Divide \U0001F4C9":
    result = division.divide(a, b)
    if b == 0:
        st.error("ZeroDivisionError")

if st.button('Calculate \U0001F4BB'):
    if result is not None:
        if isinstance(result, str):  # Check if result is an error message
            st.error(result)
        else:
            st.success(f'Result: {result}')
    else:
        st.error("Please select a valid operation.")

if st.checkbox('Perform another calculation \U0001F504'):
    st.experimental_rerun()
