# Sales Commission Calculator

def commission(amount):
    return amount * 0.10

sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}
leaderboard = []

# Repeatedly select the highest commission not already placed on the leaderboard.
while len(leaderboard) < len(sales):
    top_employee = ""
    top_commission = -1
    for employee, amount in sales.items():
        employee_commission = commission(amount)
        if employee not in leaderboard and employee_commission > top_commission:
            top_employee = employee
            top_commission = employee_commission
    leaderboard.append(top_employee)

print("Commission leaderboard:")
rank = 1
for employee in leaderboard:
    employee_commission = commission(sales[employee])
    print(f"{rank}. {employee}: ${employee_commission:.2f}")
    rank += 1
