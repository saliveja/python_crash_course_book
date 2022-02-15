pollo = {
    'animal': 'dog',
    'owner': 'helga',
}

tilda = {
    'animal': 'cat',
    'owner': 'fey',
}

berit = {
    'animal': 'dog',
    'owner': 'kenny',
}

smirre = {
    'animal': 'rabbit',
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
