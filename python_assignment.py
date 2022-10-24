

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

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#printing even numbers
even_numbers_for_loop()
even_numbers_while_loop()
#printing odd numbers
odd_numbers_for_loop()
odd_numbers_while_loop()


#ahmed budgetting issue
total_budget=50000.00
marketing= 0.25*total_budget
operations= 0.5*total_budget
customer_acquisition_cost= 0.25*total_budget
cac_per_customer=5.00
acquired_customers= int(customer_acquisition_cost/cac_per_customer)
print("\n")
print(color.BOLD+ "Financial Statement"+ color.END)
print(f"{color.RED} Marketing budget {color.END} :  {marketing} ")
print(f"{color.RED} Operations budget {color.END} :  {operations} ")
print(f"{color.RED} Customer acquisition budget {color.END} :  {customer_acquisition_cost} ")
print(f"{color.RED} {color.BOLD}Total {color.END} :  {total_budget} ")
print(f"{color.DARKCYAN} Customers acquired {color.END} :  {acquired_customers} ")
print("\n")

