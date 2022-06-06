""" This program focuses on when X entered the loop will stop
Made by Abigael Ward
23/5/2022
"""
# main routine
product = ""  # product is a string
while product != "X":  # when x has never been entered
    product = input("Please enter the product: ").title()
    print(product)
else:  # when x has been entered
    print("You have exited the program")
