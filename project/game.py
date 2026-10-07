# main program for the Cooking Mission game
import json
import os
from modules import Player, Room, Item

# Dynamic base directory relative to game.py location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def show_file_content(filename):
    # Build full path combining BASE_DIR + filename
    file_path = os.path.join(BASE_DIR, filename)

    try:
        with open(file_path, "r", encoding="utf-8") as file:  # <-- Use file_path here!
            print(file.read())
    except FileNotFoundError:
        print(f"[Warning: '{filename}' not found.]")
    except IOError:
        print(f"[Error reading '{filename}'.]")


def save_game_state(player):
    """Saves the player's current progress into a JSON file named after the player."""
    filename = f"{player.name.lower()}_save.json"
    save_data = {
        "name": player.name,
        "age": player.age,
        "inventory": [item.name for item in player.inventory],
        "location": player.location.category if player.location else None
    }
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(save_data, file, indent=4)
        print(f"\nGame successfully saved to '{filename}'!")
    except IOError:
        print("\nFailed to save game state.")


def load_game_state(player_name, rooms):
    """Loads a saved game state if the save file exists."""
    filename = f"{player_name.lower()}_save.json"
    
    if not os.path.exists(filename):
        return None

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            
        player = Player(data["name"], data["age"])
        
        # Restore inventory
        for item_name in data.get("inventory", []):
            player.inventory.append(Item(item_name))
            
        # Restore location
        saved_location = data.get("location")
        if saved_location in rooms:
            player.location = rooms[saved_location]
            
        print(f"\nWelcome back, {player.name}! Game progress loaded.")
        return player
    except (IOError, json.JSONDecodeError, KeyError):
        print("\nError loading save file. Starting a new game...")
        return None


def get_valid_age():
    """Prompts for player age using error handling loop."""
    while True:
        try:
            age = int(input("Enter your age: "))
            return age
        except ValueError:
            print("Invalid input! Please enter a valid numeric age.")


def main():
    # 1. Read introductory text and instructions from separate text files
    show_file_content("intro.txt")
    show_file_content("instructions.txt")

    # Instantiate rooms
    rooms = {
        "bake": Room("bake"),
        "pizza": Room("pizza"),
        "pasta": Room("pasta")
    }

    # 2. Check if player wants to load an existing game state
    player_name = input("Enter your name: ").strip()
    player = load_game_state(player_name, rooms)

    # 3. If no existing save, start a new game
    if not player:
        player_age = get_valid_age()

        if player_age <= 12:
            print("\nYou are a minor! Mission access denied.\n")
            return

        # Instantiate player
        player = Player(player_name, player_age)
        print(f"\nWelcome {player.name} to the Cooking Mission!\n")

    # Main Game Loop
    while True:
        print("\n         *****Main Menu*****   ")
        print("------------------------------------------")
        print("| Cooking Room          | Command        |")
        print("------------------------------------------")
        print("| Move to Room          | move           |")
        print("| View Inventory        | inventory      |")
        print("| Save Game             | save           |")
        print("| Exit Game             | lopeta         |")
        print("------------------------------------------")

        command = input("\nEnter a command: ").strip().lower()

        if command == "lopeta":
            print(f"\nExiting the mission. Goodbye {player.name}!\n")
            break

        elif command == "inventory":
            player.show_inventory()

        elif command == "save":
            save_game_state(player)

        elif command == "move":
            print("\n--- Available Rooms ---")
            print(" 1. Bake Kitchen (bake)")
            print(" 2. Pizza Kitchen (pizza)")
            print(" 3. Pasta Kitchen (pasta)")
            
            room_choice = input("\nWhich room would you like to enter? (bake / pizza / pasta / lopeta): ").strip().lower()

            if room_choice == "lopeta":
                continue

            if room_choice in rooms:
                selected_room = rooms[room_choice]
                player.move_to(selected_room)

                # Room Command Menu Loop
                while True:
                    print(f"\n--- Kitchen Options ({selected_room.dish_name}) ---")
                    print("Commands:")
                    print("  collect : Find and collect missing ingredient")
                    print("  save    : Save game progress")
                    print("  lopeta  : Return to main menu")
                    
                    room_cmd = input("\nEnter command: ").strip().lower()

                    if room_cmd == "lopeta":
                        print(f"Leaving the {selected_room.name} kitchen...")
                        break

                    elif room_cmd == "save":
                        save_game_state(player)

                    elif room_cmd == "collect":
                        selected_room.display_checklist()
                        
                        print(f"\nHey {player.name}: can you help us find the missing ingredient?")
                        print(f"What is the missing ingredient for {selected_room.dish_name}?")
                        
                        for idx, option in enumerate(selected_room.options, start=1):
                            print(f" {idx}. {option}")

                        choice = input("\nEnter item number (or 'lopeta' to cancel): ").strip().lower()

                        if choice == "lopeta":
                            continue
                        
                        if choice.isdigit():
                            idx = int(choice) - 1
                            if 0 <= idx < len(selected_room.options):
                                chosen_name = selected_room.options[idx]
                                
                                # Check if chosen option matches target item
                                if chosen_name == selected_room.missing_item.name:
                                    player.collect_item(selected_room.missing_item)
                                    print("\nUpdated Inventory:")
                                    for item in player.inventory:
                                        print(f" - {item}")
                                    break
                                else:
                                    print(f"\nIncorrect! '{chosen_name}' is not the right ingredient for {selected_room.dish_name}.")
                            else:
                                print("\nInvalid choice number!")
                        else:
                            print("\nInvalid input! Please enter a number.")
                    else:
                        print("\nInvalid command. Please enter 'collect', 'save', or 'lopeta'.")
            else:
                print("\nInvalid room selection!")
        else:
            print("\nInvalid command. Please try again.")

if __name__ == "__main__":
    main()