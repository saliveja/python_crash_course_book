def city_country(city, country):
    city_and_country = (f'"{city}, {country}"')
    return city_and_country.title()


info = city_country('oslo', 'norway')
print(info)
