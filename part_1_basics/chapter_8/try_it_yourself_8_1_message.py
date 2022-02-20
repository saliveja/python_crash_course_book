names = ['sara', 'hanna', 'eva', 'karl', 'kerstin']


def display_message(name):
    """making function with message"""
    print(f"Hello {name.title()}, in this chapter I'm learning about how to "
          "define and call functions.")
    print("\n")


for name in names:
    display_message(name)
