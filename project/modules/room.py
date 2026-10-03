import random
from .item import Item

class Room:
    # Predefined recipes and options per category
    RECIPES = {
        "bake": [
            {
                "dish": "Chocolate Cake",
                "ingredients": ["Flour", "Sugar", "Cocoa Powder"],
                "target": Item("Chocolate Chips"),
                "options": ["Chocolate Chips", "Apple", "Garlic"]
            },
            {
                "dish": "Apple Pie",
                "ingredients": ["Flour", "Butter", "Cinnamon"],
                "target": Item("Apple"),
                "options": ["Pineapple", "Apple", "Potato"]
            }
        ],
        "pizza": [
            {
                "dish": "Hawaiian Pizza",
                "ingredients": ["Pizza Flour", "Olive Oil", "Cheese"],
                "target": Item("Pineapple"),
                "options": ["Pineapple", "Apple", "Potato"]
            },
            {
                "dish": "Chicken Pizza",
                "ingredients": ["Pizza Flour", "Tomato Sauce", "Cheese"],
                "target": Item("Chicken"),
                "options": ["Chicken", "Fish", "Banana"]
            },
            {
                "dish": "Margherita Pizza",
                "ingredients": ["Pizza Flour", "Tomato Sauce", "Mozzarella"],
                "target": Item("Basil"),
                "options": ["Basil", "Chocolate", "Carrot"]
            }
        ],
        "pasta": [
            {
                "dish": "Carbonara Pasta",
                "ingredients": ["Spaghetti", "Eggs", "Pecorino Cheese"],
                "target": Item("Pancetta"),
                "options": ["Pancetta", "Strawberry", "Rice"]
            },
            {
                "dish": "Pasta Pomodoro",
                "ingredients": ["Spaghetti", "Olive Oil", "Garlic"],
                "target": Item("Tomato"),
                "options": ["Tomato", "Orange", "Beef"]
            }
        ]
    }

    def __init__(self, category):
        self.name = category.capitalize()
        self.category = category.lower()
        self.dish_name = ""
        self.ingredients = []
        self.missing_item = None
        self.options = []
        self.setup_random_recipe()

    def setup_random_recipe(self):
        """Randomly assigns a dish and target item for this room session."""
        recipe_data = random.choice(self.RECIPES[self.category])
        self.dish_name = recipe_data["dish"]
        self.ingredients = recipe_data["ingredients"]
        self.missing_item = recipe_data["target"]
        self.options = recipe_data["options"]

    def display_checklist(self):
        """Displays ingredients checklist with the missing item slot."""
        print(f"\n--- Checklist for {self.dish_name} ---")
        for ing in self.ingredients:
            print(f"- {ing}")
        print("- ----------- ? (Missing Ingredient)")