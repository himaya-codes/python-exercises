#1 
import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    #2 
    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed
    #3
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

car = Car("ABC-123", 142)

print(f"Registration number: {car.registration_number}")
print(f"Maximum speed: {car.max_speed} km/h")
print(f"Current speed: {car.current_speed} km/h")
print(f"Travelled distance: {car.travelled_distance} km")

#4
cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_num, max_speed))

race_finished = False
hours_passed = 0

while not race_finished:
    hours_passed += 1
    
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        
        car.drive(1)        
        if car.travelled_distance >= 10000:
            race_finished = True

print(f"Race finished in {hours_passed} hours!\n")

# Table Header
print(f"{'Reg. Num':<12} | {'Max Speed':<12} | {'Current Speed':<15} | {'Distance':<15}")
print("-" * 62)

# Table Rows
for car in cars:
    print(f"{car.registration_number:<12} | {car.max_speed:<8} km/h | {car.current_speed:<10} km/h | {car.travelled_distance:<10.1f} km")