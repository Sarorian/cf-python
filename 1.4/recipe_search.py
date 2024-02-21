import pickle

def display_recipe(recipe):
    print("Recipe Name:", recipe["name"])
    print("Cooking Time:", recipe["cooking_time"], "minutes")
    print("Ingredients:", ", ".join(recipe["ingredients"]))
    print("Difficulty:", recipe["difficulty"])
    print()

def search_ingredient(data):
    print("Available Ingredients:")
    for index, ingredient in enumerate(data["all_ingredients"]):
        print(f"{index + 1}. {ingredient}")

    try:
        ingredient_index = int(input("Enter the number of the ingredient to search for: ")) - 1
        ingredient_searched = data["all_ingredients"][ingredient_index]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
    else:
        print(f"Recipes containing '{ingredient_searched}':")
        found = False
        for recipe in data["recipes_list"]:
            if ingredient_searched in recipe["ingredients"]:
                display_recipe(recipe)
                found = True
        if not found:
            print("No recipes found containing", ingredient_searched)

filename = input("Enter the filename containing recipe data: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please make sure the file exists.")
else:
    search_ingredient(data)
