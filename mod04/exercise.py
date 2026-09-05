#Question 1
zander_length = int(input("What is Zander's length in centimeters? "))
size_limit = 42
if zander_length >= 42:
    print("The zander meets the size limit! You may keep it.\n")
else:
    print(f"Please release the fish back into the lake. \nIt's length should be greater than or equal to {size_limit}cm size limit\n")

#Question 2
cabin_class = input("Enter cabin class (LUX, A, B, C): ")
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else: 
    print("Invalid cabin class")

    
#Question 3
gender = input("Input biological gender (female, male): ")
hemoglobin_value = int(input("Input hemoglobin value (g/l)"))

if gender == "female" and hemoglobin_value < 117:
    print("Hemoglobin value is low.")
elif gender == "female" and hemoglobin_value <= 155:
    print("Hemoglobin value is normal.")
elif gender == "female":
    print("Hemoglobin value is high.")
elif gender == "male" and hemoglobin_value < 134:
    print("Hemoglobin value is low.")
elif gender == "male" and hemoglobin_value <= 167:
    print("Hemoglobin value is normal.")
elif gender == "male":
    print("Hemoglobin value is high.")
else:
    print("Invalid biological gender entered.")

#Question 4
year = int(input("Input a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")