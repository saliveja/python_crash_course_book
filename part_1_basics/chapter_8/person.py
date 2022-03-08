# returning a dictionary

class Dictionary:
    """Creating a dictionary."""

    def __init__(self, first_name, last_name, person, age=''):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.person = person

    def build_person(self):
        """Return a dictionary of information about a person."""

        self.person = self.first + self.last
        # creating a dictionary where the value is the parameter
        if self.age:
            self.person['age'] = self.age
            # if age in included in the dictionary person
        return self.person
