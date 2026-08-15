import numpy as np

# Scaler arithmetic

array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 4)
# print(array ** 5)

# vector

array2 = np.array([1.33, 2.45, 3.99])

# print(np.sqrt(array2))
# print(np.round(array2))
# print(np.floor(array2))
# print(np.ceil(array2))

# print(array2 > 2)
# print(array2 < 2)
# print(array2 == 2)
# print(array2 != 2)

# print(np.pi)
# print(np.e)

# radii = np.array([1, 2, 3, 4])
# print(np.pi * radii ** 2)


## Element-wise Arithmetic

array3 = np.array([1, 2, 3, 4])
array4 = np.array([5, 6, 7, 8])

# print(array3 + array4)
# print(array3 - array4)
# print(array3 * array4)
# print(array3 / array4)
# print(array3 ** array4)


## Comparison operator

scores = np.array([90, 55, 30, 100, 70, 30])
print(scores == 100)
print(scores >= 30)
print(scores < 30)

scores[scores < 40] = 0
print(scores)