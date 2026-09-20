# 1.
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is at {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is at {self.current}")

    def go_to_floor(self, floor):
        if floor > self.top:
            floor = self.top
        elif floor < self.bottom:
            floor = self.bottom

        while self.current != floor:
            if self.current > floor:
                self.floor_down()
            else:
                self.floor_up()


# Testing single elevator
print("--- Testing Elevator ---")
e = Elevator(1, 10)
e.go_to_floor(5)
e.go_to_floor(1)

class Building:
    def __init__(self, bottom, top, number_of_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        print(f"\nRunning Elevator {elevator_num} to floor {floor}:")
        self.elevators[elevator_num - 1].go_to_floor(floor)

    # 3. Fire Alarm
    def fire_alarm(self):
        print("\n--- FIRE ALARM ACTIVATED ---")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)


# Testing Building
print("\n--- Testing Building ---")
b = Building(1, 10, 3)

b.run_elevator(1, 5)
b.run_elevator(2, 8)
b.fire_alarm()

#4
import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Reg. Num':<12} | {'Max Speed':<12} | {'Current Speed':<15} | {'Distance':<15}")
        print("-" * 62)
        for car in self.cars:
            print(f"{car.registration_number:<12} | {car.max_speed:<8} km/h | {car.current_speed:<10} km/h | {car.travelled_distance:<10.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


# --- Main Program ---
participating_cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    participating_cars.append(Car(reg_num, max_speed))

race = Race("Grand Demolition Derby", 8000, participating_cars)

print(f"=== Beginning Race: {race.name} ({race.distance} km) ===\n")

hours_passed = 0

while not race.race_finished():
    race.hour_passes()
    hours_passed += 1

    if hours_passed % 10 == 0:
        print(f"--- Status after {hours_passed} hours ---")
        race.print_status()
        print()

print(f"RACE FINISHED in {hours_passed} hours! Final Results: \n")
race.print_status()