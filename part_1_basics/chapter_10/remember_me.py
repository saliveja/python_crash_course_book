import json

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
        # trying if the input was made before and if so, it will be loaded
        # opening in read mode

except FileNotFoundError:
    # if the file is not found, the user will be asked to give input
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        # opening in write mode which will create the file as well
        json.dump(username, f)
        # input is saved in the the file
        print(f"We'll remember you when you come back, {username}!")

else:
    print(f"Welcome back, {username}!")
    # if the data already exists, this message will be printed
