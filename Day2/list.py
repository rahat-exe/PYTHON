# A list is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1, 2, 3, 5, 6]

# print(numbers)
print(numbers[0])
print(numbers[-1])

numbers[2] = 10
print(numbers[2])

numbers.append(60) # add items at last
print(numbers)

numbers.insert(1, 69) # add item at a particular location
print(numbers)

numbers.remove(69)  # remove a element
print(numbers)

numbers.pop(0) # remove by index
print(numbers)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


names = ["Abbasi", "muksid", "rahat"]

for i in names:
    print(i)