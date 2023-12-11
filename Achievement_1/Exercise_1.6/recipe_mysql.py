import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="cf-python", passwd="LMV=10203017CaLe"
)

cursor = conn.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

# Creating the TABLE
cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
ingredients VARCHAR(255),
cooking_time INT,
difficulty VARCHAR(20)
)"""
)


# Creating main menu function
def main_menu(conn, cursor):
    choice = ""
    while choice != "quit":
        print("\n--------------------------------------------")
        print("\nMain Menu:")
        print("\nPick a choice:")
        print("\n1. Create a new recipe")
        print("\n2. Search for a recipe by ingredient")
        print("\n3. Update an existing recipe")
        print("\n4. Delete a recipe")
        print("\n5. View all recipes")
        print("\nType 'quit' to exit the program.")
        choice = input("\nYour choice: ")
        print("\n--------------------------------------------")

        # Loop where user selects an option
        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "5":
            view_all_recipes(conn, cursor)


# Create recipe function
def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("Enter a name for you recipe: "))
    cooking_time = int(input("Enter the cooking time (mins): "))
    ingredient = input("Enter the ingredients: ")

    recipe_ingredients.append(ingredient)
    difficulty = calc_difficulty(cooking_time, recipe_ingredients)
    recipe_ingredients_str = ", ".join(recipe_ingredients)

    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    val = (name, recipe_ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("\nRecipe has been saved!")


# Calculating difficulty function
def calc_difficulty(cooking_time, recipe_ingredients):
    if (cooking_time < 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Easy"
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Medium"
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Intermediate"
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Hard"

        print("\nDifficulty level: ", difficulty_level)
        return difficulty_level


# Search recipe function
def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    for recipe_ingredient_list in results:
        for recipe_ingredients in recipe_ingredient_list:
            recipe_ingredient_split = recipe_ingredients.split(", ")
            all_ingredients.extend(recipe_ingredient_split)

    all_ingredients = list(
        dict.fromkeys(all_ingredients)
    )  # removes duplicates from the list
    all_ingredients_list = list(
        enumerate(all_ingredients)
    )  # shows the user the available ingredients

    print("\nAll ingredients list:")
    print("\n---------------------")

    for index, tup in all_ingredients_list:
        print(str(index + 1) + ". " + tup)

    try:
        ingredient_search_num = input(
            "\nEnter the number of the ingredient from the ingredients list shown above: "
        )
        ingredient_searched_index = int(ingredient_search_num) - 1
        ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

        print("\nYou selected ", ingredient_searched)

        print("\nThe Recipe(s) below include(s) the selected ingredient: ")
        print("\n-------------------------------------------------------")

        cursor.execute(
            "SELECT * FROM  Recipes WHERE ingredients LIKE %s",
            (f"%{ingredient_searched}%",),
        )

        final_search_results = cursor.fetchall()
        for row in final_search_results:
            print("\nID: ", row[0])
            print("name: ", row[1])
            print("ingredients: ", row[2])
            print("cooking_time: ", row[3])
            print("difficulty: ", row[4])

    except IndexError:
        print(
            "\nAn unexpected error occurred. Ensure that you have selected a number from the list."
        )
    except ValueError:
        print("\nPlease enter a valid number.")


# Updating recipe function
def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)

    recipe_ID = int((input("\nEnter the ID of the recipe you would like to update: ")))
    col_for_update = str(
        input(
            "\nEnter the data you would like to update among name, cooking time and ingredients: (select 'name' or 'cooking_time' or 'ingredients'): "
        )
    )
    updated_value = input("\nEnter the new value for the recipe: ")
    print("Choice: ", updated_value)

    if col_for_update == "name":
        cursor.execute(
            "UPDATE Recipes SET name = %s WHERE id = %s",
            (
                updated_value,
                recipe_ID,
            ),
        )
        print("\nData has been updated!")

    elif col_for_update == "cooking_time":
        cursor.execute(
            "UPDATE Recipes SET cooking_time = %s WHERE id = %s",
            (
                updated_value,
                recipe_ID,
            ),
        )
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_ID,))
        updated_recipe = cursor.fetchall()

        name = updated_recipe[0][1]
        recipe_ingredients = tuple(updated_recipe[0][2].split(", "))
        cooking_time = updated_recipe[0][3]

        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        print("\nDifficulty level has been updated", updated_difficulty)
        cursor.execute(
            "UPDATE Recipes SET difficulty = %s WHERE id = %s",
            (
                updated_difficulty,
                recipe_ID,
            ),
        )

        print("\nData has been updated!")

    elif col_for_update == "ingredients":
        cursor.execute(
            "UPDATE Recipes SET ingredients = %s WHERE id = %s",
            (
                updated_value,
                recipe_ID,
            ),
        )
        cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_ID,))
        update_recipe = cursor.fetchall()

        print("recipe_ID: ", recipe_ID)

        name = updated_recipe[0][1]
        recipe_ingredients = tuple(updated_recipe[0][2].split(", "))
        cooking_time = updated_recipe[0][3]
        difficulty = update_recipe[0][4]

        updated_difficulty = calc_difficulty(cooking_time, recipe_ingredients)
        print("\nDifficulty level has been updated", updated_difficulty)
        cursor.execute(
            "UPDATE Recipes SET difficulty = %s WHERE id = %s",
            (
                updated_difficulty,
                recipe_ID,
            ),
        )

        print("\nData has been updated!")

        conn.commit()


# Deleting recipe function
def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)

    del_recipe_ID = input("\nEnter the ID of the recipe you would like to delete: ")
    cursor.execute("DELETE FROM  Recipes WHERE id = (%s)", (del_recipe_ID,))

    conn.commit()
    print("\nThe Recipe has been successfully deleted.")


# View all the recipes function
def view_all_recipes(conn, cursor):
    print("\nThis is the full list of your Recipes: ")
    print("----------------------------------------")

    cursor.execute("SELECT * FROM Recipes")
    results = cursor.fetchall()

    for row in results:
        print("\nID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty: ", row[4])


main_menu(conn, cursor)
print("\nUntil next time!")
