import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print()

# This resize the array
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)
print()

# Numpy also provides a reshape function to resize an array
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)