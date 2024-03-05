from car import Car, ElectricalCar

gas_fleet = []
electric_fleet = []

for _ in range(500):
    car = Car('ford', 'focus', 2016)
    gas_fleet.append(car)

for _ in range(500):
    ecar = ElectricalCar('nissan', 'leaf', 2018)
    electric_fleet.append(ecar)

for car in gas_fleet:
    car.fill_tank()
for ecar in electric_fleet:
    ecar.charge()

print("Gas cars: ", len(gas_fleet))
print("Electric cars: ", len(electric_fleet))

































