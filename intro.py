#print("Hello world! My name is Papatumba fron Uganda")
#simple python program to add two number and print the outcome
a=0
b=0
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
except:
    print("Please enter a number")
    quit()
sum=a+b
print(f"The sum of {a} and {b} is {sum}")