import numpy as np

a = np.arange(24)
# print(a)

a.ndim

# Now reshape it
b = a.reshape(2, 4, 3)
# print(b)

# numpy.itemsize returns the length of each element of array in bytes
x = np.array([1, 2, 3, 4, 5678910], dtype = np.int8)
print(x.itemsize)

x = np.array([1, 2, 3, 4], dtype= np.float32)
print(x.itemsize)

x = np.array([1, 2, 3, 4])
print(x.flags)