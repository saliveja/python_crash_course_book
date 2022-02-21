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

    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        # the for loop starts when the while statement are no longer valid
        # when the list of items are finished
        # the for loop the prints all items that have been completed
