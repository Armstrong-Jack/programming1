products = [
    {"name": "Apple", "price": 0.50},
    {"name": "Bread", "price": 1.20},
    {"name": "Milk", "price": 0.90}
]

for product in products:
    name = product["name"]
    price = product["price"]
    print(f"the price of {name} is £{price}")