recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or type 'done' to finish): ")
        if ingredient.lower() == "done":
            break
        ingredients.append(ingredient)
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

n = int(input("How many recipes would you like to enter? "))

for _ in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)

for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = 'Easy'
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = 'Medium'
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = 'Intermediate'
    else:
        difficulty = 'Hard'
    
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time: {cooking_time} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print("- " + ingredient)
    print(f"Difficulty Level: {difficulty}")

print("\nAll Ingredients:")
for ingredient in sorted(ingredients_list):
    print("- " + ingredient)