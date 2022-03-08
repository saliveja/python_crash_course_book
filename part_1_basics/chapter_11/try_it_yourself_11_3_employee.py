class Employee:
    """class for first name, last name and salary of an employee"""

    def __init__(self, first, last, salary, amount=5000):
        self.first = first
        self.last = last
        self.salary = salary
        self.amount = amount

    def give_raise(self):
        """Raising the annual salary."""

        self.salary = f"{self.salary} + {self.amount}"