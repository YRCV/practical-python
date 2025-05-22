# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

#assuming that the extra payments are together with normal payments
while principal > 0:
    if months>=extra_payment_start_month and months<=extra_payment_end_month:
        paid = payment + extra_payment
    else:
        paid = payment

    if principal < payment:
        paid = principal * (1+rate/12)

    principal = principal * (1+rate/12) - paid
    total_paid += paid
    months += 1
    
    print(months, round(total_paid,2), round(principal,2))

print(f'\nTotal paid: {total_paid:0.2f} \nMonths:{months}')