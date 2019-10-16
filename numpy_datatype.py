import numpy as np

# Print out int32
dt = np.dtype(np.int32)
# print(dt)

# int8, int16, int32, int64 can be replaced by equivalent string 'i1', 'i2', 'i4', 'i8'
dt = np.dtype('i4')
# print(dt)

dt = np.dtype('>i4')
# print(dt)

dt = np.dtype([('age', np.int8)])
# print(dt)

dt = np.dtype([('age', np.int8)])
a = np.array([(10, ), (20, ), (30, )], dtype = dt)
print(a)

# file name can be used to access the content of age column
dt = np.dtype([('age', np.int8)])
a = np.array([(10, ), (20, ), (30, )], dtype = dt)
print(a['age'])

# Define a structured data type called student with a string field 'name', an integer field 'age' 
# and a float field 'marks'. This dtype is applied to ndarray object
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

# Create an student object
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 66), ('amgio', 3, 77.7)], dtype = student)
print(a)