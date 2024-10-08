from taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100)

"""Drive the taxi 40 km"""
my_taxi.drive(40)

"""Print the taxi's details and the current fare"""
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

"""Restart the meter (start a new fare) and then drive the car 100km"""
my_taxi.start_fare()
my_taxi.drive(100)

"""Print the details and the current fare"""
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")