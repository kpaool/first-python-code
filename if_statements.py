name = input("Enter your username: ")
password = input("Enter you password: ")

dbusername ="Admin"
dbpassword="1234@admin"

if(name==dbusername and password==dbpassword):
    print("Hello you are logged in")
else:
    print("Wrong username, password combination")