#preamble
def even_numbers_for_loop():
    for number in range(1,31):
        if number%2==0:
            print(number)

def even_numbers_while_loop():
    even_number=2
    while even_number<=30:
        print(even_number)
        even_number+=2

def odd_numbers_for_loop():
    for number in range(1,31):
        if number%2!=0:
            print(number)

def odd_numbers_while_loop():
    odd_number=1
    while odd_number<=30:
        print(odd_number)
        odd_number+=2

#ahmed budgetting issue

total_budget=50000.00
marketing= 0.25*total_budget
operations= 0.5*total_budget
customer_acquisition_cost= 0.25*total_budget
cac_per_customer=5.00
acquired_customers= int(customer_acquisition_cost/cac_per_customer)
print(acquired_customers)