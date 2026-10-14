# Business Growth Projection

initial_revenue = float(input("Enter the initial revenue: "))
growth_rate = float(input("Enter the annual growth rate (%): ")) / 100

print("Revenue projection")
print("Year  | Revenue")
print("------+----------")

revenue = initial_revenue
# Apply one year of growth before printing each year's projected revenue.
for year in range(1, 11):
	revenue *= 1 + growth_rate
	print(f"{year:>4}  | ${revenue:,.2f}")
