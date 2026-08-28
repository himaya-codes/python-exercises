#print("Hellow")
#print('test')
#print("it's order")

#print("Hellow\nworld")

#name= "Himaya"

#print(name)

#user = input('what is your name: ')
#add = id(user)
#print('Thank you ' + user)
#print('Your ID is: ' + str(add))


#string1 = "Enter a number: "

#number1 =  int(input(string1))
#number2 = int(input(string1))

#sum = number1 + number2

#print("The sum is: " + str(sum))

#string1 = "Enter a number: "

#number1 = int(input(string1))
#number2 = int(input(string1))

#devisionValue = float(number1 / number2)

#print("The devision is: " + str(number1) + " / " +  str(number2) + " = " + str(devisionValue))

############
string1 = "Enter a number: "

number1 = int(input(string1))
number2 = int(input(string1))      
sum = number1 + number2
#devision = number1 / number2
#print(devision)
print(sum)

a=7
b=2

#---------------    remaining = 7%2 = 1
remaining = a%b
print(remaining)

#---------------    7**2 = 7*7 = 49
power = a**b 
print(power)

#---------------    farenheit to celsius
#Enter temperature in Fahrenheit: 98.6
#Temperature in Celsius: 37.0
#Temperature in Celsius: 37.00
#Temperature in Celsius:  37.00000000

fahrenheit_str = input("Enter temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius: " + str(celsius))
print(f"Temperature in Celsius: {celsius: 6.2f}")
print(f"Temperature in Celsius: {celsius: 10.8f}")

import math
print(f"{'pi':10s}: {math.pi: 10.8f}")
