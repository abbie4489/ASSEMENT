"""This program sorts the list by best value least to greatest
"""

# import the library
import pandas as pd

# Original list
test_list = [["Greggs", 200.0, 7.0, 0.04], ["Moccona", 90.0, 10.49, 0.12],
             ["Nescafe", 180.0, 7.79, 0.04]]

# sorting the original list
test_list.sort(key=lambda row: (row[3]))

# new list with headers and pandas format
displayed_list = pd.DataFrame({'Name': [item[0] for item in test_list],
                               'Weight': [item[1] for item in test_list],
                               'Prices': [item[2] for item in test_list],
                               'Value': [item[3] for item in test_list]})

# print statements
print(displayed_list)
