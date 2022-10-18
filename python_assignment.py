#pre
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

#