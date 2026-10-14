# Retail Checkout Simulation

prices = []
price = float(input("Enter an item price (0 to finish): $"))

# Keep accepted prices for the summary; zero is only the stopping signal.
while price != 0:
	if price < 0:
		print("Price cannot be negative. Try again.")
	else:
		prices.append(price)
	price = float(input("Enter an item price (0 to finish): $"))

total = sum(prices)
count = len(prices)
# An empty checkout has no average, so report zero instead of dividing by zero.
average = total / count if count > 0 else 0

print(f"Total purchase amount: ${total:.2f}")
print(f"Average item cost: ${average:.2f}")
print(f"Number of items bought: {count}")
