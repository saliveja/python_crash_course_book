prompt = "\nPlease enter the name of a city you have visted:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    # while True will run until it reaches a break statment
    city = input(prompt)
    if city == 'quit':
        break
        # the program exits the loop when 'quit' is entered
    else:
        print(f"I'd love to go to {city.title()}!")
        # if 'quit' is not written, the message will be printed
