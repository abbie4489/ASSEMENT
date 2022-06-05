"""Identifying the price that is the lowest below the budget make the
recommendation. version 1
"""


# Functions
# function that ends when appropriate answer is entered
def float_checker(question):
    floats = float()
    while not floats:
        try:
            floats = float(input(question))
            return round(floats, 2)
        except ValueError:
            print("please enter a float")


# Function that finds the best value and most affordable
def best_value(test_list):
    affordable = [item for item in test_list if item[2] <= budget]
    max_affordable = []
    for i in range(0, len(affordable)):
        if i == 0:
            max_affordable = affordable[i]
        elif affordable[i][2] > max_affordable[2]:
            max_affordable = affordable[i]
        elif affordable[i][2] == max_affordable[2]:
            max_affordable.append(affordable[i])

    return max_affordable


# Lists
test_list = [["Greggs", 200.0, 7.0, 0.04], ["Moccona", 90.0, 10.49, 0.12],
             ["Nescafe", 180.0, 7.79, 0.04]]

# Loop
a = []
while a == []:
    cheapest_item = min(test_list, key=lambda x: x[2])
    print(f"The lowest price is ${cheapest_item[2]}")
    budget = float_checker("what is your budget? (please enter above "
                           "the lowest price): ")
    a = best_value(test_list)

# recommendation
print(f"The next item below your budget is {a}")
