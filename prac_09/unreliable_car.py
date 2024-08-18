"""
CP1404/CP5632 Practical
UnreliableCar class inherited from Car class
"""

import random
from car import Car  # Import the Car class

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)  # Call the parent class constructor
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance, depending on reliability.

        Generate a random number between 0 and 100, and only drive the car if
        that number is less than the car's reliability.
        """
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
