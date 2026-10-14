# Customer Loyalty Tiers

def loyalty_tier(total):
	# The upper boundary of Silver is inclusive; larger totals qualify for Gold.
    if total < 1000:
        return "Bronze"
    elif total <= 4999:
        return "Silver"
    else:
        return "Gold"

customers = {"Ava": 800, "Ben": 1200, "Cara": 5000, "Dee": 3200}
tiers = {"Bronze": 0, "Silver": 0, "Gold": 0}

for customer, total in customers.items():
    tier = loyalty_tier(total)
    tiers[tier] += 1
    print(f"{customer}: {tier}")

print("Customer totals by tier:")
for tier, count in tiers.items():
    print(f"{tier}: {count}")
