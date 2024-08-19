from silver_service_taxi import SilverServiceTaxi

"""Create a SilverServiceTaxi object with fanciness of 2"""
silver_taxi = SilverServiceTaxi(name="Luxury Car", fuel=100, fanciness=2)

"""Drive the taxi 18 km"""
silver_taxi.drive(18)

"""Calculate the fare and print it"""
fare = silver_taxi.get_fare()
print(f"Fare for 18 km: ${fare:.2f}")

"""Print the taxi's details"""
print(silver_taxi)

"""Assert test to ensure correctness"""
assert fare == 48.78, f"Expected fare: $48.78, but got ${fare:.2f}"