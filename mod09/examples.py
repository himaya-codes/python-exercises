#class and object
class Dog:
    pass

dog = Dog()
dog.name = "Buddy"
print(dog.name)  # Output: Buddy

#initializer
class Dog:
    def __init__(self, name, age, sound = "woof woof"):
        self.name = name
        self.age = age
        self.sound = sound

    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return 
    
dog = Dog("Buddy", 10)
dog2 = Dog("Max", 5 , "arf arf")
print(f"{dog.name} is {dog.age} years old. Sound: {dog.sound}")  # Output: Buddy is 10 years old. Sound: woof woof
print(f"{dog2.name} is {dog2.age} years old. Sound: {dog2.sound}")  # Output: Max is 5 years old. Sound: arf arf

dog.bark(3)  # Output: woof woof
dog2.bark(2)  # Output: arf arf