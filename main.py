import sys
import os
from langchain.llms.bedrock import Bedrock

import edamam
import app
from edamam import search_food

food_name = 'pasta'
health_labels = 'alcohol-free'
calories_range = '0-1000'

food = edamam.food
calories = edamam.calories
fat = edamam.fat
protein = edamam.protein
carbs = edamam.carbs


def generateMealPlan():

    #calculate BMR
    if app.gender=='m':
        BMR=10*app.weight+6.25*app.height-5*app.age+5
    else:
        BMR=10*app.weight+6.25*app.height-5*app.age-161
        
    PAL=1.6
    cal=BMR*PAL*app.modifier

    prompt = f"""Objective: Generate a comprehensive meal plan with three meals per day that adheres to the following criteria:
    
    Meal Structure: The meal plan should consist of breakfast, lunch, and dinner. 
    
    Nutritional Balance: Each meal should offer a balanced distribution of macronutrients (proteins, carbohydrates, fats) and include a variety of fruits and vegetables to ensure nutritional completeness.
    
    Simple Recipes: Prefer recipes that are simple to prepare, with steps and ingredients that are easily accessible and budget-friendly. Each recipe should come with a brief description, ingredient list, and approximate preparation time.
    
    Budget Considerations: Provide cost estimates for the meals and suggestions on how to optimize spending, such as using seasonal ingredients or cost-effective substitutes.
    
    Adaptability: Offer alternative ingredients or adjustments for each meal to accommodate potential variations in dietary restrictions or preferences not initially specified.
    
    Specific Requests:
    
    Calorie Goal: {cal}
    Dietary Restrictions: {app.diet}
    Expected Outcome: A detailed 7-day meal plan that includes breakfast, lunch, and dinner recipes tailored to the specified calorie goal, dietary restrictions, and budget. Each meal description should include the name of the dish, a list of ingredients, preparation instructions, and an estimated cost.
    """




#The following section is to configure the ai model and generated text

def get_interference_parameters(model)
    bedrock_model_provider = model.split('.')[0] #function caller
    
    if (bedrock_model_provider == 'anthropic'):
        return { # anthropic information
            "max_tokens_to_sample": 512,
            "temperature": 0,
            "top_k": 250,
            "top_p": 1,
            "stop_sequences": ["\n\nHuman"]
        }
    elif (bedrock_model_provider == 'ai21'): #AI21
        return { # A121 information
            "maxTokens": 512,
            "temperature": 0,
            "topP": 0.5,
            "stopSequences": {"scale": 0},
            "pre"
