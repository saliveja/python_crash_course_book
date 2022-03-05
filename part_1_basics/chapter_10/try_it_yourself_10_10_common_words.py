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
        print(f"The file {filename} contains {number} of the word: 'the'.")


word = 'the'
filename = 'immortals_without_a_god.txt'
count_words(filename, word)
