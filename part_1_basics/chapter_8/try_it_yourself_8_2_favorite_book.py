def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")


favorite_book('Alice in wonderland')

titles = ['alice in wonderland', 'narrative economics', 'agorism in the '
                                                        '21st century']


# making a list containing three books
def favorite_book(title):
    """Different messaged depending on book"""
    if title == 'alice in wonderland':
        print(f"{titles[0].title()} is a funny story.")
    if title == 'narrative economics':
        print(f"{titles[1].title()} is a book that one shouldn't read "
              f"before sleeping.")
    if title == 'agorism in the 21st century':
        print(f"It's interesting to read {titles[2].title()} but I enjoy "
              f"more to listen to my comrade talking about her perspectives.")


for title in titles:
    favorite_book(title)
print("\n\n")

# using definintion within a while loop with input
question = "Which book is your favorite?\n"
question_2 = "Cool, do you have other books you enjoy?\n"
question_3 = "What types of books do you prefer:\n"
question_4 = "Do you want more recommendations? yes/no\n"

continuation_rec = "Here are some other books you might enjoy:\n"

philosophies = {'Beyond Good & Evil': 'by Friedrich Nietzsche',
                'Analects': 'by Confucius',
                'The orinins of totalitarianism': 'by Hanna Arendt', }

sci_fis = {'Solaris': 'by Stanslaw Lem',
           'Dune': 'by Frank Herbert',
           'The left hand of darkness': 'by Ursula Le Guin', }

histories = {'The first world war': 'by Michael Howard',
             'Learning to fight': 'by Aimee Fox',
             'Pagans and christians': 'by Robin Lane Fox', }

histories_2 = {'The crisis of the European mind': 'by Paul Hazard',
               'The last king of Poland': 'by Adam Zamoyski',
               'The empire project': 'by John Darwin', }


def book_rec_philosophy():
    """Making a function in the while loop"""
    for key, value in philosophies.items():
        print(f"{key.title()}, {value.title()}")
    print("\n")


def book_rec_scifi():
    for key, value in sci_fis.items():
        print(f"{key.title()}, {value.title()}")
    print("\n")


def book_rec_history():
    for key, value in histories.items():
        print(f"{key.title()}, {value.title()}")
    print("\n")


def book_rec_history2():
    for key, value in histories_2.items():
        print(f"{key.title()}, {value.title()}")
    print("\n")

    print("I gave you enough, now get off the internet!\n")


active = True
while active:
    answer = input(question)
    response = input(question_2)
    print(f"You shared that you like {answer.title()} and {response.title()}.")
    response_3 = input(question_3)
    if response_3 == 'philosophy':
        print("If you like Philosophy I would also recommend:\n")
        book_rec_philosophy()
    elif response_3 == 'sci fi':
        print("If you like Sci fi I would also recommend:\n")
        book_rec_scifi()
    elif response_3 == 'history':
        print("If you like History I would also recommend:\n")
        book_rec_history()
    response_4 = input(question_4)
    if response_4 == 'no':
        break
    else:
        book_rec_history2()
        break

print("Have a nice reading time!")
