# using conditions - active, while and if

question = "How old are you? "
answer_input = "Welcome, your ticket cost $"
price_1 = str('0')
price_2 = str('10')
price_3 = str('15')
#
# active = True
# while active:
#     answer = input(question)
#     if answer == 'quit':
#         # the answer is 'quit'
#         print("Hope to see you soon!")
#         # this message will be printed
#         active = False
#         # the condition is no longer true
#
#     elif int(answer) < 3:
#         print(answer_input + price_1)
#         # if the input is less than 3
#     elif int(answer) < 12:
#         print(answer_input + price_2)
#         # if the input is less than 12
#     elif int(answer) > 11:
#         print(answer_input + price_3)
#         # if the input is more than 12

# using break instead of active
# question = "How old are you? "
stop = 'quit'
while True:
    answer = input(question)
    if answer.lower() == stop:
        print("Hope to see you soon!")
        break

    elif int(answer) < 3:
        print(answer_input + price_1)
    elif int(answer) <= 12:
        print(answer_input + price_2)
    elif int(answer) < 110:
        print(answer_input + price_3)
    elif int(answer) >= 110:
        print("Serinko you are the only one testing this")
    # elif answer != int(answer):
    #     print("This is not an age, enter a digit, you degen.")
    # how to make sure that letters are not accepted except quit?


