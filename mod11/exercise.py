class Publication:
    def __init__(self, name):
         self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"name:{self.name}, author:{self.author}, page count:{self.page_count}")

class Magazine(Publication):
    def __init__(self, name, cheif_editor):
        super().__init__(name)
        self.cheif_editor = cheif_editor

    def print_information(self):
        print(f"name:{self.name}, cheif editor:{self.cheif_editor}")
        
#main program
publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for p in publications:
    p.print_information()

#2
class Car:

    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.odometer = 0  # Kilometer counter

    def accelerate(self, change):
        self.current_speed = max(
            0, min(self.max_speed, self.current_speed + change)
        )

    def drive(self, hours):
        self.odometer += self.current_speed * hours

class ElectricCar(Car):

    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity  # in kWh

class GasolineCar(Car):

    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume  # in liters

# Main program

electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

electric.accelerate(120)  # Drive electric car at 120 km/h
gasoline.accelerate(100)  # Drive gasoline car at 100 km/h

electric.drive(3)
gasoline.drive(3)

print(
    f"Electric car ({electric.registration_number}) distance: {electric.odometer} km")
print(
    f"Gasoline car ({gasoline.registration_number}) distance: {gasoline.odometer} km")