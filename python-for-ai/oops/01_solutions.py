
class Car:

    def __init__(self, brand, model): #Constructor
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"Fullname: {self.brand} {self.model}"

my_car = Car("Toyota","Fortuner") #Object creation
print(my_car)
print(my_car.brand)
print(my_car.model)
print(my_car.full_name()) #full_name


my_new_car = Car("Tata","Safari")
print(my_new_car.brand)
print(my_new_car.model)
