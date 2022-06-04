"""Identifying the price that is the lowest below the budget make the
recommendation. make it into a function
"""


def float_checker(question):
    while True:
        try:
            floats = float(input("Sorry that is not a valid answer. What is your budget? "))
            return round(floats, 2)
        except ValueError:
            print()


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


test_list = [["coffee", 200.0, 70.0, 0.04], ["Moccona", 90.0, 10.0, 0.11],
             ["Nescafe", 180.0, 7.79, 0.35]]

a = []
while a == []:
    budget = float_checker(input("what is your budget? "))
    a = best_value(test_list)
print(a)
