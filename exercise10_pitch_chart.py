# Startup Pitch Deck Visualizer

charts = {
	"Projected revenue": {
		"Year 1": 3,
		"Year 2": 5,
		"Year 3": 8,
		"Year 4": 10,
		"Year 5": 14,
	}
}

# Multiply '#' by each value to create that year's bar.
for chart_name, yearly_values in charts.items():
	print(chart_name)
	for year, bar_length in yearly_values.items():
		bar = "#" * bar_length
		print(f"{year}: {bar}")
