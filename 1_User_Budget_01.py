""""User_budget_01
Abigael Ward
"""


def integer_checker(question):
    error = "\nSorry, you must enter a number\n"
    string = ""
    while not string:
        try:
            string = int(input(question))
            return string
        except ValueError:
            print(error)


budget = integer_checker("What is the maximum amount you want to spend?")

