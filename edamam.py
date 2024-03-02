import requests
   
APP_ID = '38a686ba'
APP_KEY = 'c9f3fd2bc6d9e8a0e65ae08058907de5'

def search_food(food, health, calories):
    url = f'https://api.edamam.com/api/food-database/v2/parser'
    params = {
        'ingr': food, 
        'health': health,
        'calories': calories,
        'app_id': APP_ID,
        'app_key': APP_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

def get_nutrition(food_id):
    url = f'https://api.edamam.com/api/food-database/v2/nutrients'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "ingredients": [
            {
                "quantity": 1,
                "measureURI": "http://www.edamam.com/ontologies/edamam.owl#Measure_unit",
                "foodId": food_id
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload, params={'app_id': APP_ID, 'app_key': APP_KEY})

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

# Example usage
if __name__ == "__main__":
    # Search for a food item
    search_result = search_food('pasta','alcohol-free','0-1000')
    if search_result:
        print("Search Results:")
        for item in search_result['hints']:
            print("- Food:", item['food']['label'])
            print("  Food ID:", item['food']['foodId'])

        # Get nutrition information for a specific food item
        if len(search_result['hints']) > 0:
            food_id = search_result['hints'][0]['food']['foodId']
            nutrition_info = get_nutrition(food_id)
           
            if nutrition_info:
                print("\nNutrition Information:")
                food = ("- Food:", nutrition_info['ingredients'][0]['parsed'][0]['food'])
                calories = ("- Calories:", nutrition_info['calories'])
                fat = ("- Fat:", (nutrition_info['totalNutrients'])['FAT']['quantity'])
                protein = ("- Protein:", (nutrition_info['totalNutrients'])['PROCNT']['quantity'])
                carbs = ("- Carbs:", (nutrition_info['totalNutrients'])['CHOCDF']['quantity'])
