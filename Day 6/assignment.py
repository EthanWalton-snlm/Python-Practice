# Inventory Management Assignment
# Ethan Walton

inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
]

proceed = "Y"

while proceed.lower() != "n":
    item_name = input("What is the product name? ")
    item_qty = int(input("What is the quantity? "))
    item_price = float(input("What is the price? "))

    for prod in inventory:
        if prod["name"] == item_name:
            prod["quantity"] = item_qty
            prod["price"] = item_price
            print(f"Updated {item_name} successfully! 🎉")
            break
    else:
        product = {"name": item_name, "quantity": item_qty, "price": item_price}
        inventory.append(product)
        print(f"Added new product {item_name}! 🎉")

    print(f"Updated Inventory: {inventory}")

    proceed = input("Would you like to add another product? (Y/N): ")

print(inventory)
