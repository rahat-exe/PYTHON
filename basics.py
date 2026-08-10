
name = "Rahat"  # string
age = 23        # integer
height = 5.6    # float
is_student = True  # boolean

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

print(height)
print(int(height))


# if / elif / else
# Used for decision making.

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 75

if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")

age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")


# for / while loops

for i in range(5):
    print(i)

names = ["Rahat", "John", "Alex"]

for name in names:
    print(name)


# while loop

i = 0

while i < 5:
    print(i)
    i += 1


## Functions

def greet():
    print("Hello")

def greetByName(name):
    print(f"Hello {name}")

greet()
greetByName("Rahat")

def add(a, b):
    return a + b

add(1, 2)
print(add(1, 2))


## Input/Output

print("Hello")

userName = input("Enter your name: ") #input
userAge = int(input("Enter your age: "))

print(f"Hello {userName}")  # f-string
print(f"You are {userAge} years old")


for i in range(5):
    student = input("Enter student name: ")
    marksObtained = int(input("Enter marks obtained: "))
    print(f"Student: {student}, Marks: {marksObtained}")