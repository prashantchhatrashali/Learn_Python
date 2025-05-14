'''
Loop Practice: Shopping List Calculator
Create a program that:

1. Asks the user how many items they want to add to their shopping list
2 . For each item, asks for the item name and price
3. Calculates and displays the total cost of all items
4. Finds and displays the most expensive item
'''
#from To_Do_List import user_input

goods = []

print(" Shopping List Calculator! ")
artical_count = int(input("Please enter the number of artical you want to add in your shopping list \n"))

for i in range(artical_count):
    artical_name = input(f"Please enter the artical {i+1} name: ")
    try:
        artical_price = int(input(f"Please enter the price for {artical_name}: "))
        goods.append({artical_name: artical_price})
    except ValueError:
        print("Invalid Price! Using 0 as the price.")
        goods.append({artical_name: 0})

print("Your shopping list:")
for i in goods:
    for name, price in i.items():
        print(f"{name}: ${price}")

# Calculate and print total
total = 0
for item in goods:
    # Get the first (and only) value from the dictionary
    price = list(item.values())[0]
    total += price
print(f"Total cost: ${total}")