# writing information to a file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    # 'w' opens the file in write mode
    # 'r+' is read and write mode
    # default mode if unspecified is read only
    file_object.write("I love programming.\n")
    # python can only store string data
    # numerical data need to be converted
    file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    # after we've used 'w' to write data into the text file
    # we can change and use 'a' so that the data that already exist won't
    # be deleted. 'a' means append and will add the data ti the end of the file
