import json

data = {
    "name": "Rahat",
    "age": 23
}

with open("data.json", "w") as file:
    json.dump(data, file)

with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])