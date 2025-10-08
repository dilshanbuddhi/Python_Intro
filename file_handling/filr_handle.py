"""file_1 = open("my_file.txt" , "r")

print(file_1.read())

file_1.close()"""


"""
#with
 open("my_file.txt" , "r") as file_1:
    print(file_1.read())
"""

"""file_1 = open("my_file.txt" , "r")

while True:
    line = file_1.readline()
    if not line:
        break
    print(line.strip())"""


"""
#with
 open("my_file.txt" , "r") as file_1:
    lines = file_1.readlines()
    #print(lines)   # not recommended for large files
    
    for line in lines:
        print(line.strip())"""



"""
#with
 open("my_file_1.txt" , "w") as file_1:
    file_1.write("hyyyyyyyyyyyyyyyyyyyyyyyyyyy\n")

with open("my_file_1.txt" , "a") as file_1:
    file_1.write("\tbyeeeee\n")"""

with open("my_file_1.txt" , "w") as file_1:
    file_1.writelines("hyyyyyyyyyyyyyyyyyyyyyyyyyyy\n" , "\tbyeeeee\n")



