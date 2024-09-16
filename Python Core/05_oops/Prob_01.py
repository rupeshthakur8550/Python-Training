class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.__brand = brand #__ if used before any variable then it becomes private
        self.__model = model
        Car.total_car += 1

    def display(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand

    def fuel_type(self):
        return "petrol or Diesel"
    
    @staticmethod
    def get_total_car_instance_count():
        return Car.total_car
    
    @property
    def model(self):
        return self.__model


myCar = Car("Tata", "Nexon")
# print(myCar.display())
# print(myCar.fuel_type())

my_new_car = Car("Mahindra","Scorpio")
# print(my_new_car.display())

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla", "Model S", "85KWh")
# print(my_tesla.display())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())

# print(Car.get_total_car_instance_count())

# my_new_car.model = "City" @property use to make attributes of class as encapsulates
# print(my_new_car.model)

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(Self):
        return "this is engine"

class Electric_car(Battery, Engine, Car):
    pass

my_car = Electric_car("Mahindra", "Thar")
print(my_car.engine_info())
