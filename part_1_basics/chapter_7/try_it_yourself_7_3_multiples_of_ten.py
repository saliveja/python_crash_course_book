info = input("Can you give me a number and I will say if it's a multiple "
             "of ten or not. ")
info += input("What number do you choose?)
# adding a string to the first input by using +=
info = int(info)
# that the string should be interpreter as numerical
if info % 10 == 0:
# multiple of ten means that it is an even number and will return 0 if True
    print("\nThe number you have chosen is muliple by ten.")
else:
    print("The number yo have chosen is not multiple of ten.")
    # conditional test. If the number is a multiple of ten -
    # the first message will be printed
    # if not, the second message