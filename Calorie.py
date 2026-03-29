import requests

def get_calories(food_name):
    # Replace these with your actual API credentials
    APP_ID = "YOUR_APP_ID"
    APP_KEY = "YOUR_APP_KEY"
    
    url = f"https://api.edamam.com/api/food-database/v2/parser"
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "ingr": food_name,
        "nutrition-type": "cooking"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Check for errors
        data = response.json()

        if data['hints']:
            # Grab the first result from the search
            food_data = data['hints'][0]['food']
            label = food_data['label']
            calories = food_data['nutrients']['ENERC_KCAL']
            
            print(f"\n--- Results for '{label}' ---")
            print(f"Calories: {calories:.2f} kcal (per 100g/serving)")
        else:
            print("Sorry, I couldn't find that food item.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("--- AI Calorie Lookup Tool ---")
    user_input = input("Enter a food item: ")
    get_calories(user_input)
