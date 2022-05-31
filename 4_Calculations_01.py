"""Average unit price
"""

number = 0
total_price = 0
calc = float()
test_list = [["coffee", "200", "7"], ["Moccona", "90", "10"], ["Nescafe", "180", "7.79"]]
for index in range(len(test_list)):
    number += 1
    price_numbers = float(test_list[index][2])
    quantity_numbers = float(test_list[index][1])
    total_price += float(price_numbers)
    calc += round(price_numbers / quantity_numbers, 2)

print(f"The average unit price is ${round(calc / number, 2)}")
