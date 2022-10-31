from abc import ABC, abstractmethod

class User():
    firstname=""
    lastname=""
    password=""
    email=""
    number=""

    def __init__(self,firstname,lastname,password,email,number) :
        self.firstname=firstname
        self.lastname=lastname
        self.password=password
        self.email=email
        self.number=number

class UserAbstract(ABC):

    @abstractmethod
    def create_user(self,user:User):
        pass

    @abstractmethod
    def get_all_users(self):
        pass

    @abstractmethod
    def get_user_by_id(self,user_id):
        pass

class UserManager(UserAbstract):
    def create_user(self, user: User):
        print("User information")

    def get_all_users(self):
        print("Print all user information")

    def get_user_by_id(self,user_id):
        print("Print all user information")
    

user = User(firstname="Jonathan Paul",lastname="Katumba",password="12345",email="jonathan.katumba@meltwater.org",number="+233554242228")

abstract_user = UserManager()
abstract_user.get_all_users()


#create an abstract class for product and improve it ProductAbstract, implement product abstract in ProductManager