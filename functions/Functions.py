from Variables.Dictionaries import new_list


def sum_numbers(num1 , num2):
    return num1 + num2


print(sum_numbers(10,10))

"""
write a func remove duplicates (mylist) that return a List with duplicates removed (reserving the original order)
also you should write a few line of code to text the function
"""

def remove_duplicates(mylist):
    new_list = []
    for i in mylist:
            if i not in new_list:
                new_list.append(i)
    return new_list


my_list = [ 1,1,3,4,5,5,7,2,8,8,5,0.3 ]
print("remove duplicates : ",remove_duplicates(my_list))


"""
write the function factorial(n) that returns the factorial of a given number n
"""

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(5))

"""
write a function that calculate and returns a value of a number raise to certain power. the function access two arguments,
the number and the exponent if the exponent is not provided it should calculate the square of the number
"""

def power(num , exponent = 2):
    return num ** exponent

print(power(2))

"""
write a function to calc employee net salary the function should accept baseSalary , bonus(default to 0),
and tax rate (default to 0) demonstrate different ways of calling the function using and positional and keyword arguments
"""

def net_salary(base_salary , bonus = 0 , tax_rate = 0.1):

    net_salary = base_salary + bonus - (base_salary / tax_rate)
    return net_salary

print(net_salary(base_salary= 2000 , bonus=500 , tax_rate=10))

def arbitary_args(*args):
    for arg in args:
        print(arg)

arbitary_args(1,2,3,4,5,6,7)

"""
write a func multiple that all that accept any number of numbers and returns their product. 
if  no numbers are provided return 1
"""

def multiple(*args):
    if len(args) == 0:
        return 1
    result = 1
    for i in args:
        result *= i
    return result

print("multiple : " , multiple(3,4,5,6))


"""
write the function that accept any number of numbers and returns the maximum value among them. do not use the built-in max() function
"""

def maximum(*args):
    if len(args) == 0:
        return "no numbers provided"
    max_value = args[0]
    for i in args:
        if i > max_value:
            max_value = i
    return max_value

print("maximum : " , maximum())


"""
*kwargs allows you to pass in any number of keyword arguments to a function.
"""

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="John", age=30, city="New York")


my_dict = {"name": "John", "age": 30, "city": "New York"}
for key in my_dict.keys():
    print(f"{key}")

"""
 map function
"""

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

"""
filter function
"""

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

"""
what is the difference between map and filter
"""

"""
map returns a new list with the results of the function applied to each element of the original list
filter returns a new list with the elements of the original list that satisfy the condition of the function
"""


""" 
sum function
"""

numbers = [1, 2, 3, 4, 5]
total = sum(numbers , 100)
print(total)


"""
isinstance function
"""

x = 100.98
print(isinstance(x , (int , float)))


"""
f string   
"""

name = "John"
age = 30
print(f"Hello, {name}! You are {age} years old.")
