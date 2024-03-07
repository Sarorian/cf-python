class Recipe:
    all_ingredients = set()

    def __init__(self, name):
        self._name = name
        self._ingredients = []
        self._cooking_time = None
        self._difficulty = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value):
        self._cooking_time = value

    def add_ingredients(self, *args):
        self._ingredients.extend(args)
        self.update_all_ingredients()

    @property
    def ingredients(self):
        return self._ingredients

    def calculate_difficulty(self):
        if self._cooking_time < 10 and len(self._ingredients) < 4:
            self._difficulty = "Easy"
        elif self._cooking_time < 10 and len(self._ingredients) >= 4:
            self._difficulty = "Medium"
        elif self._cooking_time >= 10 and len(self._ingredients) < 4:
            self._difficulty = "Intermediate"
        else:
            self._difficulty = "Hard"

    @property
    def difficulty(self):
        if not self._difficulty:
            self.calculate_difficulty()
        return self._difficulty

    def search_ingredient(self, ingredient):
        return ingredient in self._ingredients

    def update_all_ingredients(self):
        for ingredient in self._ingredients:
            Recipe.all_ingredients.add(ingredient)

    def __str__(self):
        return f"Recipe: {self._name}\nIngredients: {', '.join(self._ingredients)}\nCooking time: {self._cooking_time} minutes\nDifficulty: {self.difficulty}\n"


def recipe_search(data, search_term):
    print(f"Recipes containing {search_term}:")
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.cooking_time = 5

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.cooking_time = 5

cake = Recipe("Cake")
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.cooking_time = 50

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.cooking_time = 5

print(tea)
print(coffee)
print(cake)
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")