def car_info(company, model, **more_info):
    """Making a dictionary storing information about cars."""
    more_info['Company'] = company
    more_info['Model'] = model
    # adding the first two parameters to the dictionary

    for key, value in more_info.items():
        # looping through arbitrary arguments
        more_info[key] = value
        return more_info


complete_car_info = car_info('Toyota', 'Chrome', Origin='Germany', Seats=5)
# the variable complete_car_info equals the function including all arguments
print(complete_car_info)
