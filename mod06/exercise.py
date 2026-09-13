#Question 1
import random
num_dice = int(input("How many dice would you like to roll? "))

total_sum = 0

for i in range(num_dice):
    roll = random.randint(1, 6)
    total_sum = total_sum + roll
print(f"The total sum of the numbers is: {total_sum}")


#Question 2
numbers = []

user_input = input("Enter a number (or press Enter to quit): ")

while user_input != "":
    number = float(user_input)
    numbers.append(number)
    user_input = input("Enter a number (or press Enter to quit): ")

numbers.sort(reverse=True)

print("\nThe five greatest numbers in descending order:")
for num in numbers[0:5]:
    print(num)


#Question 3
number = int(input("Enter an integer: "))

if number <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#Question 4
cities = []

for i in range(5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("\nThe cities you entered:")

for city in cities:
    print(city)