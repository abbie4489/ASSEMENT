"""this program works out the the cheapest item
Made by Abigael
27/05/2022
"""

# Variables
total_value = float()
total_price = float()
cheapest_item = float()
expensive_item = float()

# Lists
test_list = [["Greggs", 200.0, 7.0], ["Moccona", 90.0, 10.49],
             ["Nescafe", 180.0, 7.79]]

# Main Routine
test_list = sorted(test_list, key=lambda x: x[2])
for index in range(0, len(test_list)):
    value = round(float((test_list[index][2]) / (test_list[index][1])), 2)
    total_price += float(test_list[index][2])
    total_value += round(float(test_list[index][2]) / float(test_list[index][1]), 2)
    test_list[index].append(value)
    cheapest_item = test_list[0]
    expensive_item = test_list[-1]

# Print Statements
print(test_list)
print(f"Average unit price: ${round(total_value / len(test_list), 2)}\nCheapest "
      f"item: {cheapest_item[0]} with the price of ${cheapest_item[3]} per unit "
      f"and a overall price of ${cheapest_item[2]}\nMost expensive item: "
      f"{expensive_item[0]} with the price of ${expensive_item[3]} per unit and"
      f" a overall price of ${expensive_item[2]}")
