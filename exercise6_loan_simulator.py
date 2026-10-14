# Bank Loan Repayment Simulator

loan_amount = float(input("Enter the loan amount: "))
annual_rate = float(input("Enter the annual interest rate (%): "))
monthly_payment = float(input("Enter the monthly payment: "))

while loan_amount <= 0:
	print("Loan amount must be greater than zero.")
	loan_amount = float(input("Enter the loan amount: "))

while annual_rate < 0:
	print("Interest rate cannot be negative.")
	annual_rate = float(input("Enter the annual interest rate (%): "))

monthly_rate = annual_rate / 100 / 12

while monthly_payment <= loan_amount * monthly_rate:
	print("Payment must be greater than the first month's interest.")
	monthly_payment = float(input("Enter the monthly payment: "))

def months_to_pay_off(balance, rate, payment):
	months = 0
	while balance > 0:
		# Apply monthly interest before the payment, as with a typical loan balance.
		balance += balance * rate
		balance -= payment
		months += 1
		if balance < 0:
			balance = 0
	return months

months = months_to_pay_off(loan_amount, monthly_rate, monthly_payment)
print(f"Loan paid off in {months} months.")
