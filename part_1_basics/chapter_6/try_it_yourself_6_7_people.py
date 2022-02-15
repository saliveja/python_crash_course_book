person = {}
person['first name'] = 'elin'
person['last name'] = 'andersson'
person['age'] = 25
person['city'] = 'berlin'

# creating a dictionary storing values
# first name, last name, age and city and printing

person_2 = {}
person_2['first name'] = 'ivan'
person_2['last name'] = 'berg'
person_2['age'] = 38
person_2['city'] = 'odessa'

person_3 = {}
person_3['first name'] = 'sam'
person_3['last name'] = 'kant'
person_3['age'] = 13
person_3['city'] = 'barcelona'

people = []
people.append(person)
people.append(person_2)
people.append(person_3)

for each_person in people:
    for name, info in each_person.items():
        print(name.title() + ": " + str(info).title())
    print("\n")
