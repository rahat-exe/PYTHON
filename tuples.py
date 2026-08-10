# A tuple is similar to a list, but it is immutable, meaning you cannot change its elements after creation.

coordinates = (10, 20)
print(coordinates)

print(coordinates[0])

# coordinates[0] = 50  # cannot be done as it is immutable

### Tuple unpacking

person = ("Rahat", 24)

name , age = person
print(name, age)

x, y = coordinates
print(x, y)