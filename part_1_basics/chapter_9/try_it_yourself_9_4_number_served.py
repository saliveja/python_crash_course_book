class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing a message containing name of restaurant and type of food"""
        print(f"If you go to {self.name.title()}, they serve {self.type}.")

    def open_restaurant(self):
        print(f"{self.name.title()} is open until {str('2100')}.")

    def served_guests(self, number):
        """Making a condition so there cannot be less guests
        than current number"""
        if number >= self.number_served:
            self.number_served = number
        else:
            print("The number of guests cannot decrease.")

    def increment_number_served(self, add_number):
        """Adding new number to existing value/number of guests."""
        self.number_served += add_number

    def sharing_guest_number(self):
        """Sharing the number of guests."""
        print(
            f"Today, {self.number_served} of people "
            f"dined at the restaurant.")
        # It was help[ful to make a method which only focuses on
        # printing the message


restaurant = Restaurant('Ocean', 'seafood')
# arguments on restaurant_name and cuisine_type
restaurant.describe_restaurant()
# method print the name and food of the restaurant
restaurant.open_restaurant()
# printing opening hours of the restaurant
restaurant.served_guests(5)
# the first number inserted on guests dining at the restaurant
restaurant.increment_number_served(6)
# an additional 6 guests
restaurant.increment_number_served(11)
restaurant.increment_number_served(4)
restaurant.increment_number_served(7)
restaurant.sharing_guest_number()
# printing the total amounts pf guests adding number to previous
