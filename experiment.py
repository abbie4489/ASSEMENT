# Integer checking function - loops until a valid number is entered

def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    type = float()
    while not type:
        try:
            type = float(input(question))
            return type
        except ValueError:
            print(error)


# Main routine
age = integer_checker("Please enter your age: ")
print(f"Age = {age}")

