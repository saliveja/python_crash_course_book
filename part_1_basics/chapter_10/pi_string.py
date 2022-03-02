filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    # text from a file is interpreted as a string

pi_string = ''
# this space appears on the left side of each part of the string
# if we want to work with numbers we need to use int()
# that's why there is spacing in between the numbers
for line in lines:
    pi_string += line.strip()
    # using rstrip() removes the space on the right side which results in
    # the lines to align on one row
    # using strip will remove the spacing in between so that the numbers
    # will all come together

print(pi_string)
print(len(pi_string))
# shows the length of the pi string underneath --> 32

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]} ...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    # comparing the number entered with the numbers of pi (or the ones we put
    # in the text file)
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
