# positional arguments
# is when parameters and the arguments/values are in the same order
def describe_pet(animal_type, pet_name):
    # making a function which contains two parameters
    """Display information about a pet."""
    print((f"\nI have a {animal_type}."))
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
# calling for function and giving the values that connects with the parameters
# animal_type = 'hamster
# pet_name = 'harry'

# multiple functions call
describe_pet('dog', 'willie')
# we can change the value and the function work the same
# but the new values will be printed instead

# keyword argument (is a name-value pair)
describe_pet(animal_type='hamster', pet_name='harry')


# when using keyword arguments the order doesn't matter
# it's specifies where each value should go

# default value
def describe_pet(pet_name, animal_type='dog'):
    # if there is information that  is constant
    # we can write a default value where we usually write parameters
    """Display information about a pet."""
    print((f"\nI have a {animal_type}."))
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    # it's not enough to have parameters and arguments
    # we need to print for the function to be visible


describe_pet(pet_name='willie')
describe_pet(pet_name='berit')
print("\n")
describe_pet(pet_name='harry', animal_type='hamster')
# when we define the value when calling for the function
# python disregards the default value
# default value need to be listen after all parameters \
# that dont have default value
print("******************")

describe_pet('willie')
describe_pet(pet_name='willie')
print("\n**")

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
# the function we called the three last times all have the same output
# we can use different styles according to what works best for us

# avoiding argument errors
# if we in the function define parameters, we also need to write arguments
# it's helpful to give variables and functions descriptive names
# if an error occurs the messages will be more useful
