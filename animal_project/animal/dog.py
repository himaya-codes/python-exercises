def bark():
    print("Woof!")

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks: Woof woof!")

if __name__ == "__main__":
    dog = Dog("TestRex", "Labrador")
    dog.bark()