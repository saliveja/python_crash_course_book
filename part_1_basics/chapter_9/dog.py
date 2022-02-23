# creating and using a class
# the _init_ method

class Dog():
    # when defining a class we start with an uppercase letter in python
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        # init method run automatically whenever we create a new instance
        # self parameter always need to be included and first
        # self is a reference to the instance
        # a function that is a part of a class is called a method
        """Initialize name and age attributes."""
        self.name = name
        # the prefix self makes the variable available to every method,
        # in the class (method = functions)
        # variables accessible through instances are called attributes
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulating rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name.title()}.")
# adding.name makes it possible to access the value of my_dog
print(f"My dog is {str(my_dog.age)} years old.")

my_dog.sit()
my_dog.roll_over()
