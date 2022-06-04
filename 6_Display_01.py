# import the library
import pandas as pd

test_list = pd.DataFrame([["coffee", "200", "70"], ["Moccona", "90", "10"],
                          ["Nescafe", "180", "7.79"]])

test_list.index = ['name:', 'unit:', 'price:']
print(test_list)
