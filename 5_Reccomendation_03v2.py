"""Identifying the price that is the lowest below the budget make the
recommendation. version 2
Made by Abigael
28/05/2022
"""


# Functions
# function that ends when appropriate answer is entered
def get_budget():
    cheapest_item = min(test_list, key=lambda x: x[2])
    cheaper = cheapest_item[2]
    print(f"The cheapest price is ${cheaper}")
    budget = 0
    valid = False
    while not valid or budget < cheaper:
        try:
            budget = float(input('what is your budget? (please enter budget '
                                 'above lowest price): '))
        except ValueError:
            print('not a valid response')
        else:
            valid = True
    return budget


# Function that finds the best value and most affordable
def best_value(test_list, budget):
    affordable = [item for item in test_list if item[2] <= budget]
    max_affordable = []
    for i in range(0, len(affordable)):
        if i == 0:
            max_affordable = affordable[i]
        elif affordable[i][3] < max_affordable[3]:
            max_affordable = affordable[i]
        elif affordable[i][3] == max_affordable[3]:
            max_affordable.append(affordable[i])

    return max_affordable


# Lists
test_list = [["Greggs", 200.0, 7.0, 0.04], ["Moccona", 90.0, 10.49, 0.12],
             ["Nescafe", 180.0, 7.79, 0.04]]


# main routine
budget = get_budget()
value = best_value(test_list, budget)
# Recommendation
print("The item with the best value for you is", '{}, {}, {}'.format(value[0],
                                                                     value[1],
                                                                     value[2]))
