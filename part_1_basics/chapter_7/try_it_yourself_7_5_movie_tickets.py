question = "How old are you? "
# because we just need one answer, we don't need to make a loop

answer = input(question)
if int(answer) < 3:
    # if the anser is less than 3
    print("Welcome. Your ticket is free!")
    # this message is printed
elif int(answer) < 12:
    # if the answer is less than 12
    print("Welcome! Your ticket cost $10")
    # this answer is printed
else:
    print("Welcome! Your ticket cost $15")
    # if it's any other number, this message is printed
