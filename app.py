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
        weight = st.number_input('Weight (lbs)', min_value=50.0, max_value=300.0, value=150.0) # Weight input
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
        for food in foodList[:3]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])

    with tab2:
        for food in foodList[3:6]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])
    
    with tab3:
        for food in foodList[6:9]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])
    
    with tab4:
        for food in foodList[9:12]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])
    
    with tab5:
        for food in foodList[12:15]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])
    
    with tab6:
        for food in foodList[15:18]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])
    
    with tab7:
        for food in foodList[18:]:
            st.header(food)
            macros = getMacros(food)
            chart([macros[0] / macros[3], macros[1] / macros[3], macros[2] / macros[3]])

def chart(sizes):
    fig, ax = plt.subplots()  # Define fig and ax here
    labels = 'Fat', 'Protein', 'Carbs'
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)



if __name__ == "__main__":
    main()
