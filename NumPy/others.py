import numpy as np

randomNumber = np.random.default_rng(seed=1)

# print(randomNumber.integers(1,101))

# print(randomNumber.integers(1, 7, size=(3,3)))
# print(randomNumber.integers(1, 7, size=(3)))

# print(np.random.default_rng().integers(1, 7, size=(3,3)))

# print(np.random.uniform(low=1, high=7, size=(3,3)))

array = np.array([1, 2, 3, 4])
rng = np.random.default_rng()
rng.shuffle(array)

np.random.default_rng().shuffle(array)

print(array)

fruits = np.array(["apple", "banana", "cherry", "kiwi", "mango", "orange"])
fruit = rng.choice(fruits)
fruitss = rng.choice(fruits, size=(3))
print(fruitss)
