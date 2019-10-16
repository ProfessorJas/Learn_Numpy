import numpy as np

# numpy.empty creates an uninitialized array of specified shape and dtype
x = np.empty([3, 2], dtype = int)
# print(x)

# returns a new array of specified size, filled with zeros
x = np.zeros(5)
# print(x)

x = np.zeros((2, 2), dtype = [('x', 'i4'), ('y', 'i4')])
print(x)

# numpy.ones return a new array of specified size and type, filled with ones
x = np.ones(5)
print(x)

x = np.ones([2, 2], dtype = int)
print(x)