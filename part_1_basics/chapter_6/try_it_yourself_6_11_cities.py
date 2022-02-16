cities = {
    'oslo': {
        'country': 'norway',
        'population': '5.4 million',
        'fact': 'norway was officially neutral during first and second world \n'
                'wars, but was selling fish to germany in the first war until '
                'the \nBritish governmen put a stop to it. In the second'
                'world war Germany \ninvaded. Neutrality it seems did not '
                'help Norway much.',
    },

    'edmonton': {
        'country': 'canada',
        'population': '1.01 million',
        'fact': 'edmonton is a name that came from capitalists in the '
                'Hudsons Bay\n company as well as Edmonton, Middlesex in '
                'England. Edmonton is part of\n indigenous territory that '
                'was colonized.',
    },

    'rome': {
        'country': 'italy',
        'population': '2.86 million',
        'fact': 'in Rome we can find the Sistine chapel, in Vatican city. '
                'It is\n most known for its frescos that decorates the '
                'interior, for example\n The last judgement by Michelangelo.'
    },
}

for name, info in cities.items():
    print(str(name).title())
    for name, value in info.items():
        print(str(name).title() + ": " + str(value))
    print("\n")

# to get back to:
# How to make the names in the info text title() when mentioned in the text
# s = "blaa edmonton foo"
# edmonton = "edmonton"
