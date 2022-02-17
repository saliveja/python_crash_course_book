# using conditions - active, while and if

question = "How old are you? "
active = True

while active:
    answer = input(question)
    if answer == 'quit':
        # the answer is 'quit'
        print("Hope to see you soon!")
        # this message will be printed
        active = False
        # the condition is no longer true

    elif int(answer) < 3:
        print("Welcome. Your ticket is free!")
        # if the input is less than 3
    elif int(answer) < 12:
        print("Welcome! Your ticket cost $10")
        # if the input is less than 12
    elif int(answer) > 12:
        print("Welcome! Your ticket cost $15")
        # if the input is more than 12

# using break instead of active
question = "How old are you? "

while True:
    answer = input(question)
    if answer == 'quit':
        print("Hope to see you soon!")
        break

    elif int(answer) < 3:
        print("Welcome. Your ticket is free!")
    elif int(answer) < 12:
        print("Welcome! Your ticket cost $10")
    elif int(answer) > 12:
        print("Welcome! Your ticket cost $15")
