"""import Addition as add
"""

from addition import sum_of_nums
from addition import sub_of_nums
from math import pi
from math import factorial
from math import pow
from random import randint

"""
from addition import *
"""
result = sum_of_nums(19, 11)
subs = sub_of_nums(19, 11)

print(f"""Sum of 19 and 11 is : {result}""")
print(f"""sub of 19 and 11 is : {subs}""")

print("________________________________________________________________")
print(f"""the value of pi is : {pi}""")

factorial = factorial(9)
print(f"factorial of 9 is : {factorial}")

power = pow(2,3)
print(f"2 raised to the power 3 is : {power}")

random_num = randint(0, 100)
print(f"random number between 0 and 100 is : {random_num}")



