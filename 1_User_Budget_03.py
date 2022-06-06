""""User_budget_03 minimises the code by using while true - version 2
Made by Abigael Ward
22/5/2022
"""


def float_checker(question, error):
    while True:
        try:
            floats = float(input(question))
            return round(floats, 2)
        except ValueError:
            print(error)


budget = float_checker("What is the maximum amount you want "
                       "to spend? ", "Sorry You must enter a number")
print(budget)

