# main.py
import streamlit as st


def main():
    # Title
    st.title('Meal Planner')

    # Header
    st.header('Header')
   
    # SubHeader
    st.subheader('Sub header')

    # Text
    st.text('Some text')
    
    #Radio
    gender = st.radio('Gender', ['Male','Female'])

   #NumberInput1
    age = st.number_input('Age')

   #NumberInput2
    weight = st.number_input('Weight (lbs)')

   #NumberInput3
    height = st.number_input('Height (cm)')

    #Selectbox1
    scale = st.selectbox('Scale Level', [1,2,3,4,5])
    
    #Selectbox2
    modifier = st.selectbox('Scale Level', ['Lose Weight', 'Gain Weight', 'Maintain Weight'])
    
    #TextInput
    diet = st.text_input('Dietary Restrictions')
    
    #Button
    generate = st.button('Generate Your Meal Plan')


if __name__ == "__main__":
    main()
