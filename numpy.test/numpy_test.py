import numpy as np

from Control_flow.Match import temperatures

a = np.array([1, 2, 3])
print(a)
print(type(a))

b = np.array([3, 4, 5])
c = a + b
print(c , " addition")

d = a - b
print(d , " subtraction")

e = a * b
print(e , " multiplication")

f = a / b
print(f , " division")

print(np.sum(a))
print(np.mean(a)) #AVG

print(np.min(a))
print(np.max(a))


#multidimensional array
array_1 = np.array([[1, 2, 3], [4, 5, 6] ])
print(array_1)
print(type(array_1))

print(array_1.shape)
print(array_1.size)
print(array_1.ndim)
print(array_1.dtype )

#3D array
array_2 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(array_2)
print(type(array_2))

print(array_2.shape)
print(array_2.size)


array_3 = np.array([[1, 2, 3], [4, 5, 6] ])
print(array_1[0,0])

array_4 = np.array([[[4 ,5 ,8], [11,20,15]], [[9 ,6 ,4], [13, 12 ,15]]])

print(array_4[0, 1, 1])
print(array_4[1, 0, 2])




"""
# Q) your are given the following array representing the body temperature (in celsius) of 5 patients over three time plots(morning, afternoon, and evening).
#   31 30 28  
#   29 24 32  
#   26 24 27 
#   31 34 35 
#   28 31 30
# identify and extract all temperature readings greater than the daily avarage temperature using boolean indexing in numpy arrays
"""

print("qqqqqqqqqqqqqqqq")

temp = np.array([[31, 30, 28], [29, 24, 32], [26, 24, 27], [31, 34, 35], [28, 31, 30]])

daily_avg = np.mean(temp)

print(daily_avg)

condition = temp > daily_avg

print(condition)