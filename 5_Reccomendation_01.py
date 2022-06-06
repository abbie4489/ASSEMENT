"""Identifying the price that is the lowest below the budget
Made by Abigael
27/05/2022
"""


# Lists
test_list = [["coffee", 200.0, 70.0], ["Moccona", 90.0, 10.0],
             ["Nescafe", 180.0, 7.79]]

# Main routine
budget = 9  # just a trial
for index in range(0, len(test_list)):
    if (test_list[index][2]) <= budget:
        print((test_list[index]))
        break
    else:
        print(f'Place in list: {index}')
        continue


print("Done")
