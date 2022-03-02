with open('learning_python.txt') as file:
    # opening learning_python as another name 'file'
    text_file = file.read()
    # using the variable text_file to store the file info and read function

print(text_file)
# printing the content of the file

with open('learning_python.txt') as file:
    text_file = file.read()
    print(text_file)
    # printing inside of the with block

with open('learning_python.txt') as file:
    text_file = file.readlines()
    # using readline() to store each line separately in the list text_file

for text in text_file:
    print(text.rstrip())
    # using for loop to print each line. Need to use readlines()
    # with read, one letter will be printed on each row
    # using rstrip() to remove the space in between
