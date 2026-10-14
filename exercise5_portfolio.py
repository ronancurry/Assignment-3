# Stock Portfolio Tracker

import random

portfolio = {
	"AAPL": {"shares": 10, "price": 170},
	"TSLA": {"shares": 4, "price": 250},
	"AMZN": {"shares": 2, "price": 130},
}

def portfolio_value():
	total_value = 0
	for stock in portfolio.values():
		total_value += stock["shares"] * stock["price"]
	return total_value

for ticker, stock in portfolio.items():
	stock_value = stock["shares"] * stock["price"]
	print(f"{ticker} value: ${stock_value:.2f}")

print(f"Total portfolio value: ${portfolio_value():.2f}")

# Update every stock once per day, then report the revised portfolio value.
for day in range(1, 6):
	for stock in portfolio.values():
		daily_change = random.uniform(-0.05, 0.05)
		stock["price"] *= 1 + daily_change
	print(f"Day {day} portfolio value: ${portfolio_value():.2f}")
