""" This program focuses on when X entered the loop will stop
Abigael
"""
# main routine
product = ""  # product is a string
while product != "X":  # when x has never been entered
    product = input("Please enter the product: ").title()
    print(product)
else:  # when x has been entered
    print("You have exited the program")
