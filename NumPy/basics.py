import numpy as np

# print(np.__version__)

array = np.array([1, 3, 5, 7, 9])

print(array)
print(type(array))

array = array * 2
# print(array)

# Multidimentional Array

matrix = np.array([[1, 2], [4, 5], [7, 8]])

# print(matrix)
# print(matrix.shape)
# print(matrix.ndim)

threeDimentional = np.array([[[1, 2], [3, 4]],
                            [[5, 6], [7, 8]]])

# print(threeDimentional) 
# print(threeDimentional.shape)
# print(threeDimentional.ndim)

print(threeDimentional[0][0][0]) # chain indexing
print(threeDimentional[0, 0, 0])

print(threeDimentional[1,1,1])

