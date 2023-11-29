recipes_list = []
ingredients_list = []


def take_recipe():
    name = input("Recipe's name: ")
    cooking_time = int(input("Cooking time: "))
    ingredients = input("Ingredients: ").split(", ")
    recipe = {"Name": name, "Cooking time": cooking_time, "Ingredients": ingredients}
    return recipe


n = int(input("How many recipes would you like to enter?: "))

for n in range(n):
    recipe = take_recipe()
    for ingredient in recipe["Ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe["Cooking time"] < 10 and len(recipe["Ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    elif recipe["Cooking time"] < 10 and len(recipe["Ingredients"]) >= 4:
        recipe["difficulty"] = "Medium"
    elif recipe["Cooking time"] >= 10 and len(recipe["Ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    elif recipe["Cooking time"] >= 10 and len(recipe["Ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"

for recipe in recipes_list:
    print("Recipe: ", recipe["Name"])
    print("Cooking time (min): ", recipe["Cooking time"])
    print("Ingredients: ", recipe["Ingredients"])
    # for ingredient in recipe["Ingredients"]:
    #   print(ingredient)
    print("Difficulty level: ", recipe["difficulty"])


def print_ingredients():
    ingredients_list.sort()
    print("All Ingredients")
    for ingredient in ingredients_list:
        print(ingredient)


print_ingredients()
