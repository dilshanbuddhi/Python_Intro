"""
write a py program that prints all power of 2 (starting from 1) that are less than or equal to a given input use entered integer
N using a while loop

N = 20
print ( 1 ,2 , 4, 16)
"""

"""
num = int(input("Enter a number: "))

i = 1
while i <= num:
    print(i)
    i *= 2
"""

"""
takes integer input from user an adds them for total sum . the program will comtinue until the user enterd zero
finally display the total sum
"""

"""
total = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print("stopped")
        break
    total += num
    
    print("Total sum of numbers:", total)

    """


"""
While loop with continue
"""

i = 0

while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
else:
    print("iwaraaaii !!!!!!")