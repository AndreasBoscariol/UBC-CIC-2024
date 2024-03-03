import sys
import os
from langchain.llms.bedrock import Bedrock

#The following section is to configure the ai model and generated text

#finds what ai model we'll be using
def get_inference_parameters(model): #return a default set of parameters based on the model's provider
    bedrock_model_provider = model.split('.')[0] #grab the model provider from the first part of the model id
    
    if (bedrock_model_provider == 'anthropic'): #Anthropic model
        return { #anthropic
            "max_tokens_to_sample": 512,
            "temperature": 0, 
            "top_k": 250, 
            "top_p": 1, 
            "stop_sequences": ["\n\nHuman:"] 
           }
    
    elif (bedrock_model_provider == 'ai21'): #AI21
        return { #AI21
            "maxTokens": 512, 
            "temperature": 0.3, 
            "topP": 0.5, 
            "stopSequences": [], 
            "countPenalty": {"scale": 0 }, 
            "presencePenalty": {"scale": 0 }, 
            "frequencyPenalty": {"scale": 0 } 
           }
# NO OTHER MODELS WILL BE USED

#verifies aws credentials and runs the ai
def get_text_response(model, input_content): #text-to-text client function
    
    model_kwargs = get_inference_parameters(model) #get the default parameters based on the selected model
    
    llm = Bedrock( #create a Bedrock llm client
        credentials_profile_name=os.environ.get("BWB_PROFILE_NAME"), #sets the profile name to use for AWS credentials (if not the default)
        region_name=os.environ.get("BWB_REGION_NAME"), #sets the region name (if not the default)
        endpoint_url=os.environ.get("BWB_ENDPOINT_URL"), #sets the endpoint URL (if necessary)
        model_id=model, #use the requested model
        model_kwargs = model_kwargs
    )
    
    return llm.predict(input_content) #return a response to the prompt


def list_scrapper(meals_string):
    # Split the meals string by days
    meals_by_day = meals_string.strip().split('\n\n')
    
    # List to store all food items
    food_items = []
    
    # Iterate over each day's meals
    for day_meals in meals_by_day:
        # Split the day's meals into lines
        day_lines = day_meals.strip().split('\n')
        
        # Iterate over each line to extract food items
        for line in day_lines:
            # Check if the line contains a food item
            if ':' in line:
                # Split the line into meal and food item
                meal, food_item = map(str.strip, line.split(':', 1))
                
                # Add food item to the list
                food_items.append(food_item.strip('"'))
    
    return food_items
    
    
#Prompt generation

#Model is either ai21.j2-ultra-v1 or anthropic.claude-v2:1
def generate_prompt(prompt, Model):
    response = get_text_response(Model, prompt)
    print(response)
    foodList = list_scrapper(response)
    print(foodList)
    return foodList
    
def user_feedback(previous_prompt, user_prompt, Model):
    newPrompt = f"""You previously gave a meal plan of {previous_prompt} but the user has the following feedback: {user_prompt}. Generate a new meal plan using both pieces of information. Remember the rules are: Only respond with a list of the names of meals, no description, no sides. There should be 3 meals for 7 days (21 total meals each with 1 item per meal), which total to the Calorie Goal of 2000 calories a day. They should exclude any Dietary Restrictions: None. Do not include the day of the week."""
    response = get_text_response(Model, newPrompt)
    print(response)
    foodList = list_scrapper(response)
    print(foodList)
    return(foodList)
