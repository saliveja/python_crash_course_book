def describe_cities(city, country='Greece'):
    # defining a function with a default value
    print(f"{city.title()} is in {country.title()}.")
    # within the function printing a message about the values


describe_cities('thessaloniki')
describe_cities('athens')
describe_cities('paris', country='France')
# the last time we call for the function we change the value of country
# the value is instead 'France'
