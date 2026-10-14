# Market Survey Analyzer

preferences = ["coffee", "tea", "coffee", "soda"]
counts = {}

# Add each vote to the count for its product.
for preference in preferences:
	if preference not in counts:
		counts[preference] = 0
	counts[preference] += 1

total_votes = len(preferences)

# Convert each product's count into a percentage of all votes.
for product, count in counts.items():
	market_share = count / total_votes * 100
	print(f"{product}: {market_share:.0f}%")
