""""User_budget_03 - based on User_budget_02
Abigael Ward
"""


def float_checker(question, error):
    while True:
        try:
            string = float(input(question))
            return string
        except ValueError:
            print(error)


budget = float_checker("What is the maximum amount you want "
                       "to spend? ", "Sorry You must enter a number")

