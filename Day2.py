
# if / elif / else

age = 20

if age > 18:
    print("You are an adult")
elif age == 18:
    print("You are a teenager")
else:
    print("You are a child")

# for

for x in [1, 2, 3]:
    print(x)

for char in "Hello":
    print(char)

for x in "Hello":
    print(x)

# while

# i = 0
# while i < 5:
#     print(i)
    
# range()

for i in range(5):        # 0 to 4
    print(i)

for i in range(2, 6):     # 2 to 5
    print(i)

for i in range(1, 10, 2): # step = 2
    print(i)

# enumerate()

name = ["Rahat", "Muksid", "Rakib"]
for  index,value in enumerate(name):
    print(index,"->" ,value)

# zip()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for x, y in zip(list1, list2):
    print(x, y)


# Functions

def my_function():
    print("Hello from a function")

my_function()

def my_function(fname):
   return f"Hello {fname}"

print(my_function("Rahat"))
print(my_function("Muksid"))
print(my_function("Sohel"))

def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Muksid")

# *args

def add(*numbers):
    print(sum(numbers))

add(1,2,3)

# **kwargs
def user_info(**data):
    print(data)

user_info(name="Rahat", age=23)


# lambda

x = lambda a : a + 10
print(x(5))

square = lambda x: x * x
print(square(5))