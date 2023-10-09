class Car:
    def __init__(self, make, model, color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

my_car = Car("Toyota", "Corolla", "Blue", 2022)

# Adding instance attributes
my_car.current_mileage = 10000
my_car.service_history = ["Oil change", "Tire rotation"]

# Keeping track of instance attributes using vars()
print(vars(my_car))