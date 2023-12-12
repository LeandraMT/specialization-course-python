from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker

# Connection to database
engine = create_engine("mysql://cf-python:LMV=10203017CaLe@localhost/task_database")

# Initialize the session object to make changes to database / creating the base class
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# Declarative base class
class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return (
            f"<Recipe ID: "
            + str(self.id)
            + " - "
            + self.name
            + " - "
            + self.difficulty
            + ">"
        )

    def __str__(self):
        return (
            f"Recipe ID: " + self.id + "\n"
            f"Recipe Name: " + self.name + "\n"
            f"Ingredients: " + self.ingredients + "\n"
            f"Cooking Time: " + self.cooking_time + "\n"
            f"Difficulty: " + self.difficulty + "\n"
            "---------------------------------\n"
        )

    # function to calculate the difficulty
    def calc_difficulty(self):
        split_ingredients = len(self.ingredients.split(","))

        if (self.cooking_time) < 10 and (split_ingredients) < 4:
            return "Easy"
        elif (self.cooking_time) < 10 and (split_ingredients) >= 4:
            return "Medium"
        elif (self.cooking_time) >= 10 and (split_ingredients) <= 4:
            return "Intermediate"
        elif (self.cooking_time) > 10 and (split_ingredients) > 4:
            return "Hard"


print("Hold on - creating tables...")
Base.metadata.create_all(engine)
print("Tables were successfully created!")


# Create a new recipe function
def create_recipe():
    name = input("Enter a name for your recipe: ")
    ingredients = input(
        "Enter the ingredients for your recipe (separated by a comma): "
    )
    cooking_time = int(input("Enter the cooking time for your recipe (in minutes): "))

    # Validating the user's input
    if len(name) > 50 or not name.isalnum():
        print("Invalid input. Ensure it is alphanumeric and less than 50 characters.")
        return
    if not ingredients.replace(", ", "").isalpha():
        print("Invalid input. Ensure it is alphabetical characters.")
    if not cooking_time < 0:
        print("Invalid input. Ensure it is a positive number.")
        return

    # Collect and run a for loop for the ingredients
    ingredients_input = []
    num_ingredients = int(input("Enter the number of ingredients in the recipe: "))

    for i in range(num_ingredients):
        ingredient = input(f"Enter ingredient {i + 1}: ")
        ingredients_input.append(ingredient)
        joined_ingredients = ", ".join(
            ingredients_input
        )  # joining the ingredients into a string

        print(f"Ingredients: {joined_ingredients}")
        print(f"Recipe created successfully!")
        return ingredients_input

    # Recipe model to create a new object
    recipe_entry = Recipe(
        name=name, cooking_time=cooking_time, ingredients=joined_ingredients
    )

    # Generating a difficulty attribute to recipe
    difficulty = recipe_entry.calc_difficulty()
    recipe_entry.difficulty = difficulty

    # Adding recipe to Database
    session.add(recipe_entry)
    session.commit()
    print("Recipe has been added successfully.")


# Viewing all the recipes function
def view_all_recipes():
    recipes_list = session.query(Recipe).all()

    # If there aren't any recipes
    if len(recipes_list) == 0:
        print(f"Currently no recipes created. Go to main menu to create some recipes!")
        return None
    else:
        print(f"List of recipes created: ")
        print(f"------------------------")

        for recipe in recipes_list:
            print(f"Recipe ID: {recipe.id}")
            print(f"Name: {recipe.name}")
            print(f"Ingredients: {recipe.ingredients}")
            print(f"Cooking Time: {recipe.cooking_time}")
            print(f"Difficulty: {recipe.difficulty}")
            print("---------------------------")


# Searching by ingredients function
def search_by_ingredients():
    recipe_count = session.query(Recipe).count()

    if recipe_count == 0:
        print(f"Currently no recipes created. Go to main menu to create some recipes!")
        return None

    # Retrieving the values from the ingredients column of Database
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []  # init an empty list

    for result in results:
        temp_list = result[0].split(", ")

        for item in temp_list:
            if item not in all_ingredients:
                all_ingredients.append(item)

    # Assign a number to the ingredients
    assign_num_ingredients = enumerate(all_ingredients, start=1)
    numbered_list = list(assign_num_ingredients)

    print(f"All ingredients: \n")
    for ingredient in numbered_list:
        print(f"\n\t{ingredient[0]} {ingredient[1]}")

    # init an empty list and then fill list with numbers from the numbered_list
    options = []
    for item in numbered_list:
        num = item[0]
        options.append(num)

    # asking user to enter number of the ingredient they are searching
    selected = input(
        f"Enter the number assigned of the ingredient you are searching for (separated by spaces): "
    ).split()
    selected = [int(n) for n in selected]  # convert the input values to integers

    search_ingredients = []
    for i in selected:
        if not i.isnumeric() in options:
            print(
                "\nInvalid input. Only numeric values that match the numbers assigned to the ingredients accepted."
            )
            return None
        else:
            ingredient = numbered_list[i - 1][1]
            search_ingredients.append(ingredient)

    # init an empty list that will contain like() method
    conditions = []
    for ing in search_ingredients:
        like_term = str(f"%{ing}%")
        conditions.append(Recipe.ingredients.like(like_term))

    # Retrieving the recipes based on the conditions list
    matching_recipes = session.query(Recipe).filter(*conditions).all()

    if not matching_recipes:
        print(f"No recipes matched your search criteria. Please try again")
    else:
        print(f"Recipes matching your criteria: ")
        for recipe in matching_recipes:
            print(recipe)


# Editing recipe function
def edit_recipe():
    recipe_count = session.query(Recipe).count()

    if recipe_count == 0:
        print(f"Currently no recipes created. Go to main menu to create some recipes!")
        return None

    # Retrieving all the recipes from DB with id and name
    results = session.query(Recipe.id, Recipe.name).all()
    print(f"Available Recipes: ")
    print("\n--------------------")
    for recipe_id, recipe_name in results:
        print(f"{recipe_id} - {recipe_name}")

    # User can pick a recipe by its ID
    recipe_ID = input(f"Enter the ID of the recipe you would like to edit: ")
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_ID).first()

    if not recipe_to_edit:
        print(f"Recipe ID not found. Please try again.")
        return None

    # displaying the recipe's details
    print("\nRecipe Details:")
    print("\n--------------------")
    print("1. Recipe Name:", recipe_to_edit.name)
    print("2. Ingredients:", recipe_to_edit.ingredients)
    print("3. Cooking Time:", recipe_to_edit.cooking_time)

    selected_attribute = input(
        f"Enter the number of attribute you would like to edit: "
    )
    # loop over the selection from user's input
    if selected_attribute == "1":
        new_name = input("Enter recipe's new name: ")
        session.query(Recipe).filter(Recipe.id == recipe_ID).update(
            {Recipe.name: new_name}
        )
    elif selected_attribute == "2":
        new_ingredients = input(
            "Enter new ingredient(s), if more than one, seperate them by commas: "
        )
        session.query(Recipe).filter(Recipe.id == recipe_ID).update(
            {Recipe.ingredients: new_ingredients}
        )
    elif selected_attribute == "3":
        new_cooking_time = input("Enter the new cooking time (minutes): ")
        session.query(Recipe).filter(Recipe.id == recipe_ID).update(
            {Recipe.cooking_time: new_cooking_time}
        )
    else:
        print(
            f"Invalid input. Make sure you selected from the numbers available (1), (2) or (3)."
        )
        return None

    session.commit()  # saving new data to DB
    print("Recipe has been updated successfully.")

    # re-calculing difficulty for the edited recipe
    recipe_to_edit.difficulty = recipe_to_edit.calc_difficulty()
    session.commit()


# Deleting a recipe function
def delete_recipe():
    recipe_count = session.query(Recipe).count()

    if recipe_count == 0:
        print(f"Currently no recipes created. Go to main menu to create some recipes!")
        return None

    # Retrieving all the recipes from DB with id and name
    results = session.query(Recipe.id, Recipe.name).all()
    print(f"Available Recipes: ")
    print("\n--------------------")
    for recipe_id, recipe_name in results:
        print(f"{recipe_id} - {recipe_name}")

    # Asking user to choose which recipe id they'd like to delete
    recipe_id_to_delete = input("Enter the recipe ID you would like to delete: ")
    recipe_to_delete = (
        session.query(Recipe).filter(Recipe.id == recipe_id_to_delete).one()
    )

    if not recipe_to_delete:
        print(f"Recipe ID not found. Please try again.")
        return None

    # Proceeding to delete recipe if found
    session.delete(recipe_to_delete)
    session.commit()
    print("Recipe has been deleted successfully.")


# The main menu function
def main_menu():
    print("\nWelcome! This is the Main Menu")
    print("\n--------------------------------------")
    print("\nPick a number or type quit to exit: ")
    print("\n1. Create a Recipe")
    print("\n2. View all Recipes")
    print("\n3. Search for a Recipe")
    print("\n4. Edit a Recipe")
    print("\n5. Delete a Recipe")
    print("\nquit. Quit application")
    print("\n--------------------------------------")

    while True:
        choice = input("What would you like to do today?: ")
        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice.lower() == "quit":
            break  # exits the loop
        else:
            print(
                "\nSeems you have selected an option that does not match the choices available. Please try again."
            )

    print("\nUntil next time!")
    session.close()
    engine.dispose()
    exit()


# Calling main menu to start the app
main_menu()
