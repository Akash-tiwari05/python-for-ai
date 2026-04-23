#Inheritence

class Car:

    def __init__(self, brand, model): #Constructor
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand+"!"

    #Polymorphism
    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return f"Fullname: {self.__brand} {self.model}"

#Inheritence Car->Super Class 
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    #polymorphism
    def fuel_type(self):
        return "Electric Charge"

    def description(self):
        return f"{self.full_name()} with battery size = {self.battery_size}"
    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.get_brand())
print(my_tesla.model)
print(my_tesla.fuel_type())