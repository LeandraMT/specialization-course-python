import pickle


def take_recipe():
    name = str(input("Enter the recipe's name: "))
    cooking_time = int(input("Enter the cooking time: "))
    ingredients = [
        ingredient.strip().capitalize()
        for ingredient in input("Enter the ingredients separated by a comma: ").split(
            ","
        )
    ]
    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe = {
        "recipe_name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }
    return recipe


def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time > 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty


filename = input("Enter a name for your file: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("The file has loaded successfully!")
except FileNotFoundError:
    print("File was not found with such name, creating a new file now")
    data = {"recipes_list": [], "all_ingredients": []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]

num = int(input("How many recipes would you like to enter?: "))

for i in range(0, num):
    recipe = take_recipe()
    for element in recipe["ingredients"]:
        if element not in all_ingredients:
            all_ingredients.append(element)
    recipes_list.append(recipe)
    print("The recipe has been added successfully!")

data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}

updated_file = open(filename, "wb")
pickle.dump(data, updated_file)
updated_file.close()
print("Your recipe file has been updated")
