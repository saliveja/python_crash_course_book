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
restaurant.describe_restaurant()
restaurant.open_restaurant()


# calling the instants

class IceCreamStand(Restaurant):
    """Creating a class for an Ice cream stand."""
    def __init__(self, flavors):
        flavors = ['vanilla', 'chocolate', 'strawberry']
        self.flavor = flavors


    def ice_cream_flavors(self):


