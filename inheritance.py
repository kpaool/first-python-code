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



class ElectricCar(Car):
    battery_capacity=0
    charge_duration=0

    def __init__(self, brand, model,batter_capacity) -> None:
        self.battery_capacity=batter_capacity
        super().__init__(brand, model)

class CEngineCar(Car):
    engine_capacity=0
    
    
    def __init__(self, brand, model,capacity) -> None:
        self.engine_capacity=capacity
        super().__init__(brand, model)


class HybridCar(ElectricCar,Car):
    carbon_emmission=0

car =Car(brand="Toyota",model="2020")

electric_car=ElectricCar(brand="Tesla",model="Model S 2020",batter_capacity="230KWh")

cengine_car= CEngineCar(brand="Mistubishi",model="2017",capacity="2000cc")
cengine_car.engine_capacity

hybridcar= HybridCar(batter_capacity="230KWh",brand="Tesla",model="Model X")
hybridcar.carbon_emmission