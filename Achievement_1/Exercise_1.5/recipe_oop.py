class Recipe(object):
    all_ingredients = []

    # Initialization method
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Method for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # Method for cooking_time
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    # Method for ingredients
    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()

    def get_ingredients(self):
        return self.ingredients

    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    # Method for difficulty
    def get_difficulty(self):
        if not self.difficulty:
            self.calculate_difficulty()
        return self.difficulty

    def calculate_difficulty(self):
        num_ingredients = len(self.ingredients)

        if self.cooking_time < 10:
            if num_ingredients < 4:
                self.difficulty = "Easy"
            else:
                self.difficulty = "Medium"
        else:
            if num_ingredients >= 4:
                self.difficulty = "Intermediate"
            else:
                self.difficulty = "Hard"

    # String representation
    def __str__(self):
        output = (
            "Recipe Name: "
            + self.name
            + "\nCooking Time (mins): "
            + str(self.cooking_time)
            + "\nIngredients: "
            + str(self.ingredients)
            + "\nDifficulty: "
            + str(self.get_difficulty())
        )
        for ingredient in self.ingredients:
            output += "- " + ingredient + "\n"
        return output


# Find recipes with specific ingredient
"""
def recipe_search(self, recipes_list, ingredient):
    data = recipes_list
    search_term = ingredient
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)
"""


def recipe_search(data, search_item):
    for recipe in data:
        if recipe.search_ingredient(search_item):
            print(recipe)


# Creating some recipes
tea = Recipe("Tea", 5)
tea.add_ingredients("Water", "Sugar", "Tea Leaves")
tea.get_difficulty()

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee powder", "Water", "Milk", "Sugar (optional)")
coffee.get_difficulty()

cake = Recipe("Cake", 50)
cake.add_ingredients("Flour", "Sugar", "Eggs", "Milk", "Butter", "Vanilla Essence")
cake.get_difficulty()

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice cubes"
)
banana_smoothie.get_difficulty()

# Adding recipes to list
recipes_list = [tea, coffee, cake, banana_smoothie]


# String representation of each recipe
for recipe in recipes_list:
    print(recipe)


# Searching for recipes for the following ingredients
for ingredient in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredient)
