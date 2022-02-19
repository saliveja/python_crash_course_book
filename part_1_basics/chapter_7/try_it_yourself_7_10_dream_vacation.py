question_1 = "What is your name?\n"
question_1 += "If you want to exit write 'quit'."

question_2 = "\nIf you could visit one place in the world..."
question_2 += "\nWhere would you go?\n"

question_3 = "Do you want another person to respond yes/no \n\n"

answers = {}

active = True
while active:
    name = input(question_1.lower())
    # name is whatever input is given to this question
    if name.lower() == 'quit':
        # adding the possibility to quit at any point in the program
        print("Goodbye!")
        break

    print(f" \nHello {name.title()}!\n")
    # using the info that was given and printing a greeting

    answer = input(question_2.lower())
    # answer is whatever input is given to question_2

    if answer.lower() == 'quit':
        print("See you next time.")
        break

    print(f"\n{answer.title()} sounds amazing!")
    # printing a response including the given information

    answers[name] = answer
    # adding the key 'name' and the value 'answer' to the dictionary 'answers

    repeat = input(question_3)
    # repeat is whatever input is given to question_3
    print("\n")
    if repeat == 'no':
        active = False

    print("\nThese are the places in the world we want to visit most:")
    for name, answer in answers.items():
        print(f"{answer.title()}")
        # needed to indent the for loop to be able to give the option to\
        # quit any time
