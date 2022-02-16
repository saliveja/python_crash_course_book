# adding key-value pairs to existig exercise
pollo = {
    'animal': 'dog',
    'name': 'pollo',
    'age': 2,
    'owner': 'helga',
}

tilda = {
    'animal': 'cat',
    'name': 'tilda',
    'age': 5,
    'owner': 'fey',
}

berit = {
    'animal': 'dog',
    'name': 'berit',
    'age': 2,
    'owner': 'kenny',
}

smirre = {
    'animal': 'rabbit',
    'name': 'smirre',
    'age': 1,
    'owner': 'karin',
}

pets = []
pets.append(pollo)
pets.append(tilda)
pets.append(berit)
pets.append(smirre)

for pet in pets:
    for cat, info in pet.items():
        print(str(cat).title() + ": " + str(info).title())
    print("\n")
