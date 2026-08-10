# A list comprehension is a compact way to create a list.

number = []

# for i in range(5):
#     number.append(i)

# print(number)

number = [i for i in range(5)]
print(number)

numbers = [i for i in range(20) if i % 2 == 0]
print(numbers)

square = [i ** 2 for i in range(5)]
print(square)

names = ["Rahat", "MUKSID", "ABBASI"]

lower_name = [name.lower() for name in names ]
print(lower_name)