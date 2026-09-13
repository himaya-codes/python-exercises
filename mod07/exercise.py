"""
#In class exercises
#Question1 
import random
def dice_roll():
    return random.randint(1,6)

roll = dice_roll()
while roll != 6:
    print(roll)
    roll = dice_roll()

#2
import random
def dice_roll(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))

roll = dice_roll(sides)
while roll != sides:
    print(roll)
    roll = dice_roll(sides)


#exercise 1
def avg_list(numbers):
    return sum(numbers) / len(numbers)

numbers = [1.3, 2.7, 3.1, 4.9, 5.2]

print(f"The average of the list is: {avg_list(numbers)}")
#----------------------------------------------------------
def avg_list(numbers):
    avg =  sum(numbers) / len(numbers)

list = [1.3, 2.7, 3.1, 4.9, 5.2]
avg = avg_list(list)
print(f"The average of the list is: {avg}")


#exercise 2
def averages(list_of_floats):
    avg = sum(list_of_floats) / len(list_of_floats)
    return avg

def average_grade(list_of_grade):
   avgs = []
   for list in list_of_grade:
       avg = averages(list)
       avgs.append(avg)

grades = [[40.3, 50.23], [60.05, 70.05, 80.10]]
avgs = average_grade(grades)

for grade in avgs:
    print(f"The average grade is: {grade: .2f}")

"""
#Question 1
import random

def roll_dice():
    return random.randint(1, 6)
result = 0

while result != 6:
    result = roll_dice()
    print(f"Rolled: {result}")


#Question 2
import random

def roll_dice(sides):
    return random.randint(1, sides)

# Main program
max_sides = int(input("Enter the number of sides on the die: "))

result = 0
while result != max_sides:
    result = roll_dice(max_sides)
    print(f"Rolled: {result}")


#Question 3
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters

# Main program
gallons_input = float(input("Enter gasoline amount in gallons (negative value to quit): "))

while gallons_input >= 0:
    liters_output = gallons_to_liters(gallons_input)
    print(f"{gallons_input:.2f} gallons is {liters_output:.2f} liters.")
    
    gallons_input = float(input("\nEnter gasoline amount in gallons (negative value to quit): "))

print("Program ended.")



#question 4
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Main program for testing
test_numbers = [5, 12, 8, 3, 20]
result_sum = sum_of_list(test_numbers)

print(f"The list is: {test_numbers}")
print(f"The sum of all numbers in the list is: {result_sum}")



#question 5
def remove_uneven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Main program for testing
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = remove_uneven(original_list)

print(f"Original list: {original_list}")
print(f"Cut-down list (even numbers only): {filtered_list}")


#question 6
import math

def calculate_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    
    # Calculate area of circle (A = pi * r^2)
    area_m2 = math.pi * (radius_m ** 2)
    
    # Calculate unit price per square meter
    unit_price = price_eur / area_m2
    return unit_price

# Main program
print("Enter details for Pizza 1:")
d1 = float(input("Diameter (cm): "))
p1 = float(input("Price (€): "))

print("\nEnter details for Pizza 2:")
d2 = float(input("Diameter (cm): "))
p2 = float(input("Price (€): "))

# Calculate unit prices using the function
unit_price1 = calculate_unit_price(d1, p1)
unit_price2 = calculate_unit_price(d2, p2)

print(f"\nPizza 1 unit price: {unit_price1:.2f} €/m²")
print(f"Pizza 2 unit price: {unit_price2:.2f} €/m²")

# Determine which offers better value
if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money!")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money!")
else:
    print("Both pizzas offer the exact same value for money!")


