class Car:
    def __init__(self, brand, model, price):
        self.__brand = brand        # private attribute
        self.__model = model        # private attribute
        self.__price = price        # private attribute

    # Getter methods (controlled access)
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    # Setter method (controlled modification with validation)
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be positive!")

    # Public method
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def description(self):
        return f"Car: {self.full_name()}, Price: {self.__price}"


# Usage
my_car = Car("Toyota", "Camry", 25000)

print(my_car.get_brand())
print(my_car.get_model())
print(my_car.description())

# updating price safely
my_car.set_price(27000)
print(my_car.get_price())