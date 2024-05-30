import streamlit as st
# Title of the app
st.title("Student Information")
name=st.text_input("Enter your name", "Polina")
age=st.slider("Select the student's age:", min_value=1)

if st.button("Display information") :
    st.write("Student name :", name)
    st.write("Student age :", age)