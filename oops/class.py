class Car:

    total_car  = 0

    def __init__(self,brand, model, year):
        self.__brand = brand
        self.__model = model
        self.year = year
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        print(self.__brand, self.__model, self.year)

    def fuel_type(self):
        return "Petrol or desiel"
    
    @staticmethod
    def general_description():
        return "car i sdjk]jkfbveb"

    @property 
    def model(self):
        return self.__model


# car1 = Car("BMW", "X5", 2020)

# print(car1.brand)
# print(car1.model)
# print(car1.year)

# my_new_car = Car("Audi", "A4", 2019)

# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.year)
# car1.full_name()  # Output: BMW X5 2020

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

# my_tesla = ElectricCar("Tesla", "Model S", 2022, 100)

# print(my_tesla.brand) 
# print(my_tesla.get_brand()) # Output: Tesla
# print(my_tesla.fuel_type())

safari = Car("Tata", "safari", 2021)
print(safari.fuel_type()) # Output: Petrol or desiel
# print(my_tesla.model)  # Output: Model S
# print(my_tesla.year)  # Output: 2022
# print(my_tesla.battery_size)  # Output: 1004
# my_tesla.full_name()

# print(safari.total_car)
# test = Car("BMW", "X5", 2020)
# print(Car.total_car) # Output: 2

# isinstance(test, Car)
# print(isinstance(test, Car))




# my_car = Car("BMW", "X5", 2020)
# my_car.model = "city"

# print(my_car.model)
# print(my_car.general_description())
# print(Car.general_description(my_car))

class Battery:
    def battery_info(self):
        return "Battery info"

class jfvb:
    def engine_info(self):
        return "Engine info"

class ElectricCar(Battery, jfvb, Car):
    pass
    

my_new_tesla = ElectricCar("Tesla", "Model S", 2022)
print(my_new_tesla.battery_info()) # Output: Battery info
print(my_new_tesla.engine_info()) # Output: Engine info

