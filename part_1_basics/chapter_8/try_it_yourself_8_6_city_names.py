def city_country(city, country):
    """Three ways of calling a function"""
    city_and_country = (f'"{city}, {country}"')
    return city_and_country.title()


info = city_country('oslo', 'norway')
# positional argument
print(info)


def city_country(city, country='norway'):
    # country is default value
    city_and_country = (f'"{city}, {country}"')
    return city_and_country.title()


info = city_country('oslo')
print(info)


def city_country(city, country):
    """Printing city and country with for loop"""
    info = (f'"{city}, {country}"')
    return info.title()


city_and_country = city_country(city='oslo', country='norway')
# defining both city and country in arguments
print(city_and_country)
