# Expense Report Categorizer

expenses = {
	"Travel": [500, 200],
	"Meals": [40, 60, 30],
	"Supplies": [100],
}

grand_total = 0

print("Expense summary report")
# The inner loop totals one category; the outer loop adds each category to the grand total.
for category, amounts in expenses.items():
	category_total = 0
	for amount in amounts:
		category_total += amount
	grand_total += category_total
	print(f"{category}: ${category_total:.2f}")

print(f"Grand total: ${grand_total:.2f}")
