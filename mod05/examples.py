rounds = int(input("how many greetings: "))
finished_rounds = 0
while finished_rounds < rounds:
    print("Good Morning")
    finished_rounds = finished_rounds + 1


command = input("Enter a command: ")
while command != "stop":
   print("You entered: " + command)
   command = input("Enter a command: ")
print("Exiting the loop")

import random
dice1 = dice2 = rolls = 0
while(dice1 != 6 or dice2 !=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")

first = 1
while first <= 3:
    second = 1
    while second <= 3:        
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1
        
print("Goodbye")

import random
rounds = 0 
total_rolls = 0
while rounds < 100000:
    dice1 = dice2 = rolls = 0
    while(dice1 != 6 or dice2 !=6):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        rolls = rolls + 1
    total_rolls = total_rolls + rolls
    rounds = rounds + 1
    average_rolls = total_rolls / rounds
print(f"Average rolls required: {total_rolls:6.2f}")

command = input("Enter a command: ")
while command != "stop":
    if command == "hello":
        break
    print("You entered: " + command)
    command = input("Enter a command: ")
print("Exiting the loop")
 #While/else
command = input("Enter a command: ")
while command != "stop":
    if command == "hello":
        break
    print("You entered: " + command)
    command = input("Enter a command: ")
else:
    print("You entered stop") #else work with while, it prints when stop given 
print("Exiting the loop") #this will also print with else if stop gven but if breaks happend only this print will display


#Infinite loop

number = 1
while number < 5:
    print(number)

print("All Ready") #print number repeatedly 

