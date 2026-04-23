#Inheritence

class Car:

    def __init__(self, brand, model): #Constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"Fullname: {self.brand} {self.model}"

#Inheritence Car->Super Class 
class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def description(self):
        return f"{self.full_name()} with battery size = {self.battery_size}"
    

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.description())
