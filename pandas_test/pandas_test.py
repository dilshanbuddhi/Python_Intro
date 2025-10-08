import pandas as pd

data = {
    "Name": ["John", "Jane", "Bob"],
    "Age": [30, 25, 40],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data , index=["a", "b", "c"])
print(df)
print(type(df))
#print a and d rows
print(df.loc[['a', 'c']])

print(df.iloc[[0, 2]])

#how to add a new column
df["Gender"] = ["male", "female", "male"]
print(df)

print()
#how to add a new row
df.loc["d"] = ["John", 30, "New York", "male"]
print(df)

df["Distance"] = [100, 200, 300, 400]
print(df)

print()
#filter age > 30 and distance > 250
print(df[(df["Age"] < 30) & (df["Distance"] < 250)])

# Q) your are given the following data set representing the exam record of students in the programming course.The data includes marks for
#    two assignments and a final exam.
#    studentID        Name      Assignment1     Assignment2     FinalExam
#     #    1001     Ayesha          78              95              90
#     #    1002     Nimal           65              70              72
#     #    1003     Tharindu        88              90              95
#     #    1004     Kasun           50              45              60
#     #    1005     Sachini         80              75              85

# Write a python pragram using pandas:
# 1. Create a DataFrame using the data given amove.
# 2. Display the Names of all students who scored more than 80 in the FinalExam.
# 3. Calculate the average score for each student across all 3 assessments and add it as a new column called "Average".
# 4. Display student(s) with the highest average score.
# 5. Calculate and Display the Total Marks scored by all students in assignment 01


data = {
    "studentID": [1001, 1002, 1003, 1004, 1005],
    "Name": ["Ayesha", "Nimal", "Tharindu", "Kasun", "Sachini"],
    "Assignment1": [78, 65, 88, 50, 80],
    "Assignment2": [95, 70, 90, 45, 75],
    "FinalExam": [90, 72, 95, 60, 85]
}

df = pd.DataFrame(data)
print(df)

print(df[df["FinalExam"] > 80]["Name"])

df["Average"] = (df["Assignment1"] + df["Assignment2"] + df["FinalExam"]) / 3
print(df)

print(df[df["Average"] == df["Average"].max()]["Name"])

print(df["Assignment1"].sum())