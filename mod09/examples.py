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

#in class example questions
#question 1
seasons = ("Winter", "Spring", "Summer", "Autumn")

month_number = int(input("Enter the number of the month (1-12): "))

if month_number == 12 or month_number == 1 or month_number == 2:
    season = seasons[0]  # Winter
elif 3 <= month_number <= 5:
    season = seasons[1]  # Spring
elif 6 <= month_number <= 8:
    season = seasons[2]  # Summer
elif 9 <= month_number <= 11:
    season = seasons[3]  # Autumn
else:
    season = "Invalid month"

print(f"Month {month_number} is in {season}.")


#question 2
names = set()

name = input("Enter a name (or press Enter to quit): ")

while name != "":
    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
    
    name = input("Enter a name (or press Enter to quit): ")

print("\nAll entered names:")
for n in names:
    print(n)


#question 3
airports = {}

while True:
    print("\nOptions:")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Quit")
    
    choice = input("Choose an option (1-3): ")
    
    if choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        name = input("Enter the airport name: ")
        airports[icao] = name
        print(f"Airport {name} ({icao}) added successfully.")
        
    elif choice == "2":
        icao = input("Enter the ICAO code to search: ").upper()
        if icao in airports:
            print(f"The name of the airport with ICAO code {icao} is: {airports[icao]}")
        else:
            print("Airport not found.")
            
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")