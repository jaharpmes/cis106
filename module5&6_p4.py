principal = float(input("Enter the principal amount: $"))
years = int(input("Enter the years to maturity: "))
if principal > 100000 and years == 5:
    interest_rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    interest_rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02
interest_amount = principal * interest_rate
print(f"Principal: ${principal:.2f}")
print(f"Interest rate: {interest_rate * 100:.2f}%")
print(f"Interest amount: ${interest_amount:.2f}")
