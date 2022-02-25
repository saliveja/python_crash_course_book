class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Printing a message containing name of restaurant and type of food"""
        print(f"If you go to {self.name.title()}, they serve {self.type}.")

    def open_restaurant(self):
        print(f"{self.name.title()} is open until {str('2100')}.")


restaurant = Restaurant('Ocean', 'seafood')


# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# calling the instants

class IceCreamStand(Restaurant):
    """Creating a class for an Ice cream stand
    and inherit from restaurant class."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializing attributes of parent class."""
        super().__init__(restaurant_name, cuisine_type)
        # adding parameters from parent class

    def ice_cream_flavors(self, flavors):
        """Printing message with flavors."""
        self.flavors = flavors
        # we need a parameter for flavors
        # defining the parameter
        # we don't need
        print("These are the flavors we have right now.\n"
              "Which one would you like?\n")
        # printing message
        for flavor in self.flavors:
            print(flavor)
            # looping through the flavors


list_flavors = ['vanilla', 'chocolate', 'strawberry']
# making a list with flavors

icecream_stand_0 = IceCreamStand('panda', 'ice cream')
# making a variable for the class IceCreamStand and new arguments
# with this changing name of restaurant and typ of cuisine

icecream_stand_0.describe_restaurant()
# calling the method to print name and what they serve
print("\n")
icecream_stand_0.ice_cream_flavors(list_flavors)
# with variable for the class calling the method for flavors
