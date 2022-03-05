def count_words(filename, word):
    """Counting specific word in book."""
    word = word

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        number = contents.count(word)
        # 3389 without space
        # 2276 with space
        print(f"The file {filename} contains {number} of the word: {word}.")


# word = 'the'
filenames = ['immortals_without_a_god.txt', 'alice.txt', 'siddharta.txt',
             'moby_dick.txt', 'little_women.txt']

count_words(filenames[0], 'mountain')
count_words(filenames[1], 'love')
count_words(filenames[3], 'class')
# using index to choose which file from the list to search
# second argument defines the word

word = 'she'
for filename in filenames:
    count_words(filename, word)
    # for loop is more useful if we want to search for the
    # same word in all files
