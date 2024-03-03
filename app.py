import streamlit as st
from main import generateMealPlan
import matplotlib.pyplot as plt

def main():
    # Title
    st.title('Meal Planner')
   
    # Header
    st.header('Create your own meal plan!')

    # Text
    st.text('Select')
    with st.form('form'):
        #Radio
        gender = st.radio('Gender', ['Male','Female'])
        #NumberInput1
        age = st.number_input('Age', step=1, min_value=0, max_value=100)
        #NumberInput2
        weight = st.number_input('Weight (lbs)', step=1.0)
        #NumberInput3
        height = st.number_input('Height (cm)', step=1.0)
        #Selectbox1
        PAL = st.selectbox('Activity Level', ['Select', 'Extrememly Inactive','Sedentary','Moderately Active','Vigorously Active','Extremely Active'])
        physlvl = {'Extremely Inactive': 1.40,'Sedentary': 1.55, 'Moderately Active': 1.85, 'Vigorously Active': 2.20, 'Extremely Active': 2.40}
        #Selectbox2
        modifier = st.selectbox('Modifier', ['Select', 'Lose Weight', 'Gain Weight', 'Maintain Weight'])
        weightmod = {'Lose weight': 1,'Maintain Weight': 1.2, 'Gain Weight': 1.4,}
        #TextInput
        diet = st.text_input('Dietary Restrictions', 'Input some text here.')
        #Button
        if st.button('Generate Your Meal Plan'):
            generateMealPlan()
    
def updateChart(fat,carbs,protein,total):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Fat', 'Protein', 'Carbs'
    sizes = [fat/total, protein/total, carbs/total]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.pyplot(fig1)

if __name__ == "__main__":
    main()
