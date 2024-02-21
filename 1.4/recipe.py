import pickle

recipe = { 'Recipe Name': 'Tea',
            'Ingredients': 'Tea leaves, Water, Sugar',
            'Cooking Time': '5 Minutes',
            'Difficulty': 'Easy'}

my_file = open('recipe_binary.bin', 'wb')
pickle.dump(recipe, my_file)
my_file.close()

with open('recipe_binary.bin', 'rb') as my_file:
    recipe = pickle.load(my_file)

print("Recipe for " + recipe['Recipe Name'])
print("Ingredients: " + recipe['Ingredients'])
print("Cook Time: " + recipe['Cooking Time'])
print("Difficulty: " + recipe['Difficulty'])