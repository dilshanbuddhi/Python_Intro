import json

with open("test.json" , "r") as f:
    data = json.load(f)
    print(data)
    print(type(data))

# how to write json


data = {
    "name": "John Doe",
    "age": 30,
    "isStudent": False,
    "hobbies": [
        "reading",
        "gardening",
        "swimming"
    ]
}

with open("test.json" , "w") as f:
    json.dump(data , f)