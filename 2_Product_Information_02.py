""" This program uses a while True loop and doesnt print x
Abigael
"""
# main routine
while True:
    product = input("Please enter the product or press x to leave: ").title()
    if product != "X":  # when x has never been entered
        print(product)
    else:
        print("You have left the program")  # when x has been entered
        break  # will stop the loop completely

