#Question 1
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1

#Question 2
while True:
     input_value = int(input("Enter the centimeters value: "))
     if input_value < 0:
         break
     inches_value = input_value / 2.54
     print(f"{input_value} centimeters is equal to {inches_value:.2f} inches.")

#Question 3
smallest = None
largest = None

user_input = input("Enter a number: ")

while user_input != "":
    num = float(user_input)

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

    user_input = input("Enter a number: ")

if smallest is not None:
    print("Smallest:", smallest)
    print("Largest:", largest)
else:
    print("No numbers were entered.")

#Question 4
import random
rand_number = random.randint(1, 10)
while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == "":
        break
    elif guess > rand_number:
        print("Too high")
    elif guess < rand_number:
        print("Too low")
    else:
        print("Correct")

#Question 5
valid_username = "python"
valid_password = "rules"
login_attempts = 1

while login_attempts <= 5:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login_attempts += 1

    if username == valid_username and password == valid_password:
        print("Welcome")
        break

else:
    print("Access denied")

#Question 6
import random

N = int(input("How many random points do you want to generate? "))

n = 0
points = 0

while points < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        n += 1

    points += 1

pi = 4 * n / N

print("Approximation of pi:", pi)