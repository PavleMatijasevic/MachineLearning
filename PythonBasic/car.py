
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 15
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print('Fuel tank is full')
    
    def drive(self):
        print('The car is moving')
    
    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank can't hold that much!")
    
    def add_fuel(self, amount):
        if(self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print('Added fuel.')
        else:
            print("The tank won't hold that much")
    
#   !!!!!!!    
class ElectricalCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Battery capacity in kWh
        self.battery_size = 70
        # Charge level in %
        self.charge_level = 0
        self.battery = Battery()

    def charge(self):
        self.charge_level = 100
        print('The vehicle is fully charged.')
    
    def fill_tank(self):
        print('This car has no fuel tank!')

class Battery():
    def __init__(self, size = 70):
        self.size = size
        self.charge_level = 0

    def get_range(self):
        if self.size == 70:
            return 240
        elif self.size == 85:
            return 270
    



my_ecar = ElectricalCar('tesla', 'model s', 2019)
my_ecar.charge()
my_ecar.drive()

my_ecar2 = ElectricalCar('tesla', 'model x', 2020)
my_ecar2.charge()
print(my_ecar2.battery.get_range())
my_ecar2.drive()

my_car = Car('Audi', 'a4', 2016)
print(my_car.make)
print(my_car.model)
print(my_car.year)

my_car.fill_tank()
my_car.drive()

my_old_car = Car('subaru', 'outback', 2013)
my_truck = Car('toyota', 'tacoma', 2010)

my_car.fuel_level = 5























