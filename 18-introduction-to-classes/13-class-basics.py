# 1.

# Define a new class named “Car”. For now, since we have to put something inside the class, use the pass keyword.

# 2.

# At the end of your code, use a print statement to display the condition of my_car.


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print(f"This is a {self.color} {self.model} with {str(self.mpg)} MPG.")

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"



my_car = ElectricCar("Model X", "black", 150, "molten salt")

my_car.drive_car()
print(my_car.condition)

