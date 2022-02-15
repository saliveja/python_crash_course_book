favorite_numbers = {
    'lina': [1921, 15, 3],
    'elsa': [8, 89, 67, 56],
    'isak': [1, 55],
    'carlos': [2012],
    'amargi': [27, 33, 90, 11]
}
# making a dictionaries with lists
for name, numbers in favorite_numbers.items():
    print(str(name).title() + ": ")
    for number in numbers:
        print(number)
    print("\n")
    # using for loop to print names and numbers
