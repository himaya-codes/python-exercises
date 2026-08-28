# question 1
user_name = input("Please enter your name: ")
print("Hello " + user_name + "!" + "\n")

# question 2
radius = input("Please enter the radius of the circle: ")
radius = float(radius)
area = 3.14 * radius ** 2
print(f"The area of the circle is: {area:.2f}", "\n\n")


# question 3
width_rectangle = float(input("Please enter the width of the rectangle: "))
length_rectangle = float(input("Please enter the length of the rectangle: "))

area_rectangle = width_rectangle * length_rectangle

perimeter_rectangle = 2 * (width_rectangle + length_rectangle)

print(f"\n The area of the rectangle is: {area_rectangle:.2f}" "\n", 
      f"\n The perimeter of the rectangle is: {perimeter_rectangle:.2f}" , "\n\n") 

# question 4
num1 = int(input("Please enter the first integer: "))
num2 = int(input("Please enter the second integer: "))
num3 = int(input("Please enter the third integer: "))

sum_numbers = num1 + num2 + num3
product_numbers = num1 * num2 * num3
average_numbers = sum_numbers / 3

print(f"\n The sum of the numbers is: {sum_numbers}" "\n",
      f"\n The product of the numbers is: {product_numbers}" "\n",
      f"\n The average of the numbers is: {average_numbers:.2f}" , "\n\n")

# question 5

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots

total_grams = total_lots * 13.3

kilograms = int(total_grams // 1000)

grams = total_grams % 1000

print(f"\n The weight in modern units: {kilograms} kilograms and {grams:.2f} grams." "\n"),





