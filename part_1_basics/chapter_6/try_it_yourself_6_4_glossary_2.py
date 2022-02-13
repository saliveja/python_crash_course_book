glossary = {}
glossary['dictionary'] = "A dictionary contains key-value pairs, a cathegory" \
                         " with assigned value for example 'color': 'black."
glossary['key_value_pair'] = "A key value pair is the stored value in a " \
                             "dictionary."
glossary['if_elif_else chain'] = "An if-elif-else cchain is a series of" \
                                 " conditional tests."
glossary['lists'] = "A list contains items. Contrary to a dictionary it " \
                    " doesn't hold any stored value about the items."
glossary['modifying_value'] = "If we want to modify the value of a " \
                              " key-value pair in a dictionary we can 'add' " \
                              " it again but assign new value."
glossary['set()'] = "set() method is used to not repeat av value in the" \
                    "dictionary."
glossary['values()'] = "The values() method pulls all the values from the" \
                       "dictionary and returns is without keys."
glossary['sorted()'] = "sorted() organizes dictionary in alphabetical order."
glossary['keys()'] = "key() is pulling out the cathegory from the list, but" \
                     " not the value. If we want to see the name of everyone" \
                     "who partcipated in a a poll but not their input."
glossary['items()'] = "items() returns a list with keys and values."

for header, text in glossary.items():
    print(header.title() + ":")
    print(text)
    print("\n")
