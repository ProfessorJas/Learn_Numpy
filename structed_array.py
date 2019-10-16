import numpy as np
import pandas as pd

# A structured array
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))
# Print the structured array
print(my_array['foo'])

my_another_array = np.ones(3, dtype = ([('foo', int), ('bar', float)]))
print(my_another_array['bar'])

my_array2 = my_array.view(np.recarray)
print(my_array2)