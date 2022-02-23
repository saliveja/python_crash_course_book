# working with classes and instances

class Car():

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        # setting a default value for an attribute

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name."""
        long_name = f" {str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer to the given value.
        Reject the change if it attempts to roll the odometer back"""

        if mileage >= self.odometer_reading:
            # if a new number given is less than previous,
            # there will be a warning message
            self.odometer_reading = mileage
            # creating a new parameter
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def increment_odometer(self, miles):
        # when we use this method,
        # the number given in parenthesis will be added to the existing
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print('\n')
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print('\n')
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print('\n')
my_new_car.update_odometer(56)
my_new_car.read_odometer()

print('\n')
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

print('\n')
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

print('\n')
my_used_car.increment_odometer(100)
# this adds 100 to the updates value which is 23500
my_used_car.read_odometer()
