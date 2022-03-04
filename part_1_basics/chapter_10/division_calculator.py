# try, except, else blocks

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You can't divide by zero!")
        # the exception is anticipated and instead os showing traceback
        # it prints this message
        # this creates a more solid program
        # and at the same time it allows for the program to keep running

    else:
        print(answer)

# try works, the except block will be disregarded
# if a code doesn't work with try, python will run the exception
# we are creating a way for python to deal with the error
