# working with multiple files

def count_words(filename):
    """Count the approximate number of words in a file."""

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        pass
        # with pass the user see the word count for the existing files
        # the error is not a traceback nor a message
        # the program simply skips the file that can't be read/is not existing
        # print(f"Sorry, the file {filename} does not exist.")

    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
    # making a function makes the code more efficient
    # we can apply this to any text where we want to count words
    # the try except is helpful since it allows the program to run even
    # after encountering an error
