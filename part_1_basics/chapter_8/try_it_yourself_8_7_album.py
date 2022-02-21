# making three dictionaries

laleh = {'Laleh': "'Colors'", }

dead_prez = {'Dead prez': "'Lets get free'", }

tracy_chapman = {'Tracy Chapman': "'Crossroads'", }

albums = []
# adding them to a list
albums.append(laleh)
albums.append(dead_prez)
albums.append(tracy_chapman)


def make_album():
    """Three dictionaries with albums"""
    for album in albums:
        for key, value in album.items():
            print(f"{key.title()}, {value.title()}")


# for loop to print each artist and album
print("\n\n")

# creating a function with while statement
# attempting not save input info to a text file - NOT working
make_album()
info = "Press q if you want to exit."
question_1 = 'Artist: '
question_2 = 'Album: '
question_3 = 'Tracks: '

while True:
    print(info)
    answer = input(question_1)
    if answer == 'q':
        quit()

    else:
        store = open("test.txt", "w")
        store.writelines(answer)
        # store_1 = close('~/Desktop/test2.odt')
        print("\n")

        print(info)
        answer_2 = input(question_2)
        if answer_2 == 'q':
            quit()

        else:
            store.writelines(answer_2)
            print("\n")

            print(info)
            answer_3 = input(question_3)
            if answer_3 == 'q':
                quit()

            else:
                store.writelines(answer_3)
                print("Thank you for your participation.\n")

print("Have a nice day!")
