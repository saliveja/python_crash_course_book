# making a dictionary with favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")
# printing Sarah's favorite language

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
print("\n")
# key() method
# returns  a list of all keys
for name in favorite_languages.keys():
    print(name.title())
    # this for loop is the same as:
    # for name in favorites_languages:
print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi " + name.title() +
              ", I see you favorite language is " +
              favorite_languages[name].title() + "!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

#
