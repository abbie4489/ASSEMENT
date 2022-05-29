""""User_budget_02 - this program is based on User_budget_01 but simplifies the
error message - version 1
Abigael Ward
"""


def float_checker(question, error):
    string = ""
    while not string:
        try:
            string = float(input(question))
            return round(string, 2)
        except ValueError:
            print(error)


budget = float_checker("What is the maximum amount you want "
                       "to spend?", "Sorry You must enter a number")
print(budget)
