"""class Animal :
    age =0

    def __init__(self , color):
        self.color = color

    def speak(self):
        print("I'm an animal")


class Dog(Animal):

    def __init__(self):
        super().__init__("black")

    def display_info(self):
        print("i'm a dog")

    def speak(self):
        print("woof woof")

dog = Dog("black")
print(dog.color)
dog.speak()
dog.display_info()
"""

"""
define abase class called employee that has attributes name and salary . it should have to method call
display_info() that prints the name and salary of the employee then define a derived class called Manager
that inherits from employee and has an additional attribute called department . override the display_info()
in the Manager class to include the department information as well
finally write a py program
create a object of the manager class call the display info method using that object 
  
"""

class Employee :
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"name = {self.name}  \n salary = {self.salary}")

class Manager(Employee):
    def __init__(self ,name , salary , department):
        super().__init__( name , salary)
        self.department = department

    def display_info(self):
        print(f"name = {self.name} \nsalary = {self.salary} \ndepartment = {self.department}")

manager = Manager("dila" , 1000 , "IT")
manager.display_info()


