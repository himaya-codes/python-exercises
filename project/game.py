player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

if player_age <= 12:
    print("\nYou are a minor! Mission access denied. \n")
else:
    print(f"\nWelcome {player_name} to the Final Mission! \n")

    while True:
        print("\n       *****Main Menu*****  ")
        print("------------------------------------")
        print("| Mission Menu           | Command  |")
        print("------------------------------------")
        print("| Start Mission          | start    |")
        print("| Mission Score          | score    |")
        print("| Exit Mission           | lopeta   |")
        print("------------------------------------")

        command = input("\nEnter a command: ").lower()
        score = 0
        if command == "lopeta":
            print(f"\nExiting the mission. Goodbye {player_name}!\n")
            break
        elif command == "start":
            print(f"\nMission started! Good luck! {player_name}\n")
        elif command == "score":
            print(f"\nYour current score is: {score}\n")
        else:
            print("\nInvalid command. Please try again.\n")