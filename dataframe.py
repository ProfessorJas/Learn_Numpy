import numpy as np
import pandas as pd

# Take a 2D array as input to your DataFrame 
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(my_2darray))
print()

# Take a dictionary as input to your DataFrame
my_dict = {1: ['1', '3'], 2: ['2', '4'], 3: ['3', '6']}
print(pd.DataFrame(my_dict))
print()

# Take a DataFrame as input to your DataFrame
my_df = pd.DataFrame(data = [4, 5, 6, 7], index = range(0, 4), columns = ['A'])
print(pd.DataFrame(my_df))
print()

my_df = pd.DataFrame(data = [24, 35, 36, 57], columns = ['A'])
print(pd.DataFrame(my_df))
print()

# Take a Series as input to your DataFrame
my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
print(pd.DataFrame(my_series))