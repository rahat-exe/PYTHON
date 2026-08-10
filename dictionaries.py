# A dictionary stores key-value pairs.

student = {
    "name":"Rahat",
    "roll_no":24,
    "semister":"3rd semester"
}

print(student)
print(student["name"])
print(student["roll_no"])

student["name"] = "Rahat Islam" # change a value
print(student)

student["age"] = 23 # add a new key-value pair
print(student)

student.pop("age") # remove a key-value pair
print(student)


# check if a key is present in a dictionary
if "name" in student:
    print("Name is present in the dictionary")
else:
    print("Name is not present in the dictionary")

# Loop through dictionary

for key in student:
    print(key, student[key])

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)