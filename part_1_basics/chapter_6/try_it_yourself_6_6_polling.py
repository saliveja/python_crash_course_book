# making a dictionary with favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['emma', 'olga', 'katrin']

for names in favorite_languages.keys():
    print("Hi " + names.title() +
          ", thank you for participating in our poll!")
for friend in friends:
    if friend not in favorite_languages:
        print(friend + ", please take our poll!")
