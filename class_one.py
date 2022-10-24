class Car():
    color=""
    model=""
    speed=0
    brand=""
    fuel_tank=0
    mileage=0
    engine_size=0
    number_of_whels=0

    def __init__(self,brand,model) -> None:
        self.brand=brand
        self.model=model

    def navigation(self,direction):
        print(f"Turn {direction}")

car1 = Car()

car1.color="Blue"
car1.speed=200
car1.model="Model S"
car1.brand="Tesla"
car1.navigation("Left")

print(f"Mary's car model: {car1.model}")