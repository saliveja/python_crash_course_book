# storing guest info in a file

filename = 'guest_book.txt'

with open(filename, 'a') as file:
    while True:
        prompt = "What is your name?\n"
        prompt += "If you want to quit, enter 'q'\n\n"
        answer = input(prompt)

        if answer.lower() == 'q':
            print("See you!")
            quit()

        else:
            print(f"Hello {answer}, it is great to see you!")
            print("\n")
            file.write(answer)
            file.write("\n")
            # the input will not be printed to the file until it is closed
