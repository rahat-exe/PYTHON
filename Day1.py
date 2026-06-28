x = 10
name = "rahat"
is_active = True   # capital T/F
nothing = None     # not null

print(f"Hello, {name}")

# LIST 
# A list stores multiple items in order. It is mutable, meaning you can change it after creation.

fruits = ["Apple", "Banana", "Mango"]
print(fruits[1])
print(fruits[-1])

fruits[1] = "Orange"
print(fruits)


fruits.append("Watermelon")
fruits.insert(0, "Pineapple")
fruits.remove("Mango")
fruits.pop()
print(fruits)

for fruit in fruits:
    print(fruit)


# TUPLES
# A tuple stores multiple items in order. It is immutable, meaning you cannot change it after creation.

fruitss = ("Apple", "Banana", "Mango")
print(fruitss[1])
print(fruitss[-1])

for fruit in fruitss:
    print(fruit)

# fruitss[1] = "Orange"
# print(fruitss)  # TypeError: 'tuple' object does not support item assignment


# SET
# A set stores unique values. It is mutable, meaning you can change it after creation.

numbers = {1, 2, 3, 4, 5, 5, 5}
print(numbers) # Duplicates are removed

numbers.add(6)
print(numbers)

numbers.remove(3)
print(numbers)

print(3 in numbers)

for number in numbers:
    print(number)

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union
print(A & B)   # Intersection
print(A - B)   # Difference
print(A ^ B)   # Symmetric Difference


# DICTIONARY
# A dictionary stores a collection of key-value pairs. It is mutable, meaning you can change it after creation.

person = {
    "name": "Rahat",
    "age": 24,
    "city": "Guwahati",
}
print(person)
print(person["name"])
print(person.get("age"))
print(person.keys())
print(person.values())
print(person.items())

person["Sex"] = "Male"
print(person)
# person.pop("age")
del person["age"]
print(person)
person["name"] = "Rahat Islam"
print(person)

for key, value in person.items():
    print(key, value)

print(person.get("name"))
print(person["name"])


# Type Coercion
# Type Coercion is the automatic conversion of one data type to another data type.

# print("5" + 5) # TypeError: can only concatenate str (not "int") to str
print("5" + "5") # 55

print(int("5") + 5) # 10
print(str(5) + "5") # 55

print("5"*3) # 555

# print("5"-2) # TypeError: unsupported operand type(s) for - : 'str' and 'int'

print(int("5") - 2) # 3
# print("5"-"2") # TypeError: unsupported operand type(s) for - : 'str' and 'str'

# Truthy and Falsy

print(bool("")) # False
print(bool(" ")) # True
print(bool("0")) # True
print(bool(0)) # False

print(bool([])) # False
print(bool(())) # False 
print(bool({})) # False

print(bool([1])) # True
print(bool((1,))) # True
print(bool({"name": "Rahat"})) # True

print(bool(1)) # True
print(bool(0)) # False

# Equality

print(1 == 1) # True
print(1 == 2) # False
print("1" == 1) # False

# Division

print(10 / 3) # 3.3333333333333335
print(10 // 3) # 3

# Input

name = input("Enter your name: ")
print("Hello, " + name)

age = input("Age: ")
print("You are " + age + " years old")

print(type(age))
print(type(int(age)))


# Explicit Conversion

int("10")
float("3.14")
str(100)
bool(1)
list("abc")
tuple([1,2,3])
set([1,2,2,3])