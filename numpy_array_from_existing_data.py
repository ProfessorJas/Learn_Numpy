import numpy as np

# Converting list to ndarray
x = [1, 2, 3]
a = np.asarray(x)
# print(a)

x = [1, 2, 3]
a = np.asarray(x, dtype = float)
# print(a)

# dnarray from tuple
x = (1, 2, 3)
a = np.asarray(x)
# print(a)

x = (1, 2, 3)
a = np.asarray(x, dtype = float)
# print(a)

# ndarray from list of tuples
x = [(1, 2, 3), (4, 5, 6)]
a = np.asarray(x)
print(a)

list = range(5)
print(list)