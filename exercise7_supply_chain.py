# Simple Supply Chain Tracker

warehouses = [
	{"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
	{"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}},
]
product_totals = {}

# Add each warehouse's quantity to the running total for that product.
for warehouse in warehouses:
	for product, quantity in warehouse["inventory"].items():
		if product not in product_totals:
			product_totals[product] = 0
		product_totals[product] += quantity

print("Total stock across the supply chain:")
for product, quantity in product_totals.items():
	print(f"{product.title()}: {quantity}")
