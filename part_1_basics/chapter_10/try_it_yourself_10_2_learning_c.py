# using replace() to change word inside a textfile

filename_2 = 'learning_python.txt'
with open(filename_2) as text:
    lines = text.readlines()
    # reading each line in the text

    for line in lines:
        line = line.replace('Python', 'C')
        line = line.replace('python', 'C')
        line = line.replace('program', 'world peace')
        # we can make as many replacements as we want
        # important to cover both upper case letters and lower case letters

        print(line)
        # printing inside the for loop

# filename = 'learning_python.txt'
# with open(filename) as text_file:
#     lines = text_file.readlines()
#
#     string = ''
#     for line in lines:
#         string += line
#         new_list = string.split()
#
#         for new_list[1] in new_list:
#             new_list[1] = 'C'
#             new_string = ''
#
#             for item in new_list:
#                 new_string += f"{item} "
#
# print(new_string)

# if I write like this - with open(text_file, 'w') as file_new:
# file_new.write('some text')
# the whole text in the file will be replaced

# if I put an 'a' instead, it will append the word in brackets
# at the end of the document
