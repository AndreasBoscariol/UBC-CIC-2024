import app
from edamam import getMacros


def parseMeal():
    
    getMarcros

def generateMealPlan():

    #calculate BMR
    if app.gender=='m':
        BMR=10*app.weight+6.25*app.height-5*app.age+5
    else:
        BMR=10*app.weight+6.25*app.height-5*app.age-161
        
    PAL=1.6
    cal=BMR*PAL*app.modifier

    inital_prompt = f"""User
    Objective: Generate a comprehensive meal plan with three meals per day that adheres to the following criteria:
    
    Meal Structure: The meal plan should consist of breakfast, lunch, and dinner. 
        
    Nutritional Balance: Each meal should offer a balanced distribution of macronutrients (proteins, carbohydrates, fats) and include a variety of fruits and vegetables to ensure nutritional completeness.
        
    Specific Requests:
        
    Calorie Goal: {calories}
    Dietary Restrictions: {diet}
    Expected Outcome: A 21 meals with simple names tailored to the specified calorie goal, dietary restrictions. Each meal description should include the name of the dish
    
    Afterwards, list each meal named as concisely as possible surrounded by *
    """
