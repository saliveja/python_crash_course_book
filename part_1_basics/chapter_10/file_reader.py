# opening and reading a file

with open('pi_digits.txt') as file_object:
    # we are using with open instead of open() and close()
    # There can be bugs that can result in file not being closed which can cause
    # problems in the code
    # with this, we also don't need to decide when to close
    # python will close when it's no longer needed
    contents = file_object.read()
    # storing the reading of file in a variable
    print(contents.rstrip())
    # removing the extra space that appears with read()

# reading line by line
filename = 'pi_digits.txt'
# we store the name of the file in a variable
# the name of the file only tells us where the file is located
with open(filename) as file_object:
    lines = file_object.readlines()
    # storing the file representation inside with block
    # readlines() takes each line from the file and stores it in a list

for line in lines:
    print(line.rstrip())
    # using for loop to print each lines
