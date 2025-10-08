import csv

# Plain reader
with open("test.csv", newline="") as f:   # newline="" avoids blank lines on Windows
    reader = csv.reader(f)
    for row in reader:
        print(row)

# DictReader
with open("test.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)



csv_file_path = 'sample_output.csv'

data = [
    {"Name": 'John', "Age": 30, "City": 'New York'},
    {"Name": 'Jane', "Age": 25, "City": 'London'},
    {"Name": 'Bob', "Age": 40, "City": 'Paris'}
]

fieldnames = ['Name', 'Age', 'City']

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print(f"Data saved to {csv_file_path}")