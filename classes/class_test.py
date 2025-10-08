class Car :

    def __init__(self):
        self.color = "red"
        self.brand = "bmw"
        self.wheel_count = 4

    def display(self):
        print(f"this is a {self.color} {self.brand} car ( {self.wheel_count} wheels)")

    def drive(self, destination):
        print(f"driving to {destination} in a car ( {self.wheel_count} wheels)")

        #red color bmw driving to home


car = Car()
print(car.wheel_count)
car.display()
car.drive("home")


"""
you are ask to design a python class name rectangle that model a rectangle using object oriented principles
the class should be initialized with two parameters length and width it must include a method to calculate the area of the rectangle
that return of the rectangle , and another method get perimeter that return the perimeter of the rectangle
additionally implement and instance method describe that call both area() and perimeter() methods and print a massage
in the format the area is x and the perimeter is y where x and y respective values 

create and object of the class with length 10 and width 5 and call the describe method to show the output 

"""

class Rectangle:

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def describe(self):
        print(f"The area is {self.area()} and the perimeter is {self.perimeter()}")

rect = Rectangle(10,5)
rect.describe()
