def city_country(city, country, population=''):
    """Printing city and country name."""
    if population:
        name_city_country = f"{city}, {country}, {population}"

    else:
        name_city_country = f"{city}, {country}"
    return name_city_country.title()
