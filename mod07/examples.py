#Functions
def fruit():
    print("Apple")
    berry()

def berry():
    print("Strawberry")

def numb():
    print("123")
print("program")
numb()
fruit()

def adder(x,y):
    sum = x + y
    print(f"{x} + {y} = {sum}")

first_x= 1
first_y= 2

adder(first_x,first_y)



def great():
    name = "sam"
    greating = f"Hello, {name}"
    print(greating)

name = "tom"

print("lets greate")
great()
print("we greate")
print(f"hi {name}")



def addname(name, names):
    name = "sam"
    names.append(name)

names = ["tom", "jerry"]
name = "tom"

print(names)
addname(name, names)
print(names)
