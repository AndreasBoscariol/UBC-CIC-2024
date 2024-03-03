import requests

APP_ID = '38a686ba'
APP_KEY = 'c9f3fd2bc6d9e8a0e65ae08058907de5'

def search_food(food):
    url = 'https://api.edamam.com/api/food-database/v2/parser'
    params = {
        'ingr': food,  
        'app_id': APP_ID,
        'app_key': APP_KEY
    }

    response = requests.get(url, params=params)
    return response.json() if response.ok else None

def get_nutrition(food_id):
    url = 'https://api.edamam.com/api/food-database/v2/nutrients'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "ingredients": [
            {"quantity": 1, "measureURI": "http://www.edamam.com/ontologies/edamam.owl#Measure_unit", "foodId": food_id}
        ]
    }

    response = requests.post(url, headers=headers, json=payload, params={'app_id': APP_ID, 'app_key': APP_KEY})
    return response.json() if response.ok else None

def getMacros(food_name):
    search_result = search_food(food_name)
    if search_result and search_result['hints']:
        food_id = search_result['hints'][0]['food']['foodId']
        nutrition_info = get_nutrition(food_id)
        if nutrition_info:
            # Simplified data extraction
            calories = nutrition_info.get('calories', 'N/A')
            fat = nutrition_info['totalNutrients'].get('FAT', {'quantity': 'N/A'})['quantity']
            protein = nutrition_info['totalNutrients'].get('PROCNT', {'quantity': 'N/A'})['quantity']
            carbs = nutrition_info['totalNutrients'].get('CHOCDF', {'quantity': 'N/A'})['quantity']
            total=fat+calories+protein
            return fat, protein, carbs, total
