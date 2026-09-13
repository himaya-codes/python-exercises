days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
day_number = int(input("Enter the day number (1-7): "))
day = days_of_the_week[day_number-1]
print(f"Day number {day_number} is {day}.")

fruits = "Orange", "Banana", "Apple"
print(fruits)

fruits = "Orange", "Banana", "Apple"
(first, second, third) = fruits
print(f"The fruits are: {first}, {second} and {third}.")


import random

def cast():
    first, second = random.randint(1,6), random.randint(1,6)
    return first, second

die1, die2 = cast()
print(f"The dice show {die1} and {die2}.")

games = {"Monopoly", "Chess", "Cluedo"}
print(games)

games.add("Dominion")
print(games)

games.remove("Chess")
print(games)

games.add("Cluedo")
print(games)

for g in games:
    print(g)


names = set()
names.add("Mary")
print(names)


numbers = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

numbers["Olga"] = "050-1011012"
numbers["Mary"] = "0401-2132139"

print(numbers)

name = input("Enter name: ")
if name in numbers:
    print(f"{name}'s phone number is {numbers[name]}.")

# Create a list named 'cars'
cars = [
    # First car (dictionary)
    {
        "make": "Toyota",
        "model": "Corolla",
        "year": 2018
    },
    # Second car (dictionary)
    {
        "make": "Ford",
        "model": "Focus",
        "year": 2020
    },
    # Third car (dictionary)
    {
        "make": "VW",
        "model": "ID.3",
        "year": 2023
    }
]
# Retrieve the second car from the list (index 1)
second_car = cars[1]
print("Information about the second car:")
print(second_car)

# Retrieve the make of the first car (index 0)
first_car_make = cars[0]["make"]
print(f"The make of the first car is: {first_car_make}")

# Retrieve the model of the last car (index 2) and print it directly
# without storing it in a variable
print(f"The model of the last car is: {cars[2]["model"]}")

print("All cars and their information:")
for car in cars:
    print(f"Make: {car['make']}, Model: {car['model']}, Year: {car['year']}")