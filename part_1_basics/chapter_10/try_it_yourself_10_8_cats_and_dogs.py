class Text_management:
    """Adding text to file and reading file."""

    def __init__(self, filename='', request='Name: '):
        """Initializing."""
        self.name = filename
        self.request = request
        # making two parameters and one is default

    def saving_text_to_file(self):
        """Saving text to file."""
        for name in range(3):
            # using range to limit the loop to three times
            with open(self.name, 'a') as f:
                # using append for the file
                name = input(self.request)
                name = name.title()
                f.write('\n')
                f.write(name)

    def open_file(self):
        """Opening text file."""
        try:
            with open(self.name, 'r') as f:
                # using 'r' for read
                reading_file = f.read()
                # making a variable for the read  mode
                print(reading_file)

        except FileNotFoundError:
            # using try, except block in case file is not found
            print("We can't find your file. "
                  "Maybe you moved it somewhere else.")


print("Write three names of cats. They will be saved to a document.")
tm = Text_management('cats.txt')
tm.saving_text_to_file()
tm.open_file()
print("\n\n")

print("Write three names of dogs. They will be saved to a document.")
tm = Text_management('dogs.txt')
tm.saving_text_to_file()
tm.open_file()
print("\n\n")
