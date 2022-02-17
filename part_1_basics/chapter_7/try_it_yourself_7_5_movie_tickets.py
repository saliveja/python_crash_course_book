question = "How old are you? "

answer = input(question)
if answer < 3:
    print("Your ticket is free!")
elif answer < 12: \
        print("Your ticket costs $10")
else:
    print("Your ticket costs $15")
