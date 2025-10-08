my_list = [ "qq" , "dd" , "ss" ,"jj" ,"gg" ]
# python list are ordered
print(my_list[0])
# list are mutable

# 😶‍🌫️ length
print(len(my_list) , " length")

# 😶‍🌫️ list slicing ... how to get a part of the list
print(my_list[1:3] , " slicing")

# my_list[:1] is a slice of the list that starts at index 0 and goes up to but does not include the index 1
# so it's just the first element of the list
print(my_list[:3] , " slicing first element")

# my_list[1:] is a slice of the list that starts at index 1 and goes up to the end of the list
print(my_list[1:] , " slicing last element")

#Negative Indexing
# my_list[-1] is the last element of the list
# my_list[-2] is the second to last element of the list
print(my_list[-1] , " negative indexing")

# python List are changeable 👻👻👻
my_list[0] = "aa"
print(my_list)

# how add an element to the list
my_list.append("ee")
print(my_list , " add an element to the list")

# insert an element at a specific index
my_list.insert(1 , "ff")
print(my_list)

#how to add List to List
my_list.extend(["new" , "list"])
print(my_list)

example = [ "apple" , 20 , "orange" , True , 9.5]
#18 banana False

example[1:4] = [18 , "banana" , False]
print(example , " new One")

# how to remove the value of List
my_list.remove("new")
print(my_list , " remove item name is ''cnew''")

# we can store remove items like this
removed_items = my_list.pop(2)
print(my_list)
print(removed_items)


#python list allowed duplicates
duplicates = [ "qq" , 10 , "ss" ,20 ,"gg" , "qq" , 10 , "ss" ,20 ,"gg" ]
print(duplicates , " duplicates")

my_list = [ "qq" , "dd" , "ss" ,"jj" ,"gg" ]
del my_list[0]
print(my_list , " test del")

# how to clear the list
my_list.clear()
print(len(my_list) , " clear list")

# how delete the list
del my_list
# ❌ print(my_list)

# 👻sorting
# case sensitive
sorting_test = [ "Orange" , "cherry" , "apple" , "banana" , "kiwi" , ]
sorting_test.sort()
print(sorting_test , " sorting")

#numeric sorting
sorting_test = [ 3, 44, 8, 21, 4, 48]
sorting_test.sort()
print(sorting_test , " sorting")

#reverse sorting
sorting_test = [ 3, 44, 8, 21, 4, 48]
sorting_test.sort(reverse=True)
print(sorting_test , " reverse sorting")

# reverse the list
sorting_test = [ 3, 44, 8, 21, 4, 48]
sorting_test.reverse()
print(sorting_test , " reverse the list")

#copy the list
my_list = [ "qq" , "dd" , "ss" ,"jj" ,"gg" ]
# ❌ my_list_copy = my_list
my_list_copy = my_list.copy()
print(my_list_copy , " copy the list")