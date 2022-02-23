class Restaurant():

    def __init__(
            self, restaurant_name,
            cuisine_type, restaurant_open
    ):
        self.name = restaurant_name
        self.type = cuisine_type
        self.open = restaurant_open

    def describe_restaurant(self):
        """Printing a message containing name of restaurant and type of food"""
        print(f"If you go to {self.name.title()}, they serve {self.type}.")

    def open_restaurant(self):
        print(f"{self.name.title()} is open until {self.open}.")


restaurant = Restaurant('Ocean', 'seafood', 2100)

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n")

restaurant_2 = Restaurant('Irene', 'pizza', 1900)
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

print("\n")

restaurant_3 = Restaurant('Jannes', 'pancakes', 1700)
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
# calling instances three times
