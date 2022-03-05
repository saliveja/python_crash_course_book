# try, except when the file cannot be found
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        # 'utf-8' is needed to be specified when system's default encoding
        # doesn't match the encoding of the file
        contents = f.read()
        # content is the file in read mode

except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# analyzing text
# gutenberg.org --> collection of literary works
else:
    words = contents.split()
    # words are content split into a list where each word is an item
    num_words = len(words)
    # this shows the number of items in the list
    print(f"The file {filename} has about {num_words} words.")
