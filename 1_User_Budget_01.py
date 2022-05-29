""""User_budget_01 this program asks the maximum amount that the user wants to
spend and has a function that checks if the input is a integer
Abigael Ward
"""


# function that checks if the input is a integer
def integer_checker(question):
    error = "\nSorry, you must enter a number\n"  # if its not a integer
    string = ""
    while not string:
        try:
            string = int(input(question))
            return string
        except ValueError:
            print(error)  # prints error message here


budget = integer_checker("What is the maximum amount you want to spend?")

