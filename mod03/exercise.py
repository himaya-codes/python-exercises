user_name = input("Please enter your name: ")
print("Hello " + user_name + "!" + "\n")

#The area of the circle
radius = input("Please enter the radius of the circle: ")
radius = float(radius)
area = 3.14 * radius ** 2
print(f"The area of the circle is: {area:.2f}", "\n\n")


#The area of the rectangle
width_rectangle = float(input("Please enter the width of the rectangle: "))
length_rectangle = float(input("Please enter the length of the rectangle: "))

area_rectangle = width_rectangle * length_rectangle

perimeter_rectangle = 2 * (width_rectangle + length_rectangle)

print(f"\n The area of the rectangle is: {area_rectangle:.2f}" "\n", 
      f"\n The perimeter of the rectangle is: {perimeter_rectangle:.2f}" , "\n\n") 









