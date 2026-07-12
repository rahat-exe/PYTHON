# classes and objects

class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello {self.name}")

user1 = user("Rahat", 23)
user1.greet()


class Person(user):
    def __init__(self, name, age, gender):
        super().__init__(name,age)
        self.gender = gender
    def infoDisplay(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

person1 = Person("Rahat", 23, "Male")
person1.infoDisplay()


# dunder method

# __str__
# This is a special method that returns a string representation of the object.

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

    def info(self):
        return f"Student: {self.name}"
# __repr__
# This is a special method that returns a string representation of the object in a way that can be used to recreate the object.
    def __repr__(self):
       return f"Student('{self.name}')"
    

student1 = Student("Rahat")
print(student1)
print(student1.info())


# __len__
# This is a special method that returns the length of the object.

class Group:
    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)
    
g = Group(["Aaa", "B"])
print(len(g))  # 3
