"""This program uses panda to display the information
"""

# import the library
import pandas as pd

# List
# formats the list
test_list = pd.DataFrame([["coffee", "200", "70"], ["Moccona", "90", "10"],
                          ["Nescafe", "180", "7.79"]])

# Prints the list with panda format
print(test_list)
