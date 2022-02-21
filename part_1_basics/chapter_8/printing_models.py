# modifying a list in a function
# when passing a list to a function,
# the function can modify the list

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# one list with orders and one empty for those who are finished

while unprinted_designs:
    # as long as there are itens in the list of unprinted_designs
    current_design = unprinted_designs.pop()
    # the current design equals unprinted_designs
    # pop() starts from the end of the list
    print("Printing model: " + current_design)
    # printing message with the finished model
    completed_models.append(current_design)
    # adding the finished model to the list completed_models

print("\n")

print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    # the for loop starts when the while statement are no longer valid
    # when the list of items are finished
    # the for loop the prints all items that have been completed


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """how all the models that were printed"""
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
print("\n")
show_completed_models(completed_models)
# instead of a big chunk of code, we use the function
# so we can just can for the function for the same thing to happen
# which makes the code more efficient, bcs we if we need to change something
# we only need to do it in one place

# preventing a function from modifying a list
function_name(list_name[:])
# makes copy of the list if we don't want to change the original
print_models(unprinted_designs[:], completed_models)
# the functions will work as before but the original list is intact
# only the copy will change
# it's more efficient to work with an original though
