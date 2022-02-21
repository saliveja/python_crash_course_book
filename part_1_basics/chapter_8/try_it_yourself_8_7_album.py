laleh = {'Laleh': "'Colors'", }

dead_prez = {'Dead prez': "'Lets get free'", }

tracy_chapman = {'Tracy Chapman': "'Crossroads'", }

albums = []

albums.append(laleh)
albums.append(dead_prez)
albums.append(tracy_chapman)


def make_album():
    """Three dictionaries with albums"""
    for album in albums:
        for key, value in album.items():
            print(f"{key.title()}, {value.title()}")


make_album()
