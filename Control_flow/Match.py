# Q write a python program that days and integer input from the user representing the weekday number 1-7 ,  and print the corrensponding weekday name
# using match case statement


day_num =5
#print(type(day_num) , day_num)
match day_num :
    case 1:
        print("Today is Monday")
    case 2:
        print("Today is Tuesday")
    case 3:
        print("Today is Wednesday")
    case 4:
        print("Today is Thursday")
    case 5:
        print("Today is Friday")
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Invalid day")

"""
week_day = 2

match week_day :
    case 1 | 2 | 3 | 4 | 5 :
        print("Weekday")
    case 6 | 7 :
        print("Weekend")
    case _ :
        print("Invalid day")
        
        """

"""
 write a py program that takes an input string represeting the trafic light color,
     red , yellow , green , blinking
     use Structural pattern to display following
     print stop color is red or blinking
     print slowdown if color is yellow
     print go if color is green
     print invalid color for any other input  
"""

color = "green"

match color :
    case "red" :
        print("stop")
    case "yellow" :
        print("slowdown")
    case "blinking" :
        print("stop")
    case "green":
        print("go")
    case _ :
        print("invalid color")


numbers = [1, 2 , 3]

match numbers :
    case [1 , 2 , 3] :
        print("yes")
    case [1 , 2 , 4] :
        print("no")
    case _ :
        print("invalid")

"""
 takes a list of temperatures 
  if the list has exactly two element , print the average of the two temperatures
  if the list has the four element calc and print the deefference between the some of the first two readeing and the some of the last two reading
  so any other list length print " Unsupported list length"
  """


temperatures = [1,2,3,4]

match temperatures :
    case [x , y] :
        avg = sum(temperatures) / len(temperatures)
        print(" The average of the two temperatures is : ",avg)
    case [x , y , z , w] :
        first_two = sum(temperatures[:2])
        last_two = sum(temperatures[2:])
        diff = first_two - last_two
        print(" The difference  : ",diff)
    case _ :
        print("Unsupported list length")
