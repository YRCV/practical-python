# sears.py
bill_thickness = 0.11*0.001 #mm->m
sears_tower_height = 442 #m
bills_amount = 1
day = 1
bill_tower_height = 0

while bill_tower_height < sears_tower_height:
    print(day, bills_amount, bill_tower_height)
    day += 1
    bills_amount *= 2
    bill_tower_height = bills_amount * bill_thickness

print('\nNumber of days',day)
print('Number of bills',bills_amount)
print('Final height', bill_tower_height)