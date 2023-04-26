import streamlit as st

# Title of the app
st.title("Simple Streamlit App")

# Text input
user_input = st.text_input("Enter some text:")

# Display the user input
st.write("You entered:", user_input)
