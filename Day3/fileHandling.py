#### Read

file = open("data.txt", "r") # access a file, r means read

content = file.read()

print(content)

file.close()


### with open()
# The file automatically closes after the with block.

with open("data.txt", "r") as file:
    content = file.read()
print(content)

## The file automatically closes after the with block.

with open("data.txt", "r") as file:
    for line in file:
        print(line)

# OR

with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)

#### Write

# "w" overwrites the existing content.
with open("data.txt","w") as file: 
    file.write("Hello Python")

# "a" appends the content.
with open("data.txt","a") as file: 
    file.write("\nMachine Learning")

### JSON files
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