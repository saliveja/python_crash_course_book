# making three dictionaries

laleh = {'Laleh': "'Colors,'", }

dead_prez = {'Dead prez': "'Lets get free,'", }

tracy_chapman = {'Tracy Chapman': "'Crossroads,'", }

laleh['tracks'] = '15'
dead_prez['tracks'] = '20'
tracy_chapman['tracks'] = '12'

albums = []
# adding them to a list
albums.append(laleh)
albums.append(dead_prez)
albums.append(tracy_chapman)


def make_album():
    """Three dictionaries"""

    for album in albums:
        print("\n")

        for key, value in album.items():
            # album = ", ".join(album)
            string = f"{key.title()}, {value.title()}"
            print(string, end=' ')


make_album()
# for loop to print each artist and album
print("\n\n")
