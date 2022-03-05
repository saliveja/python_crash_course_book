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
            with open(self.name, 'a') as f:
                name = input(self.request)
                name = name.title()
                f.write('\n')
                f.write(name)

    def open_file(self):
        """Opening text file."""
        try:
            with open(self.name, 'r') as f:
                reading_file = f.read()
                print(reading_file)

        except FileNotFoundError:
            pass
            # pass is a silent exception
            # print("We can't find your file. "
            #       "Maybe you moved it somewhere else.")


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
