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