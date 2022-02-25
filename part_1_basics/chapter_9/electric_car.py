# the __init__() method for child class

class Car():
    # parent class

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neatly formatted descriptive name."""
        long_name = f" {str(self.year)} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer to the given value.
        Reject the change if it attempts to roll the odometer back"""

        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attribute."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {str(self.battery_size)}kWh battery.")
        # be aware of which order you place the classes in the program
        # it matters for how the code will be understood
        # Battery() need to be above Electric_car() in the program

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = f"This car can go approximately {str(range)}"
        message += " miles on a full charge."
        print(message)


class Electric_car(Car):
    # in the parenthesis we refer to the parent class Car
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        # the information needed to make a car instance
        """Initialize attribute of the parent class."""
        super().__init__(make, model, year)
        # the super().__init__ function makes the connection between the
        # parent (superclass) and child class (subclass)
        # and gives the child class all attributes of the parent class
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        # if there is a method like this in the parent class
        # we can define the method in the child class with new information
        # instead of filling the gas tank, this message will be printed


my_tesla = Electric_car('tesla', 'model s', 2016)
# making an instance, storing arguments in variable my_tesla
print(my_tesla.get_descriptive_name())
# calling a method in parent class
my_tesla.battery.describe_battery()
# calling method in Battery() class
my_tesla.battery.get_range()
