# A set stores unique values.

numbers = {1, 2, 3, 4, 5, 5, 4, 3}
print(numbers)

numbers.add(6)  # to add
print(numbers)

numbers.remove(6) # to remove
print(numbers)


if 3 in numbers:
    print("Found")

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}

print(a | b) # Union
print(a & b) # Intersection
print(a - b) # Difference
print(b - a) # Difference