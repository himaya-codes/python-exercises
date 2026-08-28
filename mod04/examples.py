#money = float(input("Enter the amount of money you have: "))
  #if money >=5:
    #print("You have enough money to buy a coffee.")

#age = int(input("Enter age: "))
#if 15 <= age < 18:
    #weight = float(input("Enter weight (kg): "))
#if (age >= 18 or age >= 15 and weight >= 55):
    #print("The medicine can be used.")

#else : print("The medicine cannot be used.")

#age = int(input("Enter age: "))
#if age >= 65:
    #print("You are retired")
#elif age >= 18:
    #print("You are in working-age")
#elif age >= 7:
    #print("You are in school.")
#elif age >= 3:
    #print("You are a preschooler.")

#grade = int(input("Enter grade: "))
#if grade >= 90:
    #print("A1")
#elif grade >= 80:
    #print("A2")
#elif grade >= 70:
    #print("B1")
#elif grade >= 60:
    #print("B2")
#elif grade >= 50:
    #print("C")
#else:
    #print("\nF")



status = input("Do you have citizenship? ")
age = int(input("\n Enter your age: "))

if (status == "yes" and age >= 18):
    print("\n You are eligible to work.")
else:
    print("\n You are not eligible to work.")