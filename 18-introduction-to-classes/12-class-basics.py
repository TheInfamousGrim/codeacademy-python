# 1.

# Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__() method (see the Hint for more).

# 2.

# Inside the Triangle class:

#     Create a variable named number_of_sides and set it equal to 3.
#     Create a method named check_angles. The sum of a triangle’s three angles should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.

# 3.

# Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).

# Print out my_triangle.number_of_sides

# Print out my_triangle.check_angles()


class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(60, 60, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

# 4.

# Create a class named Equilateral that inherits from Triangle.

# Inside Equilateral, create a member variable named angle and set it equal to 60.

# Create an __init__() function with only the parameter self, and set self.angle1, self.angle2, and self.angle3 equal to self.angle (since an equilateral triangle’s angles will always be 60˚).

class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
