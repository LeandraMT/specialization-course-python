import pickle


def display_recipe(recipe):
    print("")
    print("Recipe: ", recipe["name"])
    print("Cooking Time (mins): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ele in recipe["ingredients"]:
        print(", ", ele)
    print("Difficulty: ", recipe["difficulty"])
    print("")


def search_ingredients(data):
    available_ingredients = enumerate(data["all_ingredients"])
    numbered_list = list(available_ingredients)
    print("Ingredients list: ")

    for ele in numbered_list:
        print(ele[0], ele[1])
    try:
        num = int(input("Enter the number of ingredients you would like to search: "))
        ingredients_searched = numbered_list[1]
        print("Searching for recipes with ", ingredients_searched, "...")
    except ValueError:
        print("Only numberes are allowed")
    except:
        print(
            "Seems there are no matches - make sure you enter a number that matches the ingredients list!"
        )
    else:
        for ele in data["recipes_list"]:
            if ingredients_searched in ele["ingredients"]:
                print(ele)


filename = input("Enter a name for your file: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("The file has loaded successfully!")
except FileNotFoundError:
    print("File was not found with such name - please try again")
except:
    print("An unexpected error happened. Try again later")
else:
    file.close()
    search_ingredients(data)
