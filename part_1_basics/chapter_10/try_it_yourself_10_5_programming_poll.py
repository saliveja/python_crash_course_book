filename = 'poll.txt'

with open(filename, 'a') as file:
    file.write("Why do you like programming? (survey)\n")
    file.write("=====================================================")
    file.write("\n")
    file.write("Each new answer is separated this line.")
    file.write("\n")
    file.write("-----------------------------------------------------")
    file.write("\n\n")

with open(filename, 'a') as file:
    while True:
        prompt = "Why do you like programming? (submit as many " \
                 "answers as you want.)\n"
        prompt += "If you want to exit enter 'quit'.\n\n"
        answer = input(prompt)

        if answer.lower() == 'quit':
            file.write("-----------------------------------------------------")
            file.write("\n")
            quit()

        else:
            file.write("* ")
            file.write(answer)
            file.write("\n\n")
