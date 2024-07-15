import streamlit as st
import pandas as pd
import numpy as np

st.title("WELCOME TO UBAID'S CALCULATOR")
st.header("A simple calculator performs basic Arithmatic Functions  ")

a = st.number_input("Enter 1st number ")
b = st.number_input("Enter 2nd number ")
operation = st.radio('Select an operation \U00002935 ', ['Add \U00002795', 'Subtract \U00002796', 'Multiply \U00002716', 'Divide \U0001F4C9'])

if operation == "Add":
    import addition
    result = addition.add(a, b)

if operation == "Subtract":
    import subtraction
    result = subtraction.subtract(a , b)

if operation == "Multiply":
    import multiplication
    result = multiplication.multiply(a , b)

if operation == "Divide":
    import division
    result = division.divide(a , b)
    if b == 0:
       st.error("ZeroDivisionError")

if st.button('Calculate \U0001F4BB'):
  st.success(result)
if st.checkbox('Perform another calculation \U0001F504'):
  st.rerun()
