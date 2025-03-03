class Car:
    total_car = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
    def get_brand(self):
        return self.__brand + " !"
    
    def set_brand(self, brand):
        self.__brand = brand
        
    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are the transport"
    
    @property
    def model(self):
        return self.__model
    
    
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize
        
    def fuel_type(self):
        return "Electric car"
    
    


# my_car = Car('sam', 'jfkj')
# print(my_car.brand)
# print(my_car.fullName())

# # car = Car("tata", "safari")
# # print(car.model)


    
# tesla = ElectricCar('tesla', "models", "8kwh")
# # print(tesla.fuel_type())
# print(isinstance(tesla, Car))
# print(isinstance(tesla, ElectricCar))


# safari = Car("tata", "safari")
# safari.model = "feveveerrv"

# print(safari.general_description())
# print(safari.model)

# print(safari.fuel_type())
# print(Car.total_car)


class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"
    

class ElectricCarTwo(Battery, Engine, Car):
    pass

result = ElectricCarTwo("Tesla", "Modal S")
print(result.engine_info())
print(result.battery_info())

