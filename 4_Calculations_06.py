"""Average Price, Best value = price / quantity and the most expensive item,
cheapest item, adding the value to the list and then sorting the list. let the
user add the information to the list.
29/05/2022
Abigael
"""


total_value = float()
total_price = float()
cheapest_item, cheapest_value = float(), float()
expensive_item, expensive_item_value = float(), float()
test_list = [["coffee", 200.0, 70.0], ["Moccona", 90.0, 10.0],
             ["Nescafe", 180.0, 7.79]]

test_list = sorted(test_list, key=lambda x: x[2])
for index in range(0, len(test_list)):
    value = round(float((test_list[index][2]) / (test_list[index][1])), 2)
    total_price += float(test_list[index][2])
    total_value += round(float(test_list[index][2]) / float(test_list[index][1]), 2)
    test_list[index].append(value)
    cheapest_item = test_list[0]
    expensive_item = test_list[-1]

print(test_list)
print(f"Average unit price: ${round(total_value / len(test_list), 2)}\nCheapest "
      f"item: {cheapest_item[0]} with the price of ${cheapest_item[3]} per unit"
      f"and a overall price of ${cheapest_item[2]}\nMost expensive item: "
      f"{expensive_item[0]} with the price of ${expensive_item[3]} per unit and"
      f" a overall price of ${expensive_item[2]}")
