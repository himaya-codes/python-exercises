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