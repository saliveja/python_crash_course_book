name = input("Please enter your name: ")
print(f"\nHello, {name}!")
# input() makes the request and then waits for input
# when entering name, the greeting and name is printed
# the name in print refers to the answer

prompt = "If you tell us who your are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
# building a multi-line string
# the first one is variable
# the second using += is adding a string to the first string called 'prompt'
# this will be printed on a new line

# using int()
age = input("How old are you? ")
# if answer ie. is 15
# terminal will return '15'
# if writing age >= 18 there will be an error
# it's not possible to compare a string with a numerical value
# if we write age == 15 it will return False
age = int(age)
age >= 15
# returns True because the string is converted to a numerical representation
# the comparison is therefore possible
