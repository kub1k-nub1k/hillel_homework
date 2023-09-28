loan_amount = float(input("Введіть суму кредиту: "))
initial_loan_amount = loan_amount
months1 = 60

print("1 рiк")
print("{:<9} {:<13} {:<13} {:<13}".format("Місяць", "Сума платежу", "Відсотки", "Залишок"))

months = 12
payment_per_month = loan_amount / months

for month in range(1, months + 1):
    if month <= 24:
        interest_rate = 0.02
    else:
        interest_rate = 0.04

    interest = loan_amount * interest_rate
    payment = payment_per_month + interest
    loan_amount -= payment_per_month

    print("{:<9} {:<13.2f} {:<13.2f} {:<13.2f}".format(month, payment, interest, loan_amount))

print("-" *44)
print("5 рокiв")
print("{:<9} {:<13} {:<13} {:<13}".format("Місяць", "Сума платежу", "Відсотки", "Залишок"))

payment_per_month1 = initial_loan_amount / months1

for month in range(1, months1 + 1):
    if month <= 24:
        interest_rate = 0.02

    interest = initial_loan_amount * interest_rate
    payment = payment_per_month1 + interest
    initial_loan_amount -= payment_per_month1

    print("{:<9} {:<13.2f} {:<13.2f} {:<13.2f}".format(month, payment, interest, initial_loan_amount))
