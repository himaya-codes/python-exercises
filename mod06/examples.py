#self studies
names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print(names[3])
print(names[1])
print(names[-2])
print(names[1:3])
print(names[2:])
print(names)


names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
# Illegal reference :IndexError: list index out of range
print(names[5]) 

#List operations
names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

print(names)

names = []
#Going through a list using a for loop
name = input("Enter the first name or quit by pressing Enter: ")
while name != "":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

for n in names:
    print(f"Hello, {n}!")

#Range function
for number in range(3,31,3):
    print(number)