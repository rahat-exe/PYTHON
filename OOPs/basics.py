class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student = Student("Rahat Islam", 24)

print(student.name)
print(student.age)

student.info()