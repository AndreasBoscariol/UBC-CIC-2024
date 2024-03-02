pip install streamlit

# main.py
import streamlit as st


def main():
    # Title
    st.title('Meal Planner')
    # Header
    st.header('Header')
    # Text
    st.text('Some text')
    # SubHeader
    st.subheader('Sub header')
    #Button
    st.button('Hit me')
    #TextInput
    st.text_input('Enter some text')
    #NumberInput
    st.number_input('Enter a number')
   

if __name__ == "__main__":
    main()

streamlit run main.py
