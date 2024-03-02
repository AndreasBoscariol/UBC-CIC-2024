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
    st.button('Generate Your Meal Plan')
    #Button2
    st.button('Clear')
    #TextInput
    st.text_input('e.g. Pasta')
    #NumberInput
    st.number_input('e.g. 30')
    #Selectbox
    st.selectbox('What is your goal?', [1,2,3])
   

if __name__ == "__main__":
    main()

streamlit run main.py
