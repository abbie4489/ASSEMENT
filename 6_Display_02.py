"""This program renames the headers to appropriate names
Made by Abigael
28/05/2022
"""

# import the library
import pandas as pd

# The original list
test_list = [["Greggs", 200.0, 7.0, 0.04], ["Moccona", 90.0, 10.49, 0.12],
             ["Nescafe", 180.0, 7.79, 0.04]]

# new list with headers and pandas format
display_list = pd.DataFrame({'name': [item[0] for item in test_list],
                               'weight': [item[1] for item in test_list],
                               'prices': [item[2] for item in test_list],
                               'value': [item[3] for item in test_list]})

# prints the formatted list
print(display_list)
