#Tuples are used to store multiple items in a single variable.
#Tuples are ordered, "🙂‍↔️ unchangeable 🙂‍↔️", and allow duplicate values.
#Tuples are written with round brackets ()

fruits = ("apple", "banana", "cherry")
print(type(fruits) , "Type of tuple1")
print(fruits[1] , "Index ( 1 ) of tuple1")

#how get the length of a tuple
print(len(fruits) , "length of tuple1")

#tuplest cant be changed
#fruits[1] = "orange"
#print(fruits)

#tuple items can be of different data types
print(type(fruits[1]))

test = ("test",)
print(type(test))

#A tuple can contain different data types
tuple1 = ("apple", True, 3.14)
print(tuple1 , " tuple with different data types ")

# how change tuple values
temp_list = list(fruits)
#constructer (list)

print(temp_list)
print(type(temp_list) , " type of TEMP")

temp_list[1] = "orange"
print(temp_list)
#🙂‍↔️list to tuple
fruits = tuple(temp_list)
#(tuple) eken puluwn list ekta tuple ekk assign krnna
print(fruits)
print(type(fruits) , " type of fruits")

#python tuples are immutable

#nested tuple
nested_tuple = ((1,2,3) , ("a" , "b" , "c") , (True , False))
print(nested_tuple)

print(nested_tuple[1][1])
print(nested_tuple[2][0])
