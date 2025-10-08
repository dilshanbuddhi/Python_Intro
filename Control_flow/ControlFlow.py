n = 11

if n % 2 == 0:
    print(n , " is even")
else:
    print(n ," is odd")


# 🤔 write a py program to calculate the circumference of a given circle with radius r , first you have to validate
#    the given input are positive you can assume pi = 3.14

radius = 14
PI = 3.14

if radius > 0:
    circumference = 2 * PI * radius
    print("circumference os circle = " , circumference)
else:
    print("invalid radius !!!!!")

# Q2  write a py programme to calculate the length of the hypotenuse of a right angle triangle using a pythagorean

# the program should take the length og the two shorter size ( legs ) as input from the user
# the input should calculate and display the length of the hypotenuse

print("--------  Q2  ----------")

leg_1 = 3
leg_2 = 4

if leg_1 > 0 and leg_2 > 0:
    hypotenuse = (leg_1 ** 2 + leg_2 ** 2) ** 0.5
    print("length of hypotenuse = " , hypotenuse)
else:
    print("invalid input")


# elif statement

#  write a py program to display the largest between 3 number

print("--------------------   elif -----------------------")

num1 , num2 , num3 = 9 , 10 , 11

if num1 > num2 and num1 > num3 :
    if num2 > num3:
        print(num1 ,num2 , num3)
    else:
        print(num1 , num3 , num2)


elif num2 > num1 and num2 > num3:
    if num2 > num3:
        print(num2 , num1 , num3)
    else:
        print(num2 , num3 , num1)

else:
    if num2 > num3:
        print(num3 , num1 , num2)
    else:
        print(num3 , num2 , num1)


#slidely modify above code to display numbers in descending order



print("--------------------   turnury operator -----------------------")

"""

x = 30
y = 40

result = "x is larger" if x > y else "y is larger"
print(result)

"""


#given any integer n , print if its absolute value using a turnery operator without using abs function

print("--------------------   turnury operator -----------------------")

n = -10

result = n * -1  if n < 0 else n
print(result)


