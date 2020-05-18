income = int(input())
tax_rate = 0
# Find tax slab
if income <= 15527:
    tax_rate = 0
elif 15528 <= income <= 42707:
    tax_rate = 15
elif 42708 <= income <= 132406:
    tax_rate = 25
elif income > 132407:
    tax_rate = 28

calculated_tax = round(income * (tax_rate / 100))

print(f'The tax for {income} is {tax_rate}%. That is {calculated_tax} dollars!')
