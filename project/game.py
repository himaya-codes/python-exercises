#main program for the Cooking Mission game
from modules import Player, Room, Item

def main():
    player_name = input("Enter your name: ")
    player_age = int(input("Enter your age: "))

    if player_age <= 12:
        print("\nYou are a minor! Mission access denied.\n")
        return

    # Instantiate player
    player = Player(player_name, player_age)
    print(f"\nWelcome {player.name} to the Cooking Mission!\n")

    # Instantiate rooms
    rooms = {
        "bake": Room("bake"),
        "pizza": Room("pizza"),
        "pasta": Room("pasta")
    }

    while True:
        print("\n         *****Main Menu*****   ")
        print("------------------------------------------")
        print("| Cooking Room          | Command        |")
        print("------------------------------------------")
        print("| Move to Room          | move           |")
        print("| Exit Game             | lopeta         |")
        print("------------------------------------------")

        command = input("\nEnter a command: ").strip().lower()

        if command == "lopeta":
            print(f"\nExiting the mission. Goodbye {player.name}!\n")
            break

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
                    print("  lopeta  : Return to main menu")
                    
                    room_cmd = input("\nEnter command: ").strip().lower()

                    if room_cmd == "lopeta":
                        print(f"Leaving the {selected_room.name} kitchen...")
                        break

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
                        print("\nInvalid command. Please enter 'collect' or 'lopeta'.")
            else:
                print("\nInvalid room selection!")
        else:
            print("\nInvalid command. Please try again.")

if __name__ == "__main__":
    main()