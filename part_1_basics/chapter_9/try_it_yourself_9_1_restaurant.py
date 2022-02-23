class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        """Printing a message containing name of restaurant and type of food"""
        print(f"If you go to {self.name.title()}, they serve {self.type}.")
        # the first method is printing the name of the restaurant
        # and the food they serve

    def open_restaurant(self):
        print(f"{self.name.title()} is open until {str('2100')}.")
        # the second method print when it is open


restaurant = Restaurant('Ocean', 'seafood')
# making a variable defining restaurant_name and cuisine_type

restaurant.describe_restaurant()
restaurant.open_restaurant()
# calling the instants
