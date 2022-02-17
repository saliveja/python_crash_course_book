# repeating a message using input()
message = input("Tell me something,and I will repeat it back to you ")
print(message)
# the user is asked to enter information which will then be repeated back
# the text edition won't be able to run this program
# we need to use terminal

prompt = "Tell me something,and I will repeat it back to you --> "
# request to make an input
prompt += "Enter quit to end the program: "
# if the input is quit. the program will stop running
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# using a Flag
# flag acts as a signal for the program
# flag is set to True
# while statements only need to check one condition:
# if the status of the Flag is True or False
prompt = "Tell me something,and I will repeat it back to you --> "
prompt += "Enter quit to end the program: "

# using the variable active = True as one condition for the program to run
active = True
# variable that the program is in an active state
while active:
    message = input(prompt)
    # when the program is active the message is the input

    if message == 'quit':
        # if the message is 'quit'
        active = False
        # the first variable is no longer true

    else:
        print(message)
        # if the forst variable continues to be true,
        # if the input is anything else than 'quit'
        # the message should be printed
