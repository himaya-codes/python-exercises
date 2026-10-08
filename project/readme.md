# The Cooking Game
Tharushi Himaya
Recipe Rescue Mission is a text-based Python cooking game. The player visits different kitchens and finds missing ingredients for recipes.

-------------Objective-------------
The goal is to choose the correct missing ingredient and collect it in the player's inventory. There are three routes:
-Bake
-Pizza
-Pasta
Recipes are randomly selected to make the game different each time.

-------------How It Works------------
The player enters their name and age, then uses the main menu to:

The main menu provides the following commands:

move -	Choose a cooking kitchen
inventory -	View collected ingredients
save -	Save the current game progress
lopeta - Exit or leave the current menu


After entering a kitchen, the player can use:
"collect" to try to find the missing ingredient
save to save the current progress
lopeta to return to the main menu
If the player chooses the correct ingredient, it is added to their inventory. If the answer is incorrect, the player can try again.

Save the game
Exit the game
The game uses JSON files to save and load the player's progress.

-------------Main Features------------
Player name and age
Three cooking routes
Random recipes
Inventory system
Save/load system
File reading
Error handling
Player, Room, Recipe and Item classes

---------Sustainable Development-------
The game takes the perspective of sustainable development into account through its cooking theme and educational approach.

The game encourages players to think about ingredients and food rather than treating food as something disposable. The missing-ingredient challenges can also encourage awareness of what ingredients are needed to prepare a meal and the importance of planning before cooking.

***File Structure Overview***
project /
│
├── modules/
│   ├── __init__.py
│   ├── item.py
│   ├── room.py
│   └── player.py
│
├── game.py
└── README.md