#create an abstract class for product and improve it ProductAbstract, implement product abstract in ProductManager
from abc import ABC, abstractmethod

#Product class describing attributes of the class
class Product():
    id=0
    name=""
    weight=0
    description=""
    sold_by=""
    price=0.0
    availability=False
    image=""

    def __init__(self,name,weight:int,description,sold_by,price,availability,id=0):
        self.name=name
        self.weight=weight
        self.description=description
        self.sold_by=sold_by
        self.price=price
        self.availability=availability
        
class ProductAbstract (ABC):

    @abstractmethod
    def create_product(self,product:Product):
        pass

    @abstractmethod
    def edit_product(self,product:Product,action):
        pass

    @abstractmethod
    def get_product_by_id(self,product_id):
        pass

    @abstractmethod
    def get_all_products(self):
        pass
    
    @abstractmethod
    def upload_product_image(self,product_id,image_object):
        pass

    @abstractmethod
    def delete_product(self,product_id):
        pass

class ProductManager(ProductAbstract):

    def create_product(self,product:Product):
        #create new product and add to database
        #...

        print("New product has been created")
    

    def edit_product(self,product:Product,action):
        #create new product and add to database
        #...

        print("The product has been editted")

    def get_product_by_id(self,product_id):
        #create new product and add to database
        #...

        print("This is your requested product")

    def get_all_products(self):
        #create new product and add to database
        #...
        data_from_db=["Iphone 13","Iphone 12","Iphone 11"]
        print("These are all the available products:")
        for item in data_from_db:
            print(item)
    
    def upload_product_image(self,product_id,image_object):
        #create new product and add to database
        #...

        response_from_db="Product image has been uploaded"

        print(response_from_db)
    

    def delete_product(self,product_id):
        #create new product and add to database
        #...

        response_from_db="The product has been deleted"

        print(response_from_db)
    

#product= Product(name="Iphone X",weight="hg",availability=True,description="This is a good phone",price=500,sold_by="KG")
#product_manager=ProductManager()
#product_manager.edit_product(product=product,action="rename")