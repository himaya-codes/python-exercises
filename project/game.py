def choose_difficulty(levels_chosen):
    """Asks the player to select a difficulty level and adds it to a list."""
    print("\n--- Select Difficulty Level ---")
    print(" 1. Beginner")
    print(" 2. Intermediate")
    print(" 3. Hard")
    
    choice = input("\nEnter difficulty level (beginner / intermediate / hard): ").strip().lower()
    
    if choice in ["beginner", "intermediate", "hard"]:
        levels_chosen.append(choice)
        print(f"Difficulty set to: {choice}!")
    else:
        print("Invalid choice! Defaulting to 'beginner'.")
        levels_chosen.append("beginner")

def display_selected_levels(levels_chosen):
    """Prints all saved difficulty levels from the list using a manual counter."""
    print("\n--- Selected Difficulty History ---")
    if not levels_chosen:
        print("No difficulty levels selected yet.")
    else:
        i = 1
        for level in levels_chosen:
            print(f"{i}. {level.capitalize()}")
            i += 1

def display_mission_score(score):
    print(f"\nYour current score is: {score}")

#----Main program----
player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age <= 12:
    print("\nYou are a minor! Mission access denied. \n")
else:
    print(f"\nWelcome {player_name} to the Final Mission! \n")

    levels_chosen = []
    score = 0

    while True:
        print("\n       *****Main Menu*****  ")
        print("------------------------------------------")
        print("| Mission Menu           | Command       |")
        print("------------------------------------------")
        print("| Select Level           | level         |")
        print("| Show Selected Levels   | level_history |")
        print("| Mission Score          | score         |")
        print("| Exit Mission           | lopeta        |")
        print("------------------------------------------")

        command = input("\nEnter a command: ").lower()
        score = 0
        if command == "lopeta":
            print(f"\nExiting the mission. Goodbye {player_name}!\n")
            break
        elif command == "level":
            choose_difficulty(levels_chosen)
        elif command == "level_history":
            display_selected_levels(levels_chosen)
        elif command == "score":
            display_mission_score(score)
        else:
            print("\nInvalid command. Please try again.")