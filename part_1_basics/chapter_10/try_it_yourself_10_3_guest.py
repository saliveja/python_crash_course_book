# prompting user to write data that is then stored in a file
filename = 'guest.txt'

with open(filename, 'a') as file:
    # opening text file as 'file' and using 'a' so information will be appended
    prompt = "What is your name?\n"
    # prompting user for name
    answer = input(prompt)
    # user writes their input
    file.write(answer)
    # the information given by the user is stored in the file
    file.write("\n")
    # writing newline so that each word will be printed on a new line
