# storing input in a dictionary
# using flag, input(), while, if, for
responses = {}
# creating an empty dictionary

polling_active = True
# setting flag

while polling_active:
    name = input("\nWhats is your name?")
    # asking for input on name
    if name.lower() == 'no':
        # if the input is 'no', making all letters lower case
        break
        # the loop stops

    response = input("Which mountain would you like to climb someday?")
    # if the first input is submitted, this question follows
    if response.lower() == 'no':
        break

    responses[name] = response
    # key is the name
    # the value is the response on the question 'which mountain...'
    # key-value pair is added to the dictionary

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    # if the response to this question is yes,
    # the loop will start from the beginning
    if repeat == 'no':
        polling_active = False
        # if that answer is no, the condition is no longer met

print("\n--- Polling results ---")
for name, response in responses.items():
    print(f" {name.title()} would like to climb {response.title()}.")
    # the result will be printed
