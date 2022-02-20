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
