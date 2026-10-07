class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.inventory = []
        self.location = None  # Current Room object

    def move_to(self, room):
        """Moves player to a target room."""
        self.location = room
        print(f"\nWelcome {self.name} to the {room.name} Kitchen!")

    def collect_item(self, item):
        """Adds an item to player inventory."""
        self.inventory.append(item)
        print(f"\nGreat job, {self.name}! You successfully collected: {item.name}")

    def show_inventory(self):
        """Displays all collected items in player's inventory."""
        print(f"\n--- {self.name}'s Inventory ---")
        if not self.inventory:
            print("Your inventory is currently empty.")
        else:
            for item in self.inventory:
                print(f" - {item}")