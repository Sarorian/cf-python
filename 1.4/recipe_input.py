import pickle

def take_recipe():
    recipe_name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (minutes): "))
    ingredients = input("Enter ingredients (separated by comma): ").split(",")
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    return {"name": recipe_name, "cooking_time": cooking_time, "ingredients": ingredients, "difficulty": difficulty}

def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

filename = input("Enter filename to open or create: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}
except Exception as e:
    print("An error occurred:", e)
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

num_recipes = int(input("How many recipes would you like to enter? "))

for _ in range(num_recipes):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

with open(filename, 'wb') as file:
    pickle.dump(data, file)
