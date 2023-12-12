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
        elif (self.cooking_time) >= 10 and (split_ingredients) > 4:
            return "Intermediate"
        elif (self.cooking_time) > 10 and (split_ingredients) > 4:
            return "Hard"

    print("Hold on - creating tables...")
    Base.metadata.create_all(engine)
    print("Tables were successfully created!")
