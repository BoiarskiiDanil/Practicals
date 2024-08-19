from unreliable_car import UnreliableCar

"""Create an UnreliableCar object"""
unreliable_car = UnreliableCar(name="Old Timer", fuel=100, reliability=50)

"""Try to drive 40 km"""
distance_driven = unreliable_car.drive(40)
print(f"Attempted to drive 40 km, actually drove {distance_driven} km")

"""Print the car's details and try to drive another 40 km"""
print(unreliable_car)
distance_driven = unreliable_car.drive(40)
print(f"Attempted to drive 40 km, actually drove {distance_driven} km")

"""Print the car's details again"""
print(unreliable_car)