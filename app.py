import streamlit as st
import matplotlib.pyplot as plt
from edamam import getMacros
from GenerateResponse import generate_prompt

st.set_page_config(
        page_title='Meal Planner',
        page_icon='🍴️',
        layout='wide',
    )

def main():
    # Title of the app
    st.title('Meal Planner App')
    
    # Introduction or Header
    st.header('Design Your Custom Meal Plan')

    # Brief description or instruction for the user
    st.write('Fill out the details below to generate your personalized meal plan.')

    # Creating a form for user input
    with st.form(key='meal_planner_form'):
        # User inputs
        gender = st.radio('Gender', ['Male', 'Female']) # Gender selection
        age = st.number_input('Age', min_value=1, max_value=100, value=25) # Age input
        weight = st.number_input('Weight (lbs)', min_value=50.0, max_value=400.0, value=150.0) # Weight input
        height = st.number_input('Height (cm)', min_value=100.0, max_value=250.0, value=170.0) # Height input
        activity_levels = {'Extremely Inactive': 1.2, 'Sedentary': 1.3, 'Moderately Active': 1.55, 'Vigorously Active': 1.725, 'Extremely Active': 1.9}
        activity_level = st.selectbox('Activity Level', options=list(activity_levels.keys())) # Activity level selection
        goal = st.selectbox('Goal', ['Lose Weight', 'Maintain Weight', 'Gain Weight']) # Weight goal
        diet = st.text_input('Dietary Restrictions (optional)') # Dietary restrictions input
        
        # Submit button for the form
        submit_button = st.form_submit_button(label='Generate Your Meal Plan')
        
        if submit_button:
            foodList=generateMealPlan(gender, age, weight, height, activity_levels[activity_level], goal, diet)
            dailyCharts(foodList)
            
            
def generateMealPlan(gender, age, weight, height, PAL, goal, diet):
    modelUsed = "ai21.j2-ultra-v1"
    # BMR and Daily Caloric Need Calculation
    if gender == 'Male':
        BMR = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        BMR = 10 * weight + 6.25 * height - 5 * age - 161

    # Adjusting calories based on the user's goal
    goal_modifiers = {'Lose Weight': 0.85, 'Maintain Weight': 1, 'Gain Weight': 1.15}
    daily_calories = BMR * PAL * goal_modifiers[goal]

    # Display the calculated daily calories
    st.write(f"Your daily caloric need based on the provided information is {daily_calories:.0f} calories.")

    initial_prompt = f"""
    "Only respond with a list of the names of meals, no description, no sides. 
    There should be 3 meals for 7 days (21 total meals each with 1 item per meal), 
    which total to the Calorie Goal of {daily_calories}  a day. 
    They should exclude any Dietary Restrictions: {diet}. Do not include the day of the week.
    """
    
    return generate_prompt(initial_prompt, modelUsed)
    
    
def dailyCharts(foodList):
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"])
   
    with tab1:
        st.write(foodList[0])
        chart([getMacros(foodList[0])[0] / getMacros(foodList[0])[4], foodList[0][1] / getMacros(foodList[0])[4], foodList[0][2] / getMacros(foodList[0])[4]])
        
        st.write(foodList[1])
        chart([getMacros(foodList[1])[0] / getMacros(foodList[1])[4], foodList[1][1] / getMacros(foodList[1])[4], foodList[1][2] / getMacros(foodList[1])[4]])

        st.write(foodList[2])
        chart([getMacros(foodList[2])[0] / getMacros(foodList[2])[4], foodList[2][1] / getMacros(foodList[2])[4], foodList[2][2] / getMacros(foodList[2])[4]])

    with tab2:
        st.write(foodList[3])
        chart([getMacros(foodList[3])[0] / getMacros(foodList[3])[4], foodList[3][1] / getMacros(foodList[3])[4], foodList[3][2] / getMacros(foodList[3])[4]])

        st.write(foodList[4])
        chart([getMacros(foodList[4])[0] / getMacros(foodList[4])[4], foodList[4][1] / getMacros(foodList[4])[4], foodList[4][2] / getMacros(foodList[4])[4]])

        st.write(foodList[5])
        chart([getMacros(foodList[5])[0] / getMacros(foodList[5])[4], foodList[5][1] / getMacros(foodList[5])[4], foodList[5][2] / getMacros(foodList[5])[4]])

    with tab3:
        st.write(foodList[6])
        chart([getMacros(foodList[6])[0] / getMacros(foodList[6])[4], 
               foodList[6][1] / getMacros(foodList[6])[4], 
               foodList[6][2] / getMacros(foodList[6])[4]])
    
        st.write(foodList[7])
        chart([getMacros(foodList[7])[0] / getMacros(foodList[7])[4], 
               foodList[7][1] / getMacros(foodList[7])[4], 
               foodList[7][2] / getMacros(foodList[7])[4]])
    
        st.write(foodList[8])
        chart([getMacros(foodList[8])[0] / getMacros(foodList[8])[4], 
               foodList[8][1] / getMacros(foodList[8])[4], 
               foodList[8][2] / getMacros(foodList[8])[4]])
    
    with tab4:
        st.write(foodList[9])
        chart([getMacros(foodList[9])[0] / getMacros(foodList[9])[4], 
               foodList[9][1] / getMacros(foodList[9])[4], 
               foodList[9][2] / getMacros(foodList[9])[4]])
    
        st.write(foodList[10])
        chart([getMacros(foodList[10])[0] / getMacros(foodList[10])[4], 
               foodList[10][1] / getMacros(foodList[10])[4], 
               foodList[10][2] / getMacros(foodList[10])[4]])
    
        st.write(foodList[11])
        chart([getMacros(foodList[11])[0] / getMacros(foodList[11])[4], 
               foodList[11][1] / getMacros(foodList[11])[4], 
               foodList[11][2] / getMacros(foodList[11])[4]])
    
    with tab5:
        st.write(foodList[12])
        chart([getMacros(foodList[12])[0] / getMacros(foodList[12])[4], 
               foodList[12][1] / getMacros(foodList[12])[4], 
               foodList[12][2] / getMacros(foodList[12])[4]])
    
        st.write(foodList[13])
        chart([getMacros(foodList[13])[0] / getMacros(foodList[13])[4], 
               foodList[13][1] / getMacros(foodList[13])[4], 
               foodList[13][2] / getMacros(foodList[13])[4]])
    
        st.write(foodList[14])
        chart([getMacros(foodList[14])[0] / getMacros(foodList[14])[4], 
               foodList[14][1] / getMacros(foodList[14])[4], 
               foodList[14][2] / getMacros(foodList[14])[4]])
    
    with tab6:
        st.write(foodList[15])
        chart([getMacros(foodList[15])[0] / getMacros(foodList[15])[4], 
               foodList[15][1] / getMacros(foodList[15])[4], 
               foodList[15][2] / getMacros(foodList[15])[4]])
    
        st.write(foodList[16])
        chart([getMacros(foodList[16])[0] / getMacros(foodList[16])[4], 
               foodList[16][1] / getMacros(foodList[16])[4], 
               foodList[16][2] / getMacros(foodList[16])[4]])
    
        st.write(foodList[17])
        chart([getMacros(foodList[17])[0] / getMacros(foodList[17])[4], 
               foodList[17][1] / getMacros(foodList[17])[4], 
               foodList[17][2] / getMacros(foodList[17])[4]])
    
    with tab7:
        st.write(foodList[18])
        chart([getMacros(foodList[18])[0] / getMacros(foodList[18])[4], foodList[18][1] / getMacros(foodList[18])[4], foodList[18][2] / getMacros(foodList[18])[4]])
    
        st.write(foodList[19])
        chart([getMacros(foodList[19])[0] / getMacros(foodList[19])[4], foodList[19][1] / getMacros(foodList[19])[4], foodList[19][2] / getMacros(foodList[19])[4]])
    
        st.write(foodList[20])
        chart([getMacros(foodList[20])[0] / getMacros(foodList[20])[4], foodList[20][1] / getMacros(foodList[20])[4], foodList[20][2] / getMacros(foodList[20])[4]])

def chart(sizes):
    fig, ax = plt.subplots()  # Define fig and ax here
    labels = 'Fat', 'Protein', 'Carbs'
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)



if __name__ == "__main__":
    main()
