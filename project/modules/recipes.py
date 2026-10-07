from modules.room import Room

def get_game_rooms():
    bake_dishes = [
        {
            "dish": "Chocolate Cake",
            "checklist": ["Flour", "Cocoa Powder", "Eggs", "Sugar", "----------- ?", "Butter"],
            "missing": "Chocolate Chips",
            "options": ["1. Chocolate Chips", "2. Apple", "3. Potato"],
            "correct_choice": "1"
        },
        {
            "dish": "Apple Pie",
            "checklist": ["Pie Crust", "Cinnamon", "Sugar", "Butter", "----------- ?", "Vanilla"],
            "missing": "Sliced Apples",
            "options": ["1. Pineapple", "2. Sliced Apples", "3. Tomato"],
            "correct_choice": "2"
        }
    ]

    pizza_dishes = [
        {
            "dish": "Hawaiian Pizza",
            "checklist": ["Pizza Flour", "Olive Oil", "Meat", "Baking Powder", "----------- ?", "Cheese"],
            "missing": "Pineapple",
            "options": ["1. Pineapple", "2. Apple", "3. Potato"],
            "correct_choice": "1"
        },
        {
            "dish": "Chicken Pizza",
            "checklist": ["Pizza Dough", "Tomato Sauce", "Cheese", "----------- ?", "Oregano"],
            "missing": "Grilled Chicken",
            "options": ["1. Fish", "2. Grilled Chicken", "3. Chocolate"],
            "correct_choice": "2"
        },
        {
            "dish": "Margherita Pizza",
            "checklist": ["Pizza Dough", "Tomato Sauce", "Mozzarella", "----------- ?", "Olive Oil"],
            "missing": "Fresh Basil",
            "options": ["1. Fresh Basil", "2. Banana", "3. Garlic Bread"],
            "correct_choice": "1"
        }
    ]

    pasta_dishes = [
        {
            "dish": "Carbonara Pasta",
            "checklist": ["Spaghetti", "Eggs", "Pecorino Cheese", "Pancetta", "----------- ?", "Black Pepper"],
            "missing": "Parmesan",
            "options": ["1. Strawberry", "2. Parmesan", "3. Rice"],
            "correct_choice": "2"
        },
        {
            "dish": "Pomodoro Pasta",
            "checklist": ["Penne Pasta", "Tomatoes", "Garlic", "Olive Oil", "----------- ?", "Salt"],
            "missing": "Fresh Basil",
            "options": ["1. Fresh Basil", "2. Mango", "3. Butter"],
            "correct_choice": "1"
        }
    ]

    bake_room = Room("Bake", bake_dishes)
    pizza_room = Room("Pizza", pizza_dishes)
    pasta_room = Room("Pasta", pasta_dishes)

    return [bake_room, pizza_room, pasta_room]